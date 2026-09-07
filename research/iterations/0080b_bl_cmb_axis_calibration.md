# NMIR Iteration 0080b — B-L CMB axis calibration

Date: 2026-09-07
Classification: **PASS_COSMOLOGY_B_L_CMB_AXIS_CALIBRATION**

Both primary Esseili–Kribs Delta N_eff panels independently recover the same logarithmic axes from machine text. The frozen 0.015-decade ordinary and leave-one-out criteria were not changed after execution.

The common calibration in PDF user-space is:
- `log10(m_X/MeV) = 0.014151317772708815 * x - 6.9932501456724525`
- `log10(g_X) = -0.0329969798924973 * y - 2.6510803066554596`

For the mass axis, maximum ordinary residual is `0.00159947053961762` decade and maximum LOO residual `0.0020872056238765424`. For the coupling axis, maximum ordinary residual is `0.010719098650080916` and maximum LOO residual `0.011974107570777992`, both below the frozen `0.015` threshold. Majorana-vs-Dirac calibration differences are exactly zero at all frozen tick anchors; the cross-panel acceptance threshold was `1e-5` decade.

Hosted run/job `34161277512/101863457667`; 3 dedicated tests passed in 0.12 s. Artifact `10032672039`; raw JSON SHA256 `de9c9b5365dd1b7b5502d44dfdc04d4547aac997508845079ebeb04d1e300b0c`; artifact ZIP SHA256 `98155106b7b4fb72d8a89314ab6b64eb99798f41fcecd5e48ae0944cb4247a44`. Baseline CI `34161277519` also passed.

Majorana exposes all six Delta N_eff labels `0.05,0.1,0.2,0.3,0.4,0.5`; Dirac exposes `0.05,0.1,0.2,0.5` as text. This inventory was not used to assign vector paths or choose an observational threshold.

Scientific consequence: both CMB panels now have a reproducible physical-coordinate transform. A later contour can be materialized without manual raster calibration, but only after a separate primary semantics gate fixes which Delta N_eff region is observationally excluded and how the source colors map to levels.
