# NMIR preregistration — long-range/nonlocal interaction-budget gate

Date: 2026-09-06
Status: **PROSPECTIVE / FROZEN BEFORE IMPLEMENTATION**

## Funnel question
Iteration 0028 left genuinely long-range/all-to-all collective response open because an unscaled all-to-all spin control was superextensive. Does that superextensive energy-weighted response survive if the passive medium is required to have an extensive absolute interaction-energy budget, or is the apparent gain paid one-for-one by a superextensive internal interaction scale?

This gate applies to passive pair-interaction Hamiltonians and additive neutrino-coupled observables. It does not silently cover active pumping, non-pair Hamiltonians, dynamical mediator fields omitted from the energy accounting, BSM neutrino couplings, or gravitational focusing.

## Literature anchor
Defenu et al., Rev. Mod. Phys. 95, 035002 (2023), review long-range interacting quantum systems and explicitly distinguish strong nonlocal/nonadditive regimes from energy-extensive long-range regimes. Long-range statistical-mechanics reviews likewise note that strong slowly decaying interactions can make the energy superextensive and that scaling/Kac-type normalization restores extensivity.

## Frozen theorem
Let

`H = sum_{i<j} h_ij`,

and let the neutrino-coupled additive medium operator be

`O = sum_i o_i`, with `||o_i|| <= o0`.

Because only `o_i+o_j` fails to commute with a pair term,

`m1 = (1/2) <[O,[H,O]]>`

obeys term by term

`|m1| <= 2 sum_{i<j} ||o_i+o_j||^2 ||h_ij||`

and therefore

`|m1| <= 8 o0^2 W_N`,

where

`W_N = sum_{i<j} ||h_ij||`

is the absolute pair-interaction norm budget.

Thus, if a passive family satisfies an extensive absolute budget

`W_N <= epsilon * N`,

then

`|m1|/N <= 8 o0^2 epsilon`.

A superextensive first moment `m1 ~ N^(1+delta)` requires `W_N` to be at least superextensive at the same scaling level under this bound. This is a response-vs-internal-interaction-budget statement, not a universal thermodynamic theorem for arbitrary Hamiltonians.

## Frozen all-to-all scaling family
Take identical pair norm scale

`||h_ij|| = J0 / N^kappa`.

Then

`W_N = N(N-1) J0 / (2 N^kappa) ~ (J0/2) N^(2-kappa)`

and

`m1_bound/N ~ N^(1-kappa)`.

Frozen interpretations:
- `kappa=0`: unscaled all-to-all; per-particle interaction budget and response bound both grow ~N.
- `0<kappa<1`: both still diverge, as `N^(1-kappa)`.
- `kappa=1`: Kac/extensive normalization; both are O(1) per particle.
- `kappa>1`: both decrease per particle.

## Frozen power-law range scaling
For approximately uniform d-dimensional matter with pair norm `J(r) ~ 1/r^alpha`, the absolute interaction budget per constituent scales parametrically as

- O(1) for `alpha>d`,
- O(log N) at `alpha=d`,
- O(N^(1-alpha/d)) for `alpha<d`,

before any Kac/extensivity normalization. Any normalization that makes the absolute pair budget O(N) also removes this parametric superextensive first-moment upper-bound gain.

## Prospective computational gates
Hosted benchmark will test N from `1e3` to `1e6` and must satisfy before classification:
1. exact identity `m1_bound = 8 o0^2 W_N` to floating tolerance;
2. for `kappa=1`, per-particle `W_N` changes by <0.2% from N=1e3 to 1e6;
3. for `kappa=0`, per-particle `W_N` gain matches the finite-N analytic ratio `(N2-1)/(N1-1)` to `1e-12` relative;
4. for `kappa=0, 0.5, 1.0`, response-bound-per-particle gain equals interaction-budget-per-particle gain to `1e-12` relative;
5. a Kac-normalized `alpha<d` diagnostic removes the frozen power-law divergence factor exactly by construction.

## Classification rule
If all gates pass: **PASS_LONG_RANGE_BUDGET / STRONG-NEGATIVE scoped** against a free passive all-to-all energy-weighted gain at fixed extensive absolute pair-interaction budget.

The surviving loopholes would be explicitly narrower:
- a genuinely nonadditive/superextensive medium whose growing internal interaction-energy budget is physically acceptable and included in accounting;
- a dynamical mediator/field whose own energy and stability must be included;
- active/non-equilibrium pumping, which is not neutrino-supplied energy;
- non-pair/high-body interactions outside this theorem;
- BSM neutrino operator strength.

No practical-energy claim is made by this gate alone.
