# Preregistration 0078a — De Romeri et al. 2603.00554 B-L vector-asset integrity

Date frozen: 2026-09-07
Parent: `research/prereg/0078_external_survivor_authority_refresh.md`, commit `022de0c433b169b6fc8df5997d5637821f95132b`.
Source-audit run: `34154279232`, job `101842733211`, head `691710c3f2159bfae2e35fc6769acc436c0cc8f4`, artifact `10030406001`.

## Frozen primary authority

arXiv `2603.00554`, source archive SHA256
`09ab22f753ac3f5fbde5be65ac50926de67b0638550366d158aadcfde8e92564`.

The source TeX itself gives the semantic identity before this integrity test:

- `vector_BL_PnX_XnT_LZ_combined.pdf` is the **right panel** of the figure whose caption says the magenta shaded region is the combined XENONnT + PandaX-4T + LZ 90% CL exclusion for vector `B-L`; expected asset SHA256 `ace761499623535907263e780a6e96a17474adf418d3f9363dae8e28bc5e7a39`.
- `BL_vector_PnX_XnT_LZ.pdf` is the individual-bounds B-L figure whose caption maps blue/green/orange to XENONnT/PandaX-4T/LZ and magenta to the combined exclusion; expected asset SHA256 `06092f863d59cb9e7318384d44f8eb7b3421c79ee9c56fd9b64aed42f3e32071`.

This identity is frozen from TeX provenance, not inferred from geometry after inspection.

## Scientific question

Are these primary PDF assets genuinely machine-readable vector plots with enough independent text/vector structure to permit a separately preregistered contour calibration/extraction, rather than raster images embedded in PDF containers?

## Frozen audit

For each exact asset above:

1. redownload the exact arXiv source archive and verify the frozen archive SHA256;
2. extract only the named PDF and verify its frozen SHA256;
3. parse the PDF object graph with a standard PDF library;
4. recursively count image XObjects and Form XObjects on the plotted page;
5. decode page/Form content streams and count vector path-paint operations (`S`, `s`, `f`, `F`, `f*`, `B`, `B*`, `b`, `b*`) and path-construction operations (`m`, `l`, `c`, `v`, `y`, `re`);
6. extract machine-readable text and search normalized text for independent mass-axis/coupling/model/experiment semantics. Text need not preserve exact TeX glyph spelling, but at minimum the combined asset must expose recognizable mediator-mass and coupling/experiment/model tokens or otherwise remain semantically unresolved.

No curve coordinates, axis calibration or numerical limit values are to be extracted in 0078a.

## Prospective criteria

`PASS_PRIMARY_B_L_VECTOR_ASSET_INTEGRITY` requires for **both** frozen assets:

- archive and asset SHA256 exactly match;
- PDF parsing succeeds and at least one page is present;
- recursive image-XObject count is exactly zero;
- total path-construction operation count >= 100 and path-paint operation count >= 20;
- extracted text is non-empty;
- the combined B-L asset exposes at least one recognizable mass token (`m`, `mass`, `MeV`, `GeV`, `eV`) and at least one recognizable coupling/model/experiment token (`g`, `B-L`, `XENON`, `PandaX`, `LZ`, `COHERENT`) after Unicode-normalized case-insensitive matching.

`PARTIAL_VECTOR_ASSET_INTEGRITY` if exact hashes and vector paths pass but text semantics are not independently extractable; this does not yet authorize contour extraction.

`SCIENTIFIC_FAIL_VECTOR_ASSET_INTEGRITY` if a frozen PDF is raster-backed, lacks the required vector structure, has mismatched source/asset identity, or otherwise fails a frozen scientific-integrity criterion after successful source access.

`INFRASTRUCTURE_FAIL` only for package/network/runtime failure before the exact source/asset can be audited.

## Decision tree

PASS -> preregister 0078b axis/legend/path calibration for the **combined magenta B-L contour only**, with values/axis labels frozen from primary text before any path classification.

PARTIAL/FAIL -> do not read the plot manually and do not infer curve identity from color/geometry post hoc. 0078 remains partial authority unless an independent numeric/code release is found.
