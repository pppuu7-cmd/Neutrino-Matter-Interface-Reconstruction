# Preregistration 0090d — G9 source-centric finite-source sentinel authority

Date frozen: 2026-09-08
Parent: 0090c `PASS_G9_SOURCE_CENTRIC_EXACT_MEASURE_AUTHORITY`, immutable record `research/iterations/0090c_g9_source_centric_exact_measure_pass.md`.

## Scientific/numerical question
Can the already certified source-centric exact probability measure `(q,phi)` be convolved with the already certified global signed solar-lens map on a fixed finite-source sentinel set with reproducible low/high numerical replicas, without the radial-source normalization routes that blocked 0090a/0090b?

0090d is a method/sentinel authority gate. It is not the full 1350-point survivor scan. PASS can authorize only a separately preregistered full-grid finite-source G9 scan; PASS itself does not establish a final survivor count or named-source realizability.

## Frozen upstream authority
Use without changing their physical semantics:
- Model-S blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`;
- continuous signed map / turning-root chain 0089b/0089c;
- mesh-free narrow-preimage geometry authority 0089e-r2;
- 0090a `phi_fraction`, monotone-branch threshold roots, `b_intervals`, `area_at_u`, `point_area_exact` implementation semantics;
- 0090c exact source-centred measure `dP=dq*dphi/(2*pi)`.

No 0090a radial density/normalization integral and no 0090b endpoint-regularized radial normalization may be used in 0090d.

## Frozen physical sentinel set
Shard by the 9 existing `(observer control, receiver)` pairs:
- observer controls `x0={0.020,0.024,0.030}` with frozen focal distances and turning points from the existing G9 chain;
- receivers `a={1,10,100} m` from the current receiver grid.

Within every shard evaluate exactly 9 finite-source sentinels:
- theta indices `k={0,12,24}` from the existing class grid `theta_s=10^(-18+k/2) rad`;
- centre offsets `delta_y={0,0.1,100} m`.

Total authority set: `9 shards x 9 rows = 81` finite-source sentinels. This subset is fixed before results and spans the smallest, middle and largest source-angle classes and aligned/intermediate/extreme offsets. It is not outcome-selected.

## Frozen source-coordinate convolution
For source radius `s=z*AU_CM*theta_s`, source-centre offset `d`, and source coordinates

`q=r^2/s^2`, `r=s*sqrt(q)`, `0<=q<=1`,
`phi in [0,2*pi)`,

map each source point to optical-axis offset

`u(q,phi)=hypot(d+r*cos(phi), r*sin(phi))`.

Let `A(u;a)` be the accepted incident solar area returned by the inherited branch/root `area_at_u` kernel for receiver radius `a`.

The finite-source accepted area is

`Abar = integral_0^1 dq integral_0^(2*pi) dphi/(2*pi) A(u(q,phi);a)`.

Magnification is frozen as

`mu = 1 + Abar/(pi*a^2)`

with `a` in cm, preserving the prior G9 accounting convention. No extra multiplicative gain may be introduced.

## Frozen numerical replicas
Use two deterministic product replicas:

L:
- Gauss-Legendre order 8 in `q` mapped to `[0,1]`;
- 16 equal-weight azimuthal midpoint nodes;
- inherited `area_at_u` Gauss-Legendre order 32 in each prospectively root-split `b` interval.

H:
- Gauss-Legendre order 16 in `q`;
- 32 equal-weight azimuthal midpoint nodes;
- inherited `area_at_u` order 64.

Weights are exactly the 0090c product probability weights. No adaptive source quadrature, no result-selected nodes, no source-order escalation, no `b`-order escalation and no tolerance relaxation after result inspection.

Implementation may memoize/reuse exactly equal floating-point `u` nodes within a row, but may not round/merge distinct `u` values for scientific evaluation.

## Frozen validation criteria
H0 provenance/map invariants:
- exact Model-S blob match;
- focal-distance relative drift `<=2e-11`;
- batch/scalar signed-map conformance `<=2e-11`;
- inherited accepted-area invariants `0<=A<=pi*Rsun^2`;
- exact shard/row cardinalities `9/81` in aggregate.

H1 point-source control:
For each shard compute inherited `point_area_exact` and compare with the frozen 0089e-r2 aligned reference area for that `(observer,receiver)` pair; relative difference `<=0.5%`.

Additionally, for the preregistered smallest-source aligned sentinel `(theta index 0, delta=0)`, H finite-source accepted area must agree with `point_area_exact` to relative `<=0.5%` when the point area is nonzero. This is a finite-source-to-point limit control, not a fit.

H2 finite-source replica convergence:
For every one of the 81 sentinels define `e_L=mu_L-1`, `e_H=mu_H-1`.
- if `max(|e_L|,|e_H|) >= 1e-10`, require `|e_L-e_H|/max(|e_L|,|e_H|) <= 0.005`;
- otherwise require `|mu_L-mu_H| <= 1e-10`.

H3 physical/numerical invariants:
- all finite-source accepted areas finite and in `[0,pi*Rsun^2*(1+1e-9)]`;
- all `mu_L,mu_H` finite and `>=1`;
- no source-coordinate weight renormalization from computed results;
- no radial-source normalization factor is applied.

H4 reproducibility summary:
Record per shard point control, all 9 rows, maximum L/H discrepancy and exact head/contract. Aggregate only if all 9 shard payloads exist with matching head and contract.

## Frozen classifications
Per aggregate:
- `PASS_G9_SOURCE_CENTRIC_FINITE_SOURCE_SENTINEL_AUTHORITY`: all 9 shards and all 81 rows pass H0-H4.
- `BLOCKED_G9_SOURCE_CENTRIC_FINITE_SOURCE_CONVOLUTION`: exact provenance/map invariants hold but one or more fixed point-limit or L/H convergence checks fail under the frozen replicas.
- `SCIENTIFIC_FAIL_G9_SOURCE_CENTRIC_FINITE_SOURCE_INVARIANT`: an exact physical/map/accepted-area invariant fails.
- `INFRASTRUCTURE_FAIL_G9_0090D`: source/runtime/dependency/shard/artifact failure before complete scientific classification.

A finite completed H1/H2 miss is scientific BLOCKED, not infrastructure. Preflight tests may check code-path sanity only and must not enforce H1/H2 before scientific shard artifacts are written.

## Exact next actions
- On PASS: freeze a separate full-grid finite-source G9 survivor scan using exactly the validated H source method. That later gate must prospectively define the 1350 rows, survivor criterion and aggregate/reproducibility rules before calculation.
- On BLOCKED: keep 0090d immutable; do not increase 8x16/16x32 source replicas, 32/64 `b` orders or loosen 0.5%. Move to another independent actionable integration formulation or another funnel family.
- On SCIENTIFIC_FAIL: audit the affected upstream geometry/map invariant.
- On INFRASTRUCTURE_FAIL: repair infrastructure only.

## Guards
No full 1350-point scan in 0090d. No named-source/duty/positioning calculation. No detector/material gain and no BSM response/enhancement. No retroactive promotion of 0090/0090a/0090b. BSM remains LOCKED.
