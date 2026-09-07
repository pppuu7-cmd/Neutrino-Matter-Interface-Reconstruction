# Preregistration 0080a — B-L cosmology vector-integrity / machine-structure gate

Date frozen: 2026-09-07
Parent: 0080 `PASS_COSMOLOGY_B_L_VECTOR_ASSET_AUTHORITY`, immutable record `research/iterations/0080_bl_cosmology_vector_asset_authority.md`.

## Question
Are all four primary Esseili–Kribs cosmology constraint PDFs genuine vector-native scientific plots with sufficient machine structure to authorize a later axis/contour semantics gate, rather than PDF wrappers around raster images?

## Frozen source
Exact arXiv archive: `https://export.arxiv.org/e-print/2308.07955v2`, SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`.

Exact assets, fixed by 0080 before this gate:
1. `Presentation/CnstrntPlotMajoranaNeff.pdf`
2. `Presentation/CnstrntPlotDiracNeff.pdf`
3. `Presentation/CnstrntPlotMajoranaYp.pdf`
4. `Presentation/CnstrntPlotDiracYp.pdf`

## Frozen audit
For each asset independently:
- extract raw bytes from the exact source archive and SHA256-pin them;
- require one PDF page;
- count image XObjects via PyMuPDF and require exactly zero;
- count vector drawings and path items and require both > 0;
- extract text words and require non-empty text;
- record page dimensions, text word count, drawing count, path-item count, stroke/fill color inventory and all text words with bounding boxes;
- record candidate power-of-ten/tick-like text but do not interpret axis values;
- perform no contour color selection and no coordinate calibration.

## Acceptance
`PASS_COSMOLOGY_B_L_VECTOR_INTEGRITY` iff all four exact assets:
1. are single-page PDFs;
2. have zero image XObjects;
3. have at least one vector drawing and at least one path item;
4. have non-empty extractable text;
5. preserve their exact 0080 source identity from the pinned archive.

`PARTIAL_COSMOLOGY_B_L_VECTOR_TEXT_BLOCKED` iff vector-native structure passes for all four but one or more has no extractable text.

`SCIENTIFIC_FAIL_COSMOLOGY_B_L_VECTOR_INTEGRITY` iff any target asset is raster-backed, missing, multipage unexpectedly, or has no vector drawing/path structure.

`INFRASTRUCTURE_FAIL` only if the exact source archive/PDF parser cannot be acquired/executed.

## Forbidden
No manual/raster reading, no axis calibration, no identification of observational contour by shape, no CMB threshold selection, no Majorana/Dirac combination, no B-L envelope union, no BSM response scan.

PASS only authorizes 0080b axis/legend/contour-semantic calibration under a new preregistration.
