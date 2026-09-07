# Preregistration 0078b — De Romeri et al. combined solar-CEvNS B-L vector calibration

Date frozen: 2026-09-07
Parent PASS: 0078a `PASS_PRIMARY_B_L_VECTOR_ASSET_INTEGRITY`, run/job `34154515131/101843445080`, head `26c688123994e4dc832a929f7311472daee7dd46`.
Primary tick/semantic authority frozen before path classification: `data/deromeri_2603_bl_combined_tick_authority_0078b.json`, commit `46eb02ec29a7e88aa1971009ee0ef4472cd2d19f`.

## Frozen source

- arXiv `2603.00554` source archive SHA256 `09ab22f753ac3f5fbde5be65ac50926de67b0638550366d158aadcfde8e92564`;
- asset `vector_BL_PnX_XnT_LZ_combined.pdf` SHA256 `ace761499623535907263e780a6e96a17474adf418d3f9363dae8e28bc5e7a39`;
- source TeX semantic identity: right panel = vector `B-L`; magenta shaded region = combined XENONnT + PandaX-4T + LZ 90% CL solar-CEvNS exclusion.

Frozen machine-extracted text gives:
- x-axis `m_V [GeV]`, ticks `log10(m_V/GeV) = -5,-4,-3,-2,-1,0,1`;
- y-axis `g_B-L`, ticks `log10(g_B-L) = -8,-7,-6,-5,-4,-3,-2`;
- combined label `PnX + XnT + LZ (CEvNS)`.

## Scientific question

Can the primary combined solar-CEvNS `B-L` exclusion be calibrated reproducibly from the publication's vector PDF in a common `(m_V, g_BL)` convention without raster/manual reading or post-result curve identity assignment?

## Frozen sequence

### Stage A — text-coordinate calibration, before path colors

1. Extract page words with PDF user-space bounding boxes.
2. Normalize superscript/minus text such that powers rendered as `10-5 ... 101` are eligible tick labels.
3. Numeric tick candidates are words matching `10` followed only by an optional minus and decimal digits.
4. Identify the x-axis row as the unique seven-candidate subset with strictly increasing x centers, y-center range <= 0.02 page height and spanning >= 0.45 page width.
5. Identify the y-axis column from remaining candidates as the unique seven-candidate subset with strictly monotone y centers, x-right-edge range <= 0.03 page width and spanning >= 0.45 page height.
6. Associate the frozen x exponents `[-5,-4,-3,-2,-1,0,1]` in increasing x order. Associate frozen y exponents `[-8,-7,-6,-5,-4,-3,-2]` from bottom to top in physical value order, allowing PDF y direction to be inferred from the ordered coordinates.
7. Fit affine maps from PDF coordinate to each logarithmic exponent. Require max absolute residual <= 0.015 decade on each axis and leave-one-out predicted tick residual <= 0.03 decade for every tick.

No vector drawing colors or candidate contour coordinates may be inspected before Stage A passes.

### Stage B — frozen magenta vector class

After Stage A PASS, enumerate all vector drawings from the same asset. Convert stroke/fill RGB to HSV. A drawing belongs to the preregistered magenta class iff at least one painted stroke/fill color has:
- hue in `[285 deg, 345 deg]`;
- saturation `>= 0.35`;
- value `>= 0.35`.

No result-dependent RGB matching is allowed. Retain only magenta drawings containing at least two path-construction points whose calibrated coordinates lie within the frozen plot domain with a 0.05-decade numerical margin.

### Stage C — combined-contour structural checks

1. Convert all retained magenta path points through the Stage-A calibration.
2. Require all retained scientific points to be finite and within the plot domain plus the 0.05-decade margin.
3. Require at least one retained magenta drawing to span >= 2.0 decades in `m_V` or >= 1.0 decade in `g_BL`; this rejects legend swatches and tiny annotations.
4. A candidate scientific contour may consist of multiple disconnected primary paths because the source caption says `excluded regions` (plural). Paths are not joined across gaps.
5. Round-trip every calibrated point back to PDF user-space using the fitted affine maps; require max normalized page-coordinate discrepancy <= `1e-10` for the transform itself.

0078b does **not** yet build a global envelope with external constraints and does not infer the excluded-side topology. It only certifies the combined magenta solar-CEvNS B-L vector path(s) in physical coordinates.

## Prospective classifications

- `PASS_COMBINED_SOLAR_CEVNS_B_L_VECTOR_CALIBRATION`: Stage A passes, a nontrivial frozen-magenta scientific path family passes Stage B/C, and physical-coordinate output is machine reproducible.
- `PARTIAL_B_L_VECTOR_CALIBRATION`: axes calibrate but scientific magenta paths cannot be separated from non-scientific magenta objects under the frozen class without another assumption.
- `SCIENTIFIC_FAIL_B_L_VECTOR_CALIBRATION`: primary axis/tick geometry or frozen path integrity criterion fails after successful source access.
- `INFRASTRUCTURE_FAIL`: source/package/runtime failure before scientific classification.

## Decision tree

PASS -> 0078 qualifies as `PASS_NEW_EXECUTABLE_SURVIVOR_BSM` for this **new combined solar-CEvNS B-L constraint family only**. Then preregister 0078c to determine excluded-side topology and combine this family with already materialized primary constraints; no B-L enhancement/response scan until a reproducible external envelope is frozen.

PARTIAL/FAIL -> retain 0078 as partial external authority and do not manually read/digitize the plot.
