# Iteration 0090c — source-centric exact-measure authority PASS

Date: 2026-09-08
Parent prereg: `research/prereg/0090c_g9_source_centric_exact_measure_authority.md`, frozen commit `19245cf8a119e010ef161ebaeb4113a74d083158`.
Execution head: `08469606889f29044a97f8b25fe8d796dd94b935`.
Run: `34266104933`.
Job: `102195751262`.
Artifact: `10071870838` (`nmir-g9-0090c-source-centric-exact-measure`).

## Classification
`PASS_G9_SOURCE_CENTRIC_EXACT_MEASURE_AUTHORITY`.

The source-centred variables

`q=r^2/s^2`, `phi in [0,2*pi)`, `dP=dq*dphi/(2*pi)`

certify the uniformly bright displaced circular source without numerical normalization in displaced radius `u` or endpoint-regularized `t`.

## Frozen set and replicas
The hosted authority evaluated all preregistered objects:
- 9 fixed dimensionless displacement controls;
- 90 physical source geometries (`3 observer controls x 5 theta indices x 6 offsets`);
- L source replica `16 x 32` (`q x phi`);
- H source replica `32 x 64`.

Preflight was sanity-only and completed `3 passed`; all H1-H4 authority checks remained inside the scientific evaluator.

## Authoritative diagnostics
- `control_count = 9`
- `physical_count = 90`
- maximum absolute normalization/moment identity error: `1.1102230246251565e-16`
- maximum L/H moment disagreement: `1.1102230246251565e-16`
- maximum scale-normalized Cartesian/hypot geometry residual: `4.440869091360169e-16`
- all three reconstructed focal-distance drifts: `0.0`
- exact Model-S blob: `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`.

These are all comfortably below the prospectively frozen thresholds (`2e-14` identity/LH and `5e-15` geometry residual).

## Artifact integrity
Actions upload digest / independently downloaded ZIP SHA256:
`879e858a503849df690bf577faf8e3490bba9f0ca3018dbc6543d471e3652040`.

Inner `g9_0090c_result.json` SHA256 from hosted log / independent extraction:
`17e8a9390983fde216e9b2199f3aa800ed0c4f6ac92e769eef3663ea6557944a`.

Independent extraction reproduces the exact PASS status, contract `19245cf8a119e010ef161ebaeb4113a74d083158`, execution head `08469606889f29044a97f8b25fe8d796dd94b935`, counts and maxima above.

## Interpretation
0090c removes the source-probability normalization bottleneck that blocked 0090a and 0090b by using a probability measure normalized by construction. It validates source displacement geometry and uniform-disk measure only.

It does **not** validate a finite-source lens convolution, accepted image area, receiver gain, `mu_real`, `mu>=2` survivor, named-source realizability, duty cycle, detector/material response or BSM enhancement.

The PASS prospectively authorizes only a separately preregistered finite-source lens-convolution method using the `(q,phi)` measure and the already certified global signed lens map. The full 1350-point survivor scan remains forbidden until that method itself passes its own convergence/sentinel authority gate.
