# NMIR amendment 0089b — V1 implementation-mismatch observability

Date: 2026-09-08
Parent scientific preregistration: `5d99cd6cd4d3a5f1f9defecfbd7f4036c93b8636`.
Prior V0 reference-only repair: `research/amendments/0089b_toy_uniform_reference_cancellation.md`.

## Trigger
Hosted run `34211066432` passed all dedicated 0089b algebra regression tests, then terminated before V2/V3 with the preregistered implementation classification
`INFRASTRUCTURE_FAIL_G9_CONTINUOUS_PROJECTION_IMPLEMENTATION`
at the first frozen V1 point `x=0.0001`.

The terminal JSON reported only the point identity, not whether mass, derivative, or both exceeded the already frozen V1 tolerances. No V2 source-knot continuity value and no V3 continuous/discrete compatibility value was produced or inspected.

## Frozen implementation-only change
Before any retry, authorize only improved diagnostics for V1 failures:
- leave `src/nmir/g9_continuous_projection.py` unchanged;
- leave the 80-digit reference construction, frozen V1 points, Model-S source/hash, and all V0-V3 tolerances unchanged;
- when V1 fails, report `got_mass`, `reference_mass`, `mass_rel`, `got_derivative`, `reference_derivative`, and `derivative_rel` for the failing already-frozen x point in the implementation-failure reason/result.

This amendment adds observability only. It cannot promote a scientific PASS/BLOCKED result and does not authorize changing production formulas before the diagnostic output is inspected.