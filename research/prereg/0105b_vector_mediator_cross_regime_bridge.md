# 0105b — vector-mediator forward / finite-q cross-regime bridge

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105B
State: ACTIVE_PREREGISTRATION_ONLY
Parent: `research/prereg/0105_v2_model_agnostic_bsm_residual_reconstruction.md`

## Purpose

Certify, before any result-dependent fit, the minimal analytic bridge by which a single neutral vector mediator can generate both a zero-momentum coherent matter interaction and a finite-momentum neutrino-scattering deformation.

This is a mathematical/control gate. It is **not** evidence for a mediator, not an NSI fit, not a CEvNS residual claim, and not permission to combine heterogeneous experimental confidence regions.

## Frozen benchmark convention

Use a schematic interaction

`L_int ⊃ X_mu [ g_nu nu_bar gamma^mu P_L nu + g_f f_bar gamma^mu f ]`.

For one matter fermion species and spacelike momentum magnitude `q >= 0`, define the coefficient in common energy units

`C0 = gprod / mX^2`,

`Cq = gprod / (mX^2 + q^2)`,

where `gprod = g_nu g_f` and `mX > 0`.

The coefficient ratio is

`r = Cq/C0 = mX^2/(mX^2+q^2)`

for nonzero `gprod`.

The ratio is defined analytically independent of the coupling product; the implementation must calculate it directly rather than divide two nearly zero coefficients.

For `0 < r < 1` and `q > 0`, the inverse relation is

`mX = q sqrt[r/(1-r)]`.

For nonrelativistic nuclear recoil,

`q = sqrt(2 M T)`

in a single internally consistent energy unit. The exact relativistic kinematic refinement is outside this bridge preflight and can be introduced only by a later preregistered detector-specific gate if needed.

For coherent vector coupling to a nucleus,

`QX = Z gp + N gn`.

No quark-to-nucleon mapping is assumed in this preflight.

## Unit convention

The implementation uses GeV for `mX`, `q`, nuclear mass and recoil energy. Hence `C0` and `Cq` have units `GeV^-2` for dimensionless `gprod`.

Helper conversion from recoil keV to GeV is allowed only as an explicit named function/argument convention; silent unit conversion is forbidden.

## Prospectively frozen tests

All of the following must pass before any data fit can depend on the bridge:

1. `q=0` gives `r=1` exactly within floating-point representation.
2. `q>0`, `mX>0` gives `0<r<1`.
3. `mX/q -> infinity` approaches the contact limit `r->1`.
4. `mX/q -> 0` approaches the finite-range/light limit `r->0`.
5. `mediator_mass_from_ratio(finite_q_ratio(mX,q),q)` round-trips `mX` over at least six decades in `mX/q` away from floating-point singular endpoints.
6. `r<=0` or `r>=1`, `q<=0` are rejected by the inverse map.
7. `mX<=0` or `q<0` are rejected by forward ratio/coefficient functions.
8. `Cq` has the same sign as `gprod` and `|Cq|<=|C0|` for `q>=0`.
9. Changing `gprod` does not change `r`.
10. `q=sqrt(2MT)` returns zero at zero recoil and scales as `sqrt(T)` and `sqrt(M)`.
11. Nuclear vector charge obeys the proton-only, neutron-only and isoscalar limits exactly.
12. No function in this module returns an event rate, likelihood, confidence level, opacity or discovery significance.

## Synthetic scale controls

The bridge tests may use synthetic masses/momenta in GeV. They are code-path fixtures, not parameter estimates.

A descriptive scale check may report `r` at representative finite-q values to illustrate when the contact approximation loses leverage. Such values must be labelled analytic scale controls and must not be fitted to COHERENT or IceCube observations.

## Interpretation guard

A successful 0105b result establishes only:

> the same frozen vector propagator can be represented consistently in the forward and finite-q regimes, with an invertible coefficient-ratio relation in the finite-range window.

It does not establish that either experiment contains a residual, that a vector mediator is preferred over scalar/magnetic/sterile families, or that a joint likelihood is statistically valid.

## Allowed terminal classification

`PASS_0105B_VECTOR_MEDIATOR_CROSS_REGIME_MATHEMATICAL_BRIDGE_NONDISCOVERY`

Failure of any frozen invariant gives

`FAIL_0105B_VECTOR_MEDIATOR_BRIDGE_INVARIANT`.
