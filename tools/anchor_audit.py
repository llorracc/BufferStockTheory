#!/usr/bin/env python3
"""Per-object anchor truth table for the atlas.

For every authored concept, report whether its `defining_equation.anchor`
actually resolves in the built MyST paper, plus its html id and canonical URL.
Exits non-zero if any concept's defining anchor is missing from the build
(an "in-scope gap"). Root-relative; identity + URL via _anchor_lib.

Usage:
  python3 tools/anchor_audit.py            # human table
  python3 tools/anchor_audit.py --format json
"""
from __future__ import annotations

import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _anchor_lib as A  # noqa: E402

try:
    import yaml
except ImportError:  # pragma: no cover
    raise SystemExit("anchor-audit: PyYAML is required")


def audit() -> list[dict]:
    md_anchors = A.all_anchors(open(A.paper_md(), encoding="utf-8").read())
    rows = []
    for path in sorted(glob.glob(os.path.join(A.repo_root(), "concepts", "*.yml"))):
        if os.path.basename(path).startswith("_"):
            continue
        c = yaml.safe_load(open(path, encoding="utf-8")) or {}
        anchor = (c.get("defining_equation") or {}).get("anchor", "")
        present = anchor in md_anchors
        rows.append({
            "id": c.get("id", os.path.basename(path)[:-4]),
            "anchor": anchor,
            "in_myst": present,
            "html_id": A.html_id(anchor) if anchor else "",
            "canonical_url": A.canonical_url(anchor) if anchor else "",
        })
    return rows


def main() -> int:
    rows = audit()
    gaps = [r for r in rows if not r["in_myst"]]
    if "--format" in sys.argv and "json" in sys.argv:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:
        print(f"{'concept-id':42} {'anchor':26} {'in_myst':8} canonical_url")
        for r in rows:
            print(f"{r['id']:42} {r['anchor']:26} "
                  f"{'OK' if r['in_myst'] else 'MISSING':8} {r['canonical_url']}")
    print(f"\n{len(rows)} concepts; {len(gaps)} anchor gap(s)"
          + (": " + ", ".join(r["id"] for r in gaps) if gaps else ""))
    return 1 if gaps else 0


if __name__ == "__main__":
    raise SystemExit(main())
