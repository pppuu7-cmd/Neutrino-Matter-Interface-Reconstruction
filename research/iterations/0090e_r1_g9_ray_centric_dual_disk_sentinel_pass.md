# Iteration 0090e-r1 — G9 ray-centric dual-disk finite-source sentinel PASS

Date: 2026-09-08
Classification: `PASS_G9_RAY_CENTRIC_DUAL_DISK_SENTINEL_AUTHORITY`

## Frozen authority chain
Parent: 0090d `BLOCKED_G9_SOURCE_CENTRIC_FINITE_SOURCE_CONVOLUTION`.
Preregistration: `research/prereg/0090e_g9_ray_centric_dual_disk_overlap_sentinel_authority.md`.
Prereg commit: `c9d9e46860ef55bec2a5aaaafdac19f6e9de551b`.
Floating-point conformance amendment: `research/amendments/0090e_overlap_float_conformance_r1.md`, commit `c95fd80e7b2a54d04f83103e7678acbe8c51f6c6`.
Final execution head: `d48f2a37e132242d2f3d4f5421ccca616d2b6b90`.

## Initial non-authoritative execution history
Initial run `34269251144` used a direct binary64 evaluation of the exact textbook two-circle partial-overlap expression. In the extreme disparate-radius regime it suffered catastrophic cancellation and produced out-of-range floating-point overlap values before H2/H3 science could be classified.

Because the exact geometric intersection area cannot leave `[0, pi*min(s,a)^2]`, amendment 0090e-r1 prospectively reclassified that run as `INFRASTRUCTURE_FAIL_G9_0090E_OVERLAP_FLOAT_CONFORMANCE` and allowed only the same exact formula to be evaluated at 60 decimal digits whenever the frozen ratio `min(s,a)/max(s,a,h) < 1e-3`, or as a deterministic fallback when the direct double expression leaves the exact range. No physical semantics, sentinel, split rule, quadrature order or scientific tolerance changed.

## Repaired hosted authority
- run: `34269721278`
- aggregate job: `102208186432`
- aggregate artifact: `10073322174`
- independently verified ZIP SHA256: `0117d80967e39188e16340c6c84db5984a948dcb9bf1081afe0b7c447e49f47a`
- independently verified inner `g9_0090e_result.json` SHA256: `a598d511747c4e3e00eb2c790d9c36e2c32af90e86dc6a36b28e817505cbb9cb`
- `shard_count=9`, `pair_count=9`, `row_count=81`
- all 9 shard payloads: `SHARD_PASS_G9_RAY_CENTRIC_DUAL_DISK`

## Authoritative numerical diagnostics
- maximum L/H finite-source discrepancy: `1.3361210278347196e-05` against frozen `0.005` limit;
- maximum exact-overlap scale relative error: `3.98287432063186e-16`;
- maximum exact-overlap symmetry relative error: `1.5111062375575333e-15`;
- maximum inherited point-control relative error: `2.085291751613404e-09`;
- maximum smallest-source point-limit relative error: `1.7877931326412472e-09`;
- sentinel `mu_H` range: `157.28015230029052` to `2852164396.6441298`.

The large sentinel magnifications are method-authority outputs only. They are not a named astrophysical-source claim, practical duty-cycle claim, detector/material gain, event-rate gain, interaction gain, or neutrino-energy gain.

## Scientific interpretation
The exact finite uniform source disk can be convolved with the already certified continuous solar-lens signed map by exchanging the integration order and integrating source acceptance through exact two-circle overlap geometry. This removes the explicit source-point quadrature bottleneck that blocked 0090d.

0090e-r1 therefore authorizes one next step only: a separately prospectively preregistered full 1350-point G9 finite-source scan using exactly the high (H) ray-centric dual-disk method and the frozen high-precision conformance amendment.

0090e-r1 itself does not establish a final survivor count, a named source, alignment probability, duty cycle, detector feasibility or any BSM effect.

## Next admissible action
Recover the exact 1350-grid and survivor semantics from the prior 0090 authority files, freeze them in a new preregistration before computing the full grid, and run the H ray-centric dual-disk method without result-selected changes.
