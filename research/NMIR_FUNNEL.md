# NMIR Discovery Funnel

Reconciled: 2026-09-08. Repository + validated Actions artifacts are scientific authority; chat/static summaries are not. Recovery protocol: `research/RECOVERY_MANUAL.md`; compact state: `research/RECOVERY.md`.

## Mandatory funnel
F0 objective -> F1 microscopic channel -> F2 production/absorption where applicable -> F3 kinematics/source overlap -> F4 microscopic strength -> F5 collective/resonant engineering -> F6 no-free-lunch/fundamental bounds -> F7 common quantitative score -> F8 external constraints -> F9 composition only after independent validation -> F10 classification. Never multiply unvalidated gains.

## Stable broad guards
Closed in stated scopes unless a genuinely new assumption changes them: naive static `N^2`; geometry-only fixed-column gain; passive local density/phonon or spin/magnon free superextensive gain; extensive-budget long-range-pair free gain; passive stable finite linear/nonlinear mediator free gain after energy accounting; linewidth narrowing as new integrated strength; metastable stored-energy avalanche as neutrino-energy gain; bounded finite-range k-local higher-body free superextensive gain; no actual-SM growing-coordination survivor in audited passive-SM scope.

## Highest-value executable frontier
**G9 / F3-F7 — source-centric finite-source lens-convolution sentinel authority.**

0090 remains immutable `BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS`. 0090a-r3 direct radial-source normalization and 0090b-r2 endpoint-regularized radial normalization are both immutable numerical BLOCKED results, not physical no-survivor results.

0090c is now immutable **`PASS_G9_SOURCE_CENTRIC_EXACT_MEASURE_AUTHORITY`**. By using source-centred coordinates `q=r^2/s^2, phi` with exact uniform-disk probability measure `dq*dphi/(2*pi)`, it removes the displaced-radius normalization bottleneck by construction across all 90 physical source geometries and 9 fixed controls.

The current frozen gate is 0090d, prereg commit `44a9f2d9a28d7169da6166eef0634df91121434a`, hosted execution head `1dbacc4cc41a557889e0677849d2fc1095399b3b`, run `34266454694`. It tests the actual finite-source accepted-area convolution on 81 prospectively fixed sentinels before any full 1350-grid scan.

## G9 authority front
- 0075 `BLOCKED_G9_PERSISTENT_GEOMETRY`.
- 0076 `SCIENTIFIC_FAIL_G9_GLOBAL_MULTIIMAGE_KERNEL`: scan-grid crossing detection missed narrow caustic preimages.
- 0077 `BLOCKED_G9_TURNING_POINT_KERNEL`.
- 0088 independent derivative locator exhausted; no physical no-go.
- 0089 `PASS_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY`.
- 0089a `BLOCKED_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION`.
- 0089b `PASS_G9_CONTINUOUS_PIECEWISE_LINEAR_PROJECTION_AUTHORITY`.
- 0089c `PASS_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION`.
- 0089d `BLOCKED_G9_CONTINUOUS_MAP_MONOTONE_KERNEL`.
- 0089e-r1 `INFRASTRUCTURE_FAIL_G9_0089E`.
- 0089e-r2 `PASS_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA`.
- 0090 `BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS`, immutable commit `51dd4e8a904163ba1746790658f53e50fc109b88`.
- 0090a-r1/r2 `INFRASTRUCTURE_FAIL_G9_0090A` before science.
- 0090a-r3 `BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE`, immutable record `861ca1c6af4bfe55a654701f9e1b259ffc3fab03`.
- 0090b-r1 `INFRASTRUCTURE_FAIL_G9_0090B` before authority payload.
- 0090b-r2 **`BLOCKED_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE`**, immutable record `bb71e27d31f784b2fb50d687ddf8074ad39fcd4a`.
- 0090c **`PASS_G9_SOURCE_CENTRIC_EXACT_MEASURE_AUTHORITY`**, immutable record `781b95d259f5ee2339e39167869e947547e3704b`.

### 0090b-r2 validated BLOCKED authority
Prereg `c46110eecf6fae9719d37f8f3a378206c2706324`; preflight-scope amendment `350ed2cb6da6485f230e429c0d35b18938d64e56`; execution head `cf9904f7a3c65601d13982c2e76b9cfd9fcd51f4`; run/job `34265645704/102194200480`; artifact `10071689978`; independently verified ZIP SHA256 `9c2ccebcdf24dd65780788ec39e1bda3ad6a8f251ee9a85acde72f322ce120d7`; inner JSON SHA256 `d442cea592cb5028374adf373e05ef40427fb8fb8cdea0a3a24c59b0a58dc04d`.

Classification is `BLOCKED_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE`, reason `endpoint-regularized normalization exceeds frozen threshold: external_d_over_s=1.1`. The fixed 32/64 orders may not be increased post hoc. No lens convolution or magnification was tested.

### 0090c validated PASS authority
Prereg `19245cf8a119e010ef161ebaeb4113a74d083158`; execution head `08469606889f29044a97f8b25fe8d796dd94b935`; run/job `34266104933/102195751262`; artifact `10071870838`; independently verified ZIP SHA256 `879e858a503849df690bf577faf8e3490bba9f0ca3018dbc6543d471e3652040`; inner JSON SHA256 `17e8a9390983fde216e9b2199f3aa800ed0c4f6ac92e769eef3663ea6557944a`.

Classification `PASS_G9_SOURCE_CENTRIC_EXACT_MEASURE_AUTHORITY`. It evaluated 9 dimensionless controls + 90 physical source geometries. Maximum identity error `1.1102230246251565e-16`, maximum L/H moment difference `1.1102230246251565e-16`, maximum geometry residual `4.440869091360169e-16`. This PASS validates only source probability measure/displacement geometry, not finite-source lens usefulness.

### Frozen 0090d finite-source sentinel gate
Prereg `44a9f2d9a28d7169da6166eef0634df91121434a`.

Shard across 3 observer controls x 3 receivers. Within every shard evaluate fixed theta indices `{0,12,24}` x centre offsets `{0,0.1,100} m`, total 81 rows.

Finite-source area is the exact-measure expectation

`Abar = integral dq dphi/(2*pi) A(u(q,phi);a)`,

where `A(u;a)` is the inherited root-split global signed-map `area_at_u` kernel and

`u=hypot(d+s*sqrt(q)*cos(phi), s*sqrt(q)*sin(phi))`.

L source replica is `8x16` with inherited `area_at_u` order 32; H is `16x32` with `area_at_u` order 64. Point-source and smallest-source aligned controls use 0.5%; every finite-source magnification-excess L/H pair must agree within 0.5%, or absolute `1e-10` in the tiny-excess branch. No adaptive/result-selected refinement and no radial normalization factor.

PASS only authorizes a separately preregistered full 1350-grid G9 scan. It does not itself provide final survivor authority.

## B-L external-authority front
0084b Shin-Yun analytical geometry and 0085 Wagner identity-free envelope remain PASS. 0074a/0074b response benchmarks remain PASS; 0074c combined likelihood remains BLOCKED. 0087/0087a topology is partial-authority only. 0087c Cerdeno, 0087d COHERENT mass support, 0087e finite-mass fifth-force, 0087f BBN-tail and 0087g restricted-below-1-eV completeness remain BLOCKED. BSM response/enhancement remains **LOCKED**.

## Other frontier classes
1. G3 universal short-range/contact residual: `OPEN_NOT_CURRENTLY_ACTIONABLE`.
2. G2 measured scalable topology rejection x bulk acceptance: `BLOCKED_NOT_ACTIONABLE`.
3. G8 Cu63 RIOEC normalization: `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`.
4. BSM external-envelope completeness: BLOCKED; response remains LOCKED.

## Exact next gate
Complete hosted 0090d run `34266454694` -> inspect all raw shards and aggregate -> independently verify artifacts/hashes -> strict preregistered classification. On PASS, prospectively freeze the full-grid finite-source survivor gate before calculating any of its 1350 rows. On BLOCKED, do not raise frozen source/b-integrator orders or relax 0.5%.

## Guards
No raster/manual contour reading. No generic dark-photon contour promoted to B-L absent exact mapping. No Majorana/Dirac union/intersection. No T/L union. No finite-mass extrapolation of 0079a. No arbitrary Yukawa threshold. No Wagner statistical-combination claim. No COHERENT benchmark interpolation. No lowering blocked-family criteria. No blocked-family-as-null assumption. No BSM response scan before dedicated completeness PASS and formal unlock. No post-hoc patch/promotion of 0077/0088/0089a/0089d/0090/0090a/0090b; no result-selected G9 nodes/orders/intervals/tolerances.

`NMIR_READINESS: 98%`.
