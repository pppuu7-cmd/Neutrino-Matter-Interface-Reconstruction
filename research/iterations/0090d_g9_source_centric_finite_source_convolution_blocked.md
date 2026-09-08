# Iteration 0090d — G9 source-centric finite-source convolution BLOCKED

Date: 2026-09-08
Classification: `BLOCKED_G9_SOURCE_CENTRIC_FINITE_SOURCE_CONVOLUTION`

## Frozen contract
Preregistration: `research/prereg/0090d_g9_source_centric_finite_source_sentinel_authority.md`.
Prospective prereg commit: `44a9f2d9a28d7169da6166eef0634df91121434a`.
Execution head: `1dbacc4cc41a557889e0677849d2fc1095399b3b`.
Parent authority: 0090c `PASS_G9_SOURCE_CENTRIC_EXACT_MEASURE_AUTHORITY`.

0090d tested only the prospectively fixed 81 finite-source sentinels: 3 observer controls x 3 receiver radii x 3 source-angle indices x 3 source-centre offsets. It was not the full 1350-point scan.

## Hosted authority
- workflow run: `34266454694`
- aggregate job: `102198812236`
- aggregate artifact: `10072221310`
- independently verified ZIP SHA256: `baf1646ab36bd2dec0fefc2ff42fb9a716accc2eb1c1c1ca9649860098b794b1`
- independently verified inner `g9_0090d_result.json` SHA256: `6b0b3982c7db46c44ebf7fd864c918818efab33e8806c5716af8aa7fd37b5877`
- aggregate `shard_count=9`, `pair_count=9`, `row_count=0`
- `status_counts={BLOCKED_G9_SOURCE_CENTRIC_FINITE_SOURCE_CONVOLUTION: 9}`

All nine scientific shard jobs completed and produced scientific payloads. There was no infrastructure failure and no accepted-area/map invariant failure.

## Frozen misses
Every shard stopped on the first H2 source-centric finite-source L/H convergence miss, so no completed finite-source rows are authoritative beyond the diagnostic failure location.

Receiver index 0 (1 m) blocked at `theta_index=12, delta_m=0` for all three observer controls:
- control 0: `0.014072385354422401`
- control 1: `0.014126649239951444`
- control 2: `0.014161143991306909`

Receiver indices 1 and 2 (10 m and 100 m) blocked at `theta_index=24, delta_m=0`:
- control 0: `0.051046769854536059` / `0.051046816868522533`
- control 1: `0.049125159482200878` / `0.049125387386591633`
- control 2: `0.04562782712174894` / `0.045627300977202988`

Frozen limit in every case was `0.005`.

## Interpretation
0090c already proved that the source-centric `(q,phi)` probability measure itself is normalized and geometrically sound to near floating-point precision. Therefore 0090d isolates a later numerical bottleneck: the fixed tensor-product source quadrature `8x16 / 16x32` combined with inherited `area_at_u` `32/64` does not reproduce the finite-source lens convolution to the preregistered 0.5% criterion on the fixed sentinel set.

This is a method BLOCKED result, not a physical no-go, not a zero-survivor result, and not evidence that solar neutrino focusing is absent. `row_count=0` means each shard aborted at its first prospectively defined convergence miss.

The frozen 0090d orders and tolerances must not be raised or relaxed post-result.

## Next admissible step
Use an independent integration formulation rather than refining 0090d. Highest-value candidate: exchange the source/ray integration order and evaluate, for each incident ray, the exact overlap area of the finite source disk with the receiver-acceptance disk in the source plane. This removes explicit source-point quadrature and must be prospectively preregistered as a new gate before any numerical result is inspected.

No full 1350-point G9 scan is authorized by 0090d. BSM response/enhancement remains locked.
