# Grid design: final spec + the measured findings that forced it

**Status:** DESIGN CONCLUSIONS OF RECORD (2026-07-10/11, owner dialogue following the
G1 KILL). This document owns the post-KILL grid-design conversation: eight measured
findings, the agreed final scheme (owner-proposed, measurement-sharpened), and the
open items. Companion records: `grid_placement_design.md` (the killed candidate's
pre-registration), `grid_placement_p1_frontier_of_failure.md` (the KILL), the P1
harness `proto_grid_placement.py` (all measurements below ran against it and
`hark_egm_adapter.py` on the committed truth apparatus; consolidation into a single
verify script is open item 1).

---

(grid-sec-findings)=
## The findings ledger (each measured this arc, HS/CTOP/CCAP anchors)

Anchors and notation, once. **HS** = a calibration using the estimated parameters of a
representative high-school-educated household from HAFiscal; **CTOP** = the most patient
college-educated type from the same estimation; **CCAP** = the patience-ceiling college
calibration (the "GIC-cap" defined precisely in `final_proof`: an agent so patient that no
target level of wealth exists). Wealth is indexed by w̄ := m − 1 + h, perfect-foresight total
wealth in BST's notation (h = human wealth, the current period's income included; the bar
marks the optimist's upper-bound object, as in BST's c̄).

:::{prf:remark} F1 — Placement is a solved problem; `exp_mult` sits on the oracle.
:label: grid-rem-f1

Equidistribution
on the TRUE curvature (density ∝ √|c″| from the N=1024 truth solve — the optimum over
all placement rules for piecewise-linear interpolation, using unobtainable information)
ties `exp_mult` to 0–5% on the ergodic-L1 metric at every budget N_body ∈ {12,20,28,38}
(e.g. N=38: oracle 1.155e-3 vs exp_mult 1.204e-3). A theory-motivated alternative
(kink-anchored log spacing) lost by 4–5× — the near-optimal plateau is wide (the
equidistribution envelope property) but not infinitely wide. Consequence: the placement
SHAPE is frozen; all remaining leverage is in bounds, law, and tests.
:::

:::{prf:remark} F2 — The owner's mortality-adjusted stable points solve the pure-GIC anchor problem.
:label: grid-rem-f2

With perpetual-youth replacement (newborns at a=0 drawing the same transitory income),
the cross-sectional mean dynamics factor mortality EXACTLY as a return shave R → L·R in
the stable-point loci. Existence conditions become GIC-Mod-Liv /
[GIC-Raw-Liv](https://llorracc.github.io/BufferStockTheory-Latest/#giclivmoddefn) (the
latter = BST's mortality-adjusted growth impatience, the population-GPF<1 condition
already in `find_ergodic_distribution`).
Measured at the patience-ceiling college atom CCAP
([GIC-Mod](https://llorracc.github.io/BufferStockTheory-Latest/#gicmod) fails, unadjusted loci: Trg nonexistent, StE
340.9): **the L·R-adjusted balanced-growth root m̌_mort = 40.18 vs measured
neutral-measure ergodic mean 41.23** (2.5%, Jensen sign correct since a(m) is convex);
the Δm=0 version (59.4) anchors the raw-measure mean. The measure decides which locus
gets the shave: Harmenberg-neutral aggregation ⇒ E_N[ψ⁻¹]=1 ⇒ the StE locus.
:::

:::{prf:remark} F3 — Three distances that decouple.
:label: grid-rem-f3

LEVEL = rel_gap(m) (precautionary saving — the gap g between the perfect-foresight
consumption rule and c(m) — as a fraction of consumption; the corridor certificate);
FORM = local decay exponent
Q₂(m) vs min(1,q↑); NUMERICAL = solved-vs-truth error. At m≈3,500 (HS) the level gap
is still percent-scale while the form agrees to 10%; at a conventional top m≈42 the
level gap is 76% AND the measured exponent is ~1.1 vs true 0.38 (h-dominated log-log
geometry). Numerical error is 1e-4-grade throughout.
:::

:::{prf:remark} F4 — Corridor tops are deep at near-resonance; actual tail error is ~100× inside the corridor.
:label: grid-rem-f4

All three estimated anchors sit within 1% of the r=g knife-edge (λ_B =
1.0096/1.0026/0.9978). Certified-corridor tops in target units: K(1e-4) = 122,000 (HS)
/ 19,500 (CTOP) / 723 (CCAP closed-form). But the ACTUAL error of the theory-exponent
power-law tail from a tol=1e-1 handoff (m_top = 1,133 at HS): **4.1e-4** over
[m_top, 30·m_top] vs corridor 3.7e-2 — the corridor bounds any sane tail form-free;
the theory exponent delivers ~100× better than worst-case. Legacy exp tail: ~6× worse
where q↑<1.
:::

:::{prf:remark} F5 — Form convergence is unreachable; fitted exponents must not be trusted.
:label: grid-rem-f5

Q₂ agreement with min(1,q↑) to 10% needs m ≈ 3,200–3,800; to 5%, m ≈ 2×10⁶ (HS);
never in-window at CTOP/CCAP. Measured drift rates w̄^(−0.14/−0.18/−0.25) — the
resonance's long window (the amplitude-climb panel of `final_proof`'s
compactified-boundary figure, replayed in exponent space; approach
from BELOW at depth, the signed-subleading prediction). The stabilization variant
(|dQ/d ln w̄| small) certifies calm, not correctness: it triggers at a pseudo-exponent
20–40% from q (CCAP: a placid Q≈0.63 vs true 1). Consequence: the tail exponent is the
ONE object that must be imported from the theorem rather than measured —
[Prop-A0](#prop-imp-A0)'s clamp and the `guarded_fit` mode exist for exactly this.
:::

:::{prf:remark} F6 — Sparse tail knots self-contaminate; zero tail knots dominates.
:label: grid-rem-f6

With a dense
body and n_tail ∈ {1..8} log-spaced knots to the corridor top, the solved VALUES at
the sparse knots are wrong by 3–9% (their own EGM expectations interpolate across
e-fold-wide cells); body metrics are unaffected at HS and actively HURT at CCAP
(body-only M1 4.6e-3 beat body+8-tail 1.4e-2). A post-solve representation swap
(log-gap-in-log-w̄ between the same knots) cannot help — both representations are
capped by knot fidelity, not interpolation. The one clean knot is the body top
(1.2e-4), and the analytic theory tail from it delivers ~10% over the whole segment
(5× inside its own corridor). Consequence: NO tail knots, ever; the region between the
body and any deep consumer is served by the law. (In-solve transformed interpolation
could reclaim ~3× on tail knots only ≈ 10–20% total budget — not pursued.)
:::

:::{prf:remark} F7 — Local density tests at the target are false confidence.
:label: grid-rem-f7

Measured error near
the target exceeds the local piecewise-linear bound w²|c″|/8 (w the cell width) by 10–100× (propagated
solve error through the Euler operator dominates; the kink region is where error
originates). Consequence: test CONVERGENCE (a warm-started 2N re-solve + Richardson,
valid by the measured N⁻² rate), not density; plus the direct near-kink Euler panel
where the error actually originates.
:::

:::{prf:remark} F8 — Life cycle unifies through a backward amplitude recursion (OPEN: derive + validate).
:label: grid-rem-f8

At each age the gap decays with exponent EXACTLY 1 (a finite sum of
discounted premia), amplitude B_t = λ_t·B_{t+1} + F_t with B_T = 0; the
infinite-horizon problem is the recursion's fixed point, and its divergence (λ≥1)
IS the q↑≤1 regime switch. T−1 anchor = the one-period Arrow–Pratt premium.
Falsifiable check: w̄·g_t(w̄) → B_t age by age on dense finite-horizon solves.
:::

(grid-sec-the-spec)=
## THE SPEC (owner-proposed scheme, sharpened by F1–F8)

- **Placement:** stock `exp_mult` (never tuned — F1) from the (age-varying, HARK-
  automatic via BoroCnstNat_t) constraint bottom to a_max.
- **a_max (infinite horizon, once-and-for-all):** the wealth-mass-negligibility rule —
  the smallest top with negligible WEALTH-weighted mass above (agent-mass is the wrong
  measure: 0.66% of agents held 17.6% of wealth). Patience sensitivity enters
  automatically via ζ\* (tail exponent: 9.19 HS / 3.17 CTOP / none at cap), the
  mortality-adjusted anchors m̌_mort (F2) at the pure-GIC edge, and the most-patient-
  type-binds rule for heterogeneous populations (= the rule the existing
  `production_aMax` helper implements for the estimated calibrations, now with its
  theory). Constant grid (required by back-in-time-fast / Newton-FTI, TM
  methods, and estimation smoothness).
- **Life cycle:** same spec; adapt only on the backward-recursive theory objects
  (κ̲_t, h_t, B_t, BoroCnstNat_t — computable BEFORE each age's solve: no chicken-and-
  egg; h_t here follows HARK's `hNrm` convention, the PDV of income beyond the current
  period, i.e. one less than BST's age-t human wealth — the T-1 amplitude supplement
  writes its h_{T-1} in BST's convention, = `hNrm`_{T-1} + 1); one union-span constant grid
  unless profiling demands per-age.
- **Above a_max (a GIVEN, per the owner):** the power law — with the THEORY exponent
  min(1, q↑) (infinite horizon) or the recursive amplitude B_t/w̄ (life cycle); never
  the fitted exponent (F5).
- **Tests (always run, the owner's two regions):** (i) near-kink Euler-residual panel
  (direct, cheap — where error originates); (ii) self-convergence at the visited set
  (one warm-started 2N re-solve + Richardson — F7; model-revision-robust).
- **Reports (never gates):** corridor rel_gap(a_max), form distance |Q_fit/q − 1|
  (the honesty dial: 11% at HS's tol-1e-1 top, 37% at CCAP's), and the tail-law mode
  in use.
- Parameter count: a_min, the a_max rule's mass tolerance, N, two test tolerances —
  five interpretable numbers plus frozen shape and theorem-supplied law.

:::{prf:definition} F9 — The operator eigen-probe: a model-agnostic numerical estimator of q↑ (owner request: exponent computable when no closed form exists).
:label: grid-def-f9

The exponent
is the eigenvalue condition of the model's OWN one-period backward operator on
power-law perturbations of the PF line; measure it numerically: apply one
Euler-inversion step to the trial `c(m') = kappa*(m'+h-1) - eps*c(x0)*((m'+h-1)/x0)^(-s)`
(written with BST's h; the committed script's own `h` variable equals h−1),
difference two eps (isolates the linear response, cancels the premium), root-find
the unit multiplier. Grid-free (the trial is analytic — probe at x0 = 1e6..1e8),
hence immune to both diseases of estimation-from-solved-values (sparse-knot
contamination; pre-asymptopia). Validated (`verify_eigen_probe_checks.py`,
6/6): q^ matches the analytic q↑ to 5.6e-6 / 8.6e-6 / 5.0e-5 at HS/CTOP/CCAP
with depth-consistency ~1e-6. Trial normalization at the probe point is
load-bearing (an unnormalized eps*x^-s trial at depth is ~1e-40, beneath
float64 — the first implementation failed exactly there). Estimation FROM
SOLVED VALUES is confirmed unreliable even in its best form (two-term
A·w̄^−q + B·w̄^−1 fit on m-windows to 1e4: 15–40% off — with h ≈ 200 the
identifying w̄-variation is not in any reachable window). Reported open
question: outside GIC the probe (true finite-w̄ operator) and the analytic
(E)-root (idealized limit) disagree (4.68 vs 7.33 at beta*1.02); within
hypotheses they agree to 1e-5. Portability requirements: the PF asymptote
(kappa, h) + one backward step applied to a supplied next-period function —
i.e., anything a time-iteration solver already has. THE SPEC amendment: for
model variants without the analytic eigen-equation, the tail exponent comes
from this probe (the eigen-equation is the probe evaluated on paper).
:::

:::{prf:definition} F10 — The aXtraMax mass rule, made algorithmic (closes the "inconclusive aXtraMax conversations"): measure the wealth quantile; the closed form only covers; earlier estimation practice is reproduced as special cases of the explicit dial.
:label: grid-def-f10

The keystone object is the MORTALITY-AUGMENTED DUAL ROOT ζ_L, the unique ζ > 0
solving ``LivPrb · E[(Þ_Γ/ψ)^ζ] = 1``: at LivPrb = 1 it is the Kesten root ζ\*;
for LivPrb < 1 it EXISTS whenever an expanding branch exists (P(Þ_Γ/ψ > 1) > 0)
— including at the patience ceiling CCAP where ζ\* does not (mortality is what truncates the
patient tail; measured: ζ_L = 9.74 / 4.34 / 1.92 at HS / CTOP / CCAP, ordering
with patience as required). ζ_L > 1 ⟺ aggregate wealth finite = the existence
condition for a wealth-measure top; ζ_L → 1 means wealth concentration makes
any grid top economically arbitrary — refuse, don't grid.
The CLOSED-FORM Pareto inversion of ζ_L is a poor quantile estimator in exactly
the regimes that matter (measured seed/truth: 0.38× at HS — UNSAFE undershoot,
the quantile sits only ~3× the anchor so the tail regime has not begun; 128×
over at CCAP's ζ_L→1 hypersensitivity) — so it serves ONLY as the generous
covering-grid top for the measurement. THE RULE IS MEASURED: coarse solve →
deterministic neutral-measure stationary distribution with mortality reset
(the same kernel the F2 loci are exact for) → the (1−ε_w) WEALTH-weighted
a-quantile × small safety; certificate = re-measure on the final solve.
Measured quantiles (truth solves, cover 1e5):

| anchor | measure | ε=1e-2 | ε=1e-3 | ε=1e-4 |
|---|---|---|---|---|
| HS   | agent  | 2.4 | 3.1 | 3.8 |
| HS   | wealth | 2.8 | 3.6 | 4.3 |
| CTOP | agent  | 4.6 | 6.3 | 8.1 |
| CTOP | wealth | 5.6 | 7.6 | 9.8 |
| CCAP | agent  | 217 | 491 | 1,078 |
| CCAP | wealth | 679 | 2,206 | 7,108 |

The dial is now explicit where earlier practice chose it implicitly: the
agent-measure variant at conventional tolerances reproduces the quantile
definitions previously used to size the estimation grids, and the wealth measure
is the one the moment-consumers (Lorenz-type statistics) actually weight —
impatient atoms need only body-scale tops (HS ~4, CTOP ~10 even
wealth-weighted at 1e-4) while the binding patient atom's top is set by
(measure, ε_w) alone. With the theory tail law attached, wealth above the
grid is PRICED (corridor accuracy), not lost, so moderate ε_w (1e-2, cap-atom
top ≈ 700) induces wealth-moment bias of order 1e-5 of aggregate wealth.
Populations: max over atoms (most-patient binds).
Implementation: `pf_decay.aXtraMax_from_wealth_mass` (+ `dual_root(...,
LivPrb=...)`); validation battery `verify_wealth_mass_rule_checks.py`.
:::

:::{prf:definition} F11 — The C1 two-term attachment (owner ruling 2026-07-11: DEFAULT for explicit-exponent tails; motivation = SSJ-type Jacobian robustness).
:label: grid-def-f11

The owner
accepted the Jacobian case for slope-matching and ruled: keep the one-term tail
available, implement a two-term tail, make two-term the default, and name the
reason — guarding against Jacobian pathologies in SSJ-type (sequence-space
Jacobian) pipelines, where policy derivatives are primitive inputs and a C1 kink
at the attachment point makes them discontinuous for queries crossing the cut
(measured one-term kink at tol=1e-1 cuts: ~0.4% of κ at HS, ~2.9% UPWARD at CCAP
— the upward case also locally violates MPC-monotonicity).

Form and closed-form amplitudes: with ``z = (x+h−1)/(x_cut+h−1)`` (x an m-like grid
coordinate, h BST's human wealth), level gap ``G``
and fitted rate ``Q_fit = S·(x_cut+h−1)/G`` (``S`` = body slope minus κ) read at
the cut, ``gap(z) = A·z^(−Q) + B·z^(−(Q+1))`` with the two matching conditions
(level ``A+B=G``; slope ``Q·A+(Q+1)·B = Q_fit·G``) giving

$$
B = G\cdot(Q_{\mathrm{fit}} - Q), \qquad A = G\cdot(1 + Q - Q_{\mathrm{fit}}).
$$ (grid-eq-f11-amplitudes)

Collapse: ``Q_fit = Q ⟹ B = 0`` — the one-term tail is the exact special case.
Second exponent ``Q+1``, NOT the theory-subleading pair ``{min,max}(1,q↑)``:
that pair's spacing ``|q↑−1| → 0`` at resonance (every HAFiscal anchor is within
1% of the knife-edge, F4) ⟹ amplitude blow-up and catastrophic cancellation;
``Q+1`` is uniformly conditioned, and the second term is an ATTACHMENT
(boundary-layer) object absorbing exactly the one-term kink ``(Q−Q_fit)·G/p`` —
not an asymptotic claim (near resonance the true subleading has the log
structure of main-chain Lemma L11 anyway).

Properties (healthy knot ``G>0``, ``Q_fit>0``, ``A>0 ⟺ Q_fit<Q+1``): gap > 0
everywhere (c below the PF line); ``c′ > κ`` everywhere (the MPC floor is
preserved — the bracket ``Q·A + (Q+1)·B/z`` runs monotonically between
``Q_fit·G > 0`` and ``Q·A > 0``); concavity ``c″<0`` holds at the cut iff
``Q_fit ≥ Q/2`` (below that, a local convexity blip — document, don't guard);
leading exponent ``Q`` at depth. GUARD: ``Q_fit ≥ Q+1`` (``A ≤ 0``: the body
locally decays steeper than theory+1 — a coarse/broken top) ⟹ warn + one-term
fallback. Rescue case (``Q_fit ≤ 0``): attaches smoothly with ``B<0, A>G``;
inherits the body's sub-κ MPC on an initial segment (the C0 one-term rescue
instead "corrected" it with an upward kink; smooth inheritance is the C1-default
price, documented). Amplitude note: the deep amplitude is ``A = (1+Q−Q_fit)·G``
(≈12% under the one-term ``G`` at the HS tol=1e-1 handoff, where ``Q_fit≈0.5``
vs ``q=0.38``) — the reason the two-term battery accuracy band is pre-registered
at 1e-3 rather than inheriting the one-term 6e-4.

Life-cycle/infinite-horizon uniformity (owner ruling, same day): both settings
use this same form with one number changed — ``Q = min(1, q↑)`` infinite
horizon, ``Q = 1`` at every finite age; ``B_t``/``B_ψ`` stay diagnostic-only
(the continuity invariant removed amplitude-anchoring symmetrically).
:::

(grid-sec-open-items)=
## Open items

1. Consolidate the dialogue measurements (F1–F7) into a committed
   `verify_grid_design_checks.py` battery (they currently exist as inline session runs
   against the committed harness; each finding above states its construction).
2. Derive the exact (λ_t, F_t) of the F8 amplitude recursion; validate w̄·g_t(w̄) → B_t
   on dense life-cycle solves (T−1 Arrow–Pratt anchor; its closed form is recorded in
   [the T−1 amplitude supplement](#t1-prop-amplitude)); then it joins `pf_decay` as a
   per-age quantity next to the MPCmin/hNrm recursions.
3. HARK wiring of THE SPEC as a constructor + the two tests + the reports (a future
   small commit on the decay branch; the `mNrm_stable_points` helper with the L·R loci
   belongs in the same commit).
4. Union-vs-per-age grid profiling for life-cycle models (only if the union count is
   ever measured to be binding).
