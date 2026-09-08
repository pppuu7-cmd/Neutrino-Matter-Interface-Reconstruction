# NMIR iteration 0086b — NA64 2026 B-L numerical asset/materialization audit

Date: 2026-09-08
Prospective contract: `research/prereg/0086b_na64_b_minus_l_numerical_asset_materialization.md`, frozen commit `6173b4b9a62da9f44af12b100194f2c1dbcf23e1` before numerical geometry extraction.
Final classification: **PASS_NA64_B_L_NUMERICAL_ASSET_AUTHORITY**.
`NMIR_READINESS: 98%` (held pending actual coordinate materialization).

## Authoritative hosted execution
- workflow: `NMIR 0086b NA64 B-L numerical asset materialization`
- head commit: `559955fea03569610646bc67ea9a1b349c10816a`
- run: `34177444955`
- job: `101909569961`
- artifact: `10037736106`
- artifact ZIP SHA256: `a603182c34c8b684a6f9909af9da9edea6ec03c5f2fb1c1a696aef7fb537dd16`
- raw JSON SHA256: `00b8c9893db210d2fcc0e4b4ac96946b70ec583380c33f91f52c23225bf0716f`

All regression tests, source audit, and artifact upload completed successfully. The scientific classification below is based on the raw JSON artifact, not workflow color alone.

## Frozen source bytes
Primary source: NA64 Collaboration, arXiv `2606.17320v2`.

Exact downloaded source archive:
- size: `2070210` bytes
- SHA256: `4981fbe374836ed52c24c26955f90fa118295ff86aeab69f9f5f3449e60a3b9e`
- file count: `14`
- inventory SHA256: `78db241aca809ffc46f9e416be664b81bf128b62991eccfb74490ce24f6601dc`

Exact manuscript source:
- `NA64-PAPER-B-L.tex`
- SHA256 `42624987c4398f04fcc766c79b9eae117cf2123869338d9925ff2e6018d529a8`

## Source semantics
The exact TeX states that the combined 2016–2022 dataset, `(9.4 +/- 0.5)e11` EOT, is reinterpreted for U(1)_{B-L}, no signal is observed, and corresponding **90% C.L. exclusion limits** are presented.

The applicable top-panel scenario is explicitly:
- unbroken B-L symmetry;
- Dirac neutrinos / three light RHNs;
- invisibly decaying B-L Z';
- plane `(m_Z', g_{B-L})`;
- combined 2016–2022 NA64 dataset.

The scalar-DM benchmark is a separate source scenario and is not unioned with the unbroken B-L branch.

## Exact source-native vector assets
Four B-L limit/comparison figures linked by the exact TeX are PDF vector objects. PyMuPDF structural probes found drawing operators and **zero embedded raster images** in each:

1. `bminusl_unbroken.pdf`
   - SHA256 `d4b0ba8aa1cb05dad76f12c1fc6c8f98eb5c6e72dd53a6d47402b9d21b023393`
   - 1 page
   - 51 drawing objects
   - 0 images
   - source context: B-L + exclusion/limit + 90% C.L.

2. `bminusl_scalar.pdf`
   - SHA256 `c61595d32df37af3b6f2f51301e6239c6797a30c761d535c5043af73beb33f3b`
   - 1 page
   - 103 drawing objects
   - 0 images
   - separate scalar-DM scenario.

3. `comparison_AE_v3.pdf`
   - SHA256 `adb343856f9f0ed17c3b69cf63112d6ce8539ca378b20df2fa3cf652777c32a7`
   - 1 page
   - 356 drawing objects
   - 0 images.

4. `bminusl_allmodels.pdf`
   - SHA256 `db7e6d2628b869f389db6e32ffc43520daa6dd6d0b3857bdf22bc13ab84e53c1`
   - 1 page
   - 52 drawing objects
   - 0 images
   - multi-scenario comparison; not a permission to merge scenarios.

The arXiv `00README.json` is metadata, not scientific numerical geometry; the PASS does **not** rely on it.

## Scientific consequence
The collider/fixed-target family is no longer blocked by raster-only geometry. The exact primary source contains a reproducible vector object for the same canonical B-L scenario needed by NMIR. This authorizes a separate prospective geometry gate.

0086b does **not** yet claim any extracted `(m_V,g_BL)` coordinates, interpolation, excluded area, strongest-envelope comparison, or cross-family composition.

## Guards verified
- no OCR/manual digitization;
- no coordinate transform;
- no interpolation;
- no excluded-area calculation;
- no cross-family composition;
- no scenario union.

## Exact next gate
Prospectively preregister **0086c NA64 unbroken-B-L vector geometry calibration/materialization** against exact asset `bminusl_unbroken.pdf` SHA256 `d4b0ba8aa1cb05dad76f12c1fc6c8f98eb5c6e72dd53a6d47402b9d21b023393` before inspecting vector path coordinates.
