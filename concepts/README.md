# `concepts/`

YAML "concept atlas" for the paper. Each `<id>.yml` is one economic
concept with its defining equation, an English gloss, typed
cross-references to other concepts, and source anchors back into
`BufferStockTheory.md`.

## Files

- `_schema.yml` — schema documentation: every permitted top-level
  field with an example. Read this first if you're authoring a new
  concept.
- `_candidates.txt` — auto-discovered list of all concept candidates
  in `BufferStockTheory.md` (115 entries; emitted by
  `tools/concepts_discover.py`). Each row is `id <TAB> line <TAB>
  kind <TAB> co-occurring-ids <TAB> context`.
- `<id>.yml` — one authored concept. Today's set:
  `growth-impatience-condition`, `return-impatience-condition`,
  `finite-human-wealth-condition`, `finite-value-of-autarky`,
  `buffer-stock-target`. ~25 candidates from `_candidates.txt`
  remain to be authored.

## Tooling

```
/usr/bin/python3 tools/concepts_discover.py    # refresh _candidates.txt
/usr/bin/python3 tools/concepts_validate.py    # lint every <id>.yml
/usr/bin/python3 tools/concepts_render.py      # write _build/concepts/<id>.md
```

`concepts_validate.py` is the one you'll run most. It checks every
required field, dereferences every `defining_equation.anchor` and
`sources[*].anchor` against the paper, confirms every
`relations[*].target` either names another concept file or names an
existing paper anchor, and rejects cycles in the `implies` /
`special-case-of` graphs. Exits 0 with zero concepts (so it's
runnable before any are authored).

## Adding a concept

1. Find the candidate in `_candidates.txt`. Note its line number and
   the co-occurring concept ids (the auto-bootstrap signal for
   relations).
2. Read the corresponding paragraph in `BufferStockTheory.md` and the
   surrounding `prf:assumption` / `prf:theorem` blocks.
3. Copy `_schema.yml` to `<id>.yml` and fill in the fields. The id
   must equal the filename stem.
4. `tools/concepts_validate.py` should pass.
5. `tools/concepts_render.py` to see the rendered preview.

## Plans

The full 5-stage plan is at `plans_private/20260503-1218h_index-bst-
for-ai-math.md`; today's vertical slice is at `plans_private/
20260503-1228h_today-vertical-slice-deliverable.md`. The pitch
document for the coauthor demo is `CONCEPT-ATLAS-PROGRESS.md` at
the repo root.
