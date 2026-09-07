# NMIR iteration 0082c — Cerdeño B-L source-native axis calibration

Date: 2026-09-08
Parent: `research/prereg/0082c_cerdeno_bl_axis_calibration.md`
Implementation-conformance amendment: `research/amendments/0082c_parser_conformance_correction.md`
Final authoritative classification: **BLOCKED_CERDENO_B_L_AXIS_CALIBRATION**
`NMIR_READINESS: 94%`

## Scientific question
Can the exact source-native vector PDF `Figures/BL_constraints.pdf` from Cerdeño et al. `2106.11660v3` provide enough PyMuPDF text-span authority to reconstruct both logarithmic axes under the frozen no-raster/no-manual contract and thereby authorize later vector contour extraction?

Frozen archive SHA256: `f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d`.
Frozen asset SHA256: `6557571159bd7d279e9b78e026c79c2974fd487db86dcf3f60b566e54318d07f`.

## Historical first implementation — not scientific authority
Hosted run `34168121697`, job `101883111550`, artifact `10034819460` produced the string `SCIENTIFIC_FAIL_CERDENO_B_L_AXIS_CALIBRATION`, but the executable parser did not conform to the preregistered text rules: isolated exponent digits were admitted as ordinary decimal ticks and fragmented powers required PyMuPDF internal block/line equality rather than the frozen geometric local-line criterion.

This run is retained as **INFRASTRUCTURE_FAIL_PARSER_CONFORMANCE**. It is not a physical/scientific failure and is not used to retire the source.

Artifact ZIP digest reported by GitHub: `sha256:38a821eb6eafdf4de0e8db38338f3289248904677190373297f5b6e067115238`.

## Conformance rerun 0082c-r1
The parser-conformance amendment preserved all scientific inputs, tolerances, guards and PASS/BLOCKED/FAIL consequences. It forbade raster/OCR/manual sign recovery and curve/path/color information.

Authoritative hosted provenance:
- run: `34168779858`
- job: `101884961619`
- head commit: `36bdb70707e2d4970a75ce52bc25c1098b23d0af`
- artifact: `10035019993`
- GitHub artifact ZIP digest: `sha256:8dc01a9c97a765563c24089ac538cdb30dffd3b49b5a04c9727510a8f6c6093a`
- raw JSON SHA256: `0f5026982a4a88990a39c07908fc64a978511e946ea572d3b49dc61070b09d03`

Dedicated regression tests passed. The audit itself completed and uploaded a machine-readable result; the workflow was red only because the frozen fail-closed enforcement rejects any non-PASS scientific classification.

## Raw result
Overall: `BLOCKED_CERDENO_B_L_AXIS_CALIBRATION`.

The decisive frozen blocker is the y axis:
- `tick_count = 0`
- `span_decades = 0`
- reason: `fewer_than_4_ticks`

Thus the source-native text-span representation is insufficient to recover the required >=4 signed major ticks on both axes. This directly satisfies the preregistered `BLOCKED` condition.

The x-axis diagnostic is not promoted to a scientific calibration claim: its provisional candidate set contains residual ordinary-decimal/exponent-fragment ambiguity and fails the frozen residual/sign conditions. Because the y-axis insufficiency already independently triggers `BLOCKED`, no post-result parser tuning is scientifically necessary or permitted to rescue the vector route.

## Consequence
The Cerdeño **vector-geometry contour route is retired under the frozen source-native-text/no-raster contract**. No Cerdeño stellar/SN excluded polygon, contour area, excluded side, cross-paper union, global B-L envelope increment or BSM response scan is authorized by 0082c.

This is not a statement that the published Cerdeño plot is physically invalid. It is an authority/reproducibility blocker: the exact source asset does not expose enough text-span information to reconstruct both logarithmic axes under the predeclared deterministic rules without importing manual/raster/path knowledge.

## Exact next route
Per the parent preregistration, move to **primary-source analytical/text bounds or another missing 0071 constraint family**. The highest-value next branch is a source-text authority audit of the young-neutron-star / SN B-L literature already frozen in 0082/0082a, beginning with explicit analytical bounds that can be materialized without raster contour reading. Any numerical geometry/materialization must receive a new prospective contract before computation.

## Guards carried forward
No raster/manual contour reading. No sign recovery from visual inspection or vector minus strokes. No cross-paper coupling conversion/union without source authority. No blanket Hong/Cerdeño/Shin-Yun supersession. No finite-mass extension of the 0079a fifth-force asymptote. No BSM response enhancement scan until the external constraint envelope is sufficiently authority-complete and separately unlocked.
