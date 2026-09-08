# NMIR amendment 0089c — bulk evaluator conformance acceleration

Date frozen: 2026-09-08
Parent preregistration: `1f96b318b437d6a5aecf815ef829ef09a8adc7e6`.
Parent scientific authority: 0089b `PASS_G9_CONTINUOUS_PIECEWISE_LINEAR_PROJECTION_AUTHORITY`, immutable `40f88288c7996d105446918e78cce29aa4c99d83`.

## Motivation frozen before any 0089c signs/roots
The preregistered Q64 audit contains roughly 1.5e5 result-independent x probes before the separate finite-difference midpoint stress. Calling the accepted scalar 0089b evaluator independently at each probe would repeat an O(N_source) Python loop over ~2400 source intervals for every x and is an implementation/runtime risk, not a scientific requirement.

No 0089c derivative sign, root position or root count has been computed before this amendment.

## Authorized acceleration only
A bulk/vectorized evaluator may be used **only** for preregistered fixed-mesh mass/derivative/focal-distance values if it implements exactly the accepted 0089b source-interval formulas, constants, Model-S parser semantics and endpoint conventions. It may change evaluation order/rounding only; it may not interpolate, smooth, refit, approximate the density, omit source intervals, add a cutoff, or numerically differentiate.

The accepted scalar 0089b functions remain the scientific implementation authority:
- `continuous_projected_mass_g`;
- `continuous_projected_mass_derivative_g_per_x`;
- `continuous_focal_distance_au`.

All bisection roots and all independent signed-map finite-difference confirmations in R2/R4 must use the accepted scalar evaluator directly. The bulk evaluator is only a deterministic fixed-mesh accelerator for R1/R3/R5 candidate discovery/stress.

## Frozen conformance check B0
Before any scientific sign/root evaluation, compare bulk and accepted scalar values on a result-independent set consisting of:
- global x anchors `{1e-4, 3e-4, 1e-3, 0.003, 0.01, 0.02, 0.024, 0.03, 0.05, 0.1, 0.2, 0.4, 0.7, 0.9, 0.99, 0.99999825}`;
- 64 deterministic source-cell midpoints with cell indices `round(j*(N_cells-1)/63)`, `j=0..63`.

For every point require symmetric relative agreement:
- mass `<=2e-11`;
- derivative `<=2e-10`;
- focal distance `<=2e-11`.

These are implementation-conformance tolerances, not scientific root tolerances. Any failure is `INFRASTRUCTURE_FAIL_G9_0089C_BULK_EVALUATOR_CONFORMANCE` and stops before R1.

## Frozen bulk implementation semantics
If NumPy is used, evaluate in bounded x chunks and source-interval arrays using the same closed forms as 0089b:
- mass below x from exact polynomial interval integral;
- above-x mass from the accepted `_fa/_fb` algebra;
- derivative from the accepted endpoint-centered t-space shell formula frozen in amendment `a0ee082787ab15fab1a5677b40f5c3af501ee29a`;
- global sums in float64. No lower precision is allowed.

Bulk values may be cached for the exact preregistered mesh only. No root is interpolated from cached values; cached signs only define the already-authorized deterministic brackets.

## Non-changes
This amendment does not alter Q32/Q64, source-knot anchors, `tau_D`, bisection widths, R3 offsets, R4 finite-difference scales/tolerances, R5 stress points, R6 controls, PASS/BLOCKED/FAIL taxonomy, physical constants, Model-S bytes, or the accepted continuous map.

No scientific criterion may be relaxed after results are seen.
