# Appendix — Exponential decay of the buffer-stock consumption gap is impossible

*This is a standalone **appendix** to the synthesis proof (`final_proof.md` /
`final_proof_myst.md`). It is separated from the main theorem deliberately: once the
extrapolation form of record is the power law, establishing that the historical **exponential**
form is impossible is a legacy-motivated result — useful for the extrapolation-form question,
but off the main line of the theorem. The main text refers here for [](#prop-imp-A0) /
[](#prop-imp-B0).*

**Audience split.** This document is for consumers of the *extrapolation-form question* ("how
should the consumption function be extended beyond the solved grid, and is the traditional
exponential heuristic ever right?"): it is fully self-contained, its hypotheses are strictly
WEAKER than the power-law theorems' (no GIC anywhere), and its conclusion is purely negative —
the gap can never decay exponentially, nor indeed faster than w̄^{−1} (the reciprocal of
perfect-foresight total wealth, defined in §1), for any calibration in the class. Consumers of
the *sharp asymptotics* (the exponent min(1, q↑), the periodic/constant
amplitudes, the closed-form w̄^{−1} coefficients) should read `statement.md` +
`stage_A_proof.md`/`stage_B_proof.md`, whose lower-bound machinery IMPORTS the two lemmas
proven here (ownership note in [§5](#imp-sec-ownership)).

**Results owned here** (proof bodies live here and nowhere else):
- **Lemma J-A** (transitory-only quantified-Jensen floor) ⟹ **Proposition A0**;
- **Lemma J-B** (permanent-shock floor, with the human-wealth-revaluation variance) ⟹
  **Proposition B0**;
- the **no-o(1/w̄) corollary** and the practical implication for HARK/solution-method
  extrapolation.

---

## §1. Setting and (deliberately minimal) assumptions

Infinite-horizon income-fluctuation problem in permanent-income-normalized form: market
resources m > 0 (beginning of period, income included), consumption c ∈ (0, m] (savings
a = m − c ≥ 0), and

$$
m' = \frac{R}{\Gamma\psi'}\,a + \theta' \qquad \text{(transitory-only case: } \psi \equiv 1\text{)},
$$ (eq-imp-transition)

with CRRA marginal utility u′(c) = c^{−ρ}, ρ > 0, and the normalized Euler equation

$$
c(m)^{-\rho} = \ThornG^{\rho}\,\E\!\left[\psi^{-\rho}\, c(m')^{-\rho}\right] \qquad \text{wherever } a(m) > 0.
$$ (eq-imp-euler)

Notation: ℛ := R/Γ, Þ_R := (βR)^{1/ρ}/R, Þ_Γ := (βR)^{1/ρ}/Γ, κ̲ := 1 − Þ_R. As in BST,
[h := 1/(1 − ℛ⁻¹) = ℛ/(ℛ − 1)](https://llorracc.github.io/BufferStockTheory-Latest/#eq-hdef)
is human wealth — the PDV of labor income *including* the current period's — so the PDV of
future income alone is h − 1 = 1/(ℛ − 1). w̄ := m − 1 + h is **perfect-foresight total wealth
(human and market)**: the wealth of the optimist who treats future income as certain, the bar
marking the optimist's/upper-bound object as in BST's own perfect-foresight rule
[c̄(m) = κ̲(m − 1 + h) = κ̲·w̄](https://llorracc.github.io/BufferStockTheory-Latest/#eq-cfuncpfunc).
THE GAP is

$$
g(m) := \kap\,(m - 1 + h) - c(m), \qquad \text{written } g(\wbar);
$$ (eq-imp-gap)

equivalently, g is **precautionary saving** — the amount by which consumption falls short of
the perfect-foresight rule — written s(m) := c̄(m) − c(m) on the main pages, with s(m) = g(w̄)
(unrelated: the generic variance dummy s² inside Lemma E1 below).

**Assumptions (all of them — note what is absent):**

- **(X1)** ρ > 0; β ∈ (0,1); R, Γ > 0.
- **(X2) [FHWC](https://llorracc.github.io/BufferStockTheory-Latest/#ass-fhwc):** ℛ > 1.  **(X3) [RIC](https://llorracc.github.io/BufferStockTheory-Latest/#ass-ric):** Þ_R < 1 (so κ̲ ∈ (0,1)).
- **(X4) shocks:** (ψ, θ) i.i.d. over time, ψ ⊥ θ, E[ψ] = E[θ] = 1;
  supp θ ⊆ [0, θ_max] (a θ = 0 unemployment atom of probability ℘ := P(θ = 0) is permitted,
  not required); supp ψ ⊆ [ψ_min, ψ_max] ⊂ (0, ∞).
  Transitory-only case: ψ ≡ 1. Nondegeneracy:
      σ² := Var(θ) > 0                                (Prop. A0)
      σ_B² := Var(ψ(θ+h−1)) = E[ψ²]σ_θ² + h²σ_ψ² > 0   (Prop. B0).
- **(X5) existence:** the problem has a solution c with the standard properties (continuous,
  increasing, Euler characterization [](#eq-imp-euler), unique in the standard candidate class). Verified
  sufficient conditions and per-case routing (MST 2020 Thm 2.2 for θ_min > 0;
  [BST Thm 2](https://llorracc.github.io/BufferStockTheory-Latest/#sufficient-conditions-for-non-degenerate-solution) for
  the θ = 0 atom): `stage_B_proof.md` §B11. For Γ ≥ 1 in the transitory-only case, X5 is
  automatic from X2–X3 (RIC+FHWC ⟹ [FVAC](https://llorracc.github.io/BufferStockTheory-Latest/#fvac); `stage_A_proof.md` §1); for Γ < 1 or ψ ≢ 1 it is an
  assumption (FVAC^ψ).

**Absent by design: the [GIC](https://llorracc.github.io/BufferStockTheory-Latest/#gicraw)
(Þ_Γ < 1) is NOT assumed, and the unemployment atom is NOT required** — the main power-law
pages maintain ℘ > 0 as part of their income-process assumption, but every result on this page
survives ℘ = 0 (the only nondegeneracy needed is X4's variance condition). These are strictly
weaker hypotheses than any of the power-law theorems use — the impossibility results below
hold for patient and impatient consumers alike, including calibrations where no target wealth
exists and the normalized wealth process diverges.

**Imported facts** (statements restated; proofs live in the main chain and are themselves
GIC-free — citation convention: lemmas are cited by number, as L0, L1, … or Lemma 2, with
primes marking strengthened variants and a superscript B the Stage-B permanent-shock
counterparts):
- **(I-sandwich)** κ̲m ≤ c(m) ≤ min(m, κ̲(m−1+h)), i.e. 0 ≤ g ≤ ḡ := κ̲(h−1), with g(m) > 0 for
  m > m̄ := κ̲(h−1)/Þ_R, and the Euler equality region a(m) > 0 ⊇ {m > m̄}.
  [Proof: `stage_A_proof.md` Lemma 2/2′ (ψ≡1) and `stage_B_proof.md` L2^B/L2′^B (general ψ) —
  a Coleman-operator invariance argument using only Jensen at the perfect-foresight test point;
  no impatience condition of any kind enters.]
- **(I-identity)** the exact wealth recursion, pathwise on m > m̄:
      ψ′·w̄′ = Þ_Γ·w̄ + W′ + ℛ·g(w̄),    W := ψ(θ+h−1) − h,  E[W] = 0,  Var(W) = σ_B²,
  reducing at ψ ≡ 1 to w̄′ = Þ_Γw̄ + (θ−1) + ℛg(w̄).
  [Proof: `stage_A_proof.md` Lemma 3.1 / `stage_B_proof.md` Lemma B-3.1–3.2 (machine-verified);
  pure budget-constraint algebra, no optimality content beyond the definition of g.]
- **(I2)** the identity 1 + κ̲ℛ/Þ_Γ = ℛ/Þ_Γ (algebra of the patience factors).

---

## §2. The elementary inequalities (self-contained)

:::{prf:lemma} Quantified Jensen (Sub-lemma E1)
:label: lem-imp-E1

Let f be twice differentiable on an interval I with
f″ ≥ μ > 0 on I, and let Z be a random variable with values in I, E[Z] = v ∈ I, Var(Z) = s².
Then E[f(Z)] ≥ f(v) + μs²/2.
:::
*Proof.* Taylor–Lagrange pointwise: f(z) ≥ f(v) + f′(v)(z−v) + μ(z−v)²/2 for z ∈ I; take
expectations. ∎

:::{prf:lemma} Sub-lemma E2
:label: lem-imp-E2

For 0 ≤ ω ≤ min(1, ρ): (1+ω)^{−1/ρ} ≤ 1 − c_ρ·ω with c_ρ := ln2/(2ρ).
:::
*Proof.* u := ln(1+ω)/ρ ≤ 1 (since ln(1+ω) ≤ ω ≤ min(1,ρ)); e^{−u} ≤ 1 − u/2 on [0,1] (the
function 1 − u/2 − e^{−u} vanishes at 0, rises to 0.153 at ln2, and is 0.132 at 1);
ln(1+ω) ≥ ω·ln2 on [0,1] (concavity: chord through 0 and 1). Chain them. ∎

---

## §3. Lemma J-B (the master floor) and Lemma J-A (its ψ≡1 case)

:::{prf:lemma} Lemma J-B — the master floor (PROVEN-HERE)
:label: lem-imp-JB

Under X1–X5 with σ_B² > 0, there is an explicit threshold w̄_B0 < ∞ — any w̄ with m > m̄,
C_W ≤ v, ℛḡ ≤ Þ_Γw̄, and ω(w̄) ≤ min(1, ρ) below, where C_W := ess-sup|W| ≤
max{h − ψ_min(h−1), ψ_max(θ_max+h−1) − h} — such that

$$
g(\wbar) \geq c_-\,\sigma_B^2\,\wbar^{-1} \quad \text{for all } \wbar \geq \wbar_{B0}, \qquad
c_- := \ln 2 \cdot \kap(\rho+1)\, 2^{-(\rho+6)} / (\Rcal\,\ThornG).
$$ (eq-imp-floorB)
:::

*(Symbol note, RB1 N-c: the main-chain documents define their C_W as the explicit max
itself, a valid over-estimate of this ess-sup; every use below needs only
supp W ⊆ [−C_W, C_W] and the C_W ≤ v threshold, so either convention is sound — the two
symbols coincide in role, not value.)*

*Proof.* On m > m̄ the Euler equation [](#eq-imp-euler) holds with equality. By (I-sandwich),
c(m′) ≤ κ̲(m′−1+h) = κ̲w̄′, so

    c(m)^{−ρ} ≥ Þ_Γ^ρ·E[ψ^{−ρ}(κ̲w̄′)^{−ρ}] = Þ_Γ^ρκ̲^{−ρ}·E[Z^{−ρ}],
    Z := ψ·w̄′ = v + W       (by (I-identity)),      v := Þ_Γw̄ + ℛg(w̄) ≥ Þ_Γw̄,

where the ψ^{−ρ}-weight and the 1/ψ in w̄′ have merged into Z (this is the entire role of the
permanent shock here). Z is supported in [v − C_W, v + C_W] and Z = ψw̄′ ≥ ψ_min·(h−1) > 0 a.s.
(the pathwise positivity is what keeps E[Z^{−ρ}] well-defined even at the equality C_W = v,
where the interval's left endpoint touches 0 — wording tightened per RB1 N-d; an infinite
E[Z^{−ρ}] would in any case only strengthen the floor); E[Z] = v (E[W] = 0); Var(Z) = σ_B².
The map f(z) := z^{−ρ} has
f″(z) = ρ(ρ+1)z^{−(ρ+2)} ≥ μ := ρ(ρ+1)(v + C_W)^{−(ρ+2)} on the support. Sub-lemma E1:

    E[Z^{−ρ}] ≥ v^{−ρ} + μσ_B²/2   ⟹   c(m)^{−ρ} ≥ Þ_Γ^ρκ̲^{−ρ}v^{−ρ}·(1 + ω),
    ω := (μσ_B²/2)·v^{ρ} = (ρ(ρ+1)σ_B²/2)·v^{−2}·(1 + C_W/v)^{−(ρ+2)}.

For w̄ ≥ w̄_B0: v ≤ 2Þ_Γw̄ (from ℛg ≤ ℛḡ ≤ Þ_Γw̄) and (1 + C_W/v)^{−(ρ+2)} ≥ 2^{−(ρ+2)} (from
C_W ≤ v), so

    ω ≥ ω₋(w̄) := (ρ(ρ+1)σ_B²/2)·2^{−(ρ+4)}·(Þ_Γw̄)^{−2}.

Inverting the marginal-utility inequality and applying Sub-lemma E2 (valid once ω ≤ min(1,ρ),
folded into w̄_B0):

    c(m) ≤ (κ̲/Þ_Γ)·v·(1+ω)^{−1/ρ} ≤ κ̲w̄·(1 − c_ρω) + (κ̲ℛ/Þ_Γ)·g(w̄),

using v = Þ_Γw̄ + ℛg and discarding the negative cross term. Rearranging with g = κ̲w̄ − c and
the identity (I2), g·(ℛ/Þ_Γ) = g·(1 + κ̲ℛ/Þ_Γ) ≥ κ̲w̄·c_ρ·ω₋(w̄):

    g(w̄) ≥ (Þ_Γ/ℛ)·κ̲·(ln2/(2ρ))·(ρ(ρ+1)σ_B²/2)·2^{−(ρ+4)}·(Þ_Γw̄)^{−2}·w̄
         = ln2·κ̲(ρ+1)·2^{−(ρ+6)}·σ_B² / (ℛ·Þ_Γ) · w̄^{−1}.   ∎

*(The constant is deliberately crude — the 2^{−(ρ+6)} collects the v ≤ 2Þ_Γw̄ and support-shift
concessions; only positivity and explicitness matter here. The SHARP w̄^{−1} coefficients, where
they exist (q↑ > 1), are Theorems [A3](#st-thm-A3)/[B3](#st-thm-B3) of the main chain, and they
exceed every version of c₋σ² — consistency verified in `verify_algebra.py` item (5).)*

:::{prf:lemma} Lemma J-A — transitory-only (the ψ ≡ 1 case; PROVEN-HERE)
:label: lem-imp-JA

Under X1–X5 with ψ ≡ 1 and σ² = Var(θ) > 0: g(w̄) ≥ c₋·σ²·w̄^{−1} for w̄ ≥ w̄_A0 (the same
formula with W = θ − 1, C_W = max(1−θ_min, θ_max−1), σ_B² = σ²). ∎
:::

---

## §4. The impossibility theorems

:::{prf:proposition} Proposition A0 (transitory-only)
:label: prop-imp-A0

Under X1–X5 with ψ ≡ 1 and the nondegeneracy σ² = Var(θ) > 0,

$$
\liminf_{\wbar\to\infty} \wbar\,g(\wbar) \;\geq\; c_-\sigma^2 \;>\; 0.
$$ (eq-imp-A0)
:::

:::{prf:proposition} Proposition B0 (permanent shocks)
:label: prop-imp-B0

Under X1–X5 with the nondegeneracy σ_B² > 0,

$$
\liminf_{\wbar\to\infty} \wbar\,g(\wbar) \;\geq\; c_-\sigma_B^2 \;>\; 0.
$$ (eq-imp-B0)
:::

:::{prf:corollary} No exponential — indeed no o(1/w̄) — decay
:label: cor-imp-noexp

For EVERY calibration in the class (patient or impatient, GIC satisfied or violated, with or
without permanent shocks, with or without the unemployment atom):

1. g(m) = O(e^{−λm}) is impossible for every λ > 0;
2. more generally g(m) = o(m^{−1}) is impossible: any proposed decay form for the gap that
   vanishes faster than the reciprocal of wealth — exponential, Gaussian, m^{−1−δ}, m^{−1}/ln m,
   … — is wrong as an asymptotic statement;
3. quantitatively, the floor scales with the forcing variance σ_B² = E[ψ²]σ_θ² + h²σ_ψ²:
   permanent-shock risk enters through **human-wealth revaluation**, amplified by h² —
   models with permanent shocks sit FURTHER from any exponential-type heuristic than
   transitory-only models, not closer.
:::

*Proof.* Immediate from the propositions. ∎

*Sharpness.* The floor's exponent is sharp: at q↑ > 1 the gap IS ≍ w̄^{−1} (Theorems
[A3](#st-thm-A3)/[B3](#st-thm-B3)); at q↑ < 1 it is ≍ w̄^{−q↑} ≫ w̄^{−1} — the floor is then
far from tight, but the impossibility conclusion is only strengthened.

---

(imp-sec-ownership)=
## §5. Ownership and dependency note (recorded per the refactor directive)

**Factorization choice:** this document OWNS the proofs of Lemmas J-A/J-B and Propositions
A0/B0. The main chains import them:
- `stage_A_proof.md` §6.1 = statement of Lemma 6.1 ≡ J-A + pointer here (consumed by: Prop A0;
  Lemma 6.3's explicit base — the R2 F-3 repair; the doubling Lemma 7.1's lower input at
  p = 1; Theorem A3's W₁-floor);
- `stage_B_proof.md` §B3 = statement of Lemma B-6.1 ≡ J-B + pointer here (consumed by: Prop B0;
  Theorem B1's lower-bound base anchoring; L8^B; Theorem B3's W₁-floor).
Conversely this document IMPORTS (statements restated in §1, proofs by reference, both
GIC-free): the sandwich (Lemma 2 / L2^B), the exact recursion (Lemma 3.1 / B-3.1–3.2), and
existence (X5 ⟵ §B11's verified routing). Nothing is proven twice.

## §6. Practical implication for solution methods

The high-wealth extrapolation of a buffer-stock consumption function must NOT be exponential:

- HARK's historical `decay_extrap` form `exp(−B·x)` and the solution-method heuristic
  `exp(−MPCmin·m)` are **mis-specified for every calibration in the class** — not merely for
  some parameter corner. The gap they are extrapolating is bounded BELOW by c₋σ_B²/w̄.
- The principled replacement is the power-law form `gap ≈ C·w̄^{−q}` with `q = min(1, q↑)`
  (main-chain Theorems [A1](#st-thm-A1)–[A3](#st-thm-A3)/[B1](#st-thm-B1)–[B3](#st-thm-B3)),
  implemented in the HARK PR as `decay_extrap_form='powerlaw'`.
- Why the exponential heuristic *looked* fine historically: near the GIC knife-edge
  (Þ_Γ → 1) the one-step rescaling is near-additive on any bounded window w̄ ≲ 1/(1−Þ_Γ), so
  an exponential fits WELL over bounded estimation grids. For HAFiscal's patience-ceiling
  college calibration (β constructed at the growth-impatience cap, not estimated), growth
  impatience holds, but only barely — so the
  near-additive window is wide enough to cover that calibration's entire estimation grid; see
  main-chain [Cor. A4.4](#st-cor-A4). Asymptotically it is still wrong, for every calibration;
  the error is in the extrapolated tail, not the solved region.

## §7. Numerical validation

- **R1's adversarial battery** (`review/R1_check_A0.py` + `_out.txt`): the bound holds with
  THESE constants (no refitting) on 14 calibrations — σ_log ∈ {0.02, 0.10, 0.30}; true θ = 0
  atoms (℘ ∈ {0.05, 0.15}); ρ ∈ {0.5, 2, 5}; impatient (q↑ = 0.21) ± atom; near-knife-edge —
  **including a GIC-VIOLATING calibration** (Þ_Γ = 1.0098: RIC+FHWC+FVAC hold, GIC fails), the
  decisive test of the GIC-free claim. Minimum margin 4232× above the floor (consistent with
  the deliberately crude 2^{−(ρ+6)}); at q↑ > 1 the measured infimum equals the theory's own
  sharp amplitude B, exactly as the consistency requirement predicts.
- **Consistency check c₋σ² < B** across admissible calibrations: `verify_algebra_out.txt`
  item (5).
- **Stage-B floors**: the measured permanent-shock amplitudes (`measure_tail_B_out.txt`)
  sit at B_ψ ≈ 9–11 for Var(ψ) ≈ 0.002 — the h² ≈ 1200 human-wealth-revaluation
  amplification of item 3 above, measured.
- Local slope diagnostics never diverge (the exponential signature) and converge to
  −min(1, q↑) ∈ [−1, 0): `Code/HA-Models/decay_form/` saved outputs.
