# NMIR prereg 0082c — Cerdeño B-L native axis calibration

Date frozen: 2026-09-08
Status: **PROSPECTIVE / NO 0082c VECTOR-PATH RESULT INSPECTED**
Parent: 0082b `BLOCKED_B_L_STELLAR_SN_VECTOR_AXIS_AUTHORITY`, with Cerdeño independently PASS for vector/axis sufficiency.

## Frozen authority
Use only Cerdeño et al. arXiv `2106.11660v3`, archive SHA256 `f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d`, asset `Figures/BL_constraints.pdf`, exact asset SHA256 `6557571159bd7d279e9b78e026c79c2974fd487db86dcf3f60b566e54318d07f`.

Source-native parameter semantics from 0082a are fixed as x = vector mediator mass `m_{Z'}` in GeV and y = `g_{B-L}`. No other paper's transform or coupling convention may be imported.

## Question
Can the exact vector PDF's fragmented powers-of-ten tick labels be deterministically reconstructed into physical x/y major-tick values and fit to independent log10 coordinate transforms with preregistered residual control?

## Frozen tick reconstruction
1. Use PyMuPDF source-native text spans only; no raster/OCR/manual point picking.
2. Axis association uses the same page-relative bands frozen in 0082b: x labels in bottom 22% / central 90%; y labels in left 22% / central 90%.
3. Reconstruct a power-of-ten major tick only when a base span `10` has one immediately adjacent superscript/exponent span on the same local text line. The exponent may be split into sign and digit spans; join only spans whose bounding boxes are geometrically adjacent to the upper-right of the base `10` and whose font size is smaller than the base font. Do not infer exponent sign from expected physics range.
4. Ordinary decimal major ticks may be used only if they occur on the same axis baseline as the reconstructed power ticks and are not legend/annotation text.
5. Require at least 4 distinct reconstructed major ticks per axis and at least 3 decades physical span per axis.

## Frozen calibration
For each axis independently fit
`log10(value) = a * coordinate + b`
using tick-center PDF coordinates.

Acceptance requires for x and y separately:
- max absolute ordinary residual <= `0.015 decade`;
- max absolute leave-one-out prediction residual <= `0.015 decade`;
- fitted slope sign consistent with monotonically increasing physical tick values along the source-native axis direction;
- no duplicate exponent assigned to geometrically distinct major ticks.

The calibration is independent per axis. No curve/path/color information may be read in 0082c.

## PASS/BLOCKED
`PASS_CERDENO_B_L_AXIS_CALIBRATION` iff both axes satisfy all reconstruction and fit conditions.

`BLOCKED_CERDENO_B_L_AXIS_CALIBRATION` if source-native text fragmentation is insufficient to recover >=4 signed major ticks on either axis under the frozen deterministic rules. This is not permission to borrow tick values from a raster/manual view.

Parser/dependency/network failure is infrastructure failure. A reproducible nonlinearity or contradictory axis semantics is `SCIENTIFIC_FAIL_CERDENO_B_L_AXIS_CALIBRATION`.

## Guards
No vector curve style/color selection, no contour extraction, no excluded-side assignment, no cross-paper conversion/union, no global envelope or BSM response scan.

## Next action
PASS -> prospectively preregister a separate 0082d source-own Cerdeño B-L curve semantic-identity + excluded-geometry gate using the frozen transform. BLOCKED/FAIL -> retire the Cerdeño vector geometry route and move to source-text analytical bounds/other 0071 families.

`NMIR_READINESS: 94%` until a new excluded region is materialized.
