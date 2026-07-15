#!/usr/bin/env python3
"""Emit the canonical-link registry for the paper's MyST anchors.

Scans the built MyST paper for every anchor and writes, at repo root:
  anchor-registry.json  and  anchor-registry.yml
mapping each anchor id -> {kind, title, html_id, canonical_url, md_ref}.

`canonical_url` is `{myst.yml project.url}#{lowercased id}`, read at runtime —
variant-agnostic and rename-proof. Root-relative throughout (identity + paths
come from _anchor_lib, which reads the @local/ markers). Exit 0 on success.

Usage:  python3 tools/anchor_registry.py
"""
from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _anchor_lib as A  # noqa: E402

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

_KIND = {
    "thm": "theorem", "lemm": "lemma", "lemma": "lemma", "prop": "proposition",
    "cor": "corollary", "def": "definition", "ass": "assumption", "claim": "claim",
    "clm": "claim", "fact": "fact", "remark": "remark", "rem": "remark",
    "eq": "equation", "fig": "figure", "table": "table", "sec": "section",
    "subsec": "section", "subsubsec": "section", "cite": "citation",
}

# A prf directive's title sits on its opening line; its :label: follows within
# a few lines. Capture (kind, title, id) so result/definition anchors carry the
# verbatim rendered title.
_PRF_RE = re.compile(
    r":::\{prf:(?P<kind>\w+)\}[ \t]*(?P<title>[^\n]*)\n"
    r"(?:[^\n]*\n){0,6}?:label:\s*(?P<id>[A-Za-z0-9_.\-]+)"
)


def _kind_from_prefix(anchor: str) -> str:
    return _KIND.get(anchor.split("-", 1)[0], "other")


def build_registry() -> dict:
    md = open(A.paper_md(), encoding="utf-8").read()
    prf = {m.group("id"): (m.group("kind"), m.group("title").strip())
           for m in _PRF_RE.finditer(md)}
    reg = {}
    for anchor in sorted(A.all_anchors(md)):
        if anchor in prf:
            kind, title = prf[anchor]
        else:
            kind, title = _kind_from_prefix(anchor), ""
        reg[anchor] = {
            "kind": kind,
            "title": title,
            "html_id": A.html_id(anchor),
            "canonical_url": A.canonical_url(anchor),
            "md_ref": f"{A.paper_md_rel()}#{anchor}",
        }
    return reg


def main() -> int:
    reg = build_registry()
    root = A.repo_root()
    out = {
        "_meta": {
            "generated_by": "tools/anchor_registry.py",
            "project": A.project_name(),
            "variant": A.variant_name(),
            "canonical_base": A.canonical_base(),
            "count": len(reg),
        },
        "anchors": reg,
    }
    with open(os.path.join(root, "anchor-registry.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False, sort_keys=True)
        fh.write("\n")
    if yaml is not None:
        with open(os.path.join(root, "anchor-registry.yml"), "w", encoding="utf-8") as fh:
            yaml.safe_dump(out, fh, sort_keys=True, allow_unicode=True, width=100)
    print(f"anchor-registry: {len(reg)} anchors -> anchor-registry.{{json,yml}}  "
          f"(canonical base {A.canonical_base()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
