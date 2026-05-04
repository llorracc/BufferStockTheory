#!/usr/bin/env python3
"""concepts_validate.py — validate every concepts/<id>.yml against the schema.

Checks (in order):
  1. id matches filename stem
  2. required fields present (id, name, defining_equation, gloss,
     relations, sources)
  3. defining_equation.anchor exists in BufferStockTheory.md
  4. every relations[*].kind is from the permitted enum
  5. every relations[*].target either:
       (a) is the id of another concepts/*.yml file, OR
       (b) is an anchor that exists in BufferStockTheory.md
  6. every sources[*].anchor exists in the named file
  7. no cycles in `implies` / `special-case-of` graphs

Exits 0 if all concepts pass (or if there are zero concepts).
Exits 1 with a diagnostic if any fail.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS_DIR = ROOT / "concepts"
PAPER = ROOT / "BufferStockTheory.md"

REQUIRED = {"id", "name", "defining_equation", "gloss", "relations", "sources"}
RELATION_KINDS = {
    "implies", "implied-by", "assumed-by", "requires",
    "contrasts-with", "special-case-of", "generalises", "calibrated-via",
}
ACYCLIC_KINDS = {"implies", "special-case-of"}

ANCHOR_RE = re.compile(r"^\(([a-zA-Z][^)]*)\)=$")
LABEL_RE = re.compile(r"^:label:\s+(\S+)\s*$")


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


def load_concepts(d: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for path in sorted(d.glob("*.yml")):
        if path.name.startswith("_"):
            continue
        try:
            data = yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            print(f"FAIL {path.name}: invalid YAML — {e}", file=sys.stderr)
            sys.exit(1)
        if not isinstance(data, dict):
            print(f"FAIL {path.name}: top-level must be a mapping", file=sys.stderr)
            sys.exit(1)
        out[path.stem] = data
    return out


def has_cycle(graph: dict[str, set[str]]) -> tuple[bool, list[str]]:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}
    parent: dict[str, str | None] = {n: None for n in graph}

    def dfs(n: str) -> list[str] | None:
        color[n] = GRAY
        for m in graph.get(n, ()):  # ignore edges to non-graph nodes
            if m not in color:
                continue
            if color[m] == GRAY:
                cycle = [m]
                cur = n
                while cur is not None and cur != m:
                    cycle.append(cur)
                    cur = parent[cur]
                if cur == m:
                    cycle.append(m)
                cycle.reverse()
                return cycle
            if color[m] == WHITE:
                parent[m] = n
                found = dfs(m)
                if found:
                    return found
        color[n] = BLACK
        return None

    for n in graph:
        if color[n] == WHITE:
            cyc = dfs(n)
            if cyc:
                return True, cyc
    return False, []


def main() -> int:
    if not CONCEPTS_DIR.exists():
        print(f"error: {CONCEPTS_DIR} not found", file=sys.stderr)
        return 2
    if not PAPER.exists():
        print(f"error: {PAPER} not found", file=sys.stderr)
        return 2

    paper_anchors = collect_paper_anchors(PAPER)
    concepts = load_concepts(CONCEPTS_DIR)
    if not concepts:
        print("OK: zero concepts to validate.")
        return 0

    failures: list[str] = []

    for stem, c in concepts.items():
        path = f"concepts/{stem}.yml"

        if c.get("id") != stem:
            failures.append(f"{path}: id ({c.get('id')!r}) must equal filename stem ({stem!r})")

        missing = REQUIRED - set(c.keys())
        if missing:
            failures.append(f"{path}: missing required fields: {sorted(missing)}")
            continue

        defeq = c["defining_equation"]
        if not isinstance(defeq, dict):
            failures.append(f"{path}: defining_equation must be a mapping")
        else:
            anchor = defeq.get("anchor")
            if not anchor:
                failures.append(f"{path}: defining_equation.anchor is required")
            elif anchor not in paper_anchors:
                failures.append(f"{path}: defining_equation.anchor {anchor!r} not found in BufferStockTheory.md")
            for k in ("latex", "english"):
                if not defeq.get(k):
                    failures.append(f"{path}: defining_equation.{k} is required")

        rels = c.get("relations") or []
        if not isinstance(rels, list):
            failures.append(f"{path}: relations must be a list")
            rels = []
        for i, rel in enumerate(rels):
            if not isinstance(rel, dict):
                failures.append(f"{path}: relations[{i}] must be a mapping")
                continue
            kind = rel.get("kind")
            tgt = rel.get("target")
            if kind not in RELATION_KINDS:
                failures.append(f"{path}: relations[{i}].kind {kind!r} not in {sorted(RELATION_KINDS)}")
            if not tgt:
                failures.append(f"{path}: relations[{i}].target is required")
            elif tgt not in concepts and tgt not in paper_anchors:
                failures.append(
                    f"{path}: relations[{i}].target {tgt!r} is neither a concept id "
                    f"nor a BufferStockTheory.md anchor"
                )

        sources = c.get("sources") or []
        if not isinstance(sources, list) or not sources:
            failures.append(f"{path}: sources must be a non-empty list")
        else:
            for i, s in enumerate(sources):
                if not isinstance(s, dict):
                    failures.append(f"{path}: sources[{i}] must be a mapping")
                    continue
                f = s.get("file")
                a = s.get("anchor")
                if f != "BufferStockTheory.md":
                    failures.append(f"{path}: sources[{i}].file must be 'BufferStockTheory.md' (got {f!r})")
                if not a or a not in paper_anchors:
                    failures.append(f"{path}: sources[{i}].anchor {a!r} not found in {f}")

    for kind in ACYCLIC_KINDS:
        graph: dict[str, set[str]] = {cid: set() for cid in concepts}
        for cid, c in concepts.items():
            for rel in (c.get("relations") or []):
                if isinstance(rel, dict) and rel.get("kind") == kind and rel.get("target") in concepts:
                    graph[cid].add(rel["target"])
        cyclic, cyc = has_cycle(graph)
        if cyclic:
            failures.append(f"cycle in {kind!r} relation: {' -> '.join(cyc)}")

    if failures:
        for line in failures:
            print(f"FAIL {line}", file=sys.stderr)
        print(f"\n{len(failures)} validation failure(s).", file=sys.stderr)
        return 1

    print(f"OK: {len(concepts)} concept(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
