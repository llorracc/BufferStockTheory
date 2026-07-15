# Atlas Review — Machine Pre-Review Summary

> **ADVISORY — machine pre-review only.** Primary: **matsya + Opus-4.8** (`evaluation/atlas_review.py`); plus an **independent Opus-4.8 per-concept cross-check against the full paper**. **NOT** domain-expert sign-off; `concepts/_review-status.yml` stays **`pending`**. **External-literature claims were NOT verifiable** (sources unavailable to the machine judges); each is `flagged-for-expert`.
>
> **UPDATE 2026-06-23** — after author fixes + (A) polishes, the 3 prior `overstated` concepts and 4 prior `minor-issues` concepts now read `faithful`; **0 overstated remain**.

## Tallies (42 concepts)

- **overall:** 26 faithful · 16 minor-issues · 0 overstated
- **priority:** 0 high · 24 normal · 18 low
- **matsya:** 35 partial · 7 disagree · external-lit 16 flagged-for-expert

## Ranked concerns (most-concerning first)

| # | Concept | Overall | Gloss | Relations | Ext-lit | matsya | Top issue |
|--:|---|---|---|---|---|---|---|
| 1 | `buffer-stock-target` | faithful | faithful | faithful | none | disagree | NO correctness problems found in the gloss or relations; every claim verifies against the authoritative BufferStockTheory.md. |
| 2 | `hiraguchi-continuity` | faithful | faithful | minor-issues | flagged-for-expert | disagree | GLOSS IS FAITHFUL; matsya's 'overstated' verdict is false-skepticism. |
| 3 | `nondegenerate-limiting-solution` | faithful | faithful | faithful | flagged-for-expert | disagree | NO substantive error found in the entry. |
| 4 | `absolute-impatience-condition` | minor-issues | minor-issues | minor-issues | flagged-for-expert | partial | CITATION MISATTRIBUTION (confirmed; the real defect). |
| 5 | `absolute-patience-factor` | minor-issues | minor-issues | faithful | none | partial | 'The various patience conditions are all comparisons of APFac to one of *four* fundamental rates (1, Rfree, PermGroFac, PermGroFacAdj)' undercounts. |
| 6 | `consumption-c2-properties` | minor-issues | faithful | minor-issues | none | partial | the edge 'implies -> value-function-c3' is mistyped. |
| 7 | `consumption-function-c2-concave` | minor-issues | faithful | minor-issues | flagged-for-expert | partial | defining_equation and gloss say properties hold 'for each t'/'for every t', matching the paper proposition verbatim (BufferStockTheory.md:672). |
| 8 | `finite-human-wealth-condition` | minor-issues | minor-issues | faithful | none | partial | 'FHWC is the natural counterpart to the consumer's no-Ponzi condition' is an AI interpretive label not grounded in the paper's own language. |
| 9 | `growth-patience-factor` | minor-issues | minor-issues | faithful | none | partial | 'When the ratio is below 1 ... the wealth-to-permanent-income ratio drifts down' is stated UNCONDITIONALLY for raw GIC. This is only rigorously true (… |
| 10 | `limiting-consumption-strictly-positive` | minor-issues | minor-issues | minor-issues | none | partial | the edge `implies -> limiting-mpcs-lemma` is pointed at the wrong concept. |
| 11 | `maximal-mpc-at-most-one` | minor-issues | faithful | minor-issues | flagged-for-expert | partial | the `implied-by -> WRIC` edge targets node id `WRIC`, but no atlas node has id `WRIC` (the node file is `weak-return-impatience-condition.yml`, id `we… |
| 12 | `modified-growth-patience-factor` | minor-issues | minor-issues | faithful | none | partial | 'Equivalently (after a Jensen rearrangement), $\GPFacMod = \Ex[\APFac/(\PermGroFac \permShk)]$' mis-attributes the step to Jensen. |
| 13 | `mpc-bounds-convergence` | minor-issues | faithful | minor-issues | flagged-for-expert | partial | GLOSS is paper-faithful on all substantive claims (verified against the FULL proof, which IS in BufferStockTheory.md lines 2310-2349, not just 'See Ap… |
| 14 | `pseudo-target-existence` | minor-issues | minor-issues | faithful | none | partial | Gloss line 11 coins 'level-gap function' for $\difFunc(\mNrm_t):=\Ex_t[\permShk_{t+1}\mNrm_{t+1}]-\mNrm_t$. |
| 15 | `return-impatience-condition` | minor-issues | minor-issues | minor-issues | none | partial | the edge `generalises -> weak-return-impatience-condition` has the WRONG kind. |
| 16 | `return-patience-factor` | minor-issues | minor-issues | faithful | none | partial | the clause 'the consumer is willing to forgo enough consumption today to let interest accumulate, so wealth is being drawn down rather than building u… |
| 17 | `sequence-convergence-fact` | minor-issues | minor-issues | minor-issues | none | partial | GLOSS (line 13, 'no uniform convergence of the f^n is needed'): interpretive addition not stated in the paper. |
| 18 | `strong-growth-impatience-condition` | minor-issues | minor-issues | faithful | none | partial | MATSYA IS WRONG on its primary flag (false-skepticism). |
| 19 | `weak-return-impatience-condition` | minor-issues | minor-issues | faithful | none | partial | The clause 'RIC implies WRIC, but not the reverse, whenever $\pZero > 0$' uses the wrong threshold for the strict-weakness/non-reverse claim. |
| 20 | `boyd-weighted-contraction` | faithful | faithful | faithful | flagged-for-expert | partial | NONE that are errors. The gloss is paper-faithful throughout; logging the items below as notes and as explicit corrections to matsya's verdict. |
| 21 | `contraction-mapping-consumption-bounds` | faithful | faithful | faithful | flagged-for-expert | partial | NO correctness problems found; every gloss claim is supported by the full paper text. |
| 22 | `limiting-mpcs-lemma` | faithful | faithful | minor-issues | flagged-for-expert | partial | matsya's HEADLINE objection (gloss 'omits the FHWC hypothesis the paper explicitly uses for the minimal-MPC limb') is FALSE SKEPTICISM from a stale RA… |
| 23 | `nondegenerate-solution-existence` | faithful | faithful | minor-issues | flagged-for-expert | partial | GLOSS is paper-faithful throughout. |
| 24 | `ric-gives-stationary-contraction` | faithful | faithful | minor-issues | none | partial | GLOSS faithful. The defining_equation is a near-verbatim transcription of the remark (BufferStockTheory.md L850: 'Under return impatience, MPCmin_{T-n… |
| 25 | `boundfunc-weighted-space` | faithful | faithful | faithful | flagged-for-expert | disagree | — |
| 26 | `gic-implies-harmenberg-impatience` | faithful | faithful | faithful | flagged-for-expert | disagree | NO CORRECTNESS PROBLEM FOUND - concept is paper-faithful. |
| 27 | `norm-implies-compactness` | faithful | faithful | faithful | none | disagree | matsya FALSE-SKEPTICISM #1 (overturned): matsya flagged 'the paper notes convexity/openness not strictly necessary' as an unsupported attribution 'not… |
| 28 | `stochastic-discount-factor-mst` | faithful | faithful | minor-issues | flagged-for-expert | disagree | The 'special-case-of -> eq-veqnNrmRecBellman' edge has the general/special poles modeled via a proxy node. |
| 29 | `asymptotic-consumption-growth-factors` | faithful | faithful | faithful | none | partial | the requires->return-patience-factor note writes '$\Rfree\RPFac\DiscFac^{0}=\APFac$'; the dangling $\DiscFac^{0}$ is meaningless and could be dropped. |
| 30 | `buffer-stock-target-existence` | faithful | faithful | minor-issues | none | partial | the `implies -> eq-stability` edge targets a raw paper equation anchor (BufferStockTheory.md line 959, `(eq-stability)=`), not an atlas concept node —… |
| 31 | `compactness-preserved` | faithful | faithful | minor-issues | none | partial | 'requires -> norm-implies-compactness'. |
| 32 | `consumption-ratio-nondecreasing` | faithful | faithful | minor-issues | none | partial | GLOSS is faithful on independent full-text check. |
| 33 | `feasible-correspondence-not-compact` | faithful | faithful | minor-issues | flagged-for-expert | partial | the edge `contrasts-with -> Stationary-Bellman-Operator` is loosely typed. |
| 34 | `finite-value-of-autarky` | faithful | faithful | faithful | flagged-for-expert | partial | — |
| 35 | `growth-impatience-condition` | faithful | faithful | faithful | none | partial | — |
| 36 | `no-ric-no-gic-implies-no-fvac` | faithful | faithful | faithful | flagged-for-expert | partial | — |
| 37 | `pf-constrained-solution-exists` | faithful | faithful | faithful | none | partial | No correctness problems found. Every gloss claim is verbatim-supported by the full paper text: two-regime characterization = prop-PFCExist (BufferStoc… |
| 38 | `pf-consumption-function-properties` | faithful | faithful | faithful | none | partial | — |
| 39 | `pf-unconstrained-requires-fhwc` | faithful | faithful | minor-issues | none | partial | the `requires -> ass-pfincome` edge would be better typed as an `assumes`/`assumed-by`-style edge. |
| 40 | `pseudo-target` | faithful | faithful | faithful | none | partial | No correctness defects found. The gloss is paper-faithful on every checked claim: defining equation matches eq-mBalLvl (BufferStockTheory.md:1016) ver… |
| 41 | `target-ordering-part-one` | faithful | faithful | minor-issues | none | partial | the two `implies` edges -> pseudo-target and -> buffer-stock-target describe an ORDERING of two points (mBalLvl weakly below mTrgNrm), not a strict lo… |
| 42 | `value-function-c3` | faithful | faithful | faithful | none | partial | — |

### Where the independent cross-check overturned matsya

`matsya_agreement = disagree`: matsya downgraded these from **RAG-retrieval gaps (its index misses the appendix proofs)**, not defects; the full-paper cross-check found each **faithful**.

- `buffer-stock-target`
- `hiraguchi-continuity`
- `nondegenerate-limiting-solution`
- `boundfunc-weighted-space`
- `gic-implies-harmenberg-impatience`
- `norm-implies-compactness`
- `stochastic-discount-factor-mst`

### External-literature claims to verify against primary sources

`external_lit_status = flagged-for-expert` — the paper's in-text characterization was verified; the underlying source was unavailable to the machine judges.

- `hiraguchi-continuity`
- `nondegenerate-limiting-solution`
- `absolute-impatience-condition`
- `consumption-function-c2-concave`
- `maximal-mpc-at-most-one`
- `mpc-bounds-convergence`
- `boyd-weighted-contraction`
- `contraction-mapping-consumption-bounds`
- `limiting-mpcs-lemma`
- `nondegenerate-solution-existence`
- `boundfunc-weighted-space`
- `gic-implies-harmenberg-impatience`
- `stochastic-discount-factor-mst`
- `feasible-correspondence-not-compact`
- `finite-value-of-autarky`
- `no-ric-no-gic-implies-no-fvac`
