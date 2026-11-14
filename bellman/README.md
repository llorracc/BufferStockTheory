# The Bellman description of the paper's models

This folder states models of *Theoretical Foundations of Buffer Stock Saving* in the language of
[Bellman](https://github.com/econ-ark/bellman-dev). A program that compares solutions of the paper's
models (a *comparator*) can read the models here, at a pinned commit of this repository, instead of
writing its own `.bl` and YAML files. The first such reader is the comparator of
`llorracc/wg1-buffer-stock`.

It is a prototype of a default place for a paper's Bellman description, proposed in
`econ-ark/bellman-dev` (`AI/working/CDC/13112026/a-default-place-for-a-papers-bellman-description.md`),
as an optional part of the REMARK standard. The folder is always `bellman/`, at the repository's
root.

## The models

| folder | the paper's model | where the paper states it | calibrations |
|---|---|---|---|
| `natural-borrowing-constraint/` | the problem with uncertainty, with its zero-income event, under the natural borrowing constraint | the subsection "Model with Uncertainty" | `baseline`: the table "Microeconomic Model Calibration" |
| `artificial-borrowing-constraint/` | the problem with uncertainty under an artificial borrowing constraint a ≥ a_Art | the subsubsection and the appendix "The Liquidity Constrained Solution as a Limit" | `restrained_consumer`: the same table, no unemployment event, a_Art = 0 |

Each model folder is laid out as Bellman's own model folders are (the page "Model directory layout"
of Bellman's documentation, `docs/Bellman-Sym/reference/model-directory-layout.md`). Each holds:
- one stage file, `declaration/stages/<stage>/<stage>.bl`;
- the paper's one default methods file beside it, `methods.bl`;
- one calibration file for each calibration the paper reports, under `declaration/calibration/`;
- the settings the methods file reads, under `declaration/settings/`.

`models.yml`, the manifest, names the Bellman commit the files elaborate under, the models with
their files and versions, and where the paper states each.

## Reading a model

With Bellman installed at the commit `models.yml` names, from this folder:

```python
from bellman.stage import elaborate_stage, load_stage

d = "natural-borrowing-constraint/declaration/"
stage = elaborate_stage(load_stage(d + "stages/natural/natural.bl"))
stage = stage.calibrate(d + "calibration/baseline.yml")
stage = stage.methodize(d + "stages/natural/methods.bl")
stage = stage.configure(d + "settings/natural.yml")
```

Both models elaborate, calibrate, methodize and configure this way under Bellman
`3937a8eb21b78d1d10313b829fcc6fdf6bb89052` (checked 2026-11-14).

Bellman's repositories (`econ-ark/bellman-dev`, and `econ-ark/bellman`) are private today
(2026-11-14). A reader outside them can't yet open the links above, or install Bellman at that
commit.

Where Bellman is not installed, Python imports this folder as an empty package named `bellman` when
it runs from the repository's root. A missing Bellman then shows up later as a confusing error, not
as "no module named bellman".

## The rules the files keep

- **The paper states its own model.** A calibration file holds the numbers the stage file binds, in
  Bellman's names, and no comparator's format. Each says in a comment how its numbers come from the
  paper's table; some are solved for.
- **The ids of a stage are kept.** A methods file written elsewhere may name this stage's places by
  their ids (`policy`, `E_ψ_ξ`, `dcsn_to_arvl`, ...). They change only with a new `version` of the
  model in `models.yml`, as do its free parameters.
- **The stage files are the comparator's two, as they stand.** Every line but the comments is the
  stage file of the family `bst-natural/1` or `bst-artificial/1` of `llorracc/wg1-buffer-stock` at
  `3901bc69`, so the comparator can read the paper's file in place of its own. They keep their names,
  `natural` and `artificial`. Each family is at least as wide as the paper's model, and the paper's
  model is a named calibration of it.
  - `artificial.bl` admits any limit a_Art ≤ 0 and an unemployment income ξ_u ≥ 0, where the
    paper's restrained consumer is the one point a_Art = 0 with no unemployment event.
  - `artificial.bl` also requires a_Art to lie above the natural limit, −h_min. It says so in words,
    and no line of this folder enforces it; the comparator's checker enforces it for its own members.
    The restrained consumer meets it.
- **One default methods file per stage.** It states the method the paper uses, the endogenous grid
  method, and names no toolkit's handler. A comparator's own methods files stay with the comparator.
- **The paper's rule of expectation is stated in a comment.** The rule is seven equiprobable points
  for the continuous part of each law, each point its bin's conditional mean. The language has no
  word for it, so the methods files write `!quadrature`, which names no rule, with the node counts as
  settings.

## The laws of the shocks, and checks against the paper

Each calibration states the shocks' laws as the appendix "Positive Minimum Income" constructs them
in its subsection "An Example":
- a lognormal of mean one, truncated at three standard deviations of its log;
- its standard deviation after truncation is the table's 0.1.

This agrees with the bounded support of the paper's assumption on the shocks.

The text's figures were computed by `BufferStockTheory.ipynb` under an old HARK, with laws that are
not truncated, so their numbers differ slightly from a solution of these calibrations.

The appendix's table "Positive Minimum Income at the Baseline Calibration" checks the problem with
uncertainty: in its column for an unemployment income of zero, consumption at resources of 1 is
0.853.

## What the paper states that is not yet described

- **Perfect foresight without liquidity constraints.** Bellman's perfect-foresight stage file
  (`applications/consumption-perfect-foresight-crra/declaration/stages/perfect_foresight/perfect_foresight.bl`)
  writes human wealth as h := 1/(1 − Γ/R). Chris's rule of 12 November 2026 bans that formula, and
  what an infinite-horizon stage writes in its place is not settled.
- **The restrained consumer of the appendix "Positive Minimum Income" with a positive unemployment
  income.** It is bounded by minus minimum human wealth, a bound sent back from the next period as a
  field. That needs specification 0.8 of Bellman, proposed and not built.
- **The variant "No borrowing" of that appendix.** Its assumption gives the permanent shock a point
  mass at its lowest value. `artificial.bl` draws the permanent shock with none, and `natural.bl`
  has no positive benefit.
- **Perfect foresight with liquidity constraints, and the treatments of mortality.** No stage file
  states them yet.
- **What no stage file can state.** The types of a population with their shares, the length of a
  period (the manifest gives it), and the validity conditions of the theory: the impatience
  conditions on the patience factors and the finite human wealth condition.

## Still open

- Whether the paper keeps these two families or narrower stage files that state exactly its models.
- Which models come next.
- Which word a default methods file can name for the paper's equiprobable rule.
