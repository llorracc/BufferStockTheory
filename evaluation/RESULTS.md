# Benchmark results & stage ledger

Closed-loop record for the `evaluation/` matsya retrieval benchmark. See
`README.md` for how the harness works and `benchmark.yml` for the 20 questions.

> ⚠️ **Do not overwrite `baseline.json`** without explicit domain-expert
> re-blessing. It is the fixed pre-improvement reference; every stage is a
> delta against it.

## Metrics & environment

- `source_recall` / `source_precision` — retrieval metrics. **Model-independent**:
  they score matsya's `Sources:` block, not its answer text. So the LLM model
  (`claude-opus-4-7` vs `-4-8` vs `claude-fable-5`) does not affect them.
- `answer_agreement` — cosine similarity of answer vs. gold, via
  `sentence-transformers/all-MiniLM-L6-v2`. **Requires `sentence-transformers`,
  which is NOT installed in the current local environment** → `answer_agreement`
  is `null` in any local `--no-embed` re-score. The baseline's agreement numbers
  were captured in an environment where the embedder was available.

## Stage ledger

| stage | date | commit | index state | recall | precision | agreement | file |
|---|---|---|---|---|---|---|---|
| baseline (v2) | 2026-05-03 | `e6fbf8b4` | initial droplet index | 0.658 | 0.146 | 0.644 | `baseline.json` |
| rerun (current index) | 2026-06-23 | this branch | **unchanged** droplet index | 0.608 | 0.132 | null (no embedder) | `stage-2026-06-23-current-index.json` |

Stages 1–4 of the master plan
(`plans_private/20260503-1218h_index-bst-for-ai-math.md`) — equation/table-aware
chunking, additive macro substitution, concept-graph indexing, rendered-page
indexing — **were never shipped to the matsya index**, so no stage files exist
for them.

## Commands

```sh
# fresh responses (--out-dir keeps the baseline responses intact)
python3 evaluation/run_benchmark.py --force --out-dir evaluation/responses/<run>
# score into a STAGE file (never baseline.json); --no-embed since no local embedder
python3 evaluation/score.py --no-embed --responses-dir evaluation/responses/<run> --out evaluation/<stage>.json
```

## 2026-06-23 rerun — interpretation

Run against the **current, unchanged** matsya droplet index (the owner declined
an index rebuild this session). Per-category recall:
definitions 0.750→0.750, theorems 0.875→0.750, conditions 0.875→0.875,
calibration 0.167→0.167, cross-paper 0.625→0.500.

The overall dip (0.658→0.608) is **within run-to-run retrieval variance**: only
q08 and q19 moved (1.0→0.5), and both still retrieve their primary expected
chunk — they lost a secondary chunk this run. The signal that matters: **nothing
improved, because the index is the same stale artifact.** It still indexes files
the current `.ragignore` excludes (`BufferStockTheory-NoAppendix.tex`,
`Appendices-All-Referenced.pdf`), lacks table-aware chunking, and does not index
the rendered `_ai/concepts/*.md` pages (which RAG Option C now calls for).

## Known unresolved failures

| q | category | recall | cause | note |
|---|---|---|---|---|
| q13 (`\CRRA` value) | calibration | 0.00 | table content invisible to prose embeddings; wrong-repo param files retrieved | `plans_private/20260623-1900h_calibration-root-cause.md` |
| q15 (permshk σ) | calibration | 0.00 | same; pulls `Calibration.tex` (wrong file) not BST `Comparison.tex` | same |
| q17 (DDSL perches) | cross-paper | 0.00 | DDSL bridge deferred + over-specific expected chunk | `plans_private/20260623-1905h_ddsl-cross-paper-root-cause.md` |
| q06 (MPC lemma proof) | theorems | 0.50 | embedding-level (macro-heavy proof scores low under NL phrasing) | `plans_private/20260503-2213h_q06-root-cause.md` |
| q18 (Szeidl) | cross-paper | 0.50 | retrieves main body, misses `Introduction.tex` | — |

## RAG Option C status (in-repo half only)

Policy decided this session: index **both** source `concepts/*.yml` and rendered
`_ai/concepts/*.md`, tagged by `artifact_kind`. The `.ragignore` edit is the
in-repo half. The **external droplet index rebuild + a before/after benchmark are
deferred** (owner declined the rebuild). Until then there is no
`stage-rendered-concepts.json`, and the index does not yet honor even the current
`.ragignore`.

## TODO (to actually move the numbers)

- [ ] Ship master-plan **Stage 1** (table-atomic + key-value flattening) on the
      matsya / `HARK_ask-your-project` side — the targeted fix for calibration
      recall (0.167 → ≥0.667 target).
- [ ] Rebuild the droplet index honoring the current `.ragignore` (drops
      `NoAppendix`/PDF noise) **and** Option C (adds tagged rendered concept pages).
- [ ] Re-run the benchmark; record `stage-rendered-concepts.json`; compare.
- [ ] Install `sentence-transformers` to restore `answer_agreement`.
- [ ] Resolve q17: clarify it tests cross-repo retrieval (done in `benchmark.yml`),
      and either author a minimal DDSL bridge or relax its expected chunk.
