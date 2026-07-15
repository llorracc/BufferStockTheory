# `evaluation/` — matsya retrieval benchmark for BufferStockTheory

This is the load-bearing measurement infrastructure for the
"index BST for AI math" workstream (Stage 0 of
`plans_private/20260503-1218h_index-bst-for-ai-math.md`). It issues
a fixed set of 20 hand-authored questions to `matsya`, captures
both the raw answer and the cited chunk paths, and computes three
scores per question — source recall, source precision, and answer
agreement — plus per-category and overall aggregates. The first
run is captured as `baseline.json`; later changes (equation-aware
chunking, additive macro substitution, more concepts, wiki
integration) are measured as deltas against this baseline.

## Files

- `benchmark.yml` — the 20 questions in YAML, organised by
  category. Authoring shape documented in `benchmark_schema.yml`.
- `benchmark_schema.yml` — annotated schema for one entry; not
  consumed by tooling, only by humans.
- `run_benchmark.py` — issues each question to `matsya --BST`,
  captures stdout, parses the "Sources:" block, writes
  `responses/<id>.json` per question. Idempotent.
- `score.py` — validates anchors against `BufferStockTheory.md`,
  computes per-question metrics, writes a single summary JSON.
- `baseline.json` — the first scored run, captured as the
  pre-improvement reference. Do not regenerate without re-blessing
  by the domain expert.
- `responses/` — per-question raw matsya output (gitignored except
  for `.gitkeep`; regenerable by re-running `run_benchmark.py`).

## How to re-run

```sh
python evaluation/run_benchmark.py            # ~10-20 min for 20 questions with --think
python evaluation/score.py                    # writes evaluation/baseline.json
```

The runner skips questions whose `responses/<id>.json` already
exists; pass `--force` to overwrite, or `--only <id1>,<id2>` to
run a subset.

## How to add a question

1. Append a new entry to `benchmark.yml` following the shape in
   `benchmark_schema.yml`. The `id` must be unique; conventionally
   `q<NN>-<category-prefix>-<short-slug>`.
2. Each `expected_sources[*].anchor` must be a real `(X)=` or
   `:label:` anchor in `BufferStockTheory.md`. `score.py` validates
   this and exits non-zero on failure.
3. `expected_chunks` lists the `.tex` / `.md` basenames matsya
   should pull from when answering the question — these are
   matched against the basenames of paths in matsya's `Sources:`
   block to compute source recall and precision.
4. The domain expert must review the gold-standard `expected_answer`
   before any new baseline is captured (otherwise the metric measures
   what `matsya` agrees with, not what the paper says).

## How to compare a new run against the baseline

After a stage-1 change (e.g. equation-aware chunking on the matsya
side), regenerate responses and score them into a stage-tagged
output:

```sh
python evaluation/run_benchmark.py --force
python evaluation/score.py --out evaluation/stage1.json
```

Eyeball the per-category aggregates in
`stage1.json` against `baseline.json`. The plan target for stage 1
is ≥10% improvement in the `definitions` and `theorems` categories.

## Metrics

For each question:

- **`source_recall`** = |expected_chunks ∩ matsya_basenames| / |expected_chunks|
  — fraction of intended source files matsya actually retrieved.
- **`source_precision`** = |expected_chunks ∩ matsya_basenames| / |matsya_basenames|
  — fraction of matsya's retrieved chunks that came from intended
  sources. Low precision means matsya is pulling from many
  irrelevant files; high precision with low recall means matsya
  is focused but missing the right material.
- **`answer_agreement`** = cosine similarity of
  `sentence-transformers/all-MiniLM-L6-v2` embeddings of matsya's
  response vs. the gold-standard `expected_answer`. `null` if
  `sentence-transformers` is not installed locally — source recall
  and precision still work without it. Pass `--no-embed` to skip
  even when it is installed.

Aggregates report the mean of each metric per category and overall.

## Categories

Five categories, four questions each:

- **definitions** — what does symbol/term X mean?
- **theorems** — what does theorem T require / prove / depend on?
- **conditions** — relationships among GIC / RIC / FVAC / FHWC
  and their stronger / weaker siblings.
- **calibration** — numerical parameter values used in the paper.
- **cross-paper** — bridge questions to bellman-ddsl and to the
  income-fluctuation literature.

## Source-matching scope

`expected_sources[*].anchor` is validated against
`BufferStockTheory.md` (which is the `myst`-rendered form of the
paper). `expected_chunks` lists `.tex` / `.md` basenames because
matsya operates on the underlying source files, not on the
rendered Markdown. When a future matsya version exposes
chunk-level provenance back to specific anchors, the
`expected_sources` field can become directly load-bearing for
scoring; until then, it serves as the human-validated grounding
for the gold-standard answer.
