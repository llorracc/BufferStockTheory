# `glossary/`

Notation glossary, auto-derived from `mystmd-math-macros.yml`.

## Files

- `notation.yml` — every paper macro, grouped by synonym, with a
  defining-equation pointer where one could be auto-resolved.
- `README.md` — this file.

## Schema

Each entry is one canonical macro:

```yaml
- canonical: \Pat                   # auto: shortest name in body-hash group
  body: 'Ϸ'                          # the macro's expansion (verbatim from source)
  synonyms: [\APFac, \APRte, \Thorn] # auto: all macros sharing this body
  gloss: ''                          # HAND-EDITED. The only non-derived field.
  defining_equation: eq-AIC          # auto: first `(eq-X)=` block whose body
                                     # contains the canonical (or any synonym).
                                     # null if no match.
```

`gloss` is the only field a human edits. Re-running the build script
preserves any non-empty `gloss` value already present.

## Regenerating

```
/usr/bin/python3 tools/glossary_build.py
```

Inputs:

- `mystmd-math-macros.yml` — source of truth for the macro list (itself
  auto-emitted from `@resources/markdown/econark-shortcuts.md` plus
  `@local/local.sty` by `tools/build-myst/lib/math_macros.py`).
- `BufferStockTheory.md` — scanned for `(eq-X)=` blocks to populate
  `defining_equation`.

Output:

- `glossary/notation.yml` — overwritten in place; `gloss` values
  preserved across runs.

## Current numbers

- 337 canonical entries (from 379 raw macros)
- 32 synonym groups collapsed (42 macros folded into a canonical)
- 76 entries with auto-resolved `defining_equation` (22.5%)
- 0 hand-curated `gloss` entries (deferred — added one at a time as
  concept files cite them)

## Why additive, not destructive

`HARK_ask-your-project`'s `config/macros.json` currently rewrites
`\cNrm → "normalized consumption"` at index time, discarding the
LaTeX. A query mentioning `\cNrm` then can't match the indexed
chunk. The longer-term plan (Stage 2 of
`plans_private/20260503-1218h_index-bst-for-ai-math.md`) is to make
that substitution **additive** — keep both forms — driven by this
glossary. That work happens when we touch HARK_ask's build script;
for now this file is the source of truth for what gets substituted.
