# NMIR Iteration 0080 — B-L cosmology vector-asset authority

Date: 2026-09-07
Classification: **PASS_COSMOLOGY_B_L_VECTOR_ASSET_AUTHORITY**

The exact arXiv v2 source archive of Esseili & Kribs, arXiv:2308.07955v2, was acquired and SHA256-pinned as `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c` (771703 bytes). No manual figure reading or raster digitization was used.

The frozen 0080 audit resolved the exact published cosmology figures from `neff_arXiv_v2.tex`:

- Fig. 5, Majorana Delta N_eff: `Presentation/CnstrntPlotMajoranaNeff.pdf`
- Fig. 6, Dirac Delta N_eff: `Presentation/CnstrntPlotDiracNeff.pdf`
- Fig. 7, Majorana Delta Y_p: `Presentation/CnstrntPlotMajoranaYp.pdf`
- Fig. 8, Dirac Delta Y_p: `Presentation/CnstrntPlotDiracYp.pdf`

All four are primary PDF vector assets; no target raster asset or unresolved target reference was found. No source numerical CSV/DAT/JSON/Python contour asset was present, so the correct future route is calibrated vector extraction, not author-table ingestion.

The source captions themselves pin important semantics without reading values from curves. Fig. 5 defines Delta N_eff region levels 0.05, 0.1, 0.2, 0.3, 0.4 and 0.5 and states current Planck data exclude roughly Delta N_eff >= 0.3-0.4 depending on dataset. Fig. 6 is the corresponding Dirac case. Fig. 7 states a conservative Delta Y_p=0.008 upper bound at 95% C.L.; Fig. 8 is the corresponding Dirac case. These statements do not yet select a single CMB contour for envelope materialization.

Hosted run/job `34160801805/101862078831`; 4 dedicated tests passed in 0.04 s. Artifact `10032522988`; raw JSON SHA256 `351a0bb97f2b7310085a6f3313c58f2cba5bc97b6988ba2c2dfcfc278b1a4b7e`; artifact ZIP SHA256 `0efba64740d815961673d5bfb8f72cdc60ed0ccdea351fc5cbe4820f20aeae66`. Baseline CI run `34160801817` also passed.

Scientific consequence: the cosmology family is now executable at the vector-asset level. 0080 does not authorize contour extraction, scenario union, or selection between Planck 0.3 and 0.4 thresholds. A separately preregistered 0080a must first prove vector integrity and machine-readable axis/legend structure for all four assets.
