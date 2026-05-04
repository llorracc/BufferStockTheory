# Concept atlas — vertical slice

A first slice of structured representation of the paper's economic
content as machine-readable YAML, rendered as a browsable wiki and
ready to feed into a RAG index alongside the paper itself.

## What's in the repo

Five committed deliverables:

- **`concepts/`** — five YAML concept files covering the four main
  conditions of the paper and its eponymous concept:
  growth-impatience-condition (GIC), return-impatience-condition
  (RIC), finite-human-wealth-condition (FHWC), finite-value-of-
  autarky (FVAC), and buffer-stock-target. Each is schema-validated
  and includes a defining equation, an English gloss, ~3-4 typed
  relations, and source anchors back into `BufferStockTheory.md`.
  Total: 19 typed cross-references between the five.
- **`concepts/_candidates.txt`** — auto-discovered list of 115
  candidate concepts in the paper, with co-occurrence clusters as a
  bootstrap for the relations layer. The 5 authored concepts came
  from this list; ~25 more obvious candidates remain.
- **`glossary/notation.yml`** — auto-derived from
  `mystmd-math-macros.yml`. 337 canonical entries, 32 synonym groups
  collapsed (e.g. `\Pat ≡ \APFac ≡ \APRte ≡ \Thorn` → one entry).
  76 entries (22.5%) have an auto-resolved `defining_equation`
  pointer. The English `gloss` field is the only hand-edited one
  and is empty for now — it is filled when a concept file cites the
  symbol.
- **`tools/`** — four Python scripts: `concepts_discover.py`,
  `glossary_build.py`, `concepts_validate.py`, `concepts_render.py`.
  Together they make adding a new concept a fixed-cost operation
  (validate + re-render) rather than per-concept tooling work.
- **`_build/concepts/`** — five mkdocs-friendly markdown previews
  rendered from the YAML. Cross-links resolve locally (concept
  pages link to each other) and back to the paper (each cited
  paper anchor is a link into `BufferStockTheory.md`).

## How to look at it

```bash
/usr/bin/python3 tools/concepts_validate.py     # → "OK: 5 concept(s) valid."
/usr/bin/python3 tools/concepts_render.py        # → 5 .md files + index.md
open _build/concepts/index.md                    # any markdown viewer
```

A representative rendered concept (excerpt):

```markdown
# Growth Impatience Condition (GIC)

## Defining equation
$$ \GPFacRaw < 1 $$
*The absolute patience factor falls short of the permanent income growth factor.*

## Relations
- **contrasts-with** [return-impatience-condition](return-impatience-condition.md) — …
- **implies** [finite-value-of-autarky](finite-value-of-autarky.md) — Under FHWC, GIC implies FVAC (claim-PFConspC).
- **assumed-by** [thm-MSSBalExists](../../BufferStockTheory.md#thm-MSSBalExists) — …
```

## Where this is going

The full plan is at `plans_private/20260503-1218h_index-bst-for-ai-
math.md` — five stages, ~63 hours total. Today's slice covers
fragments of stages 2 (glossary) and 3 (concepts); the immediate
next steps are:

- **Authoring the remaining ~25 concepts** from `_candidates.txt`.
  Per-concept budget is now ~10 minutes hand-edit time, since
  candidates are auto-discovered, defining equations are
  auto-located, and relations are bootstrapped from co-occurrence
  data.
- **Stage 0 — eval harness** (`evaluation/`). 20-question public
  benchmark to score `matsya` retrieval against. Without it, every
  later stage ships blind.
- **Stage 1 — equation-aware chunking** in `HARK_ask-your-project`'s
  build script. The single highest-leverage retrieval fix.

This slice exists to confirm the *shape* of the artifacts before
sustained engineering on the harness and chunker. If the framing
needs adjustment — different concept set, different schema fields,
different render target — now is the moment.
