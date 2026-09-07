# NMIR Iteration 0080d — conservative current-CMB excluded geometry

Date: 2026-09-07
Classification: **PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_EXCLUDED_GEOMETRY**

Prospective contract was frozen before geometry extraction in `research/prereg/0080d_bl_cmb_conservative_excluded_geometry.md`, commit `53e54a16b86f6d422c2f6ee505a7be22f8212a2c`.

Primary: Esseili & Kribs, arXiv `2308.07955v2`, source archive SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`. The gate used only native vector objects from the pinned Majorana/Dirac `Delta N_eff` PDFs. Exact native hard-exclusion fills were dark blue `(0, 0.46666, 0.733322)` and light blue `(0.199997, 0.733322, 0.933319)`, matching the 0080c source semantics for `Delta N_eff >= 0.4` at 95% C.L. Green `(0, 0.599991, 0.533325)` was not selected.

Physical-coordinate transforms were the already validated 0080b maps:
- `log10(m_X/MeV)=0.014151317772708815*x_pdf-6.9932501456724525`
- `log10(g_X)=-0.0329969798924973*y_pdf-2.6510803066554596`.

Results remain scenario-conditioned and separate:
- **Majorana:** one valid component, area `48.332188584322665 decade^2`, bounds `(log10 m_X/GeV, log10 g_X) = [-8.997577562091603, -10.774903928382372, -1.2015738249824954, -3.0186996528406036]` in `[minx,miny,maxx,maxy]` order. Selected drawing IDs `37,42`.
- **Dirac:** one valid component, area `45.129364149717375 decade^2`, bounds `[-8.997577562091603, -10.572401176797548, -1.9985338229221234, -3.0186996528406036]`. Selected drawing IDs `46,51`.

Base/refined Bezier tolerances were frozen at `0.02/0.01 pt`. For both scenarios the relative area difference is `0.0` and the normalized symmetric-difference area is `0.0`, both far below the frozen 0.5% ceiling. Boundary round-trip maxima are `8.53e-14 pt` (Majorana) and `4.33e-14 pt` (Dirac), below the frozen `0.02 pt` criterion. No raster/manual coordinates, green inclusion, `buffer(0)`, convex hull, smoothing, manual node edits, scenario union or global-envelope union were used.

Authoritative hosted run/job `34161859886/101865153356`; dedicated tests `4 passed in 0.23s`. Artifact `10032854190`, 1228 bytes; independently downloaded artifact ZIP SHA256 `f00a461bb3780538d341c47b39b11ede9a4b5b34e928d679d2844c51db9d23bc`; raw JSON SHA256 `2d288fedc2da00da1a44e1536d0555bd5931a0052fbc48f29e4984bab2c66f97`. Machine-readable summary commit `528d6450625ff72fad20d78de5928a2ba736b877`.

Scientific consequence: NMIR now has a second finite-mass reproducible B-L excluded-region family, cosmological/CMB rather than solar CEvNS. However Majorana and Dirac are alternative physical scenarios; 0080d does **not** authorize their union/intersection or a global B-L envelope. A separate prospective scenario-semantics gate is required before composition.
