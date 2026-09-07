# NMIR prereg 0081a — B-L BBN vector calibration and semantic identity

Date frozen: 2026-09-08
Status: **PROSPECTIVE / NO 0081a VECTOR RESULT INSPECTED**
Parent scientific gate: 0081 `PASS_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS`.

## Question
Can the primary vector-native BBN assets `Presentation/CnstrntPlotMajoranaYp.pdf` and `Presentation/CnstrntPlotDiracYp.pdf` be mapped reproducibly to the same physical `(m_X,g_X)` coordinates and can the vector style/path corresponding specifically to the present-observation BBN criterion `Delta Y_p = 0.008` be identified from source-native semantics without raster/manual digitization or post-hoc color selection?

## Frozen source/provenance
Use only Esseili–Kribs arXiv `2308.07955v2`, source archive SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`, and files inside that exact archive. Primary TeX SHA256 remains `f77b577688b3609c574985b05fc9a213709c958ded60a511478357f1f881d678`.

Controlling assets are exactly:
- Majorana: `Presentation/CnstrntPlotMajoranaYp.pdf`
- Dirac: `Presentation/CnstrntPlotDiracYp.pdf`

No screenshots, raster OCR, manual point picking, external re-rendering or later-version figures are permitted.

## Frozen semantic authority from 0081
The observational BBN criterion is the conservative **signed** `Delta Y_p = Y_p(BSM)-Y_p(SM) = 0.008` at **95% C.L.**. Figure 7 is Majorana; Figure 8 has the same BBN semantics for Dirac. CMB dashed-red overlays are not BBN authority and must not be substituted.

## Frozen calibration requirements
1. Recover both x/y physical axis transforms from source-native vector tick labels/geometry independently for Majorana and Dirac BBN assets.
2. Axes are expected to represent mediator mass and coupling, but no unit or log-base convention may be imported from CMB assets unless identity is independently established in these BBN PDFs.
3. Fit each linear log-coordinate transform from >=4 distinct major tick anchors per axis when available.
4. Ordinary maximum anchor residual must be <= `0.015 decade` and leave-one-out maximum prediction residual <= `0.015 decade` for every independently calibrated axis. If the native asset does not expose enough anchors to meet this contract, classify BLOCKED rather than borrowing CMB calibration.
5. Majorana-vs-Dirac recovered transforms must agree to <= `0.015 decade` at every common major tick. Failure is scientific/calibration FAIL unless source metadata proves intentionally different axes.

## Frozen vector semantic-identity requirements
Before any polygon construction:
1. Inventory all source-native stroked/filled path styles and text labels in each BBN asset.
2. Identify the path/style corresponding to `Delta Y_p = 0.008` using only source-native labels, legend/text adjacency, exact vector style identity, or deterministic source structure.
3. Explicitly distinguish it from dashed-red CMB `Delta N_eff` overlays and from other `Delta Y_p` contour levels.
4. The same deterministic identity rule must work independently in both Majorana and Dirac assets.
5. No style may be selected merely because it visually resembles the expected exclusion boundary or produces a desirable region.

## PASS
`PASS_COSMOLOGY_B_L_BBN_VECTOR_CALIBRATION_SEMANTIC_IDENTITY` iff all axis-calibration tolerances pass for both assets and a unique deterministic source-native identity for the `Delta Y_p=0.008` contour is recovered in both scenarios while CMB overlays are excluded.

## BLOCKED
`BLOCKED_COSMOLOGY_B_L_BBN_VECTOR_CALIBRATION_SEMANTIC_IDENTITY` if source-native information is insufficient to uniquely identify the threshold contour or to calibrate both axes under the frozen requirements.

## SCIENTIFIC_FAIL
Use `SCIENTIFIC_FAIL_...` for a reproducible contradiction of the frozen calibration tolerances or cross-panel identity assumptions, not for parser/dependency/download failures.

## Infrastructure failure
Parser bugs, unsupported PDF operators, package failures, transient downloads or workflow problems are infrastructure/implementation failures and must not be converted into a scientific BLOCKED/FAIL if the primary asset contains recoverable information.

## Next actions
- PASS -> prospectively preregister 0081b excluded-side/topology geometry extraction for Majorana and Dirac separately, using the now-frozen contour identity; do not construct geometry inside 0081a.
- BLOCKED/FAIL -> stop the BBN geometry route under current primary assets; do not infer excluded side manually.

## Guards
No vector geometry extraction into a physical excluded polygon in 0081a. No Majorana/Dirac union/intersection. No CMB+BBN envelope composition. No response/enhancement scan. No post-result tolerance change.
