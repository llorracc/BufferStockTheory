#!/usr/bin/env python3
"""review_status.py — report the concept-atlas review queue.

Reads concepts/_review-status.yml and prints a summary plus the pending review
queue ordered by priority, so the 29 new glosses (and the external-literature
claims) are easy to prioritise. Read-only. Exit 0.

Usage:  python3 tools/review_status.py
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _anchor_lib as A  # noqa: E402

try:
    import yaml
except ImportError:
    print("error: PyYAML required", file=sys.stderr)
    sys.exit(2)

DIMS = ("gloss", "relations", "external_literature")


def main() -> int:
    path = os.path.join(A.repo_root(), "concepts", "_review-status.yml")
    if not os.path.isfile(path):
        print("error: concepts/_review-status.yml not found", file=sys.stderr)
        return 2
    data = yaml.safe_load(open(path, encoding="utf-8")) or {}
    concepts = data.get("concepts", {})
    meta = data.get("_meta", {})

    def pending(c):
        return any(c.get(k) == "pending" for k in DIMS)

    pend = {cid: c for cid, c in concepts.items() if pending(c)}
    high = sorted(cid for cid, c in pend.items() if c.get("priority") == "high")
    normal = sorted(cid for cid, c in pend.items() if c.get("priority") != "high")

    print(f"Concept review status — {len(concepts)} concepts; "
          f"{len(pend)} with pending review")
    warn = meta.get("WARNING") or meta.get("warning")
    if warn:
        print(f"  ! {warn}")
    print()
    print(f"HIGH priority pending ({len(high)}):")
    for cid in high:
        c = concepts[cid]
        cites = ",".join(c.get("cites") or []) or "-"
        print(f"  [{str(c.get('tier','?')):8s}] {cid:42s} "
              f"ext-lit={str(c.get('external_literature','?')):8s} cites={cites}")
    print()
    print(f"NORMAL priority pending ({len(normal)}):")
    for cid in normal:
        print(f"  [{str(concepts[cid].get('tier','?')):8s}] {cid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
