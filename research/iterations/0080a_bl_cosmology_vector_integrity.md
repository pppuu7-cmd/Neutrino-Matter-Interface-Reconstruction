# NMIR Iteration 0080a — B-L cosmology vector integrity

Date: 2026-09-07
Classification: **PASS_COSMOLOGY_B_L_VECTOR_INTEGRITY**

Exact arXiv source `2308.07955v2` remained SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`. All four 0080 target PDFs are single-page, contain zero image XObjects, have nonzero native vector drawings/path items, and expose nonempty machine-readable text.

Hosted run/job `34161020276/101862718302`; 3 dedicated tests passed in 0.15 s. Artifact `10032589964`; raw JSON SHA256 `0e25aa0817f49adf3b7a517422ac4281f6cb825a47cd88364d4e7ee48f679680`; artifact ZIP SHA256 `ba912daf553e3ba449bf0b39613e5ab4381d30fe18314aaff9726bbeb1d6dbe9`. Baseline CI run `34161020225` passed.

Target identities and native structure:
- Majorana Delta N_eff: SHA `8b5c5839...e7837`, 477 drawings, 5851 path items, 47 words.
- Dirac Delta N_eff: SHA `c06b66e5...2ed4a`, 486 drawings, 11389 path items, 45 words.
- Majorana Delta Y_p: SHA `4326f3ac...d8926`, 112 drawings, 1890 path items, 24 words.
- Dirac Delta Y_p: SHA `14d9afe1...63b15`, 106 drawings, 1289 path items, 23 words.

The CMB figures expose `mX [MeV]`, `gX`, redundant logarithmic tick labels and Delta N_eff level labels as PDF text. The BBN figures likewise expose axes and Delta Y_p level labels. This establishes an executable vector-calibration route without raster/manual digitization.

0080a does not identify an observational exclusion contour and does not combine Majorana/Dirac scenarios. Next gate: 0080b CMB axis calibration only; Planck threshold choice remains forbidden until a separate primary observational-semantics gate.
