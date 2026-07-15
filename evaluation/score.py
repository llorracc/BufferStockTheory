#!/usr/bin/env python3
"""score.py — compute source-recall, source-precision, answer-agreement.

Reads `evaluation/benchmark.yml` and every
`evaluation/responses/<id>.json`, computes per-question metrics:

  * source_recall    = |expected_chunks ∩ matsya_chunks| / |expected_chunks|
  * source_precision = |expected_chunks ∩ matsya_chunks| / |matsya_chunks|
  * answer_agreement = cosine(emb(matsya_response), emb(expected_answer))
                       (null if sentence-transformers not installed)

Aggregates per-category and overall means, writes a single summary JSON.

Also validates: every `expected_sources[*].anchor` in benchmark.yml
dereferences in `BufferStockTheory.md`. Exits non-zero on validation
failure even if scoring succeeds.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
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
PAPER = ROOT / "BufferStockTheory.md"

# Mirrors the regexes in tools/concepts_validate.py.
ANCHOR_RE = re.compile(r"^\(([a-zA-Z][^)]*)\)=$")
LABEL_RE = re.compile(r"^:label:\s+(\S+)\s*$")

VALID_CATEGORIES = {
    "definitions", "theorems", "conditions", "calibration", "cross-paper",
}


def collect_paper_anchors(paper_path: Path) -> set[str]:
    anchors: set[str] = set()
    for line in paper_path.read_text().splitlines():
        m = ANCHOR_RE.match(line)
        if m:
            anchors.add(m.group(1))
            continue
        m = LABEL_RE.match(line)
        if m:
            anchors.add(m.group(1))
    return anchors


def basename_from_matsya_path(path: str) -> str:
    """Reduce a matsya source path to the basename score.py compares on.

    matsya emits paths like
      `/root/HARK_ask-your-project/project/repos/BufferStockTheory/Tables/Comparison.tex`
      `project/repos/bellman-ddsl/docs/examples/HARK-models/ConsPerfForesight_mdp.md`
    We collapse to just the basename so that benchmark.yml entries
    only need to specify e.g. `Comparison.tex`. Future tightening can
    use full subpaths if a basename-collision turns up.
    """
    return path.rsplit("/", 1)[-1]


def validate_benchmark(entries: list[dict], paper_anchors: set[str]) -> list[str]:
    failures: list[str] = []
    seen_ids: set[str] = set()
    for i, e in enumerate(entries):
        ctx = f"benchmark.yml[{i}]"
        for k in ("id", "category", "question", "expected_answer",
                  "expected_sources", "expected_chunks"):
            if k not in e:
                failures.append(f"{ctx}: missing required field {k!r}")
        if "id" in e:
            if e["id"] in seen_ids:
                failures.append(f"{ctx}: duplicate id {e['id']!r}")
            seen_ids.add(e["id"])
            ctx = f"benchmark.yml[id={e['id']}]"
        if e.get("category") not in VALID_CATEGORIES:
            failures.append(f"{ctx}: category {e.get('category')!r} not in {sorted(VALID_CATEGORIES)}")
        srcs = e.get("expected_sources") or []
        if not isinstance(srcs, list) or not srcs:
            failures.append(f"{ctx}: expected_sources must be a non-empty list")
        else:
            for j, s in enumerate(srcs):
                if not isinstance(s, dict):
                    failures.append(f"{ctx}: expected_sources[{j}] must be a mapping")
                    continue
                f = s.get("file")
                a = s.get("anchor")
                if f != "BufferStockTheory.md":
                    failures.append(f"{ctx}: expected_sources[{j}].file must be 'BufferStockTheory.md' (got {f!r})")
                if not a or a not in paper_anchors:
                    failures.append(f"{ctx}: expected_sources[{j}].anchor {a!r} not found in BufferStockTheory.md")
        chunks = e.get("expected_chunks") or []
        if not isinstance(chunks, list) or not chunks:
            failures.append(f"{ctx}: expected_chunks must be a non-empty list")
    return failures


def get_embedder():
    """Return a callable str -> list[float], or None if unavailable."""
    try:
        from sentence_transformers import SentenceTransformer  # type: ignore
    except ImportError:
        return None
    try:
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    except Exception as e:
        print(f"warning: failed to load embedder ({e}); answer_agreement will be null",
              file=sys.stderr)
        return None
    def emb(text: str) -> list[float]:
        return model.encode(text, normalize_embeddings=True).tolist()
    return emb


def cosine(a: list[float], b: list[float]) -> float:
    # Embeddings are unit-normalised, so dot product = cosine.
    return float(sum(x * y for x, y in zip(a, b)))


def score_one(entry: dict, response: dict, embedder) -> dict:
    expected_chunks = set(entry["expected_chunks"])
    matsya_basenames = {basename_from_matsya_path(p) for p in response.get("parsed_sources", [])}
    inter = expected_chunks & matsya_basenames
    recall = len(inter) / len(expected_chunks) if expected_chunks else None
    precision = len(inter) / len(matsya_basenames) if matsya_basenames else None
    if embedder is not None and response.get("matsya_response"):
        try:
            a_emb = embedder(entry["expected_answer"])
            b_emb = embedder(response["matsya_response"])
            agreement: float | None = cosine(a_emb, b_emb)
        except Exception as e:
            print(f"warning: embedding failed for {entry['id']}: {e}", file=sys.stderr)
            agreement = None
    else:
        agreement = None
    return {
        "source_recall": recall,
        "source_precision": precision,
        "answer_agreement": agreement,
        "matsya_basenames": sorted(matsya_basenames),
        "expected_chunks": sorted(expected_chunks),
        "intersection": sorted(inter),
    }


def aggregate(per_q: dict[str, dict], by_category: dict[str, str]) -> dict:
    def mean(xs: list[float]) -> float | None:
        xs = [x for x in xs if x is not None]
        return statistics.mean(xs) if xs else None

    cats: dict[str, list[dict]] = {}
    for qid, scores in per_q.items():
        cats.setdefault(by_category[qid], []).append(scores)

    out = {"per_category": {}, "overall": {}}
    for cat, rows in cats.items():
        out["per_category"][cat] = {
            "n": len(rows),
            "source_recall": mean([r["source_recall"] for r in rows]),
            "source_precision": mean([r["source_precision"] for r in rows]),
            "answer_agreement": mean([r["answer_agreement"] for r in rows]),
        }
    rows = list(per_q.values())
    out["overall"] = {
        "n": len(rows),
        "source_recall": mean([r["source_recall"] for r in rows]),
        "source_precision": mean([r["source_precision"] for r in rows]),
        "answer_agreement": mean([r["answer_agreement"] for r in rows]),
    }
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", default=str(EVAL_DIR / "baseline.json"),
                   help="output JSON path (default: evaluation/baseline.json)")
    p.add_argument("--responses-dir", default=str(RESPONSES_DIR),
                   help="directory of per-question response JSON files")
    p.add_argument("--no-embed", action="store_true",
                   help="skip the answer_agreement metric even if sentence-transformers is installed")
    args = p.parse_args()

    if not BENCHMARK.exists():
        print(f"error: {BENCHMARK} not found", file=sys.stderr)
        return 2
    if not PAPER.exists():
        print(f"error: {PAPER} not found", file=sys.stderr)
        return 2

    paper_anchors = collect_paper_anchors(PAPER)
    entries = yaml.safe_load(BENCHMARK.read_text()) or []
    if not isinstance(entries, list):
        print(f"error: {BENCHMARK} must be a YAML list", file=sys.stderr)
        return 2

    failures = validate_benchmark(entries, paper_anchors)
    if failures:
        for line in failures:
            print(f"FAIL {line}", file=sys.stderr)
        print(f"\n{len(failures)} validation failure(s).", file=sys.stderr)
        return 1

    embedder = None if args.no_embed else get_embedder()
    if embedder is None and not args.no_embed:
        print("note: sentence-transformers not available; answer_agreement will be null",
              file=sys.stderr)

    by_category = {e["id"]: e["category"] for e in entries}
    per_q: dict[str, dict] = {}
    missing: list[str] = []
    for e in entries:
        rpath = Path(args.responses_dir) / f"{e['id']}.json"
        if not rpath.exists():
            missing.append(e["id"])
            continue
        response = json.loads(rpath.read_text())
        per_q[e["id"]] = score_one(e, response, embedder)

    if missing:
        print(f"warning: {len(missing)} question(s) with no response file: "
              f"{', '.join(missing[:5])}{'...' if len(missing) > 5 else ''}",
              file=sys.stderr)

    summary = {
        "n_questions": len(entries),
        "n_scored": len(per_q),
        "n_missing": len(missing),
        "missing_ids": missing,
        "per_question": per_q,
        "aggregates": aggregate(per_q, by_category),
        "embedder": "sentence-transformers/all-MiniLM-L6-v2" if embedder else None,
    }
    Path(args.out).write_text(json.dumps(summary, indent=2))
    print(f"wrote {args.out} ({summary['n_scored']}/{summary['n_questions']} scored)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
