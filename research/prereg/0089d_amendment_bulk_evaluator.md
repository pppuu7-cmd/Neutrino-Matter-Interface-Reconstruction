# NMIR prereg amendment 0089d — result-independent bulk evaluator conformance

Date frozen: 2026-09-08
Parent contract: `research/prereg/0089d_g9_continuous_map_monotone_kernel.md`, commit `8eab0935d54cb930495b55cbc3025225729f109c`.

## Purpose
The parent contract freezes globally uniform V4 midpoint-indicator meshes with N=2^18 and N=2^19 for every observer/radius control. Evaluating the accepted scalar continuous projection shell-by-shell at every midpoint would be computationally wasteful but adds no new scientific information. Before inspecting any 0089d crossing, accepted interval, area, grid replica, or K value, freeze a deterministic vectorized evaluator identical in algebraic semantics to the already accepted 0089b continuous piecewise-linear projection.

This amendment changes implementation/performance only. It does not change any 0089d scientific input, turning root, radius, branch, target equation, grid size, root tolerance, 0.5% criterion, classification, or next action.

## Frozen bulk semantics
Reuse the vectorized closed-form shell formulas already exercised prospectively in 0089c (`_bulk_eval_factory`) or a byte-/algebraically-equivalent implementation. Bulk evaluation may produce M_cyl(x), F_c(x), and signed y_c(x;z) for arrays of x. It may not discover crossings, add mesh points, refine locally, or alter branch topology.

Before any result-dependent 0089d V4 interpretation, perform a result-independent B0 conformance audit against the scalar accepted 0089b authority. Use the same deterministic 0089c B0 point construction: fixed physical points plus 64 approximately uniformly selected source-cell midpoints. Require max symmetric-relative discrepancy <=2e-11 for projected mass and focal distance. If derivatives are bulk-evaluated for branch diagnostics, require <=2e-10 for derivative. Failure is `INFRASTRUCTURE_FAIL_G9_0089D_BULK_EVALUATOR_CONFORMANCE`, before scientific classification.

For V4, evaluate exactly the frozen uniform midpoint meshes over [1e-4,1]: x_j = XMIN + (j+1/2)(XMAX-XMIN)/N for N in {2^18,2^19}. The bulk evaluator is only an independent indicator-area replica. It must not seed or repair authoritative crossings/intervals.

## Guards
- No result-selected chunk sizes affect mathematical nodes; chunking is memory-only.
- No local/adaptive grid refinement.
- No replacement of scalar authority for branch/crossing construction.
- No relaxed residual, area, one-ring, grid, monotonicity, aperture, or no-double-counting criterion.
- No finite-source/persistent-source calculation.

All parent 0089d PASS/BLOCKED/FAIL criteria remain unchanged.
