# Statement: power-law decay of the buffer-stock consumption gap (Stage A: ψ≡1)

**Status:** candidate theorem set with proof draft (`stage_A_proof.md`). Every claim carries its
ledger status from `00_THEOREM_PLAN.md`. Notation follows Carroll's buffer-stock papers
([BST](https://llorracc.github.io/BufferStockTheory-Latest/)). Lemmas are cited by number
(L0, L1, …, from the proof documents); primes (e.g. L9′) mark strengthened variants.
**Reading this for the first time? Start with [`final_proof_myst`](final_proof_myst.md)** — the
synthesis presentation of record (compactified boundary-fixed-point core, full economics
literature fabric, BST terminology, illustrative figures on HAFiscal's estimated
calibrations); it imports every proof body by reference from the four proof documents.

---

(st-sec-model)=
## 1. Model and assumptions

A consumer solves the infinite-horizon income-fluctuation problem

    max E₀ Σ_{t≥0} β^t L^t · Γ_t-normalized CRRA utility,   u(c) = c^{1−ρ}/(1−ρ)  (ρ>0; ρ=1 is log),

in permanent-income-normalized form: given market resources `m > 0` (beginning of period,
including current income), choose consumption `c ∈ (0, m]` (equivalently end-of-period assets
`a = m − c ≥ 0`), with next-period normalized resources

$$
m' = (R/\Gamma) \cdot a + \theta'.
$$ (st-eq-lom)

**Assumptions.**

- **(A1)** `u′(c) = c^{−ρ}`, `ρ > 0`.
- **(A2)** Constant gross return `R > 0`, constant permanent-income growth factor `Γ > 0`,
  discount factor `β ∈ (0,1)`. (Survival probability `L ∈ (0,1]` may be folded into `β`; see
  Remark 9.)
- **(A3)** `{θ_t}` i.i.d., `E[θ] = 1`, `σ² := Var(θ) ∈ (0, ∞)`, with **bounded support**
  `supp θ ⊆ [θ_min, θ_max]`, `0 ≤ θ_min < 1 < θ_max < ∞` — the bounded-support, mean-one
  transitory clause of BST's Friedman–Muth income process
  ([Assumption 1](https://llorracc.github.io/BufferStockTheory-Latest/#ass-shocks)). (In BST the
  zero-income event `θ = 0` w.p. `℘ > 0` is part of the maintained income-process assumption;
  here `θ_min = 0` is permitted throughout, the results of §§2–4 hold with or without the atom,
  and §5's constraint-end results require the worst-atom mass `℘ > 0`, which enters the maximal
  MPC `κ̄ = 1 − ℘^{1/ρ}Þ_R` directly. For unbounded θ see Remark 8.) No permanent shocks:
  `ψ ≡ 1` (Stage A).
- **(A4)** **FHWC** ([finite human wealth](https://llorracc.github.io/BufferStockTheory-Latest/#ass-fhwc)): `ℛ := R/Γ > 1`.
- **(A5)** **RIC** ([return impatience](https://llorracc.github.io/BufferStockTheory-Latest/#ass-ric)): `Þ_R := (βR)^{1/ρ}/R < 1`; write `κ̲ := 1 − Þ_R ∈ (0,1)`.
- **(A6)** **GIC** ([growth impatience](https://llorracc.github.io/BufferStockTheory-Latest/#gicraw)): `Þ_Γ := (βR)^{1/ρ}/Γ < 1`. (Note `Þ_Γ = ℛ·Þ_R`; under
  FHWC, GIC neither implies nor is implied by RIC.) — *Not needed for Proposition A0.*
- **(A0)** The problem admits a unique solution `c: (0,∞) → (0,∞)` with the standard properties
  (continuous, strictly increasing, `0 < c(m) ≤ m`; Euler equation with equality wherever
  `a(m) > 0`; `c` is the globally-stable fixed point of the Coleman–Reffett operator).
  [PROVEN-CITED: under A1–A6 the conditions
  [FVAC](https://llorracc.github.io/BufferStockTheory-Latest/#fvac) and
  [WRIC](https://llorracc.github.io/BufferStockTheory-Latest/#wric) of Carroll (*Theoretical Foundations of
  Buffer Stock Saving*, Quantitative Economics; henceforth BST) hold — `stage_A_proof.md` §1 shows
  GIC+FHWC ⟹ FVAC and RIC ⟹ WRIC — and existence/uniqueness/stability also follow from
  Li–Stachurski 2014 JEDC / Ma–Stachurski–Toda 2020 JET 187 (CITE-CHECK on the exact hypothesis
  mapping is flagged in the ledger).]

(st-def-derived-objects)=
**Derived objects.**

    h  := 1/(1−ℛ⁻¹) = R/(R−Γ)    (normalized human wealth, current income included — BST eq-HDef)
    w̄  := m − 1 + h              (perfect-foresight total wealth, human and market — the optimist's wealth)
    c̄(m) := κ̲·(m−1+h) = κ̲·w̄     (BST's perfect-foresight consumption function eq-cFuncPFUnc; the asymptote)
    g(m) := κ̲·(m−1+h) − c(m)     (THE GAP; g ≥ 0 by Prop. A0/L2; we write g(w̄) for g as a function of w̄)
    s(m) := c̄(m) − c(m) = g(w̄)   (precautionary saving)
    Λ  := ln(1/Þ_Γ) > 0          (the log-ladder step)
    q↑ := ln(ℛ)/Λ  > 0           (the transitory-only Kesten root, eq. (E0) of the derivation)

Here `h` is BST's human wealth
([eq-HDef](https://llorracc.github.io/BufferStockTheory-Latest/#eq-hdef)): its PDV series starts at
the current period's income, so the future-income-only quantity, where genuinely needed, is `h − 1`.
`w̄ := b + h = m − 1 + h` is **perfect-foresight total wealth (human and market)** — the wealth of the
optimist, viewed at the decision moment after this period's returns have been realized on the kapital
saved last period (`b = ℛa = m − 1` is BST's bank balances). The bar marks the optimist's / upper-bound
object, matching BST's own perfect-foresight bound `c̄(m) = (m − 1 + h)κ̲`
([eq-cFuncPFUnc](https://llorracc.github.io/BufferStockTheory-Latest/#eq-cfuncpfunc)) and the
Method-of-Moderation convention (bar = optimist, underline = pessimist, as in `κ̲`); `w` is unused in
BST, so there is no clash. `s(m) := c̄(m) − c(m)` is **precautionary saving** — the same object as the
gap, expressed in `m`: `s(m) = g(w̄)`.

`q↑` is equivalently the unique positive root of `Þ_Γ^{−q} = ℛ` — the ψ≡1 case of the eigenvalue
equation (E): `E[ψ^{1+q}] = ℛ·Þ_Γ^q`.

---

(st-sec-results)=
## 2. Results

:::{prf:proposition} Proposition A0 (no exponential decay — GIC-free). [PROVEN; proof body OWNED by `exponential_impossibility.md` (standalone, self-contained, weaker hypotheses); review-verified R1 §6a: 14-calibration battery incl. a GIC-VIOLATING calibration, min margin 4232×]
:label: st-prop-A0

Under A0–A5 (GIC not needed) there are explicit `c₋ > 0` and `w̄_A0 < ∞` such that

$$
g(\wbar) \geq c_{-} \cdot \sigma^2 \cdot \wbar^{-1} \qquad \text{for all } \wbar \geq \wbar_{A0}.
$$ (st-eq-A0)

Consequently `liminf w̄·g(w̄) ≥ c₋σ² > 0`: **exponential decay `g ≍ e^{−Bm}` — indeed ANY
`o(1/w̄)` decay — is impossible for every calibration in the class** (scope note for Γ < 1
existence: see the owner document §1/X5). Full proof, the stronger corollary, the
one-paragraph practical-implication statement, and the numerical battery:
`exponential_impossibility.md`.

:::

:::{prf:theorem} Theorem A1 (the power law: two-sided order). [PROVEN-HERE, L5–L7, L11; review-verified R2 (full re-derivation + 52/52 pointwise constant audit on 4 models incl. θ=0-atom and exact-resonance)]
:label: st-thm-A1

Under A0–A6 and σ² > 0 there are constants `0 < c ≤ C < ∞` (explicitly constructible from the
primitives — the q↑<1 lower constant via chaining Prop. A0 at the ladder base, repair per review
R2 F-3; the explicit constants are deliberately crude, see Remark 7) and `w̄_A1 < ∞` such that
for all `w̄ ≥ w̄_A1`:

  (i)   if `q↑ > 1`:   `c·σ²·w̄^{−1} ≤ g(w̄) ≤ C·w̄^{−1}`;
  (ii)  if `q↑ < 1`:   `c·w̄^{−q↑} ≤ g(w̄) ≤ C·w̄^{−q↑}`;
  (iii) if `q↑ = 1`:   `c·σ²·w̄^{−1}·ln w̄ ≤ g(w̄) ≤ C·w̄^{−1}·ln w̄`.

In particular the **leading exponent is `min(1, q↑)`** (with a log correction exactly at the
resonance `q↑ = 1`), and `g` is O-regularly varying with both Matuszewska indices equal to
`−min(1,q↑)` in cases (i)–(ii). **The (iii) resonance case now has a SHARP constant**
(2026-07-06): `w̄·g(w̄)/ln w̄ → κ̲(ρ+1)σ²/(2Λ)` — the ψ≡1 corollary of Stage-B Theorem B-res
(L11-const closed; see §3).

:::

:::{prf:theorem} Theorem A2 (sharp form for q↑ < 1: the Kesten channel). [PROVEN-HERE, L9; review-verified R3 incl. a constants-level measurement of the telescope increment. P's fine structure (constancy; oscillation size) is NOT required here — owned by `periodic_factor_fine_structure.md`]
:label: st-thm-A2

Under A0–A6, σ² > 0 and `q↑ < 1` there is a **positive, Lipschitz, Λ-periodic** function
`P: ℝ → [c, C]` such that

$$
g(\wbar) = \wbar^{-\qup} \cdot ( P(\ln \wbar) + O(\wbar^{-(1-\qup)}) ) \qquad \text{as } \wbar \to \infty.
$$ (st-eq-A2)

Equivalently `g(w̄) = w̄^{−q↑}P(ln w̄) + O(w̄^{−1})` — the second (income/forcing) channel appears
exactly at the predicted order `w̄^{−1}`. The amplitude object `P` is determined by the boundary
data of `g` at the edge of the linearization region (moderate w̄) and is not available in closed
form. `P` is genuinely (generically) NON-constant — so `g` is O-regularly varying but NOT
regularly varying (cf. the lattice caveat in renewal theory: Beare–Toda Remark 2.3 vs their
eq. (1.5); Kevei 2017).

**The FINE STRUCTURE of `P` (whether it is constant; how large its oscillation) is NOT required
for this or any theorem here, and is factored out to the standalone appendix
`periodic_factor_fine_structure.md`** (same discipline as `exponential_impossibility.md`). In
brief: non-constancy is measured (R3, `osc(P)/P̄ ≈ e^{−α/Λ}`, where `osc(P) := sup P − inf P` is
the oscillation — the total amplitude — of the log-periodic prefactor `P`, and `P̄` its mean) and
reduced to an explicit Fourier
criterion (generic non-constancy is a theorem; universal is probably false — tiling obstruction);
the oscillation size has a PROVEN unconditional linear bound `osc(P) ≤ Λ·TV(P′)/6` (⟹ effective
constancy on the grids of the estimated calibrations — all the application needs) and an open
sharp exponential bound.
See the appendix.

:::

:::{prf:theorem} Theorem A3 (sharp form and closed-form amplitude for q↑ > 1: the income channel). [PROVEN-HERE mod F1 (F2 since TRANSCRIBED), L10; review-verified R4: independent re-derivation with NO (I)-identity imposed and ASYMMETRIC atoms; 6 new calibrations to ≤0.2%; μ₃ proven to enter only one order deeper]
:label: st-thm-A3

Under A0–A6, σ² > 0 and `q↑ > 1`:

$$
\lim_{\wbar \to \infty} \wbar \cdot g(\wbar) = B, \qquad B = \kap \cdot (\rho+1) \cdot \sigma^2 / ( 2 \cdot (\Rcal \cdot \ThornG - 1) ) > 0.
$$ (st-eq-A3)

So `g` is genuinely regularly varying of index −1 — no lattice caveat — and the amplitude is a
closed-form *prudence (Jensen) coefficient*: `ρ(ρ+1)/2` is the second-order Taylor coefficient of
`u′` (relative prudence ρ+1, times ρ/2), and the `1/(ℛÞ_Γ−1)` factor is the resolvent of the
renewal sum, diverging as `q↑ ↓ 1` (crossover/resonance). Two flags in `stage_A_proof.md` §8:
F1 = the compounded constant bookkeeping of the L4→L10 chain (now machine-verified: the exact
rearrangement identity and the B-formula are independently reproduced by a CAS from the raw Euler
equation — appendix §2); F2 = citation transcription for L0/L1 — since TRANSCRIBED AND MAPPED
(stage_A §8 flag table + stage_B §B11; residuals bibliographic only). Neither is structural.
[Numerical status: CONFIRMED to 0.2% at the guard-clean depth — independent-EGM deep-tail
measurement at case A, m = 3e4 (g/c ≈ 8e-10, comfortably above the 1e-10 fp64 cancellation
guard; the previously-quoted m = 1e5 point sits marginally below the guard and is kept only as
corroboration, per review R2 F-9): w̄·g = 0.02811/0.02975/0.03117 vs
B(Var(θ_disc)) = 0.02805/0.02970/0.03111 at N_θ = 11/21/81 (amplitude tracks each
discretization's own Var(θ), ∝ σ² as claimed). Review R4 independently confirms B at six new
calibrations (ρ ∈ {0.7, 1.5, 2, 5}, q↑ ∈ {1.3, 2, 5}) to ≤ 0.2%, under strong skew of both signs
and a θ=0 atom to ≤ 0.03%, with the (8.1)-residual ≤ 1e-6 certifying a and c_J jointly on the
real solution. HARK 0.17 agrees to ~5%, and that residual is **grid/interpolation bias, not
solve tolerance** (correction per R4 A3-5b: tightening tol 1e-6 → 1e-12 changes nothing;
aXtraCount 800 → 3000 collapses the excess to +1% — a piecewise-linear cFunc under a concave c
over-states the gap between knots; this strengthens A3: HARK also converges to B as its grid
refines). The previously reported fitted amplitudes (≈0.6 HARK / ≈0.2 EGM) are crossover-window
fit artifacts: replicated on ONE solution by the old windows (0.607 / 0.217), while the tail-only
window returns 0.02806 at R² = 1.0000 — `numerics_appendix.md` §3. The `w̄^{−1}` **exponent** was
always solid; the amplitude is now identified too, and the approach rate to B matches Remark
8.3's `w̄^{−(q↑−1)}` (R4: measured slopes match −(q↑−1) to 4 digits across q↑ ∈ {1.05, …, 1.5}).]

:::

:::{prf:corollary} Corollary A4 (two channels, crossover, MPC rate). [PROVEN-HERE given A1–A3; expansions SKETCHED]
:label: st-cor-A4

Under A0–A6, σ² > 0:

1. **(Leading exponent.)** `−ln g(w̄)/ln w̄ → min(1, q↑)`, with `q↑` from (E0); with permanent
   shocks the same statement is *conjectured* with `q↑` from (E) (Stage B).
2. **(Crossover.)** For `q↑ > 1`, on any window `[w̄_a, w̄_b]` with
   `w̄_b ≪ w̄_cross := (A/B)^{1/(q↑−1)}` (A the effective Kesten-channel amplitude from the boundary
   data) the local log-log slope reads ≈ `−q↑`, migrating to `−1` beyond `w̄_cross` — this is the
   grid-depth migration of `Q_emp` observed in the extrapolation harness.
3. **(MPC rate.)** `c′(m) − κ̲ = −g′(w̄) = min(1,q↑)·g(w̄)/w̄·(1+o(1))` — i.e. `≍ w̄^{−(1+min(1,q↑))}`
   [PROVEN-HERE via the convex-differentiation squeeze given the sharp forms; at q↑<1 the constant
   genuinely oscillates with P — non-constancy is now a measured fact (R3), but the ORDER
   statement is unaffected: the sufficient margin holds ≥20× at every probed Λ, and
   osc(P)/P̄ ≈ e^{−α/Λ} collapses it at the estimated calibrations' Λ].
4. **(Knife-edge.)** As `Þ_Γ ↑ 1` (GIC knife-edge), `Λ ↓ 0` so `q↑ → ∞`: the Kesten channel
   steepens away and `g ≍ w̄^{−1}` purely; moreover the one-step rescaling `w̄ ↦ Þ_Γw̄ − O(1)` is
   near-additive on any bounded window `w̄ ≲ 1/(1−Þ_Γ)`, which is exactly why exponential fits look
   locally adequate on bounded grids near the knife-edge (e.g. HAFiscal's patience-ceiling college
   calibration — the most patient college-educated type, described in
   [`final_proof_myst`](final_proof_myst.md): growth impatience holds for it, but only barely, `Þ_Γ`
   sitting just below `1`, so the near-additive window covers every grid depth used in
   estimation). Asymptotically the exponential is still wrong (Prop. A0).

:::

:::{prf:lemma} Lemma A5 (eigenvalue uniqueness and selection; stated for general ψ, used in Stage B). [PROVEN-HERE, L13–L14; review-verified R2, and STRENGTHENED per R2 F-5]
:label: st-lem-A5

Let ψ ≥ 0, `E[ψ] = 1`, `E[ψ^{1+q}] < ∞` for q in a right-neighborhood of the relevant root. Define
`𝔏(q) := ln E[ψ^{1+q}] − ln ℛ − q·ln Þ_Γ`. Then 𝔏 is convex, `𝔏(0) = −ln ℛ < 0`, and **under
plain GIC — no further hypothesis** — `𝔏(q) → +∞` automatically (Jensen: `E[ψ^{1+q}] ≥ 1`, so
`𝔏(q) ≥ −lnℛ + qΛ`; if the moment explodes at finite q_c, monotone convergence gives 𝔏 → +∞
there instead — either way a root exists; the earlier draft's "GIC-Mod-type conditions" hedge is
deleted). Hence there is a **unique** positive root `q↑`, and automatically `𝔏′(q↑) ≥ lnℛ/q↑ > 0`
— and the exact q↑-tilted step mean equals `𝔏′(q↑)` itself (R2's identity, verified to 1.9e-16),
which is precisely the positive-drift condition the tilted renewal argument needs. Selection:
solutions of the homogeneous gap equation behaving like `w̄^{+|q|}` are excluded by the a-priori
bound `g ≤ κ̲(h−1)` — and this exclusion has bite: R2 exhibited a second, negative root
`q₋ = −1.327` of (E) for a ψ with mass near 0, whose branch grows like `w̄^{+1.33}`. The decaying
branch with the positive root is the only admissible one, and its amplitude is pinned by matching
at moderate w̄ (constructively: L9's telescope).

:::

---

(st-sec-stageB)=
## 3. Stage B: permanent shocks — the Kesten channel proper. [ATTEMPTED PROOFS in `stage_B_proof.md`; supersedes the former Conjecture B. Statuses per result; algebra machine-verified in `verify_algebra_B.py`]

Model: `m′ = (R/(Γψ′))a + θ′`; normalized Euler `c^{−ρ} = Þ_Γ^ρE[ψ^{−ρ}c(m′)^{−ρ}]`.
**Assumptions:** A1–A2; **(B-A3)** (ψ,θ) i.i.d., ψ ⊥ θ, `E ψ = E θ = 1`,
`supp ψ ⊆ [ψ_min, ψ_max] ⊂ (0,∞)` (ψ_min > 0), `supp θ ⊆ [0, θ_max]` (zero-income atom
permitted, as in A3), nondegeneracy `σ_B² := Var(ψ(θ+h−1)) = E[ψ²]σ_θ² + h²σ_ψ² > 0`; FHWC+RIC+GIC;
**(B-A0)** existence for the ψ-model (BST route; FVAC^ψ `βΓ^{1−ρ}E[ψ^{1−ρ}] < 1` — genuinely
stronger than FVAC, assumed, finite since ψ_min > 0); **(B-NA)** (only for Thm B2) the
**step** `S := ln(ψ/Þ_Γ)` is non-arithmetic: `supp S ⊆ λℤ` for no λ > 0. [Restated per
review RB3: the first draft's "`ln ψ` non-arithmetic" was the wrong object — RB3's solved
counterexample ψ = Þ_Γe^{±0.2} satisfies it while the walk is arithmetic (span 0.2) and the
KRT fails. Any ψ with a density satisfies (B-NA); sufficient Þ_Γ-free version: ln ψ in no
shifted lattice a + λℤ.] **κ̲ and h are UNCHANGED by ψ** (the ψ-weights cancel in the limiting-MPC
computation; `E ψ = 1` in human wealth); `q↑` = the unique positive (E)-root
`E[ψ^{1+q}] = ℛÞ_Γ^q` (Lemma A5, already ψ-general, with the corrected tilted mean `𝔏′(q↑)`).
**Master identity** (machine-verified): `ψ′w̄′ = Þ_Γw̄ + W′ + ℛg(w̄)` with
`W := ψ(θ+h−1) − h`, `E[W] = 0`, `Var(W) = σ_B²` — permanent shocks force the gap through
**human-wealth revaluation** (the `h²σ_ψ²` term), and the ψ^{−ρ} Euler weight cancels the
rescale Jacobian exactly, so Stage-A's linearization bookkeeping carries over verbatim.

:::{prf:proposition} Proposition B0 (no exponential decay with permanent shocks; GIC-free). [PROVEN; proof body OWNED by `exponential_impossibility.md`, Lemma J-B]
:label: st-prop-B0

$$
g(\wbar) \geq c_{-} \cdot \sigma_B^2 \cdot \wbar^{-1} \quad \text{for } \wbar \geq \wbar_{B0} \text{ (explicit)}, \quad \sigma_B^2 = \E[\psi^2]\sigma_\theta^2 + h^2\sigma_\psi^2.
$$ (st-eq-B0)

Exponential (indeed any o(1/w̄)) decay remains impossible; the floor carries `h²σ_ψ²` —
the human-wealth-revaluation channel — so permanent-shock models sit FURTHER from the
exponential heuristic than transitory-only ones. Details, corollary, and validation:
`exponential_impossibility.md`.

:::

:::{prf:theorem} Theorem B1 (two-sided order; leading exponent min(1, q↑), q↑ from (E)). [per-direction statuses, §B5]
:label: st-thm-B1

  (i)   `q↑ > 1`: `cσ_B²w̄^{−1} ≤ g(w̄) ≤ Cw̄^{−1}` — both PROVEN (**F-B1 CLOSED**: the upper
        bound now runs on a pathwise per-step multiplicative bound + one-step moments with
        geometric slack e^{𝔏(1)/2}; no restart, no Hölder transfer — §B5);
  (ii)  `q↑ < 1`: `c·w̄^{−q↑} ≤ g(w̄) ≤ C_δ·w̄^{−(q↑−δ)}` for every δ > 0 — both PROVEN (lower:
        q↑-tilt first-passage with pathwise overshoot ≤ S_max and explicit constants, base
        anchored by Prop B0; upper: defective-tilt supersolution). Exact-exponent upper now
        in BOTH step regimes: ⟸ Thm B2 under (B-NA), and ⟸ Thm B2-arith in the arithmetic
        case (**GAP-B-arith CLOSED 2026-07-06**);
  (iii) `q↑ = 1`: `cσ_B²w̄^{−1}ln w̄ ≤ g(w̄) ≤ w̄^{−1}(a ln w̄ + b)` — both directions PROVEN,
        **LOSS-FREE** (GAP-B-res-upper CLOSED 2026-07-06): the missing lemma — exponential
        moments of `Σ_{j<ν}1/w̄_j` under the tilt, uniform in the start — is proven as (T6)
        via new band-occupation exponential tails on the ladder ((T5): one-sided domination
        + λ = q↑ Chernoff + layer-cake), with the admissible λ scaling LINEARLY in the
        stopping threshold; the assembly runs on an exact resonance cancellation
        (`e^{−U_i}/w̄_i = w̄^{−1}∏(1−ε_j)^{−1}` pathwise), the mirror bound at the stopped
        step, and Cauchy–Schwarz against the geometric `P̌(ν > i)`. Every constant explicit;
        machine-verified with pre-registered falsifiers (`verify_resupper_checks.py`, ALL
        PASS). The η-loss first pass (`g ≤ C_ηw̄^{−1+η}ln w̄` ∀η > 0, an honest
        self-correction of the first draft's overclaim) is retained in §B5 as history.
        [RB2's exact-resonance numerics — w̄·g = C ln w̄ + D at R² = 0.99998 over three
        guard-clean decades, effective η ≤ 0.0064 — are now confirmations of a proven form.]

All probabilistic inputs reduce to 𝔏's convex geometry: the q-tilted step cgf is
`Ě[e^{λS}] = e^{𝔏(q↑+λ)}` (S = ln(ψ/Þ_Γ)), giving drift, supermartingale, occupation, and
exponential-functional bounds (§B4, all PROVEN).

:::

:::{prf:theorem} Theorem B2 (sharp constant, q↑ < 1, non-arithmetic STEP). [PROVEN-HERE — F-B2 CLOSED and SIMPLIFIED per review RB3 (direct pointwise route; smoothing demoted to a robustness alternative); residual = the section-level KRT cite, transcribed with hypothesis checklist in §B11]
:label: st-thm-B2

(st-eq-B2)=

    w̄^{q↑}·g(w̄) → A ∈ (0, ∞),    A = 𝔏′(q↑)^{−1}·∫_ℝ F̂(s) ds
    (boundary-data-dependent; the display is LITERAL — F̂ ∈ L¹(ℝ)).

**A TRUE constant — Stage B is CLEANER than Stage A here:** the random log-step S is
non-arithmetic under (B-NA), killing the lattice pathology, so Theorem A2's periodic
prefactor degenerates to a constant. Proof: reduce (B5.1) to a whole-line renewal equation
under the exact q↑-tilt; pointwise envelopes for ALL forcing pieces — the jitter piece Δ₂
has a DIRECT envelope from the one-sided-slope convexity inequality fed the proven B1(ii)-δ
bound (review RB3's simplification: the first draft's premise "Δ₂ has no pointwise envelope
without g-regularity", the entire rationale of former FLAG F-B2, was FALSE) — then the key
renewal theorem on the UNSMOOTHED equation. No doubling lemma anywhere (no circularity with
the order bounds). The Goldie-smoothing + monotone-de-smoothing route (the original F-B2
closure) is retained in §B7 as a robustness alternative. Numerics (RB3): the
A-representation reproduces the measured constant end-to-end to 0.04% on a solved model;
kernel-independence to 4.5e-5.

:::

:::{prf:theorem} Theorem B3 (sharp closed-form amplitude, q↑ > 1). [PROVEN-HERE (F-B1 closed ⟹ no inherited flag; residual = Stage-A-style constant-bookkeeping only, machine-verified at both pillars), §B8; closed form CAS-verified from the raw ψ-Euler]
:label: st-thm-B3

$$
\wbar \cdot g(\wbar) \to B_\psi = \kap(\rho+1) \cdot \sigma_B^2 / ( 2(\Rcal\ThornG - \E[\psi^2]) ), \qquad \sigma_B^2 = \E[\psi^2]\sigma_\theta^2 + h^2\sigma_\psi^2.
$$ (st-eq-B3)

Denominator `= ℛÞ_Γ(1 − e^{𝔏(1)}) > 0 ⟺ q↑ > 1`; diverges at the q↑ = 1 resonance — with the
divergence law now pinned: `B_ψ·(q↑−1) → κ̲(ρ+1)σ_B²/(2·E[ψ²]·𝔏′(1))` as q↑ ↓ 1, identifying
the resonance constant's normalization as **Λ̌ = E[ψ²]𝔏′(1) = E[ψ²S]** (DERIVED
two ways in the RB fix pass — the (B8.1) resonance balance and this boundary law — and
measured to 0.02%/0.3%; reconciles RB2-vs-RB4, §B8 remark + `fixpass_checks.py`; the q↑ = 1
LIMIT itself is now PROVEN — Theorem B-res below). Reduces to Theorem A3 at ψ ≡ 1; **depends on ψ only through
E[ψ²]** (ψ-skew-blind — machine-verified with skewed rational atoms). Notably, (B-NA) is NOT
needed: the w̄^{−1} channel is forcing-anchored for random rescales too (the associated
homogeneous equation would need E[ψ²] = ℛÞ_Γ, i.e. q↑ = 1) — genuinely tested by RB4's
exact-lattice ψ designs (supp S ⊆ λℤ by construction, spans 0.2–1.0: amplitude matches to
≤ 0.1%, lattice tones ≤ 2.3e-6 and depth-decaying; the appendix's earlier "arithmetic 2-atom"
evidence was mislabeled — that ψ is non-arithmetic under the corrected criterion below).
*(Signed subleading at q↑ < 1: `B_ψ < 0` — SKETCHED as an asymptotic statement; the u²-order
ALGEBRA producing the signed closed form is now machine-exact (RB4). It drives the Q_emp
non-monotonicity reading of the HARK-default calibration, appendix §8. Bonus evidence (RB1):
a GIC-VIOLATING calibration's measured tail amplitude matches B_ψ to 0.02% — B3's GIC
hypothesis looks weakenable; recorded as conjecture-with-evidence in §B8, NOT claimed.)*

:::

:::{prf:theorem} Theorem B2-arith (q↑ < 1, ARITHMETIC step: the lattice companion). [PROVEN-HERE 2026-07-06, §B7 — GAP-B-arith CLOSED, mod the classical arithmetic whole-line renewal cite (Gut/Asmussen, per RC3); REFUTER-REVIEWED (RC3, 0 broken; verified on a harder 3-atom aperiodic lattice); battery `verify_arith_checks.py` ALL PASS]
:label: st-thm-B2-arith

Under B-A0–A6, σ_B² > 0, `q↑ < 1`, and supp S ⊆ λℤ with span λ (the arithmetic complement
of (B-NA)): uniformly over the phase (the position of `ln w̄` modulo the lattice span `λ`),

$$
\wbar^{\qup} \cdot g(\wbar) = P_B(\ln \wbar) + o(1), \qquad P_B(\phi) = (\lambda/\Lfun'(\qup)) \cdot \sum_{m \in \mathbb{Z}} \hat{F}(\phi + m\lambda),
$$ (st-eq-B2arith)

P_B λ-periodic, continuous, positive; mean over one period = Theorem B2's constant formula
`𝔏′(q↑)^{−1}∫F̂`; Fourier coefficients EXACT: `c_k(P_B) = 𝔏′(q↑)^{−1}F̂^(2πk/λ)`. The §B7
reduction is exact with lattice steps (all drift corrections live inside F̂), so the phase
is exactly preserved and the classical lattice renewal theorem applies verbatim — stronger
than the "subsequence version" previously anticipated in the bridge note below. At ψ ≡ 1
this DEGENERATES to Stage-A Theorem A2's telescope (P_B = P; span λ = Λ), giving Stage-A's
periodic factor the exact Fourier representation `c_k(P) = Λ^{−1}F̂^(2πk/Λ)` — the rigorous
form of L9′(a)'s "k = ±1 Mellin residue" object. Oscillation SIZE deliberately not
quantified (the L9′(b)-analogue; still open). End-to-end phase-resolved verification on an
exact-lattice design: 0.116% at m ≈ 3e5, decreasing in depth.

:::

:::{prf:theorem} Theorem B-res (q↑ = 1 sharp log-law). [PROVEN-HERE 2026-07-06, §B8 — GAP-B-res CLOSED; consumes the loss-free B1(iii); REFUTER-REVIEWED (RC2, 0 broken — first adversarial pass on the B-res apparatus; C_B confirmed by two independent symbolic derivations at skewed resonance); battery `verify_resonance_const_checks.py`, 7 pre-registered falsifiers, ALL PASS]
:label: st-thm-B-res

Under B-A0–A6, σ_B² > 0 and `q↑ = 1` (⟺ `E[ψ²] = ℛÞ_Γ`):

$$
\wbar \cdot g(\wbar)/\ln \wbar \to C_B := \kap(\rho+1) \cdot \sigma_B^2/(2 \cdot \E[\psi^2] \cdot \Lfun'(1)), \qquad |\wbar \cdot g/\ln \wbar - C_B| \leq C_{\text{fin}}/\ln \wbar,
$$ (st-eq-Bres)

`𝔏′(1) = E[ψ²S]/E[ψ²]` the tilted drift. Proof: the exact tilted one-step identity
`W₁ = Ě[W₁(w̄′)] + c_J^B/ℛ + δ`, |δ| ≤ C(1+ln w̄)/w̄, telescoped along the TRUE tilted chain
to a stopping band; Wald pins the expected rung count `(u + O(1))/𝔏′(1)`; the error sum is
w̄-free by (T5′)-banded first moments. Measured: C_fit = 33.923 vs C_B = 33.929 (**0.02%**)
at the exact-resonance calibration. **The ψ ≡ 1 corollary closes Stage-A L11-const:**
`w̄·g/ln w̄ → κ̲(ρ+1)σ²/(2Λ)` at q↑ = 1 (R2's Richardson-corroborated 0.0272294 target is now
a theorem's value; `stage_A_proof.md` Lemma 6.4 updated by reference).

:::

(st-sec-B9)=
### Side conditions and the discretized-ψ bridge (§B9)

`E[ψ^{1+q↑}|ln ψ|] < ∞`, `E[ψ^{−ρ}] < ∞`: trivial under (B-A3); stated and moved past.
**(B-NA) for computational (discrete) ψ [criterion CORRECTED per reviews RB3/RB4 — the first
draft's version was wrong in both directions]:** the condition is on the step values
`s_i := ln ψ_i + Λ` — an N-atom ψ is **arithmetic iff all s_i lie in one lattice λℤ**
(equivalently: all pairwise ratios s_i/s_j rational); it involves Þ_Γ, not the ψ-atoms alone.
Consequences: a 2-atom ψ is arithmetic iff s₁/s₂ ∈ ℚ — **generically FALSE** (the old
"always arithmetic for 2 atoms" is retracted); incommensurable log-atom DIFFERENCES are
sufficient for non-arithmeticity, never necessary; where genuinely arithmetic, the span is
the gcd-type generator of the {s_i} (S = ±λ has span λ, not |ln(ψ₁/ψ₂)| = 2λ) and `w̄^{q↑}g`
carries a span-periodic prefactor — now a THEOREM (B2-arith above), with the prefactor
explicit: P_B = (λ/𝔏′)Σ_mF̂(·+mλ). Its SIZE is expected `≈ e^{−α/span}`-small by the R3
law, and RB3's solved true-lattice case measured < 1e-7 at span 0.2 (≥ 3 orders below the
naive transfer) — the size bound remains the open L9′(b)-analogue. Numerics may treat A as
constant; a theorem for a specific discretization checks the s_i ∈ λℤ condition and, where
arithmetic, applies B2-arith. (L9′ itself is a separate queue item.)

---

(st-sec-remarks)=
## 4. Remarks

1. **(What is new.)** The literature proves `c(m)/m → κ̲` and `c′(m) → κ̲` (BST
   [lemma-MPCBoundsConvg](https://llorracc.github.io/BufferStockTheory-Latest/#lemma-mpcboundsconvg); Ma–Toda 2022 JMathE, vol. 98 art. 102562,
   under regularly-varying u′) and the dual wealth-tail Pareto exponents (Beare–Toda 2022 ECMA;
   MST 2020 JET Thm 3.3 (CITE-CHECK number); Stachurski–Toda 2019 JET), but no rate or form for the
   primal gap. Even the LEVEL convergence `g → 0` (our L3) appears not to be stated in the
   literature (the ratio and derivative limits do not imply it); it falls out of the gap equation
   in two lines.
2. **(Primal ≠ shadow of dual.)** At ψ≡1 with bounded θ under GIC, the ergodic wealth distribution
   has compact support (the wealth recursion is a contraction with bounded innovations), so there
   is NO wealth Pareto tail — yet the consumption gap is a power law. The two power laws are
   distinct objects sharing a root *family*: dual root `E[(Þ_Γ/ψ)^ζ] = 1` (no positive root at
   ψ≡1) vs primal root `E[ψ^{1+q}] = ℛ·Þ_Γ^q` (root exists at ψ≡1 thanks to the level ℛ > 1).
3. **(Where the power law comes from.)** The gap equation's rescaling `w̄ ↦ Þ_Γw̄ + O(1)` is
   multiplicative; in `ln w̄` it is a random-walk/renewal structure. Exponential-in-m decay would
   require additive-in-m dynamics, i.e. `Þ_Γ = 1` — the GIC knife-edge (Cor. A4.4). This is the
   rigorous version of the derivation's §2.
4. **(Sharpness of A1's constants.)** The σ² in the lower bounds is sharp in order: as σ² → 0 the
   model degenerates to PF and `g ≡ 0`. After the R2 F-3 repair, the `w̄^{−q↑}` lower bound in (ii)
   carries its σ² **explicitly** (the ladder base is priced by Prop. A0's `c₋σ²/y_bdry` rather
   than by qualitative strict-Jensen positivity), so the σ²-degeneration of the (ii)-constant is
   now a formula, not an allusion to boundary data.
5. **(Both constraints allowed.)** The artificial constraint a ≥ 0 is assumed for concreteness;
   with the natural borrowing constraint (θ_min > 0) all statements hold verbatim above the
   respective `m̄` — the asymptotics never see the constraint directly (excursion bound), only
   through the boundary data (hence through `P` and the q↑<1 constants, NOT through q↑ or B).
6. **(Fine structure of P — factored out; NOT required for any theorem here.)** Whether `P` is
   constant and how large its oscillation is are refinements owned by the standalone appendix
   **`periodic_factor_fine_structure.md`** (same discipline as `exponential_impossibility.md`).
   In brief: "P constant" is numerically REFUTED (R3, `osc(P)/P̄ ≈ e^{−α/Λ}`, α ≈ 0.8–1.2) and
   reduced (via Theorem B2-arith at ψ≡1) to the explicit criterion `c_k(P) = Λ^{−1}F̂^(2πk/Λ)`;
   generic (a.e.) non-constancy is a theorem, universal is probably false (tiling obstruction).
   The oscillation SIZE has a PROVEN unconditional linear bound `osc(P) ≤ Λ·TV(P′)/6` (⟹
   effective constancy at the estimated calibrations' Λ, extrapolated ~10^{−10}–10^{−41}, which is all the
   application needs) and an open sharp exponential bound `osc(P) ≤ Ce^{−c/Λ}` (reduced to
   strip-analyticity of F̂, `c = 2πw` with `w` the analyticity-strip half-width — a local symbol,
   not the wealth coordinate `w̄` — measured Λ-independent `w ≈ 0.15`). None of this is
   consumed by A1/A2/A3, B1–B3, B-res, A0/B0, or the HAFISCAL/HARK application.
7. **(Effective, not practically tight — rephrased per review R2 F-8.)** All upper/lower bounds
   are effective: every constant is an explicit function of `(ρ, β, R, Γ, θ_min, θ_max, σ²)` via
   the proof's threshold (written `x₀` in the proof documents; our `w̄₀`), `C₀`, `K̂` (no
   compactness or soft arguments anywhere in L2–L11). But the
   compounded constants are astronomically conservative (R2 measured e.g. `Π̄ = e^{K̂S̄} ≈ 1e14`
   at case A, giving upper constants ~19 orders above truth; the F-3-explicit q↑<1 lower constant
   costs ~9 orders), so the finite-w̄ BOUNDS are practically vacuous on estimation grids. What is
   practically meaningful is the ORDER content plus the tight local up/down ladder inequalities
   (the displays tagged `(five-up)`/`(five-dn)` in `final_proof_myst.md`; MyST labels
   `eq-five-up`/`eq-five-dn` in `final_proof_myst.md`), which hold at their design
   tightness `1 + K̂/w̄` (R2's audit). The effectiveness claim is about
   the absence of soft steps, not about usable finite-w̄ error bars.
8. **(Unbounded θ.)** L4′ (Lemma 5.3): if `supp θ` is unbounded (θ ≥ 0) but `E[θ^k] < ∞`
   for some `k > max(1, q↑) + 1`, Theorems A1–A3 hold verbatim (**PROVEN-HERE, REFUTER-REVIEWED
   RC4** — RC4-F1 fix incorporated: the anchor carries an explicit `y_var` entry for the
   fat-tailed-θ variance floor): (A) the workhorse holds on the good event `A(w̄) = {θ ≲ Þ_Γw̄}`
   with truncated moments → the full moments (A^c-tails at relative order `w̄^{−(k−1)}`,
   below every ladder slot iff `k > max(1,q↑)+1`); (B) the UPPER chain survives verbatim
   (it consumes only the pathwise lower bracket `w̄′ ≥ Þ_Γw̄ − 1`, θ ≥ 0); (C) the LOWER
   chain runs on a depth-adapted truncation ladder `y_{j+1} = Þ_Γy_j + y_j^{1/2} + C`
   anchored at a FIXED level `y_anc ≥ 2y★` (it stalls at the fixed point `y★`, not at `w̄₀`) —
   exponent-preserving and with a positive-constant probability product, both numerically
   confirmed (`verify_L4prime_checks.py`). The lognormal benchmark has all moments; the
   *discretized*-lognormal numerics are covered by the bounded-support theorems as stated.
9. **(Mortality.)** With survival probability L (perpetual-youth), replace β by βL throughout:
   `Þ_Γ = (βLR)^{1/ρ}/Γ`, `q↑ = ln ℛ/ln(1/Þ_Γ)` — matching `qstar_discrete` in the harness. The
   Blanchard annuity variant additionally rescales R; either way mortality enters ONLY through Þ_Γ
   (and Þ_R).
10. **(Practical implication, unchanged.)** The principled tail extrapolator is
    `g ≈ C·w̄^{−q}` with `q = min(1, q↑)` (Theorems A1–A3), as implemented in the HARK PR
    (`decay_extrap_form='powerlaw'`); the slope-matched `Q_emp = B·(m_top−1+h)` sits near q↑ on
    short grids and migrates to `min(1,q↑)` on deep ones (Cor. A4.2) — the harness's observed
    migration is now a *theorem-backed* diagnostic, not a stylized fact.

---

(st-sec-constraint-end)=
## 5. The constraint end (bottom knot): the `q↓` power law

Sections 2–4 characterize how `c(m)` approaches its **high-wealth** asymptote (the
perfect-foresight line `κ̲(m−1+h)`, from below, as a power law with the eigenvalue exponent
`min(1,q↑)` — [Theorem A1](#st-thm-A1), [Corollary A4](#st-cor-A4)). This section is the
**mirror at the other end**: how `c(m)` approaches its
**constraint-end** asymptote (the maximal-MPC line, from below, as `m` falls to the borrowing
constraint). The two ends turn out to be **structurally different**
([Remark C1](#st-sec-constraint-remarks)): the high-wealth
end is governed by a nontrivial eigenvalue with a possible log-periodic prefactor
([Theorem A2](#st-thm-A2)); the
constraint end is governed by the utility curvature `ρ` alone, with **no** periodic prefactor
([Theorem CE](#st-thm-CE)).
Full derivation and proofs: [`constraint_end_proof.md`](constraint_end_proof.md); pre-registered
battery [`verify_constraint_end_checks.py`](verify_constraint_end_checks.py) (ALL PASS).

(st-def-constraint-objects)=
**Setup and objects (transitory worst atom; ψ≡1).** Add to A1–A6:

- **(C-A3)** `{θ_t}` i.i.d. with a **worst atom**: `θ = θ_min ≥ 0` with probability `℘ ∈ (0,1)`,
  and `supp θ ⊆ [θ_min, θ_max]`. The **natural borrowing constraint** is
  `m̲ := −θ_min/(ℛ−1) ≤ 0` (the most one can owe and still repay under the worst income path;
  `m̲ = 0` in the zero-income case `θ_min = 0`). Write **excess resources** `m^e := m − m̲ > 0`.

Derived (the constraint-end analogues of `κ̲`, `h`):

    κ̄  := 1 − ℘^{1/ρ}·Þ_R      (the MAXIMAL MPC — BST eq-MPCmaxDefn; the m^e→0 limit of c/m^e)
    λ   := ℛ·(1 − κ̄) = ℘^{1/ρ}·Þ_Γ < 1   (the worst-branch contraction rate toward the constraint)
    γ(m) := κ̄·m^e − c(m) ≥ 0    (THE CONSTRAINT-END GAP; γ/m^e → 0)

`κ̄` is the m→m̲ mirror of `κ̲`
([BST eq-MPCmaxDefn](https://llorracc.github.io/BufferStockTheory-Latest/#eq-mpcmaxdefn)):
`c(m)/m^e → κ̄` as `m^e → 0`
([BST lemma-MPCBoundsConvg](https://llorracc.github.io/BufferStockTheory-Latest/#lemma-mpcboundsconvg);
[eq-cBounds](https://llorracc.github.io/BufferStockTheory-Latest/#eq-cbounds) gives
`κ̲_t m ≤ c_t(m) ≤ κ̄_t m` per period). Note `λ = ℛ(1−κ̄) < 1` is the exact
factor by which the worst-income branch maps `m^e` toward the constraint.

:::{prf:proposition} Proposition C1 (worst-atom maximal MPC). [PROVEN-CITED (BST) + generalization; verified `verify_constraint_end_checks.py` C1, 5 calibrations, |fit−formula| ≤ 6e-8]
:label: st-prop-C1

Under A1–A6 and (C-A3), `lim_{m^e→0} c(m)/m^e = κ̄ = 1 − ℘^{1/ρ}·Þ_R`, where `℘` is the mass of
the **worst income atom** (`= P(θ = θ_min)`; in a discretized income process, the mass of the
minimum node). This is BST's zero-income `MPCmax`
([eq-MPCmaxDefn](https://llorracc.github.io/BufferStockTheory-Latest/#eq-mpcmaxdefn)) read with
`℘ = ℘_min`: near the constraint only the worst-income branch keeps marginal utility unbounded, so
the derivation is verbatim BST with the worst atom in the role of the zero-income event.

:::

:::{prf:proposition} Proposition C2 (finite-horizon recursion; the T−1 anchor). [PROVEN-CITED (BST eq-MPCmaxInvApndxIter), MoM restatement; verified C3, |meas−pred| ≤ 4e-14]
:label: st-prop-C2

The period-`t` maximal MPC obeys
[BST's backward recursion](https://llorracc.github.io/BufferStockTheory-Latest/#eq-mpcmaxinvapndxiter),
written here in constraint-end form:

$$
\bar\kappa_{T-n}^{-1} = 1 + \mathsf{M}\,\bar\kappa_{T-n+1}^{-1}, \quad \mathsf{M} := \wp^{1/\rho}\ThornR = 1-\bar\kappa, \quad \bar\kappa_T = 1,
$$ (st-eq-C2)

with closed form `κ̄_{T−n} = κ̄/(1 − 𝖬^{n+1})`. In particular the **one-from-terminal** MPC is
`κ̄_{T−1} = 1/(1+𝖬) = 1/(2−κ̄)`, materially above the stationary `κ̄` — this is why a solver read at
the terminal-adjacent horizon measures a larger constraint-end slope than the `∞`-horizon formula
(the recursion, not the stationary value, is the correct anchor at finite horizon).

:::

:::{prf:theorem} Theorem CE (the constraint-end power law: the approach exponent `q↓` = ρ). [PROVEN-HERE (local Euler analysis, `constraint_end_proof.md`); verified C2 (free-exponent fit), 5 calibrations ρ∈{1.5,2,2.5,3}, |q↓−ρ| ≤ 0.036]
:label: st-thm-CE

Under A1–A6 and (C-A3), there is a constant `K > 0` (explicit modulo boundary data — Remark C2)
such that, as `m^e → 0`,

$$
c(m) = \bar\kappa\,m^e - K\,(m^e)^{1+\rho}\,(1+o(1)), \qquad\text{equivalently}\qquad \bar\kappa - \frac{c(m)}{m^e} = K\,(m^e)^{\rho}\,(1+o(1)).
$$ (st-eq-CE)

Write **`q↓`** for the constraint-end approach exponent — display `q_{\downarrow}`: the down-arrow
names the constraint (lower) end of the state space, the partner of the high-wealth `q↑`
(arrow ruling 2026-07-14, superseding the earlier `q°` ring form; code and the wider
literature write `q*` for the high-wealth root — HARK's API is unchanged). Then `γ(m) = κ̄ m^e − c(m) ≍ (m^e)^{1+q↓}`,
equivalently the MPC deficit `κ̄ − c/m^e ≍ (m^e)^{q↓}`, and in the Method-of-Moderation coordinates
`μ = ln m^e`, `χ = ln((1−ω)/ω)`, `χ(μ) = μ + b₀ + O(e^{q↓·μ})` as `μ → −∞`. **Then `q↓ = ρ`, the
CRRA** (the smooth `c ↦ χ` change of variables preserves the exponent; `b₀ = ln((κ̄−κ̲)/C)`,
`C = κ̄(h − 1 + m̲)`). Unlike the high-wealth Theorem A2, **there is no log-periodic prefactor**: the
worst-branch map is the deterministic contraction `λ = ℘^{1/ρ}Þ_Γ`, and the current-gap feedback
term lifts the telescope degeneracy that produces `P(·)` on the high-wealth side (proof §3).

:::

:::{prf:corollary} Corollary C3 (two asymptotes and the crossover). [PROVEN-HERE given Thm CE + Cor A4; crossover SKETCHED]
:label: st-cor-C3

`χ(μ)` is asymptotically **linear at both ends**: slope `1` with intercept `b₀` as `μ → −∞`
(constraint end, Thm CE) and slope `q = min(1,q↑)` with intercept `b_∞` as `μ → +∞` (high-wealth
end, Cor. A4). For `q < 1` the two lines cross at `μ_c = (b_∞ − b₀)/(1 − q)`; at `q = 1` they are
parallel (a plateau/level offset rather than a crossing). This is the object the Method-of-Moderation
extrapolators bracket: the `μ < μ_c` branch is governed by `q↓ = ρ` (Thm CE), the `μ > μ_c` branch by
`q` (Thm A1).

:::

:::{prf:corollary} Corollary C4 (the bottom grid-design rule — mirror of `q·hEx`). [PROVEN-HERE given Thm CE; verified C4, predicted vs measured inside-asymptote m^e within 16%]
:label: st-cor-C4

The high-wealth grid rule "the top knot must reach `w̄ ≳ (A/B)^{1/(q↑−1)}`" has a constraint-end
mirror. Since the relative deviation of `c` from the `κ̄`-line is `(κ̄ − c/m^e)/κ̄ = (K/κ̄)(m^e)^ρ`
(Thm CE), the **bottom knot `m^e_0` sits inside the constraint asymptote to relative tolerance
`tol`** iff

$$
m^e_0 \;\lesssim\; \bigl(\text{tol}\cdot\bar\kappa/K\bigr)^{1/\rho}.
$$ (st-eq-C4)

So `aXtraMin` must be pushed **below** this scale for a solver to read the true constraint-end slope
`κ̄`; a bottom knot placed above it reports a slope biased by `O((m^e_0)^ρ)`, and a fitted-tangent
extrapolation below such a knot mis-specifies the tail exponent (the constraint-end analogue of the
`Q_emp` grid-depth migration, Cor. A4.2). This is the theory pin for the Method-of-Moderation bottom
tail: its decay constant is `ρ`, not a fitted quantity.

:::

(st-sec-constraint-remarks)=
### Remarks (constraint end)

- **C1. (The two ends are structurally different.)** High-wealth end: the one-step map
  `m ↦ (Þ_Γ/ψ)m` is **random-multiplicative**, so the gap solves a renewal/eigenvalue problem
  (root `q↑` of `E[ψ^{1+q}] = ℛÞ_Γ^q`) with a lattice/periodic prefactor. Constraint end: the
  binding one-step map is the **single deterministic contraction** `m^e ↦ λ m^e` (only the worst
  atom returns you to the constraint), so there is no eigenvalue to solve and no periodicity — the
  exponent is fixed by the curvature of `u′` at the level of the Euler expansion, giving exactly `ρ`.
- **C2. (The amplitude `K`.)** `K > 0` is explicit modulo one boundary-data constant — the non-worst
  branches' marginal-utility mass `J₀ := Þ_Γ^ρ E[c(m')^{-ρ}\mathbf 1\{θ>θ_min\}]` at `m^e = 0` —
  exactly as the high-wealth amplitude `A` (Thm A2) depends on boundary data; the closed skeleton is
  `K = J₀κ̄^ρ/(ρ[(1−λ^ρ)/κ̄ + ℛ/λ])` (proof §2). The **exponent** `q↓` (`= ρ`) needs no boundary data.
- **C3. (Permanent shocks — CLOSED 2026-07-14, see §5b below.)** The ψ-general theory
  (Theorem CE-ψ, `st-thm-CE-psi`) proves `q↓ = ρ` under the uniform-contraction criterion
  `℘_eff^{1/ρ}Þ_Γ < ψ_min` and characterizes the complementary regime as a
  renewal/eigenvalue problem — confirming both halves of the original conjecture. The
  remaining rigor item is GAP-CE-ψ-II (regime-II amplitude; `st-rem-CE-regime`).
- **C4. (Coordinate invariance.)** Thm CE is stated invariantly in `c`-space (`κ̄ − c/m^e ≍ (m^e)^ρ`,
  verified directly). The MoM `χ`-coordinate rendering `χ = μ + b₀ + O(e^{ρμ})` follows because
  `ω`, `χ` are smooth non-degenerate functions of the position of `c` between its bounding lines; the
  exact `b₀`/`χ` constants use the MoM `ω`-definition (consumed by the MoM implementation workstream,
  out of scope here).

(st-sec-ce-psi)=
### 5b. The permanent-shock extension (GAP-CE-ψ closure, 2026-07-14)

*Proof bodies: `constraint_end_proof_psi.md` (F1/F2, the (CE-ψ) equation, the (E-ψ↓)
eigen-equation, the two regimes). Pre-registered battery: `verify_ce_psi_checks.py`.
Status tags as in §2.*

(st-def-ce-psi-objects)=
**Objects.** Worst transitory atom `ξ_min` with mass `℘_w` (zero-income case: `ξ_min = 0`,
`℘_w = ℘`); `ψ ∈ [ψ_min, ψ_max]`, `E[ψ] = 1`; `ℛ̃(ψ) = R/(Γψ)`.

    m_min = −ξ_min/(ℛ̃_max − 1),  ℛ̃_max = R/(Γψ_min);   m^e = m − m_min
    λ(ψ)  = ℘_w^{1/ρ}·Þ_Γ/ψ      (branch-wise contraction on the worst-transitory event)
    ℘_eff = the worst-JOINT-atom mass: ℘_w when ξ_min = 0; ℘_w·P[ψ = ψ_min] for discrete ψ
            with ξ_min > 0 (the fiber-selection effect, proof §4) — exactly HARK's
            `WorstIncPrb`.

(st-prop-C1-psi)=
**Proposition C1-ψ (κ̄ is ψ-invariant). [PROVEN-HERE, proof §0(F2); battery gate B2]**
The growth-normalization weight `(Γψ)^{−ρ}` cancels exactly against the `(Γψ)^{+ρ}`
carried by next-period resources on the reachable worst fiber, so for EVERY
ψ-distribution

    κ̄ = 1 − ℘_eff^{1/ρ}·Þ_R,

the ψ≡1 formula with the joint worst mass (matches BST `eq-MPCmaxDef` and HARK's
`calc_mpc_max` accounting).

(st-thm-CE-psi)=
**Theorem CE-ψ (regime I: uniform contraction). [PROVEN-HERE at the ψ≡1 proof's rigor
level, proof §§1–2; battery gates B1/B4]** If the worst-branch map contracts through the
smallest permanent shock,

    ℘_eff^{1/ρ}·Þ_Γ < ψ_min        (equivalently  λ(ψ_min) < 1),

and the generic non-resonance `w·E[λ(ψ)^ρ] ≠ 1` holds, the constraint-end approach
exponent is unchanged by permanent shocks:

    q↓ = ρ:   γ(m^e) = κ̄m^e − c(m) ≍ (m^e)^{1+ρ},   MPC → κ̄,   no log-periodic prefactor

(the ψ-mixture's homogeneous root is strictly negative and excluded by `0 ≤ γ ≤ κ̄m^e`,
exactly as at ψ≡1; the mixture additionally smooths).

(st-rem-CE-regime)=
**Characterization (regime II) + the remaining gap. [DERIVED; amplitude rigor OPEN =
GAP-CE-ψ-II; battery gate B5 adjudicates empirically]** If `λ(ψ_min) > 1` (an expanding
worst fiber — e.g. any fixed `℘_w` with ψ-support reaching low enough `ψ_min`; the
precise sense in which a continuous permanent component reinstates renewal), the
homogeneous equation

    (E-ψ↓)   w·(℘_eff^{1/ρ}Þ_Γ)^s·E[ψ^{−s}] = 1,   w ∈ (0,1) the feedback weight,

acquires a positive root `s*₊`, and the constraint end becomes a random-multiplicative
(renewal) problem with

    q↓ = min(ρ, s*₊).

Whether the `x^{s*₊}` mode carries generic nonzero amplitude is the open rigor item
(GAP-CE-ψ-II); the battery's regime-II specs test it empirically: fitted exponents at
`s*₊` confirm amplitude-genericity, fits pinned at `ρ` would refute it. The regime
boundary `℘_eff^{1/ρ}Þ_Γ = ψ_min` is a primitive, checkable criterion (CAL-HS: the worst
JOINT atom is the lowest *employed*-income atom — θ_min ≈ 0.581 undercuts the unemployment
income 0.7 — giving `℘_eff ≈ 0.020` and `λ(ψ_min) ≈ 0.15`: deep in regime I, so the
estimated calibration keeps `q↓ = ρ`).
