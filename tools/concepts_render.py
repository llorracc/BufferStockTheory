#!/usr/bin/env python3
"""concepts_render.py — render concepts/*.yml to _build/concepts/*.md.

For each `concepts/<id>.yml` we emit `_build/concepts/<id>.md` with:

  - H1 title (the `name` field)
  - the `defining_equation`: a `$$ … $$` block plus the English paraphrase
  - the `gloss` (multi-paragraph body)
  - a "Relations" section: bulleted list of typed edges, each `target`
    rendered as a markdown link to either another concept page (when the
    target is a concept id) or to the paper anchor (when it's an `eq-X`,
    `ass-X`, `thm-X`, etc.)
  - a "Sources" section: links back to the paper

Also emits `_build/concepts/index.md` — a single-page table of contents
listing every concept with the kinds of relations that originate from it.

The output is plain CommonMark with `$$ … $$` math fences. Any markdown
viewer with KaTeX/MathJax will render it. Cross-links are local
relative paths.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "concepts"
OUT = ROOT / "_build" / "concepts"
PAPER_URL = "../../BufferStockTheory.md"  # relative from _build/concepts/<id>.md


def unwrap_paragraphs(text: str) -> str:
    """Join hard-wrapped lines into one line per paragraph.

    Paragraphs are separated by blank lines. Within a paragraph, lines
    are joined with a single space — except when a line ends with `-`,
    in which case the next line joins with no separator so authored
    hyphenated wraps (`buffer-\\nstock` → `buffer-stock`) survive.
    Math line-wraps inside `$...$` are not expected; if they happen the
    same rule applies and is usually fine.
    """
    paragraphs: list[list[str]] = []
    current: list[str] = []
    for line in text.splitlines():
        if line.strip() == "":
            if current:
                paragraphs.append(current)
                current = []
        else:
            current.append(line.rstrip())
    if current:
        paragraphs.append(current)
    out = []
    for p in paragraphs:
        joined = p[0]
        for line in p[1:]:
            if joined.endswith("-"):
                joined += line.lstrip()
            else:
                joined += " " + line.lstrip()
        out.append(joined)
    return "\n\n".join(out)


def load_concepts() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for path in sorted(SRC.glob("*.yml")):
        if path.name.startswith("_"):
            continue
        out[path.stem] = yaml.safe_load(path.read_text())
    return out


def render_target_link(target: str, concept_ids: set[str]) -> str:
    if target in concept_ids:
        return f"[{target}]({target}.md)"
    return f"[`{target}`]({PAPER_URL}#{target})"


def render_concept(concept: dict, concept_ids: set[str]) -> str:
    out: list[str] = []
    name = concept["name"]
    short = concept.get("short")
    out.append(f"# {name}")
    out.append("")
    if short and short != name and short not in name:
        out.append(f"*Short form: **{short}***")
        out.append("")

    defeq = concept["defining_equation"]
    out.append("## Defining equation")
    out.append("")
    anchor = defeq.get("anchor")
    if anchor:
        out.append(f"Anchor: [`{anchor}`]({PAPER_URL}#{anchor})")
        out.append("")
    out.append("$$")
    out.append(defeq["latex"])
    out.append("$$")
    out.append("")
    if defeq.get("english"):
        out.append(f"*{defeq['english']}*")
        out.append("")

    gloss = concept.get("gloss", "").strip()
    if gloss:
        out.append("## Gloss")
        out.append("")
        out.append(unwrap_paragraphs(gloss))
        out.append("")

    rels = concept.get("relations") or []
    if rels:
        out.append("## Relations")
        out.append("")
        for rel in rels:
            kind = rel.get("kind", "?")
            tgt = rel.get("target", "?")
            note = rel.get("note", "").strip()
            link = render_target_link(tgt, concept_ids)
            line = f"- **{kind}** {link}"
            if note:
                line += f" — {note}"
            out.append(line)
        out.append("")

    sources = concept.get("sources") or []
    if sources:
        out.append("## Sources")
        out.append("")
        for s in sources:
            f = s.get("file", "BufferStockTheory.md")
            a = s.get("anchor", "")
            out.append(f"- [{f}#{a}](../../{f}#{a})")
        out.append("")

    bd = concept.get("bellman_ddsl") or {}
    if bd:
        perch = bd.get("perch") or "(none)"
        stage = bd.get("stage") or "(none)"
        out.append("## bellman-ddsl correspondence")
        out.append("")
        out.append(f"- perch: `{perch}`")
        out.append(f"- stage: `{stage}`")
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def render_index(concepts: dict[str, dict]) -> str:
    out: list[str] = ["# Concept atlas — index", ""]
    out.append(f"{len(concepts)} concept(s) authored.")
    out.append("")
    for stem, c in sorted(concepts.items()):
        name = c["name"]
        short = c.get("short", "")
        out.append(f"## [{name}]({stem}.md)")
        out.append("")
        gloss_text = (c.get("gloss") or "").strip()
        if gloss_text:
            first_para = unwrap_paragraphs(gloss_text).split("\n\n", 1)[0]
            out.append(f"> {first_para}")
            out.append("")
        rels = c.get("relations") or []
        if rels:
            kinds = sorted({r.get("kind", "?") for r in rels})
            out.append(f"Relations: {', '.join(kinds)} ({len(rels)} edges)")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    concepts = load_concepts()
    if not concepts:
        print("no concepts to render.", file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    cids = set(concepts.keys())
    rendered = 0
    for stem, c in concepts.items():
        out_path = OUT / f"{stem}.md"
        out_path.write_text(render_concept(c, cids))
        rendered += 1
    index_path = OUT / "index.md"
    index_path.write_text(render_index(concepts))
    print(f"rendered {rendered} concept(s) to {OUT.relative_to(ROOT)}/ "
          f"(+ index.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
