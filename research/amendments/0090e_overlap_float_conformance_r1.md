# Amendment 0090e-r1 — dual-disk overlap floating-point conformance only

Date frozen: 2026-09-08
Parent prereg: `research/prereg/0090e_g9_ray_centric_dual_disk_overlap_sentinel_authority.md`, frozen commit `c9d9e46860ef55bec2a5aaaafdac19f6e9de551b`.
Initial execution head: `9a0493e9442854f7a0adab002b6842b93b03e93f`, run `34269251144`.

## Observed orchestration/numerical issue
The initial hosted scientific shards wrote payload status `SCIENTIFIC_FAIL_G9_DUAL_DISK_INVARIANT` with reason `dual-disk overlap range invariant` before finite-source H2/H3 classification.

That payload label is not promoted to a physical/scientific geometry failure. For positive radii and a physical separation, the exact two-circle intersection area frozen in the parent prereg is mathematically constrained to

`0 <= O(s,a,h) <= pi*min(s,a)^2`.

The direct IEEE-754 double evaluation of the frozen textbook partial-overlap expression contains subtraction of large nearly equal terms when the radii are strongly disparate and the circles are close to tangency/containment. Thus an out-of-range result produced by that direct floating-point expression is an evaluator-conformance failure, not evidence that the exact overlap geometry violates its range.

The initial run is therefore reclassified for authority purposes as `INFRASTRUCTURE_FAIL_G9_0090E_OVERLAP_FLOAT_CONFORMANCE`. It carries no PASS/BLOCKED/physical-fail conclusion about 0090e.

## Allowed implementation repair
Scientific contract, physical geometry, sentinel set, split rules, quadrature nodes/orders, H0-H4 thresholds and classifications remain unchanged.

Only evaluation of the already frozen exact partial-overlap formula may change:
1. retain exact disjoint and containment branches in ordinary double precision;
2. for the strict partial-overlap branch, evaluate the same frozen formula in higher precision whenever the deterministic input ratio
   `min(s,a)/max(s,a,h) < 1e-3`;
3. also fall back to the same higher-precision expression if an ordinary-double partial evaluation is non-finite or leaves the exact range before final roundoff clipping;
4. use at least 50 decimal digits for the fallback and convert only the final overlap area to binary64;
5. only the parent-preregistered `acos` argument clipping and nonnegative-radicand roundoff clipping remain allowed. No smoothing, interpolation, empirical correction or result-derived normalization is introduced.

The ratio trigger is fixed prospectively in this amendment and may not be changed after the repaired hosted result is inspected.

## Preflight scope
A deterministic extreme-radius partial-overlap conformance test may be added to ensure the evaluator returns a finite value in the exact geometric range. It must not test any physical sentinel magnification or H2/H3 convergence criterion.

## Re-run authority
The repaired execution must use a new head/run. The parent contract remains `c9d9e468...`; this amendment commit must be recorded with the repaired result. The original run `34269251144` remains immutable infrastructure history.
