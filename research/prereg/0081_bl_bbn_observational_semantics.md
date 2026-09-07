# NMIR preregistration 0081 — B-L BBN observational semantics

Date frozen: 2026-09-08
Status: PROSPECTIVE
Parent authority: iterations 0080/0080a established exact vector-native BBN assets `Presentation/CnstrntPlotMajoranaYp.pdf` (Fig. 7) and `Presentation/CnstrntPlotDiracYp.pdf` (Fig. 8) inside Esseili & Kribs arXiv `2308.07955v2`; 0080e established that Majorana and Dirac are separate scenario-conditioned branches with no source-authorized universal composition.

## Scientific question
What exact present-observation BBN helium criterion does the primary Esseili–Kribs source itself authorize for turning Figs. 7/8 into hard B-L exclusions, and is that criterion stated with a reproducible confidence level and the same semantics for both Majorana and Dirac cases?

## Frozen primary authority
- arXiv source: `https://export.arxiv.org/e-print/2308.07955v2`
- source SHA256: `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`
- main TeX: `neff_arXiv_v2.tex`
- main TeX SHA256: `f77b577688b3609c574985b05fc9a213709c958ded60a511478357f1f881d678`
- target figures: Fig. 7 Majorana `Presentation/CnstrntPlotMajoranaYp.pdf`; Fig. 8 Dirac `Presentation/CnstrntPlotDiracYp.pdf`

## Frozen audit requirements
Machine-read the exact primary TeX only. A PASS requires all of:
1. Fig. 7 is explicitly identified as the Majorana `Delta Y_p`/helium-abundance result and Fig. 8 as the corresponding Dirac result;
2. the source states a present/conservative observational upper bound on the BSM helium shift (or an algebraically equivalent quantity) with an explicit numerical threshold;
3. the source states the confidence level associated with that conservative bound;
4. the source applies the same Fig. 7 semantics to Fig. 8 or otherwise explicitly gives the Dirac semantics;
5. any sign/absolute-value convention for `Delta Y_p` used to define the bound is recoverable from the source definition/equations or caption prose;
6. no CMB threshold is substituted for the BBN helium threshold.

The audit must preserve the numerical threshold exactly as written by the source. Do not choose a stronger/weaker value after inspecting vector geometry.

## Prospective classifications
- `PASS_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS`: exact helium threshold, CL, sign convention, and Majorana/Dirac applicability are primary-source recoverable. Next gate may separately calibrate axes and identify/materialize the hard BBN vector region.
- `PARTIAL_PASS_BBN_THRESHOLD_ONLY`: numerical threshold/CL is recoverable but figure/scenario/sign semantics are incomplete; geometry remains forbidden.
- `BLOCKED_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS`: no reproducible hard BBN criterion can be recovered from the exact source.
- `FAIL_BBN_SEMANTIC_MISMATCH`: the figure meaning differs materially from the assumed helium-shift interpretation.

## Guards
- Source text/TeX only in 0081; do not inspect vector path colors or select polygons.
- No manual/raster plot reading.
- Keep Majorana and Dirac as separate scenario-conditioned branches per 0080e.
- Do not combine BBN and CMB constraints in this gate; the source itself notes that combined BBN+CMB limits assuming no post-BBN new physics need not apply when B-L interactions change the cosmology between epochs.
- Do not scan BSM response or infer neutrino-energy enhancement.

## Next action on PASS
Preregister an 0081a BBN axis-calibration and vector-semantic identity gate using only the two already-authorized native-vector PDFs and the exact threshold frozen here. Geometry materialization must remain a later result if color/path identity is not independently established.
