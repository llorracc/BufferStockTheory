#!/usr/bin/env python3
"""atlas_review.py — matsya + Opus-4.8 retrieval-grounded review of each concept.

For every concepts/<id>.yml, build a SKEPTICAL paper-faithfulness review prompt
(defining equation + gloss + relations + external citations) and issue it to

    matsya "<prompt>" --BST --model claude-opus-4-8 -q --session atlas-review-<id>

capturing matsya's retrieval-grounded verdict to
    evaluation/atlas-review/matsya/<id>.json

This is an ADVISORY machine pre-review, NOT domain-expert sign-off. It does NOT
modify concepts/_review-status.yml. A few queries run concurrently (the droplet
tolerates concurrency); the LLM judging happens server-side on the droplet.

Usage:  python3 evaluation/atlas_review.py [--force] [--workers N] [--only a,b]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: PyYAML required", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS = ROOT / "concepts"
OUT = ROOT / "evaluation" / "atlas-review" / "matsya"

SOURCES_HEADER = re.compile(r"^Sources\s*\(\d+\s*chunks?\):\s*$")
SOURCE_LINE = re.compile(r"^\s*\[[-+\d.]+\]\s+(\S.*)$")


def parse_sources(stdout: str) -> list[str]:
    out, inblock = [], False
    for line in stdout.splitlines():
        if SOURCES_HEADER.match(line):
            inblock = True
            continue
        if inblock:
            m = SOURCE_LINE.match(line)
            if m:
                out.append(m.group(1).strip())
            elif line.strip() == "":
                continue
            else:
                break
    return out


def build_prompt(c: dict, cites: set[str]) -> str:
    de = c.get("defining_equation") or {}
    rels = "\n".join(
        f"  - {r.get('kind')} -> {r.get('target')}"
        + (f" : {r.get('note')}" if r.get("note") else "")
        for r in (c.get("relations") or [])
    ) or "  (none)"
    cites_s = ", ".join(sorted(cites)) if cites else "none"
    return (
        "You are a SKEPTICAL reviewer checking an AI-authored concept-atlas entry "
        "against the BufferStockTheory paper for PAPER-FAITHFULNESS. Find errors; "
        "do not rubber-stamp.\n"
        f"CONCEPT: {c.get('name')}  (defining anchor: {de.get('anchor')})\n"
        f"DEFINING EQUATION (claimed): {de.get('latex')}  —  \"{de.get('english')}\"\n"
        f"GLOSS UNDER REVIEW:\n{(c.get('gloss') or '').strip()}\n"
        f"RELATIONS UNDER REVIEW:\n{rels}\n"
        f"EXTERNAL CITATIONS IN THIS ENTRY: {cites_s}\n\n"
        "Using the paper, assess: (1) GLOSS — is every claim paper-faithful? flag any "
        "overstatement, wrong symbol, or unsupported inequality. (2) RELATIONS — is each "
        "edge correct and the right type (implies / requires / assumed-by / contrasts-with "
        "/ special-case-of / ...)? (3) EXTERNAL-LIT — can you verify the cited-source claims "
        "from retrieval, or must they be flagged for domain-expert verification? Cite paper "
        "passages. END with exactly one line: "
        "'VERDICT: <faithful|minor-issues|overstated|unverifiable-here>' then a 1-2 sentence reason."
    )


def run_one(matsya: str, cid: str, prompt: str, force: bool) -> tuple[str, str]:
    outp = OUT / f"{cid}.json"
    if outp.exists() and not force:
        return (cid, "skip")
    try:
        p = subprocess.run(
            [matsya, prompt, "--BST", "--model", "claude-opus-4-8",
             "-q", "--session", f"atlas-review-{cid}"],
            capture_output=True, text=True, timeout=600,
        )
    except subprocess.TimeoutExpired:
        return (cid, "timeout")
    rec = {
        "id": cid, "prompt": prompt, "matsya_response": p.stdout,
        "sources": parse_sources(p.stdout), "returncode": p.returncode,
        "timestamp": time.strftime("%Y%m%dT%H%M%S"),
    }
    outp.write_text(json.dumps(rec, indent=2))
    return (cid, "ok" if p.returncode == 0 else f"rc={p.returncode}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--only", default=None)
    ap.add_argument("--matsya-bin", default=shutil.which("matsya") or "matsya")
    a = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    only = set(a.only.split(",")) if a.only else None

    jobs = []
    for path in sorted(CONCEPTS.glob("*.yml")):
        if path.name.startswith("_"):
            continue
        cid = path.stem
        if only and cid not in only:
            continue
        text = path.read_text()
        c = yaml.safe_load(text)
        cites = set(re.findall(r"cite-[A-Za-z0-9_]+", text))
        jobs.append((cid, build_prompt(c, cites)))

    print(f"atlas-review: {len(jobs)} concepts, {a.workers} workers "
          f"-> {OUT.relative_to(ROOT)}/", flush=True)
    n_ok = n_skip = n_fail = 0
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(run_one, a.matsya_bin, cid, pr, a.force): cid
                for cid, pr in jobs}
        for fut in as_completed(futs):
            cid, status = fut.result()
            print(f"  [{status:8s}] {cid}", flush=True)
            if status == "ok":
                n_ok += 1
            elif status == "skip":
                n_skip += 1
            else:
                n_fail += 1
    print(f"\nok {n_ok}, skipped {n_skip}, failed {n_fail}.")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
