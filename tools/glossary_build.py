#!/usr/bin/env python3
"""glossary_build.py — derive glossary/notation.yml from mystmd-math-macros.yml.

For every macro in `project.math` of mystmd-math-macros.yml:
  - capture the macro name and its expansion body
  - group macros that share the same body string (synonyms)
  - pick the canonical name per group: shortest, alpha-tiebroken
  - locate a `defining_equation` by scanning BufferStockTheory.md
    for the first `(eq-X)=` whose `$$ ... $$` block contains the
    macro literal

Output schema (one entry per canonical):

    - canonical: \\APFac
      body: 'Ϸ'
      synonyms: [\\Pat, \\APRte, \\Thorn]
      gloss: ''                       # hand-curated; deferred
      defining_equation: eq-AIC       # auto-resolved, may be null

`gloss` is the only hand-edited field. Re-running the script
preserves any existing `gloss` value by reading the prior
glossary/notation.yml first.
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
MACROS_SRC = ROOT / "mystmd-math-macros.yml"
PAPER_SRC = ROOT / "BufferStockTheory.md"
ALIASES_SRC = ROOT / "glossary" / "aliases.yml"
OUT = ROOT / "glossary" / "notation.yml"

# Pure typographic-decorator bodies. Macros that expand to one of these are
# pass-through decorators (\Foo{x} renders as a tilde/hat/etc. over x);
# multiple decorator-bodied macros sharing the same body are NOT semantic
# synonyms and should not be merged into a synonym group.
DECORATOR_BODIES = {
    "\\tilde", "\\check", "\\hat", "\\bar", "\\breve", "\\grave",
    "\\dot", "\\ddot", "\\widetilde", "\\widehat", "\\overline",
    "\\underline", "\\acute", "\\mathring",
}

ANCHOR_EQ_RE = re.compile(r"^\(eq-([A-Za-z0-9_-]+)\)=\s*$")
ANCHOR_LABELED_RE = re.compile(r"^\((eq|ass|thm|def|lemma|lemm|prop|claim|fact)-[A-Za-z0-9_-]+\)=\s*$")
PRF_OPEN_RE = re.compile(r"^:::\{prf:[a-z]+\}")
LABEL_RE = re.compile(r"^:label:\s+(\S+)\s*$")
MACRO_REF_RE = re.compile(r"\\([a-zA-Z]+)")


def load_macros() -> dict[str, str]:
    raw = yaml.safe_load(MACROS_SRC.read_text())
    return raw["project"]["math"]


def load_existing_glosses() -> dict[str, str]:
    if not OUT.exists():
        return {}
    try:
        existing = yaml.safe_load(OUT.read_text()) or []
    except yaml.YAMLError:
        return {}
    glosses: dict[str, str] = {}
    for entry in existing:
        if isinstance(entry, dict) and entry.get("canonical") and entry.get("gloss"):
            glosses[entry["canonical"]] = entry["gloss"]
    return glosses


def load_aliases() -> set[str]:
    """Read glossary/aliases.yml's `do-not-merge:` list, if present.

    Macros listed there are kept as their own canonical entry — the
    auto-grouper's body-hash equality is overridden. Use this for the
    cases where multiple paper macros happen to share a KaTeX body but
    refer to semantically distinct concepts (e.g., \\Theta is both
    \\TranShkAgg and \\TranShkEmp; \\phi is three different shocks).
    """
    if not ALIASES_SRC.exists():
        return set()
    try:
        data = yaml.safe_load(ALIASES_SRC.read_text()) or {}
    except yaml.YAMLError:
        return set()
    return set(data.get("do-not-merge", []) or [])


def group_synonyms(macros: dict[str, str], do_not_merge: set[str]) -> list[tuple[str, str, list[str]]]:
    by_body: dict[str, list[str]] = {}
    standalone: list[tuple[str, str]] = []
    for name, body in macros.items():
        if body.strip() in DECORATOR_BODIES or name in do_not_merge:
            standalone.append((name, body))
            continue
        by_body.setdefault(body, []).append(name)
    groups: list[tuple[str, str, list[str]]] = []
    for body, names in by_body.items():
        names_sorted = sorted(names, key=lambda n: (len(n), n))
        canonical = names_sorted[0]
        synonyms = names_sorted[1:]
        groups.append((canonical, body, synonyms))
    for name, body in standalone:
        groups.append((name, body, []))
    groups.sort(key=lambda g: g[0])
    return groups


def find_eq_blocks(paper_text: str) -> list[tuple[str, str]]:
    """Return [(eq-id, body)] for every `(eq-X)=` followed by a `$$ … $$` block.

    Linear scan: when we see `(eq-X)=`, hold X as the pending id until either
    (a) the next non-blank line opens with `$$`, in which case we capture the
    block body up to the closing `$$`; or (b) ~10 lines pass with no math
    block, in which case we drop the pending id (the anchor probably points
    to a `:::{math}` directive elsewhere).
    """
    lines = paper_text.splitlines()
    n = len(lines)
    out: list[tuple[str, str]] = []
    i = 0
    while i < n:
        m = ANCHOR_EQ_RE.match(lines[i])
        if not m:
            i += 1
            continue
        eq_id = m.group(1)
        j = i + 1
        skipped = 0
        while j < n and skipped < 10:
            stripped = lines[j].strip()
            if not stripped:
                j += 1
                skipped += 1
                continue
            if stripped.startswith("$$"):
                body_lines: list[str] = []
                k = j + 1
                if stripped != "$$":
                    body_lines.append(stripped[2:])
                while k < n:
                    if lines[k].rstrip().endswith("$$") or lines[k].strip() == "$$":
                        body_lines.append(lines[k].rsplit("$$", 1)[0])
                        break
                    body_lines.append(lines[k])
                    k += 1
                out.append((eq_id, "\n".join(body_lines)))
                i = k + 1
                break
            j += 1
            skipped += 1
        else:
            i += 1
            continue
        if i <= j:
            i = j + 1
    return out


def resolve_defining_eq(macro: str, eq_blocks: list[tuple[str, str]]) -> str | None:
    for eq_id, body in eq_blocks:
        if macro in body:
            return f"eq-{eq_id}"
    return None


def find_anchor_macro_associations(paper_text: str, macro_names: set[str]) -> dict[str, str]:
    """Scan the paper top-to-bottom; for each labeled anchor (eq-X, ass-X,
    thm-X, def-X, lemma-X, prop-X, claim-X, fact-X), record any macro
    mentioned in the following ~10 lines as having that anchor as its
    defining_equation. First anchor wins.

    Used as a fallback for macros that don't appear in an explicit
    `(eq-X)= ... $$ ... $$` block (which is many of them). The result is
    a coarser heuristic — a macro that appears in an assumption or
    theorem statement gets that block's label as its definition site.
    """
    lines = paper_text.splitlines()
    n = len(lines)
    out: dict[str, str] = {}
    for i, line in enumerate(lines):
        anchor = None
        m = ANCHOR_LABELED_RE.match(line)
        if m:
            anchor = line[1:line.index(")=")]
        elif PRF_OPEN_RE.match(line):
            for j in range(i + 1, min(i + 5, n)):
                ml = LABEL_RE.match(lines[j])
                if ml:
                    anchor = ml.group(1)
                    break
        if not anchor:
            continue
        for j in range(i + 1, min(i + 10, n)):
            for ref in MACRO_REF_RE.findall(lines[j]):
                full = "\\" + ref
                if full in macro_names and full not in out:
                    out[full] = anchor
    return out


def main() -> int:
    if not MACROS_SRC.exists():
        print(f"error: {MACROS_SRC} not found", file=sys.stderr)
        return 2
    if not PAPER_SRC.exists():
        print(f"error: {PAPER_SRC} not found", file=sys.stderr)
        return 2
    macros = load_macros()
    existing_glosses = load_existing_glosses()
    do_not_merge = load_aliases()
    paper_text = PAPER_SRC.read_text()
    eq_blocks = find_eq_blocks(paper_text)
    anchor_assocs = find_anchor_macro_associations(paper_text, set(macros.keys()))

    groups = group_synonyms(macros, do_not_merge)
    entries = []
    resolved = 0
    for canonical, body, synonyms in groups:
        # First try: precise eq-X-block-body match for canonical or any synonym.
        defining_eq = resolve_defining_eq(canonical, eq_blocks)
        if defining_eq is None:
            for syn in synonyms:
                defining_eq = resolve_defining_eq(syn, eq_blocks)
                if defining_eq:
                    break
        # Fallback: nearest-labeled-anchor association from prose scan.
        if defining_eq is None:
            defining_eq = anchor_assocs.get(canonical)
            if defining_eq is None:
                for syn in synonyms:
                    if syn in anchor_assocs:
                        defining_eq = anchor_assocs[syn]
                        break
        if defining_eq:
            resolved += 1
        entries.append({
            "canonical": canonical,
            "body": body,
            "synonyms": synonyms,
            "gloss": existing_glosses.get(canonical, ""),
            "defining_equation": defining_eq,
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w") as f:
        f.write("# glossary/notation.yml — auto-generated by tools/glossary_build.py\n")
        f.write(f"# {len(entries)} canonical entries derived from {len(macros)} macros\n")
        f.write(f"# defining_equation auto-resolved for {resolved}/{len(entries)} entries\n")
        f.write("# `gloss` is the only hand-edited field; re-running preserves it.\n\n")
        yaml.safe_dump(entries, f, sort_keys=False, allow_unicode=True, width=120)

    print(
        f"wrote {OUT.relative_to(ROOT)} ({len(entries)} canonical entries, "
        f"{resolved} with defining_equation, {len(macros) - len(entries)} synonyms collapsed)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
