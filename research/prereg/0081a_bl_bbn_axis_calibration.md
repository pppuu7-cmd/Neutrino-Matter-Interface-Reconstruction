# NMIR preregistration 0081a — B-L BBN axis calibration and text-level contour inventory

Date frozen: 2026-09-08
Status: PROSPECTIVE
Parent authority: 0081 `PASS_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS`; 0080a `PASS_COSMOLOGY_B_L_VECTOR_INTEGRITY`; 0080e requires Majorana/Dirac to remain separate scenario-conditioned branches.

## Scientific question
Can the native-vector BBN Figures 7/8 from the exact Esseili–Kribs source be independently calibrated into `(log10(m_X/MeV), log10(g_X))` with prospectively fixed residual tolerances, without borrowing the CMB calibration and without selecting the `Delta Y_p=0.008` scientific boundary by path/color?

## Frozen primary authority
- source: `https://export.arxiv.org/e-print/2308.07955v2`
- source SHA256: `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`
- Majorana Fig.7: `Presentation/CnstrntPlotMajoranaYp.pdf`, SHA256 `4326f3ac9ba29e515aa22afafef27d08c05d0e6be04db605c4706418c6cd8926`
- Dirac Fig.8: `Presentation/CnstrntPlotDiracYp.pdf`, SHA256 `14d9afe16f4c38f1d3c08f97ccf086a570739b18731b0b6ffee97fe4b9e63b15`
- 0080a already established both assets are native vector with zero image XObjects and text extractable.

## Frozen axis hypothesis and extraction rule
The gate tests, rather than assumes, that each BBN panel exposes the same complete logarithmic tick *values* used by this figure family:
- x-axis exponents exactly `-6,-5,-4,-3,-2,-1,0,1,2,3`, representing `m_X` in MeV;
- y-axis exponents exactly `-17,-16,...,-3`, representing `g_X`.

Tick identity must come from extractable PDF text and exponent/value syntax, not from raster position reading. The implementation may use relative page-position guards only to distinguish axis ticks from scientific contour labels, but must not import numerical coordinates or affine coefficients from the CMB 0080b calibration.

For each panel fit independently:
- `log10(m_X/MeV) = a_x * x_pdf + b_x`;
- `log10(g_X) = a_y * y_pdf + b_y`.

Required per-panel checks:
1. exactly one recovered x tick for every frozen exponent `-6..3`;
2. exactly one recovered y tick for every frozen exponent `-17..-3`;
3. max absolute OLS residual <= `0.015` decade for x and y;
4. max absolute leave-one-out residual <= `0.015` decade for x and y.

Cross-panel replication is evaluated only after the two independent calibrations pass. If both panels expose the same tick coordinate system, the maximum transform difference evaluated on the recovered Majorana ticks must be <= `1e-5` decade in both axes. Failure of this cross-panel criterion does not authorize borrowing one panel's transform for the other.

## Text-level scientific inventory
Record all extractable BBN contour-label text matching the already-known source family values, including when present `0.002, 0.003, 0.004, 0.006, 0.008`. This is inventory only. The 0081 hard criterion `Delta Y_p = 0.008 at 95% C.L.` is not yet mapped to a vector path/fill in 0081a.

## Prospective classifications
- `PASS_COSMOLOGY_B_L_BBN_AXIS_CALIBRATION`: both panels independently satisfy all tick/residual/LOO checks and cross-panel transform replication <=1e-5 decade.
- `PARTIAL_PASS_BBN_SINGLE_PANEL_CALIBRATION`: exactly one panel satisfies all independent calibration checks, or both panels pass independently but cross-panel replication fails. Each valid panel may retain its own transform; no shared transform may be asserted.
- `SCIENTIFIC_FAIL_COSMOLOGY_B_L_BBN_AXIS_CALIBRATION`: neither panel satisfies the frozen calibration requirements under the native-vector text authority.
- infrastructure/parser/dependency/source-download failure is not scientific FAIL; diagnose and repair implementation without changing the frozen exponents/tolerances.

## Guards
- Do not reuse 0080b affine coefficients as inputs.
- Do not inspect rasterized figures manually.
- Do not select paths/colors corresponding to `Delta Y_p=0.008` in this gate.
- Do not materialize an excluded polygon in 0081a.
- Do not union/intersect Majorana and Dirac.
- Do not combine BBN with CMB or the global B-L envelope.
- Do not scan BSM response or infer neutrino-energy enhancement.

## Next action
On full or panel-specific calibration PASS, preregister 0081b to identify the native-vector scientific object corresponding to the signed `Delta Y_p >= 0.008` 95% C.L. criterion, using source semantics plus vector/color/path identity. Only 0081b may materialize the BBN excluded geometry if its prospective identity checks pass.
