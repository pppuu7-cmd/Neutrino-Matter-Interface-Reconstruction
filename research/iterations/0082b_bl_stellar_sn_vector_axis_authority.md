# NMIR iteration 0082b — B-L stellar/SN vector integrity and native-axis authority

Date: 2026-09-08
Classification: **BLOCKED_B_L_STELLAR_SN_VECTOR_AXIS_AUTHORITY**
Prospective contract: `research/prereg/0082b_bl_stellar_sn_vector_axis_authority.md`, frozen commit `a46c4fd6b6e74a63bd70d4358f0218752bfd11cd`.

## Result
The all-three-source vector route is BLOCKED under the prospectively frozen no-raster/manual-inference contract, but the result is strongly scoped: Cerdeño et al. passes every vector/axis-authority requirement and remains eligible for a later deterministic contour gate; the Hong and Shin–Yun final constraint-summary PDFs are raster-only containers and therefore cannot be used for vector geometry.

### Cerdeño et al. 2021 — PASS vector route
Asset: `Figures/BL_constraints.pdf`
- asset SHA256: `6557571159bd7d279e9b78e026c79c2974fd487db86dcf3f60b566e54318d07f`
- bytes: `185486`
- single page: yes, `540 × 396` PDF points
- image XObjects: `0`
- drawings: `104`
- path items: `22716`
- text spans: `44`
- native mass-axis identity: PASS
- native B-L coupling-axis identity: PASS
- x-axis numerical anchors: `8`, span `5.0` decades
- y-axis numerical anchors: `9`, span `4.698970004336019` decades

Therefore this exact PDF is a machine-native vector figure with sufficient source-text anchor authority for a separately preregistered axis-calibration and curve-identity gate.

### Hong–Shin–Yun 2021 — BLOCKED vector route
Asset: `B-LConstraints.pdf`
- asset SHA256: `658d3664fd51689726553d86d7c5edb8014c53a6812f80b0b1d758e91e859cb7`
- bytes: `443808`
- single page: yes, `3488 × 3447`
- image XObjects: `1`
- drawings: `0`
- path items: `0`
- text spans: `0`
- source-text numerical anchors in PDF: none

The source/semantic authority from 0082/0082a is preserved, but the published summary PDF itself is raster-only for our purposes. Raster/manual digitization is forbidden, so no vector geometry is authorized from this asset.

### Shin–Yun 2022 — BLOCKED vector route
Asset: `B-L_Constraints.pdf`
- asset SHA256: `2dd30e71ebcccd1e637ace0dc1b571bb8e8946dbafbc5481bae46bda1a958acd`
- bytes: `130241`
- single page: yes, `360 × 361`
- image XObjects: `1`
- drawings: `0`
- path items: `0`
- text spans: `0`
- source-text numerical anchors in PDF: none

Again, 0082/0082a source and revision semantics remain valid. Only the vector-geometry route is blocked. Source-text analytical bounds may be studied in a separate prospectively frozen non-raster gate; they are not materialized here.

## Implementation history
The first hosted attempt, run `34167709304`, stopped before scientific source inspection because the synthetic regression PDF used Unicode superscript glyphs not supported by its built-in font. This was implementation-invalid, not scientific BLOCKED. Commit `440c7f8a5edd0d53d146bfe203c043fa54f42e1e` changed only the fixture labels to equivalent ASCII decimal values; no frozen scientific threshold, page-relative band, source list or scientific audit code was relaxed.

## Hosted provenance
- authoritative scientific run/job: `34167754777 / 101882075294`
- artifact: `10034702610`
- head SHA: `440c7f8a5edd0d53d146bfe203c043fa54f42e1e`
- dedicated tests: `4 passed in 0.14s`
- raw JSON SHA256: `121b91f5675b96f12a05e4c784ad2ce6b72f3f123df41e82a7834d68ddffa858`
- artifact ZIP SHA256: `b5864ae65d5e521e3c9b26471db2d90ce8e916d5fddacbaec99367e1acd4c294`
- artifact ZIP and inner JSON independently verified after download
- baseline CI: run `34167754778`, success (`pytest` + `nmir.baseline`)

## Interpretation
This is useful selection information rather than a loss of the stellar/SN family:
- **Cerdeño vector geometry remains executable.**
- Hong and Shin–Yun retain source/semantic physics authority but need a different machine-native route (e.g. explicit source-text analytical bounds) if they are to contribute numerical geometry without manual digitization.

## Guards preserved
No raster OCR/digitization, no curve color/path selection, no axis fit, no excluded-side assignment, no cross-paper coupling conversion, no cross-paper union/intersection, no global B-L envelope, no BSM response scan.

## Exact next gate
Highest-value executable branch: prospectively preregister a Cerdeño-only vector calibration + source-own constraint-curve semantic identity gate using the exact asset SHA above. Hong/Shin analytical-text bounds may be pursued separately and must not be reconstructed from raster plots.

`NMIR_READINESS: 94%` — unchanged until a new stellar/SN excluded region is reproducibly materialized.
