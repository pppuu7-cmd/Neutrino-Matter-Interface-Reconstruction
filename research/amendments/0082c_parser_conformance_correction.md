# NMIR 0082c post-run implementation-conformance correction

Date: 2026-09-08
Status: **INFRASTRUCTURE/PARSER CORRECTION ONLY; FROZEN SCIENTIFIC CONTRACT UNCHANGED**
Parent preregistration: `research/prereg/0082c_cerdeno_bl_axis_calibration.md`.
Affected historical run: `34168121697`, job `101883111550`, artifact `10034819460`.

## Why the first 0082c run is not scientific authority
The first hosted implementation produced `SCIENTIFIC_FAIL_CERDENO_B_L_AXIS_CALIBRATION`, but inspection of its raw JSON shows that the executable parser did not faithfully implement the frozen preregistration:

1. `ordinary_decimal_ticks()` accepted every positive numeric span in the broad axis band. This reused isolated exponent digits such as `1`, `2`, `3`, `4`, `5` as independent decimal major ticks, despite the frozen rule that ordinary decimals are admissible only on the same axis baseline as reconstructed power ticks and must not be annotation/exponent text.
2. fragmented `10` + exponent reconstruction required identical PyMuPDF `block` and `line` IDs. The preregistration instead froze a **geometric local-text-line** criterion; internal parser line IDs were never part of the scientific contract.
3. the broad bottom/left bands overlap at the lower-left corner, so a deterministic common-baseline/axis-column clustering step is required to prevent a y-axis power label from contaminating the x-axis set and vice versa. This is an implementation of axis association, not a new scientific acceptance condition.

Therefore run `34168121697` is retained as a historical **INFRASTRUCTURE_FAIL_PARSER_CONFORMANCE**. Its numerical `SCIENTIFIC_FAIL_*` string is not promoted to scientific authority.

## Frozen conformance repair for 0082c-r1
The rerun must preserve every scientific input, tolerance and PASS/BLOCKED/FAIL consequence from the parent preregistration. The only permitted changes are parser-conformance repairs:

- reconstruct fragmented powers from source-native PyMuPDF text spans using upper-right geometric adjacency and smaller exponent font, without requiring equal PyMuPDF block/line IDs;
- form x/y tick sets from the same frozen page-relative bands, then select the dominant common x-baseline / y-column cluster using only text-span geometry; no curve/path/color information may enter;
- exclude all spans already consumed as a power-of-ten label from the ordinary-decimal candidate pool;
- admit an ordinary decimal only when it lies on the selected axis baseline/column within the frozen implementation tolerance;
- if the text-span inventory yields an axis-direction contradiction while the needed sign is not represented in the source-native exponent spans, classify that axis as **BLOCKED by sign/text fragmentation**, not as a physical/scientific contradiction. No sign may be recovered from raster inspection, OCR, vector minus strokes, expected physics range, another paper, or manual reading.

Frozen numerical acceptance remains exactly: >=4 distinct major ticks and >=3 decades per axis; ordinary and leave-one-out residual <=0.015 decade; correct slope direction; no duplicate exponent at distinct major ticks.

## Guards
This correction does not authorize raster/manual tick recovery, vector-path sign recovery, contour/color/curve inspection, excluded-side assignment, cross-paper transforms/unions, global B-L envelope construction, or BSM response calculations.

`NMIR_READINESS` remains 94% until a valid scientific gate is classified.
