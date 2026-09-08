# NMIR amendment 0089b — V1 mass-reference theta identity repair

Date: 2026-09-08
Parent scientific preregistration: `5d99cd6cd4d3a5f1f9defecfbd7f4036c93b8636`.
Prior observability amendment: `research/amendments/0089b_v1_mismatch_observability.md`, commit `011fd76e317a61b725b86126a1308ebb61bf5d7a`.

## Trigger and observed scope
Hosted observability retry run `34212250608`, job `102015721854`, on head `95e9415bceecf5fce33fd23095e56f5902ad32ac` stopped at the already frozen first V1 point `x=1e-4` with the preregistered implementation classification `INFRASTRUCTURE_FAIL_G9_CONTINUOUS_PROJECTION_IMPLEMENTATION`.

The independently validated artifact shows:
- production derivative vs 80-digit derivative reference relative mismatch `4.509854236931335e-13`, comfortably inside the frozen V1 `1e-9` derivative tolerance;
- production mass `4.592225390416342e26 g` versus the existing V1 mass reference `1.9881120074729295e33 g`, relative mismatch `0.999999769015761`.

No V2 source-knot continuity value and no V3 continuous/discrete compatibility value has been produced or inspected.

## Algebraic defect in the independent V1 mass reference
The V1 reference uses the substitution

`theta = acos(x/u)`, hence `u=x/cos(theta)` and

`sqrt(1-(x/u)^2) = sin(theta)`

on the integration domain.

Therefore the above-x mass integrand

`u^2 rho(u) [1-sqrt(1-(x/u)^2)] du`

transforms exactly to

`x^3 rho(x/cos(theta)) * [1-sin(theta)] * sin(theta) / cos(theta)^4 dtheta`.

The current independent reference incorrectly used `2 sin(theta/2)^2 = 1-cos(theta)` in place of `1-sin(theta)`. This is a reference-construction identity error; it does not alter the prospectively frozen production evaluator or any scientific acceptance criterion.

For numerical stability near `theta -> pi/2`, use the algebraically identical rationalized form

`1-sin(theta) = cos(theta)^2 / [1+sin(theta)]`,

so the corrected reference integrand is

`x^3 rho(x/cos(theta)) * sin(theta) / {cos(theta)^2 [1+sin(theta)]}`.

## Frozen reference-only repair
Before any retry authorize only:
1. replace the V1 independent-reference **mass** theta integrand by the exact corrected/rationalized expression above;
2. leave the derivative theta reference unchanged;
3. leave `src/nmir/g9_continuous_projection.py` unchanged;
4. leave Model-S bytes/hash, parser semantics, frozen V1 points, 80-digit precision, quadrature rule, and all V0-V3 thresholds unchanged;
5. retain the observability-only diagnostics from the prior amendment.

No production formula, scientific tolerance, source point, V2 offset, V3 grid, or classification rule may change under this amendment.

## Taxonomy / next action
A retry remains an implementation/reference-conformance attempt under the original 0089b preregistration.
- Any remaining V1 mismatch is still `INFRASTRUCTURE_FAIL_G9_CONTINUOUS_PROJECTION_IMPLEMENTATION`.
- Only if V1 passes may the already frozen V2/V3 scientific blocker criteria be evaluated.
- This amendment cannot itself create a scientific PASS/BLOCKED result.
