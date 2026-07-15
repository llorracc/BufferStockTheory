# Alternative proof γ: the compactified domain and the boundary fixed point

**AUTHOR PASS (2026-07-07) + INDEPENDENT REFUTER PANEL RF1/RF2 (2026-07-08): ZERO
BROKEN, ZERO MODERATE.** RF1 (proof-logic lens): every PROVEN-HERE item re-derived
line-by-line from the declared imports (γ0/γ1/γ2/γ3, γ-A, γ-R1/γ-R, γ-T, γ-C1/γ-C2,
γ-B1/γ-B2/γ-B3, γ-B — all VERIFIED; no petitio principii at the boundary, no
uniqueness-class gap, no hidden uniformity in γ3, no illegitimate ψ-limit exchange);
the GAP-γ-equicont quarantine HOLDS (consumer audit clean). Two MINOR bookkeeping
findings (RF1-F1/F2) and two display notes (RF1-F3/F4) are repaired in place below,
each marked "(repaired per review RF1-…)"; no constant moves. RF2 (numerics lens):
all theorems VERIFIED on fresh/hostile designs the author never ran — Pareto-θ at the
L4′ moment boundary × Þ_Γ = 0.95, ρ = 6, zero-atom θ, skewed deep-forward
ψ_min = 0.4 ≪ Þ_Γ, a wrong-weight plateau sweep pinning the (γ7.1) ψ²-weight (root
ŵ = 1.9999, margin 6647×), and exact detection rates for γ-T; findings RF2-N1–N3
(evidence-route and remark-level) applied below. The two registered RT1 FAILs stand,
adjudicated by BOTH packs as honest crossover phenomenology (crossover-corrected
intercepts land on B to 0.006–0.10%), not masked defects. Packs:
`review/RF1_compactified_logic.md`, `review/RF1_altproof_compactified_verdicts.md`,
`review/RF2_altproof_compactified_numerics.md` (+ their `RF*_check_*` scripts).

**Companion to** `statement.md` (theorem statements and the shared assumption block),
`stage_A_proof.md` §§1–5 (the imported foundations) and `stage_B_proof.md` §§B0–B3 (their
ψ-general forms). Numerical verification with pre-registered falsifiers:
`verify_altproof_compactified_checks.py` (+ saved output `_out.txt` beside it); results
summarized in §10, including two registered near-resonance checks that FAILED as registered
and are reported, not tuned away.

---

## §0. Scope, status, and the firewall

**What this document is.** The repo owner asked for a proof route in these words:

> "compress the space from 0 to infinity by assuming the power law holds in the limit, so
> that there is a finite number (probably 1) that represents the exact limit as assets
> approach infinity — it might be easier to prove, and easier to understand, than the other
> proofs."

This document makes that intuition rigorous. The coordinate `z := 1/x` compresses the wealth
ray `[x_a, ∞)` to the half-open interval `(0, z_a]`; the point at infinity becomes the honest
boundary point `z = 0`, which we adjoin. "Assuming the power law holds in the limit" is
implemented as a *choice of units*: we study the **compensated gap** `W(z) := x^q·g(x)` with
`q := min(1, q↑)`. The theorem then says: **`W` extends to a continuous function on the
compact interval `[0, z_a]`**, and at the added point the functional equation degenerates to
one scalar equation,

    W(0) = λ·W(0) + F(0),        λ = 1/(ℛÞ_Γ) < 1,   F(0) = c_J/ℛ,

whose unique solution is the owner's "one number",

    B = F(0)/(1−λ) = κ̲(ρ+1)σ²/(2(ℛÞ_Γ−1)).

That is the `q↑ > 1` case (§3). The document is equally explicit about where the one-number
picture **degenerates**: at `q↑ = 1` the boundary value is `+∞` and the finite number is a
*slope* (§4); at `q↑ < 1` the natural boundary is not a point but a **circle** — in log
wealth the dynamics repeat with period `Λ`, so what survives at infinity is the position of
`ln x` modulo `Λ` — and the finite object is a boundary *function* on that circle, proven
here only at the envelope level, with the equicontinuity step honestly tagged
`GAP-γ-equicont` (§6).

**Standing assumptions.** A0–A6 of `statement.md` (ψ ≡ 1, bounded θ, σ² > 0) for §§1–6 and §8;
the Stage-B block B-A0/A3–A6 for §7. Notation as in the companions:

    ℛ = R/Γ > 1,  Þ_Γ = (βR)^{1/ρ}/Γ < 1,  κ̲ = 1 − (βR)^{1/ρ}/R,  h = ℛ/(ℛ−1),
    x = m − 1 + h,  g(x) = κ̲x − c(m) ∈ [0, ḡ],  ḡ = κ̲(h−1),  Λ = ln(1/Þ_Γ),  q↑ = ln ℛ/Λ,
    σ² = Var(θ);   Stage B adds  σ_B² = E[ψ²]σ_θ² + h²σ_ψ²  and  q↑ = the (E)-root.

Here `h` is [BST's human wealth](https://llorracc.github.io/BufferStockTheory-Latest/#eq-hdef)
— the Γ-normalized PDV of labor income *including* the current period's unit, with limiting
value `h = 1/(1 − ℛ^{−1}) = ℛ/(ℛ−1)` — so the PDV of future labor income alone is
`h − 1 = 1/(ℛ−1)`. Two conversions connect this page's letters to the reader-facing
statement and proof pages. First, the wealth variable `x := m − 1 + h` is exactly their `w̄`:
perfect-foresight total wealth (human and market), the wealth of the optimist, the bar
marking the optimist's upper-bound object as in BST's own
[`c̄(m) = κ̲·(m − 1 + h)`](https://llorracc.github.io/BufferStockTheory-Latest/#eq-cfuncpfunc);
this page keeps the letter `x` because its coordinate apparatus (`z := 1/x`) and the chart
convention it cites (`v = 1/x`) are built on it. Second, the gap
`g(x) = κ̲x − c(m) = c̄(m) − c(m)` is exactly their **precautionary saving** `s(m)`,
expressed in `x`; on this page the letter `s` is reserved for the free compensation exponent
of §1.2, so the gap keeps the letter `g`.

**Import list (everything consumed, nothing else).** From `stage_A_proof.md`: L0/L1
(existence; c continuous, increasing, concave), Lemma 2/2′ (sandwich `0 ≤ g ≤ ḡ`, strict
`g > 0` on `m > m̄`, g non-increasing convex, Euler equality on `m > m̄`), Lemma 3.1/Cor 3.2
(exact recursion (3.1) and excursion bound (3.2) with `C₀`), Lemma 5.1 (the one-step identity
(5.2) with (5.3)–(5.5)), Corollary 5.2 (the upper/lower one-step comparison bounds, with
`K̂`), Lemma 5.3 (= L4′, cited only in a robustness remark), Lemma 10.1 (= A5, cited only
for the convex geometry of 𝔏 in §5/§7).
From `stage_B_proof.md`: (B3.1)/(B3.2), Lemma B-5.1 ((B5.2)–(B5.5)), Corollary B-5.2, the
`x₀^B` threshold block (B5.0). As **benchmarks only** (targets to match, never used in a
proof): Theorem A3's `B`, Theorem B3's `B_ψ`, Theorem B-res's constant, Theorem A2's `P`.

**Firewall (engines deliberately NOT used).** None of: stage_A §6–§8 (ladder/renewal
machinery, Lemmas 6.2/6.3/7.2/8.1), Feller/AMN/Blackwell key-renewal theorems, the stage_B
§B4 tilt toolkit (T1)–(T6) or its deployments, Goldie/Kesten implicit renewal (§B7), the
B2-arith lattice Fourier apparatus. Every lemma below is proven from the import list plus
elementary real analysis. One honest near-miss is flagged where it occurs: the Stage-B
boundedness lemma γ-B2 uses a stopped *expectation unroll* — a path-sum-flavored argument
(no tilt, no renewal, no change of measure), the single place this route borrows that
flavor. (Disclosure sharpened per review RF1-F4: the device is structurally the same as
stage_B §B5's own B1(i) boundedness iteration — chain + stopping time + per-step weight +
E[ψ]=1 kill; no text or statement is imported, so the firewall stands, but the credit is
owed to stage_B §B5's boundedness proof specifically. The γ-route's genuinely new Stage-B
content is the boundary-stability assembly (γ-B3), not the boundedness technique.)

**Kinship note.** Two sibling alternative-proof documents (a probabilistic path-sum route and
a recursion-tree/Akra–Bazzi route) are being written independently; by construction this
document shares with them only the one-step identity and the geometric resolvent — see §9 for
why that sharing is forced. Their files were not read.

**Status vocabulary.** PROVEN-HERE / PROVEN-CITED / SKETCHED / GAP / OPEN, as in the ledger.

**Internal red-team disclosure.** Before this version was committed, an adversarial
self-pass ran the brief's attack list (shell-index bookkeeping; the phase-displacement
control of §6; the Cesàro step; the boundary cases q↑ ∈ {1±δ}; the Stage-B forward window;
fat-tailed θ). It
caught and fixed two drafting defects — the Stage-B backward-band lemma's shell width
(γ-B1: the guaranteed backward step is `ln(ψ_min/Þ_Γ)`, not Λ, so Λ-shells self-refer
whenever ψ_min < 1; recorded in place) and a missing cross-term factor in (γ6.1) — and it
kept two registered numerical falsifiers FAILED (RT1, §10) rather than repairing them
post hoc. The independent (non-author) refuter pass was completed 2026-07-08 (RF1/RF2 —
see the header block above); its repairs are applied in place.

**Reading order if you only read one page:** §9.

---

## §1. The compactified coordinate, the compensation, and the shell equation

### 1.1 The coordinate and the boundary point

Fix an anchor `x_a ≥ x₀` (pinned in (γ1.4) below; `x₀` is stage_A's (5.0) threshold) and set

    z := 1/x,     z_a := 1/x_a,

mapping `[x_a, ∞)` homeomorphically onto `(0, z_a]`. Adjoin the boundary point `z = 0`
("infinite wealth"). This is the one-dimensional instance of the classical Poincaré
compactification of dynamical systems — the chart at infinity there is literally `v = 1/x`,
with the line at infinity `{v = 0}` (Dumortier–Llibre–Artés 2006, ch. 5; coordinates
verified against the source, see References). Everything below happens on `[0, z_a]`; we
freely write `W(z)` and `W(x)` for the same object.

### 1.2 The compensation: "the power law holds in the limit" as a choice of units

For a free exponent `s > 0` define the **s-compensated gap**

(cpt-eq-g1-1)=

    W_s(x) := x^s·g(x)   ≥ 0,                                                  (γ1.1)

and reserve `W := W_q` for the theorem's compensation `q := min(1, q↑)`. Two elementary
facts, used silently: `W_s ≤ x^s·ḡ < ∞` on every bounded x-set (Lemma 2), and `W_s` is
continuous on `(0, z_a]` (c is continuous, L0/L1). The whole content of the theorems is the
behavior of `W_s` **at** `z = 0`.

### 1.3 Shells marching to the boundary, and the ζ-enlargement

The dynamics rescale wealth by `Þ_Γ` per period ((3.1): `x′ = Þ_Γx + (θ−1) + ℛg(x)`), so the
natural decomposition of `(0, z_a]` is into **geometric shells**. In x-coordinates:

(cpt-eq-g1-2)=

    X_n := [x_a·Þ_Γ^{−n}, x_a·Þ_Γ^{−(n+1)}),    n = 0, 1, 2, …                 (γ1.2)

In z these are `S_n = (z_aÞ_Γ^{n+1}, z_aÞ_Γ^n]`: `n → ∞` is exactly `z → 0`. One period of
`ln x` per shell: `Λ`.

The one-step comparison (Cor 5.2) evaluates `g` at the displaced points `Þ_Γx ∓ C₀`, and the
displacement `C₀` is *constant in x* ((3.2)); relative to the shell width (which grows like
`Þ_Γ^{−n}`) it vanishes, but near a shell edge it can cross the boundary. The clean fix is to
enlarge every shell by the **lifetime-displacement constant**

(cpt-eq-g1-3)=

    ζ := C₀/(1−Þ_Γ)      (already named ζ in stage_A (5.0a)),                   (γ1.3)

whose defining property is that it is the *fixed point of the displacement recursion*
`s ↦ Þ_Γ·s + C₀`: `Þ_Γζ + C₀ = ζ`. Why this is the right constant: `ζ = C₀ + Þ_ΓC₀ + Þ_Γ²C₀ + …`
is the largest total displacement the affine recursion can accumulate over an entire
trajectory, so a ζ-margin absorbs the worst case *exactly*, with no slack to iterate. Define
the **enlarged shells**

    X_n^ζ := [x_a·Þ_Γ^{−n} − ζ,  x_a·Þ_Γ^{−(n+1)} + ζ].

:::{prf:lemma} γ0 (exact referred-point containment). PROVEN-HERE.
:label: cpt-lem-g0

For every `n ≥ 0` and every `x ∈ X_{n+1}^ζ`, both displaced points satisfy

    Þ_Γx − C₀ ∈ X_n^ζ    and    Þ_Γx + C₀ ∈ X_n^ζ,

and the containment is exact (the extreme points of `X_{n+1}^ζ` map to the extreme points of
`X_n^ζ`).

:::

*Proof.* Upper end: `Þ_Γ·(x_aÞ_Γ^{−(n+2)} + ζ) + C₀ = x_aÞ_Γ^{−(n+1)} + (Þ_Γζ + C₀)
= x_aÞ_Γ^{−(n+1)} + ζ`, the top of `X_n^ζ`, using the fixed-point property of ζ. Lower end:
`Þ_Γ·(x_aÞ_Γ^{−(n+1)} − ζ) − C₀ = x_aÞ_Γ^{−n} − (Þ_Γζ + C₀) = x_aÞ_Γ^{−n} − ζ`, the bottom
of `X_n^ζ`. Displacements between `−C₀` and `+C₀` land between these. ∎

The payoff: the shell recursion below refers **only to the previous enlarged shell** — band
width zero, no self-reference, no sliver bookkeeping. (This is where a naive version of the
argument invites attack; the ζ-fixed-point makes the bookkeeping exact rather than
approximate. The Stage-B analogue genuinely loses this property — see §7.)

Domain admissibility: fix

(cpt-eq-g1-4)=

    x_a := ζ + max{ x₀,  2C₀/Þ_Γ,  K̂,  D̂ }        (D̂ from Lemma γ1 below),      (γ1.4)

so every point of every `X_n^ζ` (n ≥ 0) lies in `[x₀, ∞)` where the one-step identity
(5.2) and Corollary 5.2's comparison bounds hold,
and additionally `x_a ≥ 3ζ` (stage_A's (5.0a) already contains the entry `2ζ`, so
`x₀ ≥ 2ζ`), whence `inf X_{n+1}^ζ ≥ ½·x_aÞ_Γ^{−(n+1)}`. *Why each entry:* `x₀`
= the imported validity threshold of §5; `2C₀/Þ_Γ` makes the compensation ratio expandable
(u ≤ ½ below); `K̂, D̂` make the products of `(1 + small/x)` factors collapsible to one
`(1 + D̂/x)`.

### 1.4 The compensated one-step inequalities

Multiply Corollary 5.2's upper and lower one-step bounds by `x^s` and write the displaced
compensation ratio as

    x^s·g(Þ_Γx ∓ C₀) = (x/(Þ_Γx ∓ C₀))^s · W_s(Þ_Γx ∓ C₀)
                     = Þ_Γ^{−s}(1 ∓ u)^{−s} · W_s(Þ_Γx ∓ C₀),      u := C₀/(Þ_Γx).

Define the **boundary multiplier** and the **compensated forcing**

    λ(s) := Þ_Γ^{−s}/ℛ  =  Þ_Γ^{q↑−s}  =  e^{−(q↑−s)Λ},        F_s(x) := ℛ^{−1}·x^s·J(x).

*Why λ(s) has this form:* one step of the dynamics divides `x` by `Þ_Γ^{−1}` (one shell), so
the compensation `x^s` gains a factor `Þ_Γ^{−s}`, while the Euler identity (5.2) divides the
right side by `ℛ`; the second equality is stage_A's identity (I4) `Þ_Γ^{−q↑} = ℛ`. Note

    λ(s) < 1 ⟺ s < q↑,     λ(s) = 1 ⟺ s = q↑,     and at s = 1:  λ(1) = 1/(ℛÞ_Γ).

:::{prf:lemma} γ1 (the shell equation with boundary-continuous coefficients). PROVEN-HERE (i, iii, iv elementary; ii imports (5.3)/(5.4)).
:label: cpt-lem-g1

Let `s ∈ (0, 1]`. With `D̂ := 2(K̂ + 2C₀/Þ_Γ)`, for all `x ≥ x_a − ζ` (hence on every `X_n^ζ`):

(cpt-eq-gupdn)=

    (γ-up)   W_s(x) ≤ (1 + D̂/x)·[ λ(s)·W_s(Þ_Γx − C₀) + F_s(x) ],
    (γ-dn)   W_s(x) ≥ (1 − D̂/x)·[ λ(s)·W_s(Þ_Γx + C₀) + F_s(x) ],

and:

  (i) *(coefficient limit)* the effective multipliers `(1 ± D̂/x)λ(s)` converge to `λ(s)` as
      `z → 0`, with the explicit envelope `D̂/x = D̂z`;
  (ii) *(forcing limit and bound)* `0 ≤ F_s(x) ≤ ℛ^{−1}x^{s−1}·J̄` with
      `J̄ := j₊(σ² + ℛ²ḡ²)` (from (5.3)); at `s = 1`, `F₁(x) → F(0) := c_J/ℛ` as `z → 0`
      (from (5.4)); **no rate for this limit is assumed or needed anywhere below**;
      for `s < 1`, `F_s(x) → 0` at the geometric shell-rate `Þ_Γ^{(1−s)n}`, and
      `F_s(x) ≥ (j₋σ²/ℛ)·x^{s−1} > 0` (from (5.3));
  (iii) *(referred-point containment)* Lemma γ0;
  (iv) *(z-picture)* in the z coordinate the referred points are
      `z″ = z/Þ_Γ ± (C₀/Þ_Γ²)z² + O(z³)`: the map `z ↦ z/Þ_Γ` up to a displacement of order
      `z²`, which vanishes at the boundary faster than the coordinate itself; the boundary
      point `z = 0` is fixed.

:::

*Proof.* (γ-up): from Corollary 5.2's upper bound,
`W_s(x) ≤ (1+K̂/x)·λ(s)ℛ·ℛ^{−1}(1−u)^{−s}W_s(Þ_Γx−C₀)
+ (1+K̂/x)F_s(x)`. For `x ≥ 2C₀/Þ_Γ` we have `u ≤ ½`, and for `s ≤ 1`,
`(1−u)^{−s} ≤ (1−u)^{−1} ≤ 1 + 2u = 1 + 2C₀/(Þ_Γx)`. Then
`(1+K̂/x)(1+2C₀/(Þ_Γx)) ≤ 1 + D̂/x` for `x ≥ max(K̂, 2C₀/Þ_Γ)` (the cross term
`2K̂C₀/(Þ_Γx²)` is ≤ `min(K̂, 2C₀/Þ_Γ)/x` there, and the sum of the three terms is ≤ `D̂/x`
by the choice `D̂ = 2(K̂ + 2C₀/Þ_Γ)`). Since the bracket multiplying it is nonnegative, the
enlarged factor can be pulled out front. (γ-dn): `(1+u)^{−s} ≥ 1 − su ≥ 1 − u` (Bernoulli,
`s ≤ 1`), and `(1−K̂/x)(1−u) ≥ 1 − D̂/x`; the forcing keeps a factor `≥ (1−D̂/x)`.
(i) is the display; (ii) is (5.3)/(5.4) multiplied by `ℛ^{−1}x^{s−1}`, plus, on shell `X_n^ζ`,
`x ≥ ½x_aÞ_Γ^{−(n+1)}`, giving the geometric rate; (iii) is Lemma γ0; (iv) is one division:
`1/(Þ_Γx ∓ C₀) = (z/Þ_Γ)(1 ∓ C₀z/Þ_Γ)^{−1}`. ∎

### 1.5 The shell sequences

For `n ≥ 0` define

    M_n(s) := sup_{X_n^ζ} W_s,     m_n(s) := inf_{X_n^ζ} W_s,     δ_n := 2D̂·Þ_Γ^{n+1}/x_a.

Each `M_n(s)` is finite (`W_s ≤ x^sḡ` on the compact shell) and each `m_n(s) ≥ 0`. By Lemma
γ1 (take sup/inf over `x ∈ X_{n+1}^ζ`; the referred points range in `X_n^ζ` by γ0, and on
`X_{n+1}^ζ`, `D̂/x ≤ δ_n` by `x_a ≥ 2ζ` — a consequence of (γ1.4), which derives
`x_a ≥ 3ζ`; citation repaired per review RF1-F3: (γ1.4) has no literal `x_a ≥ 2ζ` entry):

(cpt-eq-g1-5)=

    (γS-up)   M_{n+1}(s) ≤ (1 + δ_n)·[ λ(s)·M_n(s) + F_n⁺(s) ],
    (γS-dn)   m_{n+1}(s) ≥ (1 − δ_n)·[ λ(s)·m_n(s) + F_n⁻(s) ],                 (γ1.5)

with `F_n⁺(s) := sup_{X_{n+1}^ζ} F_s`, `F_n⁻(s) := inf_{X_{n+1}^ζ} F_s`. Three facts carried
forward:

    Σ_n δ_n = 2D̂Þ_Γ/(x_a(1−Þ_Γ)) < ∞           (geometric — the summable perturbation budget);
    at s = 1:  F_n⁺, F_n⁻ → c_J/ℛ               (the shells recede, so (5.4) pinches both);
    at s < 1:  F_n⁺ ≤ (J̄/ℛ)(½x_aÞ_Γ^{−(n+1)})^{s−1} → 0 geometrically, Σ_n F_n⁺ < ∞.

This — a scalar recursion per shell, marching `n → ∞` toward the boundary point — is the
entire apparatus. Every theorem below is a statement about what such a recursion can do.

*Remark 1.6 (the exact equation, for the narrative).* Multiplying the exact identity (5.2)
by `x` gives the equality version at `s = 1`:

(cpt-eq-g1-6)=

    (1 + r_L(x))·ℛ·W₁(x) = (1 + r_R(x))·E[ (x/x′)·W₁(x′) ] + x·J(x),            (γ1.6)

with `r_L, r_R = O(1/x)` (5.5), `x/x′ → Þ_Γ^{−1}` a.s. (3.2), `x·J(x) → c_J` (5.4). Once a
boundary limit of `W₁` is known to exist (that is γ3's job), (γ1.6) passes to the limit by
dominated convergence and becomes the scalar boundary equation of §3. The monotone bracket
(γ-up)/(γ-dn) is the workhorse; (γ1.6) is the punchline.

---

## §2. The two core lemmas: boundedness and boundary stability

Both lemmas are self-contained: they consume only (γ1.5) and elementary analysis. In
particular **Theorem A1 is NOT imported** — boundedness is proven internally, which keeps
this route free-standing.

:::{prf:lemma} γ2 (boundedness on the compactified domain). PROVEN-HERE.
:label: cpt-lem-g2

Let `(M_n)` satisfy (γS-up) with `M_n ≥ 0`, `Σδ_n < ∞`, and either

  (i) `λ(s) < 1` and `F̄ := sup_n F_n⁺(s) < ∞`,  or
  (ii) `λ(s) ≤ 1` and `Σ_n F_n⁺(s) < ∞`.

Then `sup_n M_n(s) < ∞`. Consequently (cases): `W₁` is bounded on `[x_a, ∞)` when `q↑ > 1`
(case (i), `λ(1) = 1/(ℛÞ_Γ) < 1` by (I4)); `W_{q↑}` is bounded when `q↑ < 1` (case (ii),
`λ(q↑) = 1`, forcing geometrically summable by Lemma γ1(ii)); and for every `s < min(1, q↑)`,
`W_s` is bounded (case (i)).

:::

*Proof.* (i) Let `λ′ := (1+λ(s))/2 < 1` and pick `n₂` with `(1+δ_n)λ(s) ≤ λ′` for `n ≥ n₂`
(possible: `δ_n → 0`; explicitly `n₂ = ⌈Λ^{−1}·ln( 4D̂λ/(x_a(1−λ)) )⌉₊`, from solving
`δ_n = 2D̂Þ_Γ^{n+1}/x_a ≤ (1−λ)/(2λ)` — *why:* it is the first shell where the coefficient
perturbation `δ_n` can no longer bridge the gap between `λ` and the midpoint `λ′`). Set

    K := max( M_{n₂},  F̄′/(1−λ′) ),     F̄′ := (1 + sup_n δ_n)·F̄.

If `M_n ≤ K` for some `n ≥ n₂` then `M_{n+1} ≤ λ′K + F̄′ ≤ λ′K + (1−λ′)K = K` (the second
inequality is the definition of K). Induction from `n₂`; the finitely many shells before
`n₂` are individually finite. (ii) Unroll (γS-up) with `λ(s) ≤ 1`:

    M_n ≤ Π_{j<n}(1+δ_j) · [ M₀ + Σ_{j<n} F_j⁺ ] ≤ P_∞·[ M₀ + Σ_j F_j⁺ ] < ∞,

with `P_∞ := Π_j(1+δ_j) ≤ e^{Σδ_j} < ∞`. ∎

*Remark.* The two hypotheses are exactly the two ways a recursion `M_{n+1} ≈ λM_n + F_n` can
stay bounded; the *resonant* combination `λ = 1` with `F_n → F_∞ > 0` is precisely the
excluded case, and indeed there `W₁` is unbounded (§4). Nothing beyond `g ≤ ḡ` (for the
anchor) and (γ1.5) was used.

:::{prf:lemma} γ3 (boundary stability — the engine). PROVEN-HERE.
:label: cpt-lem-g3

Let `λ ∈ [0, 1)`, `b ∈ ℕ` fixed, and let `(M_n)`, `(m_n)` be bounded real sequences with
`m_n ≤ M_n`, satisfying for all large n

    M_{n+1} ≤ (1 + δ_n)·[ λ·max_{k∈[n−b, n]} M_k + F_n⁺ ],
    m_{n+1} ≥ (1 − δ_n)·[ λ·min_{k∈[n−b, n]} m_k + F_n⁻ ],

with `δ_n → 0` and `F_n⁺, F_n⁻ → F_∞ ∈ [0, ∞)`. Then

    lim_n M_n = lim_n m_n = F_∞/(1−λ).

:::

*Proof.* Let `S := limsup M_n < ∞`. Fix `ε > 0`; choose N with: `M_k ≤ S + ε` for all
`k ≥ N`, `δ_n ≤ ε`, `F_n⁺ ≤ F_∞ + ε` for all `n ≥ N`. For `n ≥ N + b`:
`M_{n+1} ≤ (1+ε)[λ(S+ε) + F_∞ + ε]`. Taking limsup and then `ε ↓ 0`: `S ≤ λS + F_∞`, so
`S ≤ F_∞/(1−λ)`. Symmetrically, with `I := liminf m_n > −∞`: for n large,
`m_{n+1} ≥ (1−ε)[λ(I−ε) + F_∞ − ε]`, so `I ≥ λI + F_∞`, so `I ≥ F_∞/(1−λ)`. Then

    F_∞/(1−λ) ≤ I = liminf m_n ≤ liminf M_n ≤ limsup M_n = S ≤ F_∞/(1−λ),

and the same chain with `limsup m_n` in the middle. All four limits coincide. ∎

*Remark (why this half-page is the engine).* The lemma is one-directional stability at a
boundary: an *inward-marching* recursion with asymptotically constant coefficients forgets
its data at the anchor and is trapped at the fixed point `F_∞/(1−λ)` of the limiting scalar
map `w ↦ λw + F_∞`. The window `b` is free (finite windows do not move a limsup); in Stage A
we only need `b = 0` (Lemma γ0), while Stage B uses a genuine window (§7). No rate for
`F_n → F_∞` and no monotonicity are needed — this is exactly why the compactified route is
short: (5.4) is consumed as a *limit*, never as an expansion.

*Function-level form (used in §7).* The same four lines run directly on
`S̄ := limsup_{x→∞} W(x)` and `s̲ := liminf_{x→∞} W(x)` when the recursion refers to points
`→ ∞`: one obtains `S̄ ≤ λS̄ + F(0)` and `s̲ ≥ λs̲ + F(0)`, hence both equal `F(0)/(1−λ)`.
Shells are needed only where the *count* of shells matters (§4) or the *phase* — the
position within the shell (§6) — matters.

---

## §3. Theorem γ-A: the boundary value at q↑ > 1 — the owner's one number

:::{prf:theorem} γ-A (continuity at the boundary point; the scalar boundary equation). PROVEN-HERE.
:label: cpt-thm-gA

Assume A0–A6, σ² > 0 and `q↑ > 1` (⟺ `ℛÞ_Γ > 1`, by (I4)). Let `W(z) = W₁(x) = x·g(x)`,
`z = 1/x`. Then `W` extends to a continuous function on the compact interval `[0, z_a]`,
with boundary value

    W(0) = B := F(0)/(1−λ) = (c_J/ℛ)/(1 − 1/(ℛÞ_Γ)) = c_J·Þ_Γ/(ℛÞ_Γ − 1)
          = κ̲(ρ+1)σ²/(2(ℛÞ_Γ − 1)).

Equivalently `g(x) = B/x + o(1/x)`. Moreover the exact one-step identity (γ1.6) passes to
the limit at `z = 0` and degenerates there to the **one scalar equation**

(cpt-eq-g3-1)=

    W(0) = λ·W(0) + F(0),        λ = 1/(ℛÞ_Γ),   F(0) = c_J/ℛ,                  (γ3.1)

whose unique solution (unique because `λ ≠ 1`) is `B`. The value matches Theorem A3's
amplitude exactly (benchmark import; A3 is not used).

:::

*Proof.* Boundedness: Lemma γ2(i) at `s = 1` (hypotheses: `λ(1) = 1/(ℛÞ_Γ) < 1`;
`F̄ ≤ J̄/ℛ < ∞` by Lemma γ1(ii)). Stability: the sequences `M_n(1), m_n(1)` satisfy Lemma
γ3's hypotheses with `b = 0` (by (γS-up)/(γS-dn), absorbing the outer `(1±δ_n)` into the
lemma's `δ_n`), `λ = 1/(ℛÞ_Γ)`, and `F_n^± → c_J/ℛ` (Lemma γ1(ii): the shells recede, so
(5.4) pinches sup and inf). Hence `M_n, m_n → F(0)/(1−λ) = B`. Every `x ≥ x_a` lies in some
plain shell `X_{n(x)} ⊂ X_{n(x)}^ζ` with `n(x) → ∞` as `x → ∞`, and
`m_{n(x)} ≤ W(x) ≤ M_{n(x)}`, so `lim_{x→∞} W(x) = B`, i.e. `lim_{z→0} W(z) = B`. Define
`W(0) := B`; continuity on `(0, z_a]` holds since c is continuous (L0/L1); continuity at 0
is the limit just proven. For (γ3.1): in (γ1.6), `r_L, r_R → 0` by (5.5); `x′/x → Þ_Γ`
uniformly a.s. by (3.2); `W₁(x′) → B` a.s. (since `x′ ≥ Þ_Γx − C₀ → ∞` a.s.) and `W₁` is
bounded, so dominated convergence gives `E[(x/x′)W₁(x′)] → Þ_Γ^{−1}B`; and `xJ(x) → c_J`
(5.4). The limit equation reads `ℛB = Þ_Γ^{−1}B + c_J`, which is (γ3.1) after dividing by ℛ,
and solves to `B = c_JÞ_Γ/(ℛÞ_Γ−1)`. Substituting `c_J = κ̲(ρ+1)σ²/(2Þ_Γ)` (5.4) gives the
closed form; the `Þ_Γ` cancels — *why the formula is clean:* the forcing constant carries a
`Þ_Γ^{−1}` from the rescale Jacobian and the resolvent carries a `Þ_Γ` from the one-shell
delay, and they are inverse to each other. ∎

*Remark 3.2 (the geometric resolvent).* Unrolling (γ3.1): `B = Σ_{k≥0} λ^k F(0)` — the
boundary value is the geometric sum of the forcing received one shell at a time, discounted
by the boundary multiplier. This sum is the shared skeleton of all four proof routes (§9).

*Remark 3.3 (approach rate — observed, not proven here).* The recursion heuristic
`e_{n+1} ≈ λ·e_n + (F_n − F_∞)` predicts `|W − B| ≍ x^{−min(1, q↑−1)}` provided
`F_n − F_∞ = O(Þ_Γ^n)`; since (5.4) is imported rate-free, this document does not prove a
rate, and none of §§2–7 needs one. The prediction matches the falsifier F1a (fitted x-power
0.597 vs q↑−1 = 0.6 at q↑ = 1.6, §10) and statement.md Remark 8.3 / review R4. Curiosity: at
`q↑ = 2` the two rates collide (`λ = Þ_Γ`) — a *second-order* resonance in the error term,
invisible in the value.

*Remark 3.4 (honesty: uniformity near the resonance).* `B ∝ 1/(ℛÞ_Γ−1) → ∞` as `q↑ ↓ 1`, and
the shell contraction `λ = e^{−(q↑−1)Λ} ↑ 1`: the number of shells to enter the plateau
scales like `((q↑−1)Λ)^{−1}`, i.e. the theorem's content becomes visible only for
`ln x ≫ 1/(q↑−1)`. (Quantitatively — added per review RF2-N3 — the onset is
`ln x ≳ ln x_c + O(1)/(q↑−1)` with the crossover scale `x_c = |b₁/B|^{1/(q↑−1)}`
calibration-dependent and GROWING as Þ_Γ ↑ 1: RF2 measured x_c ≈ 30 at Þ_Γ = 0.95
vs ≈ 730 at Þ_Γ = 0.96 at fixed q↑ = 1.6, leaving 3.5% raw residuals at x ≈ 2e5 that
the crossover-corrected intercept resolves to 0.05%; cf. Cor. A4.2's additive window.)
γ-A is a fixed-q↑ statement, NOT uniform in q↑ near 1. The registered
near-resonance falsifier RT1 FAILED as registered precisely because of this (the author's
own pre-registered window criterion mis-modeled the crossover; §10, kept as a FAIL): at
`q↑ = 1 ± 0.05` and `ln x ≤ 12` the quantity `(q↑−1)·ln x` is order one, and the measured
behavior interpolates between §4's line and §3's plateau. The correct uniform-in-q↑ objects
near the resonance are the crossover statements of Cor. A4.2 and Theorem B3's divergence law
`B·(q↑−1) → κ̲(ρ+1)σ²/(2Λ·E[ψ²])|_{ψ≡1}` (statement.md §3), consistent with §4 below.

---

## §4. Theorem γ-R: the resonance q↑ = 1 — a slope, not a value

At `q↑ = 1` (⟺ `ℛÞ_Γ = 1`), `λ(1) = 1`: the boundary multiplier is **neutral** — equal to
one, so the recursion neither contracts nor expands — and the forcing does not fade
(`F_n^± → c_J/ℛ > 0`). A neutral recursion with persistent forcing grows linearly in the
shell index — the boundary value is `+∞`, and the finite invariant is the **slope per
shell**. The Cesàro lemma:

:::{prf:lemma} γ-R1 (perturbed-additive Cesàro). PROVEN-HERE.
:label: cpt-lem-gR1

Let `a_n ≥ 0`, `Σδ_n < ∞`, `F_n → F_∞ ∈ [0,∞)`, `F_n ≥ 0`.

  (i) If `a_{n+1} ≤ (1+δ_n)(a_n + F_n)` for all large n, then `limsup a_n/n ≤ F_∞`.
  (ii) If `a_{n+1} ≥ (1−δ_n)(a_n + F_n)` for all large n, then `liminf a_n/n ≥ F_∞`.

:::

*Proof.* (i) For `K` large and `n > K`, unroll:
`a_n ≤ Π_{j=K}^{n−1}(1+δ_j)·a_K + Σ_{j=K}^{n−1} Π_{i=j}^{n−1}(1+δ_i)·F_j
≤ P_K·[a_K + Σ_{j=K}^{n−1}F_j]`, with `P_K := Π_{j≥K}(1+δ_j)`. Divide by n; the Cesàro mean
of a convergent sequence converges: `limsup a_n/n ≤ P_K·F_∞`. Let `K → ∞`: `P_K ↓ 1`
(summability), giving (i). (ii) Same unroll downward:
`a_n ≥ Π(1−δ_j)a_K + Σ_j Π_{i≥j}(1−δ_i)F_j ≥ Q_K·Σ_{j=K}^{n−1}F_j` with
`Q_K := Π_{j≥K}(1−δ_j) ↑ 1`; divide by n, let `K → ∞`. ∎

This is the Stolz–Cesàro mechanism (classical; e.g. Muresan 2009) run through a summable
multiplicative perturbation — the perturbation products `P_K, Q_K → 1` are exactly the
summable perturbation budget `Σδ_n < ∞` of §1.5.

:::{prf:theorem} γ-R (the resonance constant). PROVEN-HERE.
:label: cpt-thm-gR

Assume A0–A6, σ² > 0 and `q↑ = 1`. Then with `W = W₁ = x·g(x)`:

    M_n/n → c_J/ℛ   and   m_n/n → c_J/ℛ,

and consequently, converting shells to logs (`n(x) = ln(x/x_a)/Λ + O(1)` on `X_n^ζ`),

    (x/ln x)·g(x) → c_J/(ℛΛ) = κ̲(ρ+1)σ²/(2Λ)        (using ℛ = Þ_Γ^{−1} at q↑ = 1).

:::

*Proof.* At `s = 1`, `λ(1) = 1` and (γS-up)/(γS-dn) are exactly the hypotheses of Lemma γ-R1
for `a_n = M_n` (upper) and `a_n = m_n` (lower; note (γS-dn) has the referred point in
`X_n^ζ` by Lemma γ0 — band width zero, so no window enters and the constant is sharp), with
`F_n^± → c_J/ℛ` (Lemma γ1(ii)). Hence `M_n/n, m_n/n → c_J/ℛ`. For `x ∈ X_n`,
`m_n ≤ W(x) ≤ M_n` and `|n − ln(x/x_a)/Λ| ≤ 1`, so `W(x)/ln x → c_J/(ℛΛ)`. Finally
`c_J/(ℛΛ) = c_JÞ_Γ/Λ = κ̲(ρ+1)σ²/(2Λ)` by (5.4)'s constant and `ℛÞ_Γ = 1`. ∎

**Benchmark.** The constant equals the ψ≡1 corollary of Stage-B Theorem B-res
(`statement.md` §3), proven there by the tilted-walk engine; γ-R is an independent,
elementary proof of that corollary at ψ ≡ 1. Falsifier F1b/F3 (§10): per-shell increment
measured 0.036476 vs `c_J/ℛ = 0.036449` (0.07%); log-slope 0.224075 vs 0.224276 (0.09%).

*Remark 4.1 (reconciliation with γ-A).* As `q↑ ↓ 1`, γ-A's boundary value blows up at the
law `B·(ℛÞ_Γ−1) = c_JÞ_Γ`, while its plateau recedes (`Remark 3.4`); expanding
`x^{−(q↑−1)} = e^{−(q↑−1)ln x}` in the crossover window `(q↑−1)ln x = O(1)` gives
`W ≈ B(1 − x^{−(q↑−1)}) ≈ ln x · c_JÞ_Γ/Λ` — the resonance slope is the `q↑ → 1` limit of
"boundary value × approach rate". The failed RT1 registration and its post-hoc diagnostics
(§10) measure exactly this interpolation.

*Remark 4.2 (why the resonance is where the one-number picture first degenerates).* The
scalar boundary equation (γ3.1) at `λ = 1` reads `W(0) = W(0) + F(0)` with `F(0) > 0` — no
finite solution. The compactified picture survives, but the continuous extension is to
`W/ln(1/z)` rather than `W`; the finite number the owner asked for is the coefficient of the
divergence.

---

## §5. Theorem γ-T: the trichotomy — the compactified problem detects the exponent

Compensation is a dial, not a hypothesis. Turning `s` away from `q = min(1, q↑)` makes the
boundary behavior degenerate in a *diagnostic* direction:

:::{prf:theorem} γ-T (wrong-exponent detection). PROVEN-HERE (as a corollary of §§2–4, 6).
:label: cpt-thm-gT

Assume A0–A6, σ² > 0. For `s > 0`, as `z → 0`:

  (i)  `s < q`:  `W_s(z) → 0`;  exactly:  `W_s ≍ x^{−(q−s)}` (times `ln x` at q↑ = 1),
       per-shell decay factor `e^{−(q−s)Λ}`;
  (ii) `s > q`:  `W_s(z) → ∞`;  exactly:  `W_s ≍ x^{s−q}` (times `ln x` at q↑ = 1),
       per-shell growth factor `e^{(s−q)Λ}`;
  (iii) `s = q`: the boundary behavior is finite and nonzero in the regime-appropriate
       sense: `q↑ > 1`: `W_q → B ∈ (0,∞)` (γ-A); `q↑ = 1`: `W_q/ln x →` the resonance
       constant `∈ (0,∞)` (γ-R); `q↑ < 1`: `0 < m_∞ ≤ liminf W_q ≤ limsup W_q ≤ M_∞ < ∞`
       (γ-C, §6).

Hence `q = min(1, q↑)` is the **unique** compensation exponent with nondegenerate boundary
behavior: the compactified problem *detects* the exponent.

:::

*Proof.* Everything follows from `W_s = x^{s−q}·W_q` and the two-sided control of `W_q`:
`W_q` is bounded above (γ2) and eventually bounded below by a positive constant — at
`q↑ > 1` by `W₁ → B > 0` (γ-A), at `q↑ = 1` by `m_n ≥ (c_J/ℛ − ε)n → ∞` (γ-R), at `q↑ < 1`
by `m_n → m_∞ > 0` (Lemma γ-C1 below). The per-shell factors are `Þ_Γ^{−(s−q)} = e^{(s−q)Λ}`
by construction of the shells. ∎

*Remark 5.1 (the dynamical reading, and the two dials).* Intrinsically, the recursion
(γS-up/dn) at compensation s has boundary multiplier `λ(s) = e^{−(q↑−s)Λ}` and forcing scale
`F_s ≍ x^{s−1}`:

  - the **homogeneous dial**: `λ(s)` crosses 1 exactly at `s = q↑` — below it the recursion
    contracts, above it expands;
  - the **forcing dial**: `F_s` stays bounded exactly for `s ≤ 1` — for `s > 1` the forcing
    itself diverges like `x^{s−1}` and no contraction can absorb it (at `q↑ > 1`, for
    `s ∈ (1, q↑]`, `λ(s) ≤ 1` yet `W_s → ∞`: **the income/prudence channel caps the usable
    compensation at 1** — this is the `q↑ > 1` subtlety the min(1, q↑) formula encodes).

  Whichever dial binds first sets `q = min(1, q↑)`. (Bookkeeping note: Lemma γ1 derives
  (γ-up)/(γ-dn) only for `s ≤ 1` — its `D̂` would become `D̂(s) = 2(K̂ + 2sC₀/Þ_Γ)` for
  `s > 1` — but no `s > 1` recursion is ever used: every `s > 1` claim in γ-T is read off
  the `s ≤ 1` results through the identity `W_s = x^{s−q}·W_q`.)

*Remark 5.2 (relation to Lemma A5 / branch selection).* For general ψ (Stage B) the boundary
multiplier at compensation s is `λ_B(s) = E[ψ^{1+s}]/(ℛÞ_Γ^s) = e^{𝔏(s)}` (§7), so
"`λ_B(s) = 1`" IS the eigenvalue equation (E), and A5's convex geometry (`𝔏` convex,
`𝔏(0) < 0`, unique positive root) is the statement that the boundary map has exactly one
neutral compensation. γ-T is the dynamical restatement of A5's root-selection: the growing
branch `x^{+|q|}` excluded there by `g ≤ ḡ` is here excluded by γ2's boundedness — the same
a-priori sandwich, used once. (Kesten-theory kinship, one line: `q↑` is the Kesten exponent
of the rescale `x′ ≈ (Þ_Γ/ψ)x` weighted by the Euler ψ-factor; the detection statement is
the primal, compactified face of that root.)

Falsifier F4 (§10): all four wrong-compensation per-shell log-rates, in units of Λ, measured
within ±0.012 of `(s−q)`, correct signs (the q↑ = 1.6 cases carry the predicted small deficit
from the still-decaying `W₁ − B` factor).

---

## §6. γ-C: q↑ < 1 — the honest geometry: a boundary circle, not a boundary point

At `q = q↑ < 1`: `λ(q↑) = 1` exactly (definition of q↑), and the forcing **fades
geometrically** (`F_n^± ≤ CÞ_Γ^{(1−q↑)n}`, Lemma γ1(ii)). A neutral recursion with summable
forcing converges — but *to what* depends on where you stand within the shell: the map
`z ↦ z/Þ_Γ` (one shell inward) preserves the **log-phase**

    φ(x) := (ln x mod Λ) ∈ ℝ/Λℤ,

the position of `ln x` modulo the period `Λ` (the quotient `ℝ/Λℤ` is a circle of
circumference `Λ`). In log wealth the dynamics repeat with period `Λ`, so what matters
asymptotically is this position alone: the compactification's natural boundary here is not
the point `z = 0` but the **circle of phases** `ℝ/Λℤ`. Call the set of wealth levels
sharing one phase — the geometric sequence `{x = x̄·Þ_Γ^{−j}, j ∈ ℕ}`, equal `ln x` modulo
`Λ` — a **fiber**: distinct fibers march to the boundary without ever mixing (up to the
small per-step displacement of phase, the "phase blur", bounded next). What is proven here,
and what is imported:

:::{prf:lemma} γ-C1 (envelope convergence and the positive floor). PROVEN-HERE.
:label: cpt-lem-gC1

Assume A0–A6, σ² > 0, `q↑ < 1`, `s = q↑`. Then `M_n → M_∞` and `m_n → m_∞` exist with

    0 < m_∞ ≤ M_∞ < ∞,

and: `limsup_{z→0} W = M_∞`, `liminf_{z→0} W = m_∞`, and the set of accumulation points of
`W(z)` as `z → 0` is exactly the interval `[m_∞, M_∞]`.

:::

*Proof.* Boundedness: γ2(ii). Upper convergence: by (γS-up) with `λ = 1`,
`M_{n+1} − M_n ≤ δ_n·M̄ + (1+δ₀)F_n⁺ =: s_n` with `Σ s_n < ∞` (`M̄ := sup M_n`). The sequence
`a_n := M_n − Σ_{k<n}s_k` is non-increasing and bounded below, hence convergent; therefore
`M_n` converges. Lower convergence: by (γS-dn), `m_{n+1} ≥ (1−δ_n)m_n`, so
`m_{n+1} − m_n ≥ −δ_n·M̄`, and `b_n := m_n + Σ_{k<n}δ_kM̄` is non-decreasing and bounded,
hence `m_n` converges. Positive floor: `m_{n+1} ≥ (1−δ_n)·m_n` iterates to
`m_n ≥ m_{n₃}·Π_{k≥n₃}(1−δ_k) > 0`, provided `m_{n₃} > 0` for some `n₃` with `δ_k < 1`
beyond it — and `m_{n₃} = inf_{X_{n₃}^ζ} W_{q↑} > 0` because g is continuous and strictly
positive on the compact shell (Lemma 2 strict; take `n₃ ≥ 1` so the shell's bottom
`x_aÞ_Γ^{−n₃} − ζ > x_a − ζ ≥ x₀ ≥ (h−1) + m̄` sits strictly above the strictness threshold,
i.e. `m > m̄` everywhere on the shell). Identification of
limsup/liminf: every `x` lies in `X_{n(x)}`, so all accumulation points lie in
`[m_∞, M_∞]`; both endpoints are attained along maximizing/minimizing sequences; and since
`W` is continuous on `(0, z_a]`, the intermediate value theorem fills the interval. ∎

(cpt-lem-gC2)=
### Lemma γ-C2 (summable phase blur). PROVEN-HERE.

Along a fiber `x_j := x̄·Þ_Γ^{−j}` (x̄ ∈ X₀^ζ), the one-step comparison at `x_{j+1}` refers
to the points `Þ_Γx_{j+1} ∓ C₀ = x_j ∓ C₀`, whose log-phase differs from `φ(x_j)` by

    |Δφ_j| ≤ 2C₀/(Þ_Γ·x_j)      (for x_j ≥ 2C₀/Þ_Γ);

this per-step displacement `Δφ_j` of the consulted phase is the **phase blur**, and the
total blur accumulated from shell N inward is geometrically small:
`Σ_{j≥N}|Δφ_j| ≤ (2C₀/(Þ_Γx̄))·Þ_Γ^N/(1−Þ_Γ) → 0`. Likewise the coefficient perturbations
sum to `Σ_{j≥N}δ_j → 0` and the forcing to `Σ_{j≥N}F_j → 0`. *Proof:* `|ln(1∓u)| ≤ 2u` for
`u ≤ ½` applied to `u = C₀/(Þ_Γx_j)`; geometric sums. ∎

So the recursion **asymptotically decouples across phases**: each fiber talks only to
`o(1)`-neighborhoods of itself. What follows from γ-C1/γ-C2 by elementary means: every fiber
sequence `W(x_j)` has convergent subsequences, all with limits in `[m_∞, M_∞]`; and, writing
`osc(f; A) := sup_A f − inf_A f` for the oscillation of a function over a set, the per-step
fiber increment obeys

(cpt-eq-g6-1)=

    |W(x_{j+1}) − W(x_j)| ≤ δ_j·M̄ + (1+δ_j)·[ F_j + osc( W ; x_j·e^{[−u_j, u_j]} ) ],   (γ6.1)

with everything except the last term summable. The last term is the local oscillation of `W`
over the multiplicative window `x_j·e^{[−u_j, u_j]}` — an interval of phases of width `2u_j`,
`u_j = 2C₀/(Þ_Γx_j)`.

(cpt-sec-gap-equicont)=
### GAP-γ-equicont (the honest missing step). GAP.

To convert (γ6.1) into *convergence along each fiber* one needs an asymptotic modulus of
continuity in the phase direction — a uniform bound on how much `W` can move under a small
multiplicative shift of wealth: some `ω` with `ω(0+) = 0`,

    |W(x·e^u) − W(x)| ≤ ω(|u|)   for all large x, |u| ≤ Λ,

and summability of `Σ_j ω(u_j)` along the geometric sequence `u_j ≍ Þ_Γ^j` (a Dini-type
condition `∫₀ ω(t)/t·dt < ∞`; any Hölder modulus qualifies). Given such an ω, (γ6.1) is
summable, each fiber sequence is Cauchy, and the fiber limits assemble into a function
`P_γ: ℝ/Λℤ → [m_∞, M_∞]` with `W(x) − P_γ(φ(x)) → 0`; the compensated gap then extends
continuously to the compactified space whose boundary is the **circle**, with
`W|_{boundary} = P_γ`, `max P_γ = M_∞`, `min P_γ = m_∞`. **This equicontinuity control is
exactly the L8/L9 (doubling / log-Lipschitz) territory of the Stage-A engine, which is
off-limits for this self-contained route** — so it is tagged here as a GAP and NOT claimed.
The sharp form is **imported as Theorem A2** (`g = x^{−q↑}(P(ln x) + O(x^{−(1−q↑)}))`, P
positive, Lipschitz, Λ-periodic): under that import, `P_γ = P` and the circle picture above
is a theorem. Without the import, this document proves the envelope (γ-C1), the blur budget
(γ-C2), and subsequential fiber limits — no more.

*Remark 6.1 (how the owner's one number degenerates, exactly).* At `q↑ > 1` the boundary
circle is still there, but γ-A forces the boundary function to be the constant B — the
circle collapses to a point and "one number" is exact. At `q↑ < 1` the boundary object is a
function on a circle; the honest scalar summaries are the pair `(m_∞, M_∞)` (proven here)
or the mean of P (owned by the B2-arith Fourier representation, off-limits here). Whether
`M_∞ > m_∞` — i.e. whether the circle is *visible* — is the fine structure of P: measured
non-constant with relative amplitude `osc(P)/P̄ ≈ e^{−α/Λ}` (`osc(P) := sup P − inf P`, the
total amplitude of the periodic factor; `P̄` its mean) where **α is calibration-dependent**
(softened per review RF2-N2: R3 measured α ≈ 0.8–1.2 on its lognormal designs, but RF2
resolved a grid-independent oscillation, locked to the phase φ, of amplitude 7.8e-4 at
Λ = 0.693 on an atomic-θ design — implying α ≈ 4.9, so the prefactor-1 α≈1 extrapolation
over-predicts ~250–400× there; positive side: that oscillation is the first direct
resolution of a non-constant P in this route's numerics, confirming the imported A2 circle
picture); analyzed in
`periodic_factor_fine_structure.md` (owner document; not needed by anything here — the
RF2 data point is recorded there). At the Λ of the estimated calibrations the oscillation
is far below numerical visibility — falsifier F1c′ measured a phase profile flat to 3.4e-5 at
Λ = 0.288, an *upper bound* contaminated by residual envelope drift, consistent with both
"effectively constant" and the (calibration-dependent) R3 law (§10).

*Remark 6.2 (Stage-A resonance q↑ = 1 sits between).* There the circle also exists but the
divergence is common to all fibers (γ-R's slope is phase-free); the phase question only
affects the O(1) intercept — visible in F3's fitted intercept, not pursued.

---

## §7. γ-B: Stage B (permanent shocks), q↑ > 1 — the boundary value B_ψ

Setting: `stage_B_proof.md` §§B0–B3. The recursion is now a random rescale
(B3.1): `ψ′x′ = Þ_Γx + W′ + ℛg(x)`, `|W′| ≤ C_W`, and the one-step identity carries the
Euler weight ψ inside the expectation ((B5.2), Cor B-5.2). Two structural changes against
Stage A, both honest:

  1. the referred point `y_ψ := (Þ_Γx − C₀^B)/ψ` is **random**: in logs it lands in a
     bounded *window* `ln x − Λ + [−ln ψ_max, −ln ψ_min] + O(1/x)` — the band is back
     (its correct shell-binning is by the guaranteed step `μ = ln(ψ_min/Þ_Γ)`, NOT by Λ —
     see γ-B1);
  2. if `ψ_min < Þ_Γ` — **the generic case** at real calibrations (stage_B (B5.0a) note) —
     the window reaches *forward* (`y_ψ > x` with positive probability): the shell-indexed
     sup-induction has **no well-founded order to induct on**, and the band-sup route of §2
     does NOT close verbatim. This corrects the design brief's expectation ("γ2/γ3 close
     verbatim in band-sup form"): they do only when `ψ_min > Þ_Γ` (γ-B1); the generic case
     needs one genuinely new (still elementary) argument (γ-B2).

### 7.1 The compensated Stage-B one-step

Multiply Corollary B-5.2's upper and lower one-step bounds by x and compensate at `s = 1`.
Using
`ψ·x/y_ψ = ψ²·(1 − u_B)^{−1}/Þ_Γ`, `u_B := C₀^B/(Þ_Γx)`, and folding `(1 ± K̂_B/x)` and
`(1 ∓ u_B)^{−1}` into one factor exactly as in Lemma γ1 (constant
`D̂_B := 2(K̂_B + 2C₀^B/Þ_Γ)`):

(cpt-eq-g7-1)=

    (γB-up)  W₁(x) ≤ (1 + D̂_B/x)·[ (ℛÞ_Γ)^{−1}·E[ψ²·W₁(y_ψ)] + F_B(x) ],
    (γB-dn)  W₁(x) ≥ (1 − D̂_B/x)·[ (ℛÞ_Γ)^{−1}·E[ψ²·W₁(y′_ψ)] + F_B(x) ],       (γ7.1)

with `y′_ψ := (Þ_Γx + C₀^B)/ψ`, `F_B(x) := ℛ^{−1}xJ(x) → c_J^B/ℛ` ((B5.4); bounded by
(B5.3)). *Validity threshold (stated per review RF1-F1):* (γ7.1) holds for `x ≥ x₀^B` —
its folding needs `u_B ≤ ½` (i.e. `x ≥ 2C₀^B/Þ_Γ`) and `x ≥ K̂_B` for the D̂_B-collapse,
and both are dominated by `x₀^B` because stage_B's (B5.0a)/(B5.0) contain the entries
`8(ρ+1)C₀^B/Þ_Γ ≥ 2C₀^B/Þ_Γ` and `2K̂_B` (domination re-verified by RF1 against
`stage_B_proof.md`); Lemma γ-B2's X₁ secures this through its entry (a) `x₀^B` — the
dependence was previously silent, and a future edit of stage_B's threshold display
should re-check it here. The **boundary multiplier**

    λ_B := E[ψ²]/(ℛÞ_Γ) = e^{𝔏(1)} < 1  ⟺  q↑ > 1

(A5's convex geometry: 𝔏 convex, 𝔏(0) = −ln ℛ < 0, unique root q↑, so 𝔏(1) < 0 iff
1 < q↑). *Why ψ² and not ψ:* one ψ is the Euler marginal-utility weight of (B5.2), the
second arises because the compensation `x/y_ψ` reintroduces the rescale — the same reason
Theorem B3's denominator carries `E[ψ²]`. The review harness's `delta_B81` diagnostic (wrong
-weight controls) certifies on solved models that the ψ²-weight is the one carrying signal
(F5, §10: main residual 3.5–4 orders below the ψ¹ control and a factor ≈8/≈47 below the
Stage-A-shaped control; the registered margin `|main| ≤ 0.2·min(controls)` holds in both
designs). *Evidence-route caveat and robust replacement (per review RF2-N1):* the
Stage-A-shaped control ctrlB is NOT an O(1)-plateau control — it decays like
`x^{−min(1,q↑−1)}` and vanishes with the ψ-spread (law RF2-D: ctrlB − main =
`−C(Þ_Γx)^{−p}(E[ψ^{2+p}]−E[ψ²])/(ℛÞ_Γ)`, verified power 0.594 vs 0.6, amplitude ratio
1.03), so the `0.2·min(controls)` margin is probe-depth- and grid-fragile in mild
ψ-designs (the author's 1.66× headroom at Na = 5000 inverts to 0.46× at Na = 3000 at the
aMax/50 probe). The ROBUST certification of the ψ²-weight is RF2's wrong-weight plateau
sweep: ctrl_w plateaus at `B_ψ(E[ψ²]−E[ψ^w])/(ℛÞ_Γ)` (law RF2-P, measured to 0.5–0.9%
across w ∈ {0, 1, 1.5, 2.5, 3}), the root of w ↦ ctrl_w is ŵ = 1.9999, margin 6647×
(`review/RF2_check_5_bpsi_discrimination.py`). The identification itself is robust;
this caveat is about the evidence route only.

(cpt-lem-gB1)=
### Lemma γ-B1 (boundedness, backward-band case `ψ_min > Þ_Γ`). PROVEN-HERE (shell width corrected by the internal red-team pass).

Let `μ := ln(ψ_min/Þ_Γ) > 0`, the **guaranteed backward log-step**: pathwise
`ln y_ψ = ln x − ln(ψ/Þ_Γ) + ln(1 − u_B) ≤ ln x − μ` (the jitter term is ≤ 0 on this
side). *Red-team catch, recorded:* the first draft binned by the Λ-shells of §1 and claimed
a backward window `[n − b_ψ, n]`; that is FALSE whenever `ψ_min < 1` (the generic sub-case),
because then `μ < Λ` and the referred point can land in shell `n+1` itself — the guaranteed
step is `μ`, not `Λ`. The correct bins are **μ-shells**: `Y_k := [X₀e^{kμ}, X₀e^{(k+1)μ})`,
`X₀ := max(x₀^B, 4C₀^B/(Þ_Γμ))` (the second entry keeps the downward log-jitter `2u_B ≤ μ/2`
for the window's bottom edge). For `x ∈ Y_{k+1}`: `ln y_ψ ≤ ln x − μ < top(Y_k)`, so the
referred point lies in `Y_j` with `j ≤ k` (no self-reference), and
`ln y_ψ ≥ ln x − ln(ψ_max/Þ_Γ) − μ/2` bounds the window depth by
`b_w := ⌈ln(ψ_max/Þ_Γ)/μ⌉ + 1`. With `M_k^Y := sup_{Y_k} W₁` and
`P_k := max_{j∈[k−b_w, k]} M_j^Y`, (γB-up) gives `M_{k+1}^Y ≤ (1+δ_k)[λ_B·P_k + F̄_B]`
(`δ_k := D̂_B e^{−kμ}/X₀`, geometric), and the window-max induction of Lemma γ2(i) closes:
`P_{k+1} ≤ max(P_k, λ′P_k + F̄′) ≤ max(P_{k₂}, F̄′/(1−λ′))` for `k ≥ k₂`, where
**`k₂ := max(⌈the γ2(i)-type shell index⌉, b_w)`** — base and sub-X₀ bookkeeping made
explicit per review RF1-F2: (i) the displayed recursion needs the whole window
`[k−b_w, k]` to consist of defined bins, so the induction starts no earlier than
`k = b_w` (the finitely many bins below `k₂` are individually finite, `W₁ ≤ ḡ·x` on
each compact `Y_j`, so `P_{k₂} < ∞`); (ii) for the few early steps whose referred
points fall below `X₀`, the crude bound `W₁(y) ≤ ḡ·y ≤ ḡ·X₀` (from L2^B) covers them.
Hence `sup W₁ < ∞` on `[X₀, ∞)`. As `ψ_min ↓ Þ_Γ`, `μ ↓ 0` and the shells degenerate —
the quantitative signal that the forward case is a genuine phase change, not a
bookkeeping inconvenience. (γ-B1 is in any case redundant for Theorem γ-B: γ-B2 covers
all bounded ψ including this one.) ∎

:::{prf:lemma} γ-B2 (boundedness, general `ψ ∈ [ψ_min, ψ_max] ⊂ (0,∞)`). PROVEN-HERE.
:label: cpt-lem-gB2

Assume q↑ > 1 (so `λ_B < 1`). There are explicit `X₁ < ∞` and `K_B < ∞` such that
`W₁(x) ≤ K_B` for all `x ≥ X₁`.

:::

*Proof (stopped expectation-unroll; the one path-sum-flavored argument in this document —
no tilt, no renewal, no change of measure: only (γB-up) iterated plus i.i.d. factorization
and one stopping time).*

Let `(ψ_j)_{j≥1}` be i.i.d. copies of ψ and define the **comparison chain**

    y₀ := x,     y_{j+1} := (Þ_Γ·y_j − C₀^B)/ψ_{j+1},

(the bracket points of (γB-up) composed), and the stopping index
`τ := inf{ j : y_j < X₁ }`. Choose

    X₁ := max{ x₀^B,  (C₀^B + hψ_max)/Þ_Γ,  D̂_B·2λ_B/(1−λ_B),  D̂_B·2/(ℛ−1) },

whose entries buy, in order: (a) admissibility of (γB-up) at every alive point; (b) domain
safety one overshoot step below `X₁` (if `y_{τ−1} ≥ X₁` then
`y_τ ≥ (Þ_ΓX₁ − C₀^B)/ψ_max > h > 0`, so `g(y_τ)` is defined and `W₁(y_τ) ≤ ḡ·X₁` since
`y_τ < X₁`); (c) `(1 + D̂_B/X₁)·λ_B ≤ λ̄ := (1+λ_B)/2 < 1`; (d) `(1 + D̂_B/X₁)/ℛ ≤ r̄ :=
(1 + ℛ^{−1})/2 < 1`.

Iterate (γB-up) k times along the chain, applying it only at alive indices `j < τ∧k` (where
`y_j ≥ X₁`, hence `(1 + D̂_B/y_j) ≤ 1 + D̂_B/X₁`); at the stopped index bound
`W₁(y_τ) ≤ ḡX₁`; at the un-stopped horizon bound `W₁(y_k) ≤ ḡ·y_k`. Writing
`w_j := (1 + D̂_B/X₁)·ψ_{j+1}²/(ℛÞ_Γ)` for the alive weight factors:

    W₁(x) ≤ E[ Π_{j<τ∧k} w_j · W₁(y_{τ∧k}) ] + Σ_{i<k} E[ 1{i<τ}·Π_{j<i} w_j ]·(1+D̂_B/X₁)·F̄_B,

with `F̄_B := ℛ^{−1}·sup_x xJ(x) < ∞` (B5.3). Three estimates:

  1. **Forcing.** `E[1{i<τ}Π_{j<i}w_j] ≤ E[Π_{j<i}w_j] = ((1+D̂_B/X₁)λ_B)^i ≤ λ̄^i`
     (drop the indicator — all factors positive; i.i.d. factorization
     `E[Πψ_j²] = E[ψ²]^i`; entry (c)). Sum: `≤ F̄_B(1+D̂_B/X₁)/(1−λ̄)`.
  2. **Stopped mass.** `E[Π_{j<τ∧k}w_j·1{τ ≤ k}]·ḡX₁ ≤ ḡX₁·Σ_{i≤k} λ̄^i ≤ ḡX₁/(1−λ̄)`
     (decompose over `{τ = i}`, bound each layer as in 1).
  3. **Alive linear term.** On `{τ > k}` every `y_j ≥ X₁`, so the (1+·) factors are
     controlled, and pathwise `y_k ≤ x·Π_{j≤k}(Þ_Γ/ψ_j)` (the `−C₀^B` only helps). Hence

         E[Π_{j<k}w_j·ḡy_k·1{τ>k}] ≤ ḡx·(1+D̂_B/X₁)^k·E[ψ²·(Þ_Γ/ψ)]^k/(ℛÞ_Γ)^k
                                    = ḡx·((1+D̂_B/X₁)/ℛ)^k ≤ ḡx·r̄^k → 0   (k → ∞),

     using `E[ψ²·(Þ_Γ/ψ)] = Þ_Γ·E[ψ] = Þ_Γ` and entry (d). *This is the step the band-sup
     route cannot reproduce: the weight ψ² and the position (Þ_Γ/ψ)x are correlated, and
     any sup-over-window bound throws the correlation away exactly when ψ_min < Þ_Γ.*

Let `k → ∞`:  `W₁(x) ≤ [ḡX₁ + (1+D̂_B/X₁)F̄_B]/(1−λ̄) =: K_B` for every `x ≥ X₁`. ∎

:::{prf:lemma} γ-B3 (boundary stability, Stage B). PROVEN-HERE.
:label: cpt-lem-gB3

Assume q↑ > 1. Then `lim_{x→∞} W₁(x) = F_B(0)/(1−λ_B)` with `F_B(0) = c_J^B/ℛ`.

:::

*Proof (function-level γ3 — direction-agnostic, so the forward window is harmless).*
`S̄ := limsup_{x→∞}W₁ < ∞` (γ-B2; γ-B1 in the backward case). Fix ε > 0 and X with
`W₁(y) ≤ S̄ + ε` for `y ≥ X`. For `x ≥ (X·ψ_max + C₀^B)/Þ_Γ`, every window point satisfies
`y_ψ ≥ (Þ_Γx − C₀^B)/ψ_max ≥ X` a.s., so `E[ψ²W₁(y_ψ)] ≤ E[ψ²](S̄+ε)`; with (γB-up) and
`x → ∞` then `ε ↓ 0`: `S̄ ≤ λ_B·S̄ + F_B(0)` (also using `F_B(x) → F_B(0)`, (B5.4)).
Symmetrically `s̲ ≥ λ_B·s̲ + F_B(0)` via (γB-dn). Hence
`S̄ ≤ F_B(0)/(1−λ_B) ≤ s̲ ≤ S̄`. ∎

:::{prf:theorem} γ-B (Stage-B boundary value). PROVEN-HERE.
:label: cpt-thm-gB

Under B-A0/A3–A6, σ_B² > 0 and `q↑ > 1` (general bounded ψ):

    lim_{z→0} W₁ = (c_J^B/ℛ)/(1 − E[ψ²]/(ℛÞ_Γ)) = c_J^B·Þ_Γ/(ℛÞ_Γ − E[ψ²])
                 = κ̲(ρ+1)σ_B²/(2(ℛÞ_Γ − E[ψ²])) = B_ψ,

matching Theorem B3's closed form (benchmark; B3 not used). The scalar boundary equation is
`W(0) = λ_B·W(0) + F_B(0)` — same one-liner, with the multiplier now carrying `E[ψ²]`.

:::

*Proof.* γ-B2 (or γ-B1) + γ-B3 + `c_J^B = κ̲(ρ+1)σ_B²/(2Þ_Γ)` (B5.4). ∎

*Remark 7.1 (the compactification's gift).* The band-sup crudeness that costs sharpness at
finite depth **evaporates at the boundary**: as `x → ∞` every window position converges to
the same boundary point, so `E[ψ²W₁(y_ψ)] → E[ψ²]·W₁(0)` exactly — no correlation loss in
the limit. This is why γ-B3 is four lines while the finite-depth Stage-B machinery (off-
limits §B4–§B8) is heavy: the compactified route only ever asks questions AT the boundary.

*Falsifiers (§10):* F5a (backward design, `ψ_min = 0.94 > Þ_Γ = 0.85`): deepest
`W₁/B_ψ − 1 = +0.22%`, `M_n` decreasing; F5b (generic/forward design,
`ψ_min = 0.75 < Þ_Γ`): `+0.35%`, approach from **below** (`M_n` increasing to the plateau —
the registered "M_n non-increasing" wording anticipated only the from-above case and passed
via its ≤1e-3 wiggle clause; reported honestly, see §10); `delta_B81` weight-controls
discriminate in both designs (ψ¹ control 3.5–4 orders above the main residual; Stage-A-shaped
control ≈8×/≈47×).

(cpt-sec-stageB-open)=
### Stage-B resonance and q↑ < 1: OPEN-here (proven elsewhere).

At `q↑ = 1` (`E[ψ²] = ℛÞ_Γ`) the shell displacement `ln(ψ/Þ_Γ)` makes the shell index a
**random walk**, not a march: the per-fiber/per-shell bookkeeping above needs occupation and
drift control for the walk under the ψ²-weight — exactly the (T)-toolkit's business
(off-limits here), and Theorem B-res proves the sharp log-law with it. Likewise `q↑ < 1`
Stage B (Theorems B2/B2-arith: KRT/lattice-renewal engines). This document does not attempt
either; the γ-route's honest scope at Stage B is `q↑ > 1`. Status: OPEN-here, PROVEN in
`stage_B_proof.md` by the other engine.

---

## §8. Proposition A0 from the boundary picture — a remark, not a new claim

One application of (γ-dn) at `s = 1`, dropping the (nonnegative) W-term, gives for
`x ≥ x_a`:

    W₁(x) ≥ (1 − D̂/x)·F₁(x) ≥ (1 − D̂/x)·j₋σ²/ℛ,     i.e.   g(x) ≳ σ²/x,

the A0-shaped floor with a one-step constant `j₋σ²/ℛ`; iterating instead of dropping resums
the geometric series and recovers γ-A's `B` — **the floor is the first Neumann term of the
boundary fixed point**. The sharp, GIC-free version of the floor (weaker hypotheses, better
constant, the no-`o(1/x)` corollary, Stage-B form with σ_B²) is owned by
`exponential_impossibility.md` (Lemmas J-A/J-B ⟹ Props A0/B0); nothing new is claimed here.
PROVEN-CITED (the one-step display above is PROVEN-HERE but adds nothing to the owner doc).

---

## §9. Why this is the easy proof

*(Plain language; one page; the section the owner's request was really asking for.)*

**Compress.** Wealth runs over `[x_a, ∞)`. The change of variable `z = 1/x` squeezes this
ray into the bounded interval `(0, z_a]`, and infinite wealth becomes an ordinary boundary
point, `z = 0`, which we glue on. This move is a one-dimensional Poincaré compactification —
the standard trick from dynamical systems for studying behavior "at infinity" with finite
tools (the classical planar chart at infinity is literally `v = 1/x`).

**Choose units.** The gap `g` itself vanishes at the boundary — too little information. So
we measure it in units that are *expected to make the limit finite*: `W = x^q·g(x)` with
`q = min(1, q↑)`. That unit choice is the rigorous meaning of "assume the power law holds in
the limit": no assumption is made — if the units are right, the compensated gap has a finite
nonzero boundary behavior, and if they are wrong, the boundary behavior degenerates to 0 or
∞ *and tells you the true exponent by the rate at which it does so* (§5).

**One equation at the boundary.** The Euler equation, rewritten in these coordinates, links
each shell of the interval (a geometric band `z ≈ z₀Þ_Γ^n`) to the next-outer shell:

    W(shell n+1) ≈ λ·W(shell n) + F_n,       λ = 1/(ℛÞ_Γ),   F_n → F(0) = c_J/ℛ.

March inward (`n → ∞` = `z → 0`): the recursion forgets the anchor data and is trapped at
the fixed point of the limiting map. AT the boundary, the whole functional equation collapses
to one line of high-school algebra:

    W(0) = λ·W(0) + F(0)        ⟹        W(0) = F(0)/(1−λ) = B.

That is the owner's finite number: `B = κ̲(ρ+1)σ²/(2(ℛÞ_Γ−1))`. The proof has exactly three
moving parts, each elementary: coefficients converge at the boundary (§1, from the imported
one-step identity), the sequence is bounded (§2, a three-line induction), and bounded +
asymptotically-autonomous ⟹ trapped at the fixed point (§2, a four-line limsup argument).
The theorem *is* the continuity of one function on one compact interval at one point.

**The three regimes are the three things a linear recursion can do at a boundary.**

  - `λ < 1` (q↑ > 1): contract — the boundary value is `F(0)/(1−λ)`; one number (§3).
  - `λ = 1` with persistent forcing (q↑ = 1): drift — linear growth in the shell index,
    `≍ ln x`; the finite number is the slope, `κ̲(ρ+1)σ²/(2Λ)` (§4).
  - `λ = 1` with fading forcing (q↑ < 1): neutral — the recursion converges but no longer
    mixes phases, so the "number" is a function on the circle of phases; its envelope
    `[m_∞, M_∞]` is elementary, its pointwise form is the periodic factor P (§6).

**The exponent is detected, not guessed.** Compensating with the wrong `s` flips the
boundary multiplier `λ(s) = e^{−(q↑−s)Λ}` across 1, or blows up the forcing `x^{s−1}` (for
`s > 1`): `W_s → 0` below the true exponent, `→ ∞` above it, at predicted geometric rates —
verified to ±0.012 (in units of Λ) per shell (§10). `min(1, q↑)` is the unique dial setting with a finite
nonzero reading; and the equation "`λ(s) = 1`" is, at Stage B, literally the eigenvalue
equation (E) of Lemma A5 — with `λ_B(s) = e^{𝔏(s)}`, convexity of 𝔏 says the dial crosses 1
once.

**A master's-class one-liner.** "In units where the limit is finite, the Euler equation at
infinite wealth reads `W = W/(ℛÞ_Γ) + c_J/ℛ`; solve for W." Everything else in this
document is the bookkeeping certifying that the two words "at infinity" are legitimate.

**Kinship (why four proofs share one constant).** `B = Σ_k λ^k F(0)` is a geometric sum —
and it must be: the gap at huge wealth is the discounted pile-up of the small prudence
corrections (`J ≈ c_J/x`) collected once per period while wealth decays geometrically toward
its target. Every correct proof computes this same sum; the routes differ ONLY in the engine
that justifies the exchange of limits: renewal/ladder theorems (stage_A/B), a probabilistic
path-sum, a recursion-tree/Akra–Bazzi induction, or — here — continuity at the boundary of a
compactified domain, where the exchange of limits is a four-line limsup argument. The
compactified route is the shortest because it asks the weakest question: not "how fast?"
(rates), not "along which paths?" (fluctuations), only "what number at the boundary?".

---

## §10. Numerical verification (pre-registered falsifiers; author-pass)

Harness: `verify_altproof_compactified_checks.py` (bare python3 + numpy 1.26.4, longdouble
EGM solvers imported from `review/R4_egm_lib.py` and `review/RB4_egm_lib_B.py`; per-point
`g/c > 1e-10` cancellation guard AND per-point Euler-residual gap-certificate ≤ 1e-3 on
every shell sample; Þ_Γ ≤ 0.9 for all amplitude checks). Falsifiers F1–F6, CC, RT1 were
registered in the script docstring BEFORE any measurement; saved output:
`verify_altproof_compactified_checks_out.txt`. **13 PASS / 2 FAIL of 15 registered checks**
(+5 post-hoc INFO controls PH1–PH3, added after the first registered run and marked as such
in the script) — both FAILs are the author's own registered near-resonance window
predictions (RT1), reported as failures and diagnosed below (not tuned away).

Main calibrations: `Þ_Γ = 0.85` (Λ = 0.16252), ρ = 2, G = 1, θ = lognormal(0.2, N=7) + 5%
unemployment atom (σ²_disc = 0.087565, θ_min = 0), q↑ ∈ {1.6, 1.0, 0.6} via
`ℛ = e^{q↑Λ}`. Shell geometry as in §1 (ζ reported per run; measurement bins are the plain
geometric shells).

| falsifier | section | registered criterion | result |
|---|---|---|---|
| F1a | §3 | fitted x-power of abs(mean−B) = (q↑−1) ± 0.10 at q↑=1.6 | **PASS**: 0.597 vs 0.6 (42 shells) |
| F2 | §3 | deepest shell mean within 2% of B, with trend | **PASS**: 0.897% at x ≈ 1e5; 2.37% ten shells earlier |
| CC | §1 | one-step residual r(x) → 0 with depth, deep ≤ 2%·B | **PASS**: 3.3e-5 → 2.8e-6 (x = 1e3 → 1e5) |
| F1b | §4 | per-shell increment → c_J/ℛ (5%; last-10 raw within 25%) | **PASS**: 0.036476 vs 0.036449 (0.07%) |
| F3 | §4 | slope of x·g on ln x within 5% of κ̲(ρ+1)σ²/(2Λ) | **PASS**: 0.224075 vs 0.224276 (0.09%) |
| F1c | §6 | envelope Cauchy (≤2e-2), positive floor | **PASS**: increments ≤ 2.4e-5; envelope [4.28234, 4.28240] |
| F4 | §5 | four wrong-s rates within ±0.02 of (s−q)/shell | **PASS**: −0.1118/+0.0882 (q↑=1.6), −0.0999/+0.1001 (q↑=0.6) |
| F5a | §7 | Stage-B backward design: W₁ → B_ψ ≤3%; δ(B8.1) controls | **PASS**: +0.22%; main 4.5e-7 vs ctrls 1.6e-3/3.7e-6 |
| F5b | §7 | Stage-B forward/generic design: same | **PASS**: +0.35%; main 1.0e-5 vs ctrls 1.1e-1/4.8e-4 |
| F6 | §2 | fat-tail θ (Pareto α=3 tail), θ_max ∈ {10,40,160}: W₁ → B(σ²_disc) ≤5% each | **PASS**: 0.16% / 0.29% / 0.37% |
| F1c′ | §6 | fiber flattening at Λ = 0.288 (signature; profile reported) | **PASS**: drift 4.6e-4 → 2.6e-4; profile flat to 3.4e-5 |
| RT1 (q↑=0.95) | §4 | resonance slope law to 10% on the window | **FAIL**: slope 0.629 vs 0.220 (+186%) |
| RT1 (q↑=1.05) | §4 | resonance slope law to 10% on the window | **FAIL**: slope 0.028 vs 0.229 (−88%); deepest W₁ = 90.0% of B |

**Reading the passes.**

- *F1a/F2/CC (γ-A):* the shell means contract to `B` at the predicted per-shell rate
  `e^{−(q↑−1)Λ}` (x-power 0.597 ≈ 0.6), land within 0.9% at the guard ceiling, and the
  one-step residual `W₁(x) − λW₁(Þ_Γx) − c_J/ℛ` — the finite-z version of the scalar
  boundary equation (γ3.1), and the same object as the review libs' `delta81` diagnostics —
  vanishes with depth. The mechanism, the constant, and the coefficient-limit lemma are all
  exercised independently.
- *F1b/F3 (γ-R):* at exact resonance (`ℛÞ_Γ = 1` to 1e-12), the per-shell increment of the
  shell means matches `c_J/ℛ` to 0.07% and is *flat* across the last 40 shells — the
  cleanest possible signature of Lemma γ-R1's mechanism (neutral multiplier + convergent
  forcing); the log-slope matches the resonance constant `κ̲(ρ+1)σ²/(2Λ)` to 0.09%.
- *F1c/F1c′ (γ-C):* envelope converges (increments 2.4e-5 and shrinking), floor positive.
  The deepest-shell phase profile at Λ = 0.288 is flat to 3.4e-5 — far below the crude
  `e^{−α/Λ}` extrapolation of the R3 oscillation law (~2e-2..6e-2 at α ∈ [0.8, 1.2]): the
  measured number is an UPPER bound on osc(P)/P̄ contaminated by residual envelope drift
  (the profile is a monotone micro-ramp, not a resolved oscillation), so the run is
  consistent with "P effectively constant here" and does NOT resolve the circle-vs-point
  question — which belongs to `periodic_factor_fine_structure.md`, not to this route.
- *F4 (γ-T):* the wrong-exponent dial responds at the predicted geometric rates with the
  predicted signs in all four registered cases; the q↑ = 1.6 pair carries the expected small
  deficit/excess from the still-decaying `W₁ − B` factor (measured −0.1118/+0.0882 vs ±0.1;
  the q↑ = 0.6 pair is exact to ±0.0001 because there the envelope has already converged).
- *F5 (γ-B):* both ψ-designs land on `B_ψ` (+0.22% / +0.35%) — including the GENERIC
  forward-window design `ψ_min = 0.75 < Þ_Γ = 0.85` where the band-sup induction provably
  does not close and boundedness rests on Lemma γ-B2's stopped unroll. Honest note: design
  (b) approaches the boundary value from BELOW (M_n increasing), while the registered
  wording ("M_n eventually non-increasing") anticipated only the from-above case; the check
  passed through its ≤1e-3 late-wiggle clause, and the from-below approach is the correct
  reading (the subleading coefficient changes sign between the designs). The wrong-weight
  controls exceed the main residual by 3.5–4 orders (ψ¹-weight) and by factors ≈8 / ≈47
  (Stage-A-shaped argument, designs a/b) — the registered `|main| ≤ 0.2·min(controls)`
  margin holds in both designs: the `E[ψ²]` multiplier of (γ7.1) is what the data selects.
  *(Caveat per review RF2-N1: the Stage-A-shaped control decays like `x^{−min(1,q↑−1)}`
  rather than plateauing, so this margin is probe-depth- and grid-fragile in the mild
  design (a) — it inverts at Na = 3000; the robust ψ²-weight certification is RF2's
  wrong-weight plateau sweep, root ŵ = 1.9999 with 6647× margin — see §7.1.)*
- *F6 (γ2 robustness, refuter lesson honored):* a fat-tailed θ (discretized Pareto α = 3.0
  tail, L4′-admissible) with θ_max escalated 10 → 160 degrades the constants exactly as the
  proof says it must (C₀: 9 → 140; ζ: 60 → 934; usable shells: 40 → 23) while the
  CONCLUSION is untouched (W₁ → B(σ²_disc) to 0.16–0.37% at every escalation). Bounded-θ
  theorems applied to the discretization; the unbounded case is L4′'s import, not re-proven
  here.

**Reading the failures (RT1) — kept as failures.** The author's registered criterion said
the resonance slope law should govern the whole guard-clean window at `q↑ = 1 ± 0.05` to
10%. It does not: at `q↑ = 0.95` the measured ln-x slope is 2.9× the resonance constant
(the window is already feeling the growing `x^{1−q↑}` Kesten-channel amplitude); at
`q↑ = 1.05` it is 8× SMALLER (the window is already 90% of the way to the plateau at B —
mostly past crossover). Diagnosis: the registered criterion implicitly required
`|q↑−1|·ln x ≪ 1`, but on this window `|q↑−1|·ln x ≈ 0.2–0.7` — order one, mid-crossover.
The post-hoc diagnostics quantify it (PH2): the split-window local slope at `q↑ = 0.95`
GROWS with depth (0.519 shallow → 0.746 deep, against the resonance constant 0.220 — the
`x^{1−q↑}` amplitude regime), while at `q↑ = 1.05` it SHRINKS toward zero (0.031 → 0.024
— flattening onto B). The honest uniformity statement (now Remark 3.4/4.1): γ-A's plateau
needs `ln x ≫ 1/(q↑−1)`; γ-R holds exactly at q↑ = 1; in between, behavior interpolates
along the crossover of Cor. A4.2, and no fixed-window law with a 10% tolerance exists for
`|q↑−1| ≈ 0.05` at accessible depths (`|q↑−1| ≲ 0.01` would be needed). The failed
registration is retained in the script and the output verbatim.

**Post-hoc controls (PH1–PH3; INFO, not falsifiers).** PH1 (solver quality): doubling the
EGM grid (Na 6000 → 12000) moves the q↑ = 1.6 deepest-shell mean by −4.6e-5 relative;
shifting the shell anchor by half a shell (`x_b → x_b·e^{Λ/2}`) moves the measured
|mean−B|/B from 0.897% to 0.942% — both far inside the 2% falsifier tolerance (grid- and
binning-invariance of the headline). PH2: the RT1 diagnosis above. PH3: the Stage-B
approach to `B_ψ` is from ABOVE in design (a) (mean/B_ψ: 1.231 → 1.0022) and from BELOW in
design (b) (0.712 → 0.9965) — documenting the sign flip behind the F5b wording note.

**Prior art.** The orchestrator's pre-brief mechanism check (`mech_check_unroll.py`,
2026-07-07 — committed alongside this document; quoted for provenance,
nothing below depends on it; near-knife-edge calibrations Þ_Γ ≈ 0.99) already measured the
same skeleton via the forward unroll of Cor 5.2: unroll/solved ratios {1.006, 1.032, 1.047} at
q↑ ∈ {1.6, 1.0, 0.6} and per-term head/tail ratios {19.7, 0.87, 0.051} — respectively the
λ < 1 contraction, the Cesàro flatness, and the end-dominated (fading-forcing) signatures of
§§3, 4, 6. This suite reproduces all three signatures on large-Λ calibrations with
registered tolerances and adds the boundary-value, detection, Stage-B, and fat-tail checks.

**Solver-quality note (honesty).** The Stage-A solves stop on the library's plateau guard
(it ≈ 700, sup-rel policy-churn ≈ 2e-2 concentrated at the constraint-boundary nodes); deep-
tail solution quality is certified NOT by that global norm but per point, by the
Euler-residual gap-certificate `(er/ρ)(c/g) ≤ 1e-3` enforced on every sample (the library's
own design: "tail quality is certified separately per point"), and independently by six
theory-target agreements at 0.07–0.9% and by PH1's grid-doubling control (−4.6e-5 relative
shift of the headline under Na 6000 → 12000).

---

## References

Internal (this repo): `statement.md`; `stage_A_proof.md` §§1–5 (imports); `stage_B_proof.md`
§§B0–B3 (imports); `exponential_impossibility.md` (owner of A0/B0);
`periodic_factor_fine_structure.md` (owner of P's fine structure); review harnesses
`review/R4_egm_lib.py`, `review/RB4_egm_lib_B.py`.

External (kept deliberately minimal — simplicity is this document's product;
`alt_proof_econlit.md` owns the literature fabric):

- F. Dumortier, J. Llibre, J.C. Artés, *Qualitative Theory of Planar Differential Systems*,
  Springer Universitext, 2006, ch. 5 (Poincaré compactification; the chart at infinity is
  `(u, v) = (y/x, 1/x)` with the line at infinity `{v = 0}` — the coordinate `z = 1/x` used
  here is the one-dimensional instance). Chart convention verified against the source
  before citing (2026-07-07).
- M. Muresan, *A Concrete Approach to Classical Analysis*, Springer, 2009 (the
  Stolz–Cesàro theorem; any standard real-analysis text serves).

---

*Document status recap:* γ0/γ1/γ2/γ3/γ-A/γ-R1/γ-R/γ-T/γ-C1/γ-C2/γ-B1/γ-B2/γ-B3/γ-B:
PROVEN-HERE. §6 circle-limit: IMPORTED (Theorem A2) modulo GAP-γ-equicont (tagged). §7
Stage-B resonance and q↑ < 1: OPEN-here (PROVEN in stage_B by the off-limits engine). §8:
PROVEN-CITED (owner: `exponential_impossibility.md`). Two registered numerical falsifiers
(RT1) FAILED as registered; diagnosis in §10; no proof statement depends on them.
Refuter panel 2026-07-08 (RF1/RF2): every PROVEN-HERE status CONFIRMED, the quarantine
HOLDS, the RT1 FAILs adjudicated as honest crossover phenomenology; repairs
RF1-F1/F2/F3/F4 and RF2-N1/N2/N3 applied in place (marked).
