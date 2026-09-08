# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-08
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Protocol: `research/RECOVERY_MANUAL.md`
Funnel: `research/NMIR_FUNNEL.md`
Latest completed immutable scientific record: `research/iterations/0090a_r3_g9_radial_source_measure_blocked.md`, record commit **`861ca1c6af4bfe55a654701f9e1b259ffc3fab03`**, classification **`BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE`**.
Current prospectively frozen scientific gate: `research/prereg/0090b_g9_endpoint_regularized_radial_measure_authority.md`, frozen commit **`c46110eecf6fae9719d37f8f3a378206c2706324`**.
`NMIR_READINESS: 98%`.

## Mandatory recovery order
Read `RECOVERY_MANUAL.md` -> this file -> `NMIR_FUNNEL.md` -> newest numbered iterations/preregs/amendments -> commits newer than this reconciliation -> relevant queued/in-progress/newly-terminal Actions. Repository and independently validated Actions artifacts are authority; green CI alone is never scientific PASS.

## Frozen mission / accounting
Separate focusing/state control, microscopic interaction probability, detector visibility/amplification and irreversible neutrino-supplied deposited energy. Event gain != interaction gain != neutrino-energy gain. Never multiply unvalidated gains. Stored free energy, pumping, preparation and reset work are not neutrino-supplied power.

## Stable non-BSM frontiers
- G2: 0063 `BLOCKED_NOT_ACTIONABLE` pending same-configuration measured sub-keV rejection x bulk-NR acceptance.
- G3: 0065 universal short-range/contact coefficient `OPEN_NOT_CURRENTLY_ACTIONABLE`.
- G8: 0068 `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`.

## G9 authority chain
- 0075 `BLOCKED_G9_PERSISTENT_GEOMETRY`.
- 0076 `SCIENTIFIC_FAIL_G9_GLOBAL_MULTIIMAGE_KERNEL`: scan-grid crossing detection missed narrow caustic preimages.
- 0077 `BLOCKED_G9_TURNING_POINT_KERNEL`.
- 0088 independent derivative locator exhausted; no physical no-go.
- 0089 `PASS_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY`.
- 0089a `BLOCKED_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION`.
- 0089b `PASS_G9_CONTINUOUS_PIECEWISE_LINEAR_PROJECTION_AUTHORITY`.
- 0089c `PASS_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION`.
- 0089d `BLOCKED_G9_CONTINUOUS_MAP_MONOTONE_KERNEL`: fixed midpoint meshes cannot resolve a finite narrow accepted interval.
- 0089e-r1 `INFRASTRUCTURE_FAIL_G9_0089E`.
- 0089e-r2 **`PASS_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA`**.
- 0090 **`BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS`**: frozen 2-D source quadrature/Simpson method cannot certify finite-source convolution; not a physical no-survivor result.
- 0090a-r1/r2 **`INFRASTRUCTURE_FAIL_G9_0090A`**: both stopped in non-scientific preflight before any scientific shard.
- 0090a-r3 **`BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE`**: preflight passed, all nine scientific shards executed, and every shard failed the unchanged H1 radial-normalization criterion before finite-source area rows.

## 0089e-r2 validated geometry authority
Prereg `da8e7c5664cf0980b3490926036231bea9270fcb`; execution head `466f6fee04f6052e4c758cb613290f33610373e8`; run/job `34227872401/102066360966`; artifact `10061342281`; ZIP SHA256 `d76b3937a9ea0fcced50769c8098642b96e1345dd1f5b77bbd1754f53c104bb3`; inner JSON SHA256 `010a9f55c11c9bb7c7020293f2ebef9ce3e00b4dc8401ade700a417c327ba56e`.

Interpretation: mesh-free continuous radial geometry only; no finite-source usefulness, detector/material or BSM claim.

## 0090 authoritative result
Prereg `cf8ffbcca69477939430272777f573d94e4b1e24`; point-control amendment `f4d6538c551d724949089435707137d7155fd6ed`; head `48b9313aa10fd13f63ed7b3b2c98d0ac12428ff6`; run/aggregate job `34241211305/102112686829`; artifact `10062169885`; ZIP SHA256 `607220c60161046caf2ac36e4bbd9be487e756a34624c6931f7ce6a558e909bb`; inner JSON SHA256 `1dfdf40a86cf099d32c278a0bb963b7f4f55f8b852fd2637ffbe38b1d2303326`.

All 9 shards returned the preregistered numerical BLOCKED class. Raw failures include source 12x24 vs 24x48 final-excess disagreement >0.5% and composite-Simpson non-convergence to `1e-8` by 4096 panels. Aggregate `row_count=0/1350`; this is not a zero-survivor count.

## 0090a-r3 authoritative result
Parent prereg **`fb4aad7d1ffe23fb4863d09e26c0c3b20f47364c`**. Preflight-only amendment 2 **`95281f6476daeec648ff5762bb2160392cec6fe0`** removed no scientific requirement. Scientific execution head **`c87b9b0ab241ff7b6c2f5b104e2ab90fff098d18`**.

Hosted authority:
- run **`34259571174`**
- preflight job `102173841087` success
- nine scientific shard jobs: `102173925468`, `102173925477`, `102173925489`, `102173925499`, `102173925411`, `102173925384`, `102173925414`, `102173925623`, `102173925538`
- aggregate job **`102174309495`**
- aggregate artifact **`10069347381`**
- independently verified aggregate ZIP SHA256 **`d626896f0641da052d7c63730d9b906cf7c09535b4f5c68a2934bc66b9be7c01`**
- independently verified inner `g9_0090a_result.json` SHA256 **`1667c471a0f02c88f25cb9e85e2d42d9d4a675db8cb4967619f1cd29bd417f8f`**.

Every raw shard payload has exact contract `fb4aad7d...`, exact head `c87b9b0...`, status `BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE`, reason `radial source normalization exceeds frozen threshold`. Aggregate has `shard_count=9`, `status_counts={BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE:9}`. Because the frozen script raises on the first H1 miss, no finite-source rows are produced and H2 cannot be promoted or inferred. The result strictly says that direct fixed-order Gauss-Legendre integration in source radius `u` failed to certify the displaced-disk radial measure to `2e-10` on the frozen sentinel experiment. It does not invalidate the exact geometric measure or the physical focusing class.

Immutable result note: `research/iterations/0090a_r3_g9_radial_source_measure_blocked.md`, record commit `861ca1c6af4bfe55a654701f9e1b259ffc3fab03`.

## Current 0090b prospective front
Frozen prereg **`c46110eecf6fae9719d37f8f3a378206c2706324`** asks a narrower independent question: certify the displaced-disk radial measure using an endpoint-regularized variable, without direct numerical GL integration of `p(u)` in `u` and without any lens accepted-area calculation.

For `d>0`, freeze

`u(t)=sqrt(d^2+s^2-2*d*s*cos(t)), 0<=t<=pi`,

so `du/dt=d*s*sin(t)/u`, and evaluate

`N_partial = d/(pi*s) * integral_0^pi Omega(u(t);s,d)*sin(t) dt`.

For `d<s`, add the analytic full-ring contribution `N_full=(s-d)^2/s^2`; for `d>=s`, `N_full=0`; for `d=0`, normalization is analytic. Fixed replicas remain GL orders 32 and 64 in `t`; no adaptive/result-selected refinement. The physical set is the 90 unique source geometries inherited uniformly from 0090a (3 controls x 5 theta indices x 6 offsets), plus fixed analytic/scale controls. Both L and H must satisfy normalization `<=2e-10`, replica agreement `<=2e-10`, and fixed dimensionless scale replicas `<=2e-12`.

PASS 0090b authorizes only a separately preregistered finite-source lens-convolution method gate. It cannot produce `mu_real`, a survivor, a named-source claim or a full 1350 scan.

## BSM / B-L authority
0069 unlocks only the constraints ledger. BSM response/enhancement remains **LOCKED** pending reproducible external-envelope completeness + formal unlock. 0084b Shin-Yun and 0085 Wagner remain PASS. 0074a/0074b detector response benchmarks remain PASS; 0074c combined-likelihood numerical benchmark remains BLOCKED. 0087/0087a are partial topology authority only; 0087c Cerdeno, 0087d COHERENT mass support, 0087e finite-mass fifth-force, 0087f BBN tail and 0087g restricted-below-1-eV completeness remain BLOCKED.

## Exact next action
Implement 0090b strictly from prereg `c46110eec...`: endpoint-regularized normalization only -> dedicated tests -> hosted reproducibility artifact -> raw log + independent artifact/hash inspection. Do not rerun 0090a, do not increase its orders, and do not start a finite-source or 1350-point lens scan before a separately frozen post-0090b gate.

## Critical guards
No raster/manual contour reading. No generic dark-photon contour promoted to B-L absent exact mapping. No Majorana/Dirac union/intersection. No T/L union. No finite-mass extrapolation of 0079a. No arbitrary Yukawa threshold. No Wagner statistical-combination claim. No COHERENT benchmark interpolation. No lowering blocked-family criteria. No blocked-family-as-null assumption. No BSM response scan before dedicated completeness PASS and formal unlock. No post-hoc patch/promotion of 0077/0088/0089a/0089d/0090/0090a; no result-selected G9 nodes/orders/intervals/tolerances.
