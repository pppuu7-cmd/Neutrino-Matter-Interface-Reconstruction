# 0105d result — composition / finite-range identifiability

Date: 2026-09-10
Gate ID: NMIR-V2-0105D
Final state: `PASS_0105D_COMPOSITION_RANGE_IDENTIFIABILITY_PREFLIGHT_NONDISCOVERY`

## Scope

This result closes only the pre-data coefficient-level identifiability gate frozen in `research/prereg/0105d_composition_range_identifiability_preflight.md`. It contains no observed CEvNS or oscillation residual, no likelihood preference, and no BSM significance.

## Algebraic result

For equal nonzero momentum transfer `q`, two composition-distinct targets satisfy

`k = R1/R2 = (Z1 rho + N1)/(Z2 rho + N2)`

with

`rho = gp/gn = (N1-k N2)/(k Z2-Z1)`.

The sufficient composition nonparallelism control

`Delta12 = Z1 N2 - Z2 N1 != 0`

is satisfied by the frozen isotope controls:

- Ar-40 versus Cs-133: `Delta = 194`;
- Ar-40 versus I-127: `Delta = 166`.

After `rho` is recovered, the finite-q factor

`f = mX^2/(mX^2+q^2)`

can be inverted to

`mX = q sqrt[f/(1-f)]`

provided the absolute propagation-to-scattering normalization is known and `0<f<1`.

A common unknown multiplicative scale cancels from the two-target ratio and therefore can preserve `rho`, but it does not preserve the absolute `mX` inversion.

## CI failure audit and correction

An initial full-CI execution on commit `c7a3e5a6a50cc5f83b56d48caed8890f8a527b70` failed one 0105d round-trip test. At `mX/q=1e-2` the test reported `rho=-0.180766...` instead of the injected `rho=0.35`.

The failure was investigated as a possible light-mediator conditioning problem before any tolerance or acceptance criterion was changed. The root cause was instead a test-fixture identity mismatch:

1. `forward_ratios(...)` defaulted to the Ar-40 + Cs-133 pair;
2. the failing mass-scan test generated its coefficients with those defaults;
3. the same coefficients were then passed to an inversion declared as Ar-40 + I-127.

Thus the failed inversion was being asked to reconstruct parameters from coefficients produced by a different nuclear composition. The negative recovered `rho` was not a failure of the frozen algebra and not evidence for light-mediator non-identifiability.

Commit `7fa928a72acb6370f2305801816eea1c579d5057` corrects only this fixture mismatch. The revised test explicitly generates and inverts the same named target pair and checks **both** Ar+Cs and Ar+I across

`mX/q = 1e-2, 1e-1, 1, 1e1, 1e2`.

No physics formula, domain, tolerance or pass criterion was relaxed.

## Hosted full-CI authority

Corrected workflow run:

- run: `34417578879`
- job: `102685758734`
- head: `7fa928a72acb6370f2305801816eea1c579d5057`
- result: SUCCESS
- pytest: `673 passed`
- `python -m nmir.baseline`: SUCCESS

Therefore the frozen 0105d synthetic/algebraic invariants are satisfied.

## Interpretation

0105d establishes an **in-principle algebraic identifiability condition**, not an experimental sensitivity statement. In particular, the preregistered very-light and heavy/contact practical-conditioning cautions remain active. Statistical certifiability versus `mX/q` is separated into 0105e rather than being retrofitted into this gate after the CI failure.

## Discovery guard

This result must not be described as:

- evidence for a new mediator;
- a measured value of `gp/gn` or `mX`;
- a new observation of multi-target CEvNS complementarity;
- an observed residual preference.

It is a pre-data control establishing that the proposed cross-regime coordinate map is algebraically capable of separating composition and finite range under its stated assumptions.
