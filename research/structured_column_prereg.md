# NMIR preregistration — G10 staggered / multi-isotope fixed-column gate

Date: 2026-09-06
Gate: G10 structured matter
Status at preregistration: PARTIAL NEGATIVE from density f-sum; geometry/isotope-selective fixed-column branch OPEN

## Question
Can staggered atomic layers, layer ordering, beam incidence angle, or a multi-isotope stack increase total neutrino absorption at fixed target mass/column when the microscopic cross sections themselves are unchanged?

This gate targets the user's proposed geometry in which each successive atomic layer is transversely displaced so ordinary line-of-sight geometric holes disappear.

## Frozen theorem domain
- passive independent capture/scattering events;
- no change of microscopic `sigma_i(E)` caused by the layering itself;
- no coherent interlayer structure-factor enhancement (already a separate density-response gate);
- no resonance/polarization/active pumping/BSM modification of `sigma_i`;
- fixed mass column or fixed slab mass/face area as stated below.

## T1 — layer-order/offset invariance
For layer `j`, define optical depth `tau_j(E)=Ncol_j sigma_j(E)`. Independent survival through all layers is

`S(E)=product_j exp(-tau_j)=exp(-sum_j tau_j)`.

Thus

`A(E)=1-S(E)=1-exp(-sum_j tau_j)`

is exactly invariant under layer permutation and transverse offsets, provided the microscopic cross sections are unchanged and events are independent.

Prospective result: exact numerical permutation tests must agree to machine precision.

## T2 — fixed-mass isotope-mixture bound
Let mass-column fractions be `w_i>=0`, `sum w_i=1`, isotope masses `m_i`, and cross sections `sigma_i`. Then

`tau / Sigma_mass = sum_i w_i (sigma_i/m_i) <= max_i sigma_i/m_i`.

Because `1-exp(-tau)` is monotone, no passive mixture/layer ordering at fixed mass column can beat the best pure component unless the structure changes the microscopic response itself.

Prospective result: random mixture tests must never exceed `max sigma_i/m_i` up to floating-point tolerance.

## T3 — slab tilt cannot increase total captured power
For a parallel beam incident on a slab of fixed face area with face-on optical depth `tau`, write `c=cos(theta)`. The projected intercepting area is `A c`, while path optical depth is `tau/c`. Up to a common incident flux factor,

`C(c)=c [1-exp(-tau/c)]`.

Freeze the claim that `C(c) <= C(1)` for `0<c<=1`; the thin limit approaches angle invariance, while finite optical depth makes tilting worse because projected area is lost before path-length gain can help total capture.

Prospective numerical scan: `C(c)/C(1) <= 1+1e-12` over `tau in [1e-12,100]`, `c in [1e-4,1]`.

## T4 — projected atomic coverage is not neutrino opacity
Use a deliberately extreme microscopic stress cross section, not a realistic material value:
- start from the iteration-0026 A=300, Z=119, E_nu=20 MeV one-body operator-norm cross-section envelope;
- multiply by the iteration-0033 one-body subleading amplitude stress `(1+r_1b)^2`;
- compare with a square lattice cell of spacing `a=2 Angstrom`.

Per-layer optical depth is `tau_layer = sigma_stress/a^2`. Record the number of ideal dense layers `1/tau_layer` and physical thickness `N_layers*a` needed for tau~1.

This is illustrative, not a crystal theorem. It tests whether atomic-scale projected staggering could matter before weak-interaction disks begin to overlap appreciably.

## Scope guards
1. If layering changes `sigma(E,q)` through a coherent structure factor, that is not geometry-only and must pass the density/spin sum-rule gates.
2. If isotope-specific resonances change `sigma_i`, compare the changed `sigma_i/m_i`; the mixture theorem still applies once microscopic values are fixed.
3. Directional redistribution is not total absorption gain.
4. No claim is made about active media or BSM.

## Prospective classification
If T1–T3 pass and T4 shows an astronomical layer count even under the frozen stress cross section, classify:

`G10_GEOMETRY_ONLY_STRONG_NEGATIVE / FIXED_COLUMN_MIXTURE_THEOREM_PASS`.

Keep only microscopic-response-changing structured matter (coherence/resonance/polarization) open under their own gates.
