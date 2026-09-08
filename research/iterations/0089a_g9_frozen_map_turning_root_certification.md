# NMIR iteration 0089a — G9 frozen-map turning-root certification

Date: 2026-09-08
Scientific preregistration: `research/prereg/0089a_g9_frozen_map_turning_root_certification.md`, frozen commit `e350cd19beec7c9d3ca9f43a439337ef9e88a099`.
Runtime conformance amendment: `research/amendments/0089a_runtime_replica_pypy_conformance.md`.

## Terminal classification
`BLOCKED_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION`

Reason, identically reported by both hosted runtime replicas:
`unstable knot-boundary orientation`.

This is a numerical-map/root-certification blocker, not a physical no-go and not a detector/BSM result. The frozen source-knot one-sided derivative-sign semantics failed to stabilize across the preregistered offsets. Therefore no turning-root set, caustic partition, `y=+-r` boundary, annular area, magnification, one-ring control, finite-source convolution, persistent-source convolution or BSM quantity is promoted from 0089a.

## Frozen source authority
- Model-S commit: `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`
- Model-S git blob SHA1: `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`
- Exact 0089 derivative authority remains separately PASS and unchanged.

## CPython authoritative replica
- hosted run: `34209664773`
- job: `102007385687`
- head: `bc7c493203cefa87a3b6cb384cf2baa724a884d6`
- artifact: `10049541112`, `nmir-g9-0089a-root-certification`
- artifact ZIP SHA256: `178cbac01d152f1374a60187862e753bc14051077fbee06e1879040b60d903b5`
- inner `g9_0089a_result.json` SHA256: `b27ca27f317154918c53011074e07122f19060795f6e639461a33553d15c8f64`
- workflow conclusion: success because preregistered BLOCKED is a valid fail-closed scientific-route outcome; green workflow is not itself a scientific PASS.

Raw JSON fields:
- status: `BLOCKED_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION`
- reason: `unstable knot-boundary orientation`
- contract commit: `e350cd19beec7c9d3ca9f43a439337ef9e88a099`
- Model-S blob: exact expected value above.

## PyPy runtime-conformance replica
Frozen before any 0089a Model-S root positions, derivative signs, boundary turns or scientific classification were observed.

- hosted run: `34210222751`
- job: `102009184130`
- head: `960119f94280da2af808fb382d3c93917d669fca`
- runtime: PyPy 7.3.19 / Python 3.10.16
- dedicated tests: `6 passed in 0.31s`
- artifact: `10049484438`, `nmir-g9-0089a-root-certification-pypy-replica`
- independently downloaded artifact ZIP SHA256: `6d5206211da0c53953cd534747571cada91f60023569a908409eee143afc1ea2`
- inner `g9_0089a_result.json` SHA256: `974230e4a82b29d4a3550dbf6c3bce37990aec2358a8126cbefe37af82837306`
- raw job log was inspected and independently confirms the same terminal JSON classification/reason and exact Model-S blob.

## Runtime-conformance result
PASS for runtime conformance of the terminal classification: CPython and PyPy agree on status, reason, scientific contract and source blob. No runtime-dependent scientific discrepancy exists to adjudicate.

## Interpretation
0089 remains valuable: it proved an exact analytic derivative of the *frozen discrete trapezoidal map* away from source knots. 0089a shows that this does not suffice for a global turning partition because the moving-point trapezoidal representation creates unresolved source-knot one-sided orientation behavior under the already frozen source-boundary audit.

Per preregistration, 0089a is closed. Do not change the knot offsets, threshold, root grids or confirmation scales to rescue it. A new route must use a genuinely different prospectively registered numerical representation rather than a post-hoc patch.

## Successor
0089b was independently prospectively registered before inspecting any offending-knot identity/root position/turn list. It tests an exact continuous piecewise-linear projection of the same frozen Model-S density semantics, eliminating the moving-point trapezoidal source-knot cusp mechanism without changing the source density interpolation or solar physics.
