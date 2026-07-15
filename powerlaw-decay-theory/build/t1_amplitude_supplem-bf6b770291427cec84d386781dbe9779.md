# Supplement: the T−1 gap amplitude in closed form (the F8 recursion's seed)

**Status:** RECORD, SUPPLEMENTAL (2026-07-12; owner placement ruling: "maybe
as supplemental material or an appendix; not in the main body"). This file
records one validated data point for [open item 2 of
`grid_design_final_spec.md`](#grid-sec-open-items) (derive the exact (λ_t, F_t) of [the F8
amplitude recursion](#grid-rem-f8)). It changes no main-body document and anchors no shipped
machinery: per [the F11 uniformity ruling](#grid-def-f11), B_t stays DIAGNOSTIC-ONLY (level
continuity removed amplitude-anchoring), and the deep-tail region has
negligible agent occupancy — the practical weight of this constant is
validation/derivation bookkeeping, nothing more.

## The result

:::{prf:proposition} The T−1 gap amplitude in closed form
:label: t1-prop-amplitude

For the transitory-only case (ψ ≡ 1, LivPrb = 1, Γ = 1; discretized θ with
E[θ] = 1), one period before the c(m) = m terminal — writing h_{T−1} = 1 + 1/R
for human wealth at T−1 (BST's convention: the current period's income is
included), w̄ := m − 1 + h_{T−1} for perfect-foresight total wealth (the bar
marks the optimist's upper-bound object, as in BST's c̄), and
g_{T−1}(w̄) := c̄_{T−1}(m) − c_{T−1}(m) for the gap (precautionary saving)
below the perfect-foresight rule c̄_{T−1}(m) = κ(m − 1 + h_{T−1}), κ = R/(R+Þ):

$$
\wbar \cdot g_{T-1}(\wbar) \to B_{T-1} = (\rho+1) \cdot \mathrm{Var}(\theta) / (2 \cdot \Thorn \cdot R), \qquad \Thorn = (\beta R)^{1/\rho}.
$$ (t1-eq-amplitude)

Since B_T = 0, [the F8 recursion](#grid-rem-f8) B_t = λ_t·B_{t+1} + F_t gives
**B_{T−1} = F_{T−1}**: this is the exact forcing term at the recursion's
seed, and a falsifiable target for any candidate (λ_t, F_t) derivation.
:::

## Derivation sketch (verified numerically; see Validation)

1. T−1 Euler with the terminal policy: c^{−ρ} = βR·E[(Ra + θ)^{−ρ}],
   a = m − c.
2. Expand at large a using E[θ] = 1: E[(Ra+θ)^{−ρ}] = (Ra)^{−ρ}·
   [1 − ρ/(Ra) + ρ(ρ+1)E[θ²]/(2R²a²) + O(a^{−3})]. Inverting through
   (·)^{−1/ρ}, the E[θ]-terms assemble the perfect-foresight line
   c̄(a) = (Ra+1)/Þ exactly, and the surviving second-order coefficient is
   −(ρ+1)(E[θ²]−1)/(2R²) = −(ρ+1)Var(θ)/(2R²):
   c(a) = (Ra+1)/Þ − (ρ+1)Var(θ)/(2ÞRa) + O(a^{−2}).
3. The gap is defined at MATCHED m, not matched a: inverting m = a + c(a)
   and comparing with c̄(m) = κ(m − 1 + h_{T−1}) cancels the
   (1−κ) bookkeeping exactly and leaves g(m) = D/m + O(m^{−2}) with
   D = (ρ+1)Var(θ)/(2ÞR); w̄ = m − 1 + h_{T−1} ⟹ w̄·g → D. (A matched-a
   reading gives a spurious (Þ+R)/Þ-type factor — the inversion step is
   load-bearing.)

## Validation (2026-07-12, adversarial-refuter pass of the downstream
mapping workflow; all three routes independent)

At the public MoM notebook calibration (ρ = 2, β = 0.96, R = 1.02,
θ ~ 7-atom lognormal(σ = 1) discretization, Var(θ_disc) = 1.035381):
B_{T−1} = 1.538706, and

1. measured w̄·g at the deepest Euler-certified knot of a dense T−1 solve:
   ratio to B_{T−1} = 0.999946;
2. a 1/X-form extrapolation of the measured w̄·g: W_∞ = 1.538706
   (rel. dev. −1.4e−07);
3. a solver-independent direct bisection of the T−1 Euler equation at
   m = 10⁶: w̄·g / B_{T−1} = 1.000010 (and |c_direct/c_solved − 1| = 0).

Provenance pin: logistic-vs-powerlaw-unit-interval-mapping @ b4225a1 ::
checks/refuter_chi_slope_checks.py :: R6 (+ committed
refuter_chi_slope_checks_out.txt).

## Scope and open remainder

Un-derived here: the general-ψ / LivPrb < 1 / Γ ≠ 1 form of F_{T−1} (the
expansion generalizes mechanically — ψ enters the return factor R/(Γψ) and
the premium becomes a joint-moment expression — but no general form has been
written down or validated), and everything about λ_t and F_t for t < T−1.
[Open item 2 of `grid_design_final_spec.md`](#grid-sec-open-items) remains open; this
supplement just gives its future derivation a validated seed and a registered target.
