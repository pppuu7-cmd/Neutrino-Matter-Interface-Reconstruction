# Iteration 0090a-r3 — radial-source-measure quadrature scientifically BLOCKED

Date: 2026-09-08
Parent prereg: `research/prereg/0090a_g9_radial_source_measure_quadrature_authority.md`, frozen commit `fb4aad7d1ffe23fb4863d09e26c0c3b20f47364c`.
Preflight amendment 2: `95281f6476daeec648ff5762bb2160392cec6fe0`.
Execution head: `c87b9b0ab241ff7b6c2f5b104e2ab90fff098d18`.
Run: `34259571174`.
Preflight job: `102173841087`.
Aggregate job: `102174309495`.
Aggregate artifact: `10069347381`.

## Classification
`BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE`.

This is a scientific numerical BLOCKED result under the prospectively frozen 0090a H1 criterion, not an infrastructure failure and not a physical no-survivor result. The preflight succeeded and all nine scientific shards executed. Every shard stopped at the same preregistered H1 condition before finite-source area rows: `radial source normalization exceeds frozen threshold`.

The frozen threshold remains `abs(integral p(u;s,d) du - 1) <= 2e-10` using the fixed H replica with Gauss-Legendre order 64 on the prospectively specified source intervals. No order, interval, tolerance, sentinel, source radius or offset was changed after the result.

## Raw Actions evidence
All jobs checked out exact head `c87b9b0ab241ff7b6c2f5b104e2ab90fff098d18` and contract `fb4aad7d1ffe23fb4863d09e26c0c3b20f47364c`.

Scientific shard jobs and payload SHA256 values:
- `(0,0)` job `102173925468`: inner JSON `dc589761bf56660834b56dd5577afbc399507831dc3f38cca2cadb57f0a11229`, artifact `10069317707`, ZIP SHA256 `2556371e06e9f14de6f53bba014d5b04d7fa2a154e21d7062b0daa9bc1fa74dc`.
- `(0,1)` job `102173925477`: inner JSON `470357930dbbc2347c5a79badd2dd596120bef79d9ae06b94a64e732b45839c2`, artifact `10069340453`, ZIP SHA256 `7fb72ea10ce8e5ff1cf913383ff44f3e96d816c70407bf872571b0fbbce875b3`.
- `(0,2)` job `102173925489`: inner JSON `0c5e6221fff8ad710abe773f4280e88c2c7d044f94ebd2330f6b5408e56e7b48`, artifact `10069318777`, ZIP SHA256 `9e3507716d33e96abfcb49f7a9a7c7848cb469b1e4fe515315fd5eff07754313`.
- `(1,0)` job `102173925499`: inner JSON `98e0bc5822189cc43249c893c79d7ed90b7497d9211cf7b4a24fb34968e1f23d`, artifact `10069310507`, ZIP SHA256 `7771b0c345b48250a3adaa6f7d423336da06613a2089b73ec0b7b4f9db55b314`.
- `(1,1)` job `102173925411`: inner JSON `ec9a6da92433ceba0ef0b1d46352445af1af8341b9bac35835a9708955944eef`, artifact `10069316111`, ZIP SHA256 `af775c6256b84dd4a637a2a0ebbbb21be542321399a98bdb1b481c0e8d5b572f`.
- `(1,2)` job `102173925384`: inner JSON `c1968317a9da949e84fa1a9369cd92dbce39fe56d84a6efa77a55205661cb5c8`, artifact `10069315574`, ZIP SHA256 `13f602b1dd8cb5fcdb2a4732543a4633eac1e389d94a5d96b1019b547cbda8a9`.
- `(2,0)` job `102173925414`: inner JSON `50baccd4eca30c19862ff2999491cc39dc83967b7d3f867dfc538dc929765213`, artifact `10069317263`, ZIP SHA256 `ae4232e0431cd7928340888d4d6b7f5b03aef94fafc3a108fbd87814efcb6911`.
- `(2,1)` job `102173925623`: inner JSON `2801fd5a943607160b0ae93302ac56fa1f49be5a7d9783bfc2d5f52387fe2a11`, artifact `10069312521`, ZIP SHA256 `959efd1a5605c0e0e6cae9e8b52ff8de0e3dc9f9c401b95b81738df1ebb4de39`.
- `(2,2)` job `102173925538`: inner JSON `ae303985b1fccc1589430b134521cfb10d2e1d725e8a3c5ecdb1996bf2117c3b`, artifact `10069316163`, ZIP SHA256 `cb3c8d312a6f56a62381c1de32bee196aa508f717aed98ce5b5e66c3d1fc5204`.

Aggregate raw payload:
- `status = BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE`
- `reason = at least one shard did not certify frozen radial quadrature`
- `shard_count = 9`
- status count `BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE: 9`
- aggregate inner JSON SHA256 `1667c471a0f02c88f25cb9e85e2d42d9d4a675db8cb4967619f1cd29bd417f8f`.

Because each shard raises on the first H1 normalization miss, the blocked payload intentionally contains no finite-source rows and the aggregate maxima are null. Therefore this execution does not quantify the largest normalization error and does not reach H2/H3 finite-source classification beyond the point-control code path.

## Independent aggregate artifact verification
Artifact `10069347381` was independently downloaded after the run.
- ZIP SHA256: `d626896f0641da052d7c63730d9b906cf7c09535b4f5c68a2934bc66b9be7c01`, exactly matching the Actions upload digest.
- inner `g9_0090a_result.json` SHA256: `1667c471a0f02c88f25cb9e85e2d42d9d4a675db8cb4967619f1cd29bd417f8f`, exactly matching the raw aggregate log.

## Interpretation
0090a answers its numerical-method question negatively in the frozen scope: direct fixed-order Gauss-Legendre integration in source radius `u` does not certify the exact displaced-disk radial measure to the preregistered `2e-10` normalization tolerance for the sentinel suite. This does **not** show that the displaced-disk formula is wrong, that the transparent-Sun lens has no finite-source survivor, or that 0090's physical class is excluded.

Inspection of the frozen implementation shows that H1 applies ordinary Gauss-Legendre directly to the partial-overlap `acos` radial-density representation. The fact that all shards stop at H1 motivates a mathematically different endpoint-regularized authority route, but no post-result refinement of 0090a is allowed.

## Next action
Do not rerun or weaken 0090a. Prospectively preregister a separate endpoint-regularized displaced-disk radial-measure gate before computing any new normalization or lens-convolution result. That gate must independently validate normalization and only then may authorize a later finite-source convolution method gate. Full 1350-point survivor scanning remains forbidden. BSM response/enhancement remains LOCKED.
