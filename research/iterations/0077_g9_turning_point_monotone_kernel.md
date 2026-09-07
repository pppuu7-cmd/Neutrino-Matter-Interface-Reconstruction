# NMIR iteration 0077 — G9 turning-point / monotone-segment global radial kernel

Date: 2026-09-07
Prospective contract: `research/prereg/0077_g9_turning_point_monotone_kernel.md`, frozen commit `71c21236b1da1817d122567286c938ca6efcce6c`.
Implementation commits: `27793fd432716e2eb2149ff1fb185bb5288a4f4f`, `cc13fe57feae6e55e3f85532def3e6029a294bbc`, `01514027c775396396b469254b1b5b3ff2fb60f4`, workflow head `c5a09c8da671fd829144065f978cf71b7f3faf02`.

## Classification
**`BLOCKED_G9_TURNING_POINT_KERNEL`**.

This is not a physical falsification of transparent-Sun neutrino focusing and is not a scientific tolerance failure. Under the prospectively frozen 0077 method, the pinned Model-S signed radial map contains an unresolved derivative sign reversal inside a segment that the scan-bracketed turning-point construction had classified as monotone. The preregistration explicitly requires this condition to be BLOCKED rather than silently subdividing with result-selected nodes.

## Hosted authority
- workflow: `NMIR G9 turning-point monotone kernel`
- run: `34153760956`
- job: `101841193992`
- head: `c5a09c8da671fd829144065f978cf71b7f3faf02`
- dedicated regression tests: `5 passed in 0.02s`
- artifact: `10030249765`, `nmir-g9-0077-result`
- artifact ZIP SHA256: `f9873870bbf8f615366c18fef9edb56d4b907148f2d6d60dff70d60a0b096620`
- raw result JSON SHA256: `0091ee87c1a331847737d01878ef3629e39ff5e7e07ca4b322bd37e3cb466a76`
- pinned Model-S Git blob: `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`

Raw machine result is persisted at `data/g9_turning_kernel_result_0077.json`.

## What passed before the block
The implementation itself passed five dedicated toy/regression tests covering derivative evaluation, an analytic turning point, monotone partitioning, recovery of multiple zero preimages, two disjoint accepted preimages, annular-area accounting and half-step stability on the toy model. The hosted workflow therefore reached the real pinned Model-S benchmark.

## Exact blocker
The real benchmark stopped fail-closed with:

`unresolved derivative sign reversal in monotonicity audit`

No root/area/grid/receiver tolerance was weakened. No result-selected grid nodes were inserted. The benchmark did not proceed to claim a physical aperture magnification after this ambiguity.

## Scientific consequence
0076 showed that scan-grid crossing detection is not sufficiently grid-independent near radial caustics. 0077 then showed that the prospectively frozen sign-reversal turning-point bracketing plus 9-point monotonicity audit still does not uniquely partition the pinned map without an additional numerical/physical assumption. Therefore this specific persistent-source numerical geometry route is closed at 0077 under its frozen decision tree.

This does **not** imply that gravitational focusing is absent. The already closed 0061 result for the 10-kpc Galactic CCSN case remains valid in its own scope. It does mean that NMIR may not reopen finite-source persistent-source convolution from 0077, because only `PASS_G9_TURNING_POINT_MONOTONE_KERNEL` was authorized to do that.

## Next action
Per the frozen 0077 decision tree, return to other funnel survivors. Do not patch the 0077 turning-point grid post hoc and do not relax the 0.5% criteria. Priority becomes an external-authority audit for currently blocked survivors (G2/G8/BSM) to determine whether genuinely new primary data now make any of them executable.

## Readiness
`NMIR_READINESS: 91%` (unchanged). The blocker closes a method branch but does not earn a new positive readiness point.
