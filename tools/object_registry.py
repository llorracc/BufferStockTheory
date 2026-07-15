#!/usr/bin/env python3
"""object_registry.py — derive the in-scope scholarly-object registry.

Reads the mechanical anchor-registry.yml (all resolvable anchors) and emits a
smaller, curated tier — object-registry.{yml,json} at repo root — containing only
the NAMED SCHOLARLY OBJECTS that belong in the mathematical concept graph:
theorems, lemmas, propositions, corollaries, definitions, assumptions,
properties, claims, facts, remarks, plus the named equations the concept atlas
actually references.

This lets an AI distinguish "all resolvable anchors" (anchor-registry, mechanical)
from "objects that belong in the concept graph" (object-registry, curated). It
does NOT modify anchor-registry.{yml,json}; the mechanical tier is preserved.

Root-relative and variant-agnostic (per project policy): no hardcoded paths.

Usage:  python3 tools/object_registry.py
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _anchor_lib as A  # noqa: E402

try:
    import yaml
except ImportError:
    print("error: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

# Named scholarly-object kinds, as classified by tools/anchor_registry.py.
SCHOLARLY_KINDS = {
    "theorem", "lemma", "proposition", "corollary", "definition",
    "assumption", "property", "claim", "fact", "remark",
}


def load_yaml(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def atlas_anchor_refs(concepts_dir: str) -> set[str]:
    """Every paper anchor the concept atlas references (defining equations,
    sources, and relation targets that name an anchor)."""
    refs: set[str] = set()
    for name in sorted(os.listdir(concepts_dir)):
        if not name.endswith(".yml") or name.startswith("_"):
            continue
        c = load_yaml(os.path.join(concepts_dir, name)) or {}
        de = (c.get("defining_equation") or {}).get("anchor")
        if de:
            refs.add(de)
        for s in (c.get("sources") or []):
            if isinstance(s, dict) and s.get("anchor"):
                refs.add(s["anchor"])
        for r in (c.get("relations") or []):
            if isinstance(r, dict) and r.get("target"):
                refs.add(r["target"])
    return refs


def main() -> int:
    root = A.repo_root()
    reg_path = os.path.join(root, "anchor-registry.yml")
    if not os.path.isfile(reg_path):
        print("error: anchor-registry.yml not found; run tools/anchor_registry.py first",
              file=sys.stderr)
        return 2
    reg = load_yaml(reg_path)
    anchors = reg.get("anchors", {})
    atlas_refs = atlas_anchor_refs(os.path.join(root, "concepts"))

    objects: dict[str, dict] = {}
    for aid, rec in anchors.items():
        kind = rec.get("kind", "other")
        in_atlas = aid in atlas_refs
        # In scope iff it's a named scholarly object, OR a named equation the
        # atlas itself leans on (bare eq- anchors are otherwise too numerous).
        if kind not in SCHOLARLY_KINDS and not (kind == "equation" and in_atlas):
            continue
        aliases = []
        if "-" in aid:
            bare = aid.split("-", 1)[1]
            if bare != aid and bare in anchors:
                aliases.append(bare)
        objects[aid] = {
            "kind": kind,
            "title": rec.get("title", ""),
            "html_id": rec.get("html_id", ""),
            "canonical_url": rec.get("canonical_url", ""),
            "md_ref": rec.get("md_ref", ""),
            "in_atlas": in_atlas,
            "aliases": sorted(set(aliases)),
            "needs_title": not rec.get("title"),
        }

    kinds = Counter(o["kind"] for o in objects.values())
    out = {
        "_meta": {
            "generated_by": "tools/object_registry.py",
            "derived_from": "anchor-registry.yml",
            "project": reg.get("_meta", {}).get("project"),
            "variant": reg.get("_meta", {}).get("variant"),
            "count": len(objects),
            "kinds": dict(sorted(kinds.items())),
            "in_atlas_count": sum(1 for o in objects.values() if o["in_atlas"]),
            "needs_title_count": sum(1 for o in objects.values() if o["needs_title"]),
            "note": ("In-scope named scholarly objects + atlas-referenced named "
                     "equations. A derived VIEW of anchor-registry.yml; the mechanical "
                     "registry is preserved separately. TODO: enrich the needs_title "
                     "entries (assumptions/properties/remarks whose prf directive "
                     "carried no rendered title) with curated titles before relying on "
                     "`title` for display."),
        },
        "objects": objects,
    }

    with open(os.path.join(root, "object-registry.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False, sort_keys=True)
        fh.write("\n")
    with open(os.path.join(root, "object-registry.yml"), "w", encoding="utf-8") as fh:
        yaml.safe_dump(out, fh, sort_keys=True, allow_unicode=True, width=100)
    print(f"object-registry: {len(objects)} in-scope objects "
          f"({out['_meta']['in_atlas_count']} in atlas, "
          f"{out['_meta']['needs_title_count']} need titles) -> "
          f"object-registry.{{json,yml}}")
    print(f"  kinds: {dict(sorted(kinds.items()))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
