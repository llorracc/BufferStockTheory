#!/usr/bin/env python3
"""concepts_freshness.py — guard against stale concept counts.

Asserts that three independently-maintained counts agree:
  1. authored concept YAMLs  (concepts/*.yml, excluding _-prefixed)
  2. rendered concept pages   (_ai/concepts/*.md, excluding _-prefixed + index.md)
  3. the "N concept(s) authored." number in _ai/concepts/index.md

Exit 0 if all agree, 1 (with a diagnostic) otherwise. This catches the drift the
orientation docs once suffered (status text claiming "5 concepts" while the atlas
held 42). Run it after adding/removing concepts and re-rendering.

Usage:  python3 tools/concepts_freshness.py
"""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _anchor_lib as A  # noqa: E402


def main() -> int:
    root = A.repo_root()
    cdir = os.path.join(root, "concepts")
    rdir = os.path.join(root, "_ai", "concepts")

    n_yaml = len([f for f in os.listdir(cdir)
                  if f.endswith(".yml") and not f.startswith("_")])

    rendered = ([f for f in os.listdir(rdir)
                 if f.endswith(".md") and not f.startswith("_") and f != "index.md"]
                if os.path.isdir(rdir) else [])
    n_rendered = len(rendered)

    n_index = None
    idx_path = os.path.join(rdir, "index.md")
    if os.path.isfile(idx_path):
        m = re.search(r"(\d+)\s+concept\(s\)\s+authored",
                      open(idx_path, encoding="utf-8").read())
        if m:
            n_index = int(m.group(1))

    if n_yaml == n_rendered == n_index:
        print(f"OK: concept counts agree — {n_yaml} YAML "
              f"= {n_rendered} rendered = {n_index} in index.md")
        return 0

    print("FAIL: concept counts disagree:", file=sys.stderr)
    print(f"  concepts/*.yml (non-_):        {n_yaml}", file=sys.stderr)
    print(f"  _ai/concepts/*.md (non-index): {n_rendered}", file=sys.stderr)
    print(f"  _ai/concepts/index.md says:    {n_index}", file=sys.stderr)
    print("  -> re-run tools/concepts_render.py, and update any status doc that "
          "hardcodes a different count.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
