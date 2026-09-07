# Preregistration 0080b — Esseili–Kribs CMB B-L axis calibration

Date frozen: 2026-09-07
Parent: 0080a `PASS_COSMOLOGY_B_L_VECTOR_INTEGRITY`.

## Scope
Calibrate only the logarithmic `(m_X [MeV], g_X)` axes of the primary Majorana and Dirac Delta N_eff figures (published Figs. 5 and 6). Inventory Delta N_eff text labels but do not assign colors/paths to levels and do not select a Planck exclusion threshold.

## Frozen source/assets
Source arXiv `2308.07955v2`, SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`.
- Majorana: `Presentation/CnstrntPlotMajoranaNeff.pdf`, SHA256 `8b5c5839fada534ed10d79768335050814765a6ec00bddcb51e75cc0f64e7837`.
- Dirac: `Presentation/CnstrntPlotDiracNeff.pdf`, SHA256 `c06b66e5cb35c3b1cae341da393e9b638d3f3f536cef09a3ca5431600fb2ed4a`.

## Frozen text-tick authority
From 0080a machine text, before any calibration fit:
- x-axis tick strings in increasing x order are exactly `10-6,10-5,10-4,10-3,10-2,0.1,1,10,102,103`, corresponding to `log10(m_X/MeV) = -6,-5,-4,-3,-2,-1,0,1,2,3`.
- y-axis tick strings from bottom to top are `10-17,...,10-3`, corresponding to `log10(g_X) = -17,...,-3`.
- x tick candidates are selected by expected strings with PDF word y-center in `[430,462]`.
- y tick candidates are selected by expected strings with PDF word x-center `<68` and y-center `<435`.
The coordinate-band rules are frozen from the machine-structure inventory, not chosen after fitting.

## Fit
For each PDF independently fit affine relations
`log10(m_X/MeV) = a_x * x_center + b_x`
and
`log10(g_X) = a_y * y_center + b_y`
by ordinary least squares.

Compute ordinary residuals and leave-one-out (LOO) residuals in decades.

## Frozen acceptance
For each panel:
1. exactly 10 x ticks are recovered, one for each frozen exponent -6..3;
2. exactly 15 y ticks are recovered, one for each frozen exponent -17..-3;
3. max absolute ordinary residual <= 0.015 decade on both axes;
4. max absolute LOO residual <= 0.015 decade on both axes.

Cross-panel replication:
5. evaluate both Majorana and Dirac calibrations at every recovered Majorana x/y tick center; maximum difference must be <= `1e-5` decade for each axis.

`PASS_COSMOLOGY_B_L_CMB_AXIS_CALIBRATION` iff all checks pass. Otherwise `SCIENTIFIC_FAIL_COSMOLOGY_B_L_CMB_AXIS_CALIBRATION`.

## Inventory only
Record occurrences and PDF positions of text strings `0.05,0.1,0.2,0.3,0.4,0.5` inside the scientific plotting area (`y_center < 400`). This is not a contour-to-color assignment and is not an observational threshold.

## Forbidden
No raster/manual reading; no path/color selection; no conversion of Delta N_eff level to excluded region; no choice between 0.3 and 0.4; no Majorana/Dirac union/intersection; no global B-L envelope union; no BSM response scan.

PASS authorizes a separate 0080c primary observational-threshold/contour-semantics gate.
