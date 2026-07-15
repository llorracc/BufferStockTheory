#!/usr/bin/env python3
"""run_benchmark.py — issue every benchmark.yml question to matsya.

For each question in `evaluation/benchmark.yml`, invoke
`matsya "<q>" --BST --session <S>`, capture stdout, parse the
"Sources:" block into a list of file paths, and write
`evaluation/responses/<id>.json`.

Idempotent: skips questions whose response file already exists.
Use `--force` to overwrite.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
EVAL_DIR = ROOT / "evaluation"
BENCHMARK = EVAL_DIR / "benchmark.yml"
RESPONSES_DIR = EVAL_DIR / "responses"

# matsya prints `Sources (<n> chunks):` followed by lines like
#   `  [-0.642] /root/HARK_ask-your-project/project/repos/BufferStockTheory/BufferStockTheory-NoAppendix.tex`
SOURCES_HEADER = re.compile(r"^Sources\s*\(\d+\s*chunks?\):\s*$")
SOURCE_LINE = re.compile(r"^\s*\[[-+\d.]+\]\s+(\S.*)$")


def parse_sources(stdout: str) -> list[str]:
    """Return the list of file paths in matsya's 'Sources:' block.

    Returns [] if no sources block is found (best-effort parser; the
    plan explicitly allows tightening this later).
    """
    lines = stdout.splitlines()
    out: list[str] = []
    in_block = False
    for line in lines:
        if SOURCES_HEADER.match(line):
            in_block = True
            continue
        if in_block:
            m = SOURCE_LINE.match(line)
            if m:
                out.append(m.group(1).strip())
            elif line.strip() == "":
                continue
            else:
                # First non-source, non-blank line ends the block.
                break
    return out


def run_one(matsya_bin: str, question: str, session: str) -> tuple[str, int]:
    """Invoke matsya for a single question, return (stdout, returncode)."""
    proc = subprocess.run(
        [matsya_bin, question, "--BST", "--session", session],
        capture_output=True,
        text=True,
        timeout=600,
    )
    return proc.stdout, proc.returncode


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--matsya-bin", default=shutil.which("matsya") or "matsya",
                   help="path to matsya executable (default: from PATH)")
    p.add_argument("--session-prefix", default="bench",
                   help="session-name prefix; full name is <prefix>-<timestamp>-<id>")
    p.add_argument("--out-dir", default=str(RESPONSES_DIR),
                   help="directory to write per-question response JSON files")
    p.add_argument("--force", action="store_true",
                   help="re-run even if response file already exists")
    p.add_argument("--only", default=None,
                   help="comma-separated id list; only run these questions")
    args = p.parse_args()

    if not BENCHMARK.exists():
        print(f"error: {BENCHMARK} not found", file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    entries = yaml.safe_load(BENCHMARK.read_text())
    if not isinstance(entries, list):
        print(f"error: {BENCHMARK} must be a YAML list", file=sys.stderr)
        return 2

    only = set(args.only.split(",")) if args.only else None
    run_ts = time.strftime("%Y%m%dT%H%M%S")
    n_run = n_skip = n_fail = 0

    for entry in entries:
        qid = entry["id"]
        if only and qid not in only:
            continue
        out_path = out_dir / f"{qid}.json"
        if out_path.exists() and not args.force:
            n_skip += 1
            continue

        question = entry["question"]
        session = f"{args.session_prefix}-{run_ts}-{qid}"
        print(f"  [{qid}] querying matsya ...", flush=True)
        try:
            stdout, rc = run_one(args.matsya_bin, question, session)
        except subprocess.TimeoutExpired:
            print(f"  [{qid}] TIMEOUT", file=sys.stderr)
            n_fail += 1
            continue
        except FileNotFoundError:
            print(f"error: matsya executable not found at {args.matsya_bin!r}", file=sys.stderr)
            return 2

        parsed = parse_sources(stdout)
        record = {
            "question_id": qid,
            "question": question,
            "session": session,
            "matsya_response": stdout,
            "parsed_sources": parsed,
            "returncode": rc,
            "timestamp": run_ts,
        }
        out_path.write_text(json.dumps(record, indent=2))
        if rc == 0:
            n_run += 1
        else:
            n_fail += 1

    print(f"\nran {n_run}, skipped {n_skip}, failed {n_fail}.")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
