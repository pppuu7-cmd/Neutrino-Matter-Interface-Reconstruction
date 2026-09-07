# Preregistration 0080b — B-L cosmology CMB vector-axis calibration

Date frozen: 2026-09-07
Parent: 0080a `PASS_COSMOLOGY_B_L_VECTOR_INTEGRITY`, immutable record `research/iterations/0080a_bl_cosmology_vector_integrity.md`.

## Question
Can the two primary Esseili–Kribs CMB panels (Majorana and Dirac Delta N_eff) be mapped reproducibly from PDF coordinates into the published `(m_X, g_X)` axes using text-native tick positions only, before any contour selection or observational-threshold choice?

## Frozen inputs
Exact source archive: arXiv `2308.07955v2`, SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`.

Exact PDFs:
- Majorana: `Presentation/CnstrntPlotMajoranaNeff.pdf`, SHA256 `8b5c5839fada534ed10d79768335050814765a6ec00bddcb51e75cc0f64e7837`.
- Dirac: `Presentation/CnstrntPlotDiracNeff.pdf`, SHA256 `c06b66e5cb35c3b1cae341da393e9b638d3f3f536cef09a3ca5431600fb2ed4a`.

0080a established one page, zero image XObjects, native vector paths and extractable text in both assets.

## Frozen calibration method
For each CMB PDF independently:
1. Re-extract PDF bytes from the pinned source archive and verify the exact SHA256 above.
2. Read PDF text words and bounding boxes with PyMuPDF; no rendered/raster image may be used.
3. Identify x-axis tick labels from the bottom-axis text row by position and parse the published sequence `10^-6, 10^-5, 10^-4, 10^-3, 10^-2, 10^-1, 1, 10, 10^2, 10^3` in MeV. Treat visually compact PDF strings such as `10-6` and `102` as power-of-ten labels only when their ordered positions and full frozen sequence make the exponent unambiguous.
4. Identify y-axis tick labels from the left-axis text column and parse the published sequence `10^-17 ... 10^-3` for `g_X`.
5. Use tick-center coordinates. Fit affine maps
   `log10(m_X/MeV) = a_x * x_pdf + b_x`
   and
   `log10(g_X) = a_y * y_pdf + b_y`
   by ordinary least squares using all identified major ticks.
6. Record coefficients, all tick residuals, RMS residual and maximum absolute residual in decades.
7. Cross-panel check: evaluate both fitted maps at every common tick value and record the PDF-coordinate disagreement after mapping back to decades. Do not force the two panels to share coefficients.

## Frozen acceptance
`PASS_COSMOLOGY_B_L_CMB_AXIS_CALIBRATION` iff BOTH panels satisfy all of:
- all 10 frozen x ticks are identified in strictly increasing PDF x order;
- all 15 frozen y ticks (`10^-17` through `10^-3`) are identified in the expected monotonic PDF y order;
- fitted x and y maps have the physically correct monotonic signs;
- maximum absolute calibration residual <= `0.01 decade` on each axis;
- RMS residual <= `0.005 decade` on each axis;
- the two panels agree on the recovered value of every common x/y tick to <= `0.01 decade` when evaluated with their independent calibrations;
- no raster/manual coordinate input entered the result.

`PARTIAL_COSMOLOGY_B_L_CMB_AXIS_TEXT_AMBIGUITY` iff both figures remain vector-native but the exact frozen tick sequences cannot be deterministically parsed from text positions.

`SCIENTIFIC_FAIL_COSMOLOGY_B_L_CMB_AXIS_CALIBRATION` iff a deterministic calibration is obtained but any frozen residual/order/sign/cross-panel criterion fails.

`INFRASTRUCTURE_FAIL` only for source acquisition/parser/runtime failure before scientific classification.

## Forbidden
No selection/extraction of Delta N_eff contour paths; no choice between Planck `Delta N_eff~0.3` and `~0.4`; no CMB-S4 projection materialization; no BBN contour extraction; no Majorana/Dirac union/intersection; no union with 0078c/0079a; no BSM response or enhancement calculation.

## Next action
PASS authorizes a separately preregistered 0080c primary observational-semantics/contour-identity gate. That later gate must freeze the observational threshold and contour identity before any `(m_X,g_X)` exclusion geometry is extracted. PARTIAL/FAIL retires this calibration route unless a genuinely new machine-readable primary representation changes the assumptions.
