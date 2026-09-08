# NMIR preregistration 0086c — NA64 unbroken-B-L vector geometry materialization

Date frozen: 2026-09-08
Status: PROSPECTIVE
Parent: iteration 0086b `PASS_NA64_B_L_NUMERICAL_ASSET_AUTHORITY`.

## Scientific question
Can the exact source-native NA64 2026 unbroken-B-L vector figure be calibrated and its current 90% C.L. limit materialized reproducibly in `(m_V,g_BL)` without raster/OCR/manual digitization and without importing any generic dark-photon contour?

## Frozen exact source object
Primary archive: arXiv `2606.17320v2`, archive SHA256
`4981fbe374836ed52c24c26955f90fa118295ff86aeab69f9f5f3449e60a3b9e`.

Target figure only:
- path: `bminusl_unbroken.pdf`
- SHA256: `d4b0ba8aa1cb05dad76f12c1fc6c8f98eb5c6e72dd53a6d47402b9d21b023393`
- exact source context: 90% C.L. exclusion limits, unbroken B-L symmetry, Dirac neutrinos / three light RHNs, combined 2016–2022 NA64 dataset.

No scalar-DM or all-model figure may substitute for this object.

## Frozen coordinate convention
Materialized coordinates must be reported as
- `x = log10(m_V / eV)`
- `y = log10(g_BL)`
with `g_BL = g_{B-L}` from 0086a.

No epsilon conversion is allowed.

## Axis-calibration protocol
1. Extract PDF text spans and vector drawing objects programmatically from the exact PDF bytes.
2. Detect candidate x/y tick labels from source-native text only; no raster rendering or OCR.
3. Require at least three distinct numerical tick anchors per axis spanning nonzero range.
4. Test both linear and logarithmic numerical interpretations only where the printed labels themselves authorize them; for the expected log-log plot, fit an affine map between PDF coordinate and `log10(physical value)`.
5. PASS calibration requires finite ordered anchors and maximum anchor reproduction residual `<= 1e-6 decade` after accounting for printed numeric precision. If exact printed-label precision makes this tolerance inapplicable, fail closed and record the precision obstruction rather than loosening it post-result.

## Curve-identity protocol
The current NA64 unbroken-B-L limit must be identified from source-native vector structure plus source-native legend/text identity, not visual judgment.

Permitted evidence:
- identical stroke/fill style between a legend sample and a plot path;
- direct text/path adjacency encoded in the vector object;
- a uniquely labelled source-native path/object.

Forbidden:
- choosing the visually strongest curve;
- choosing by vertical order;
- naming a path from prior literature appearance;
- manual clicking or screenshot comparison.

If multiple geometrically plausible paths share indistinguishable style/identity, classify `BLOCKED_NA64_B_L_VECTOR_CURVE_IDENTITY`.

## Geometry integrity
For an identified current-NA64 path:
- require finite coordinates after calibration;
- preserve all disconnected components separately;
- do not bridge gaps;
- do not extrapolate beyond source support;
- report source vertex count and calibrated support;
- require transform round-trip residual `<= 1e-9 decade` for extracted vertices;
- no smoothing except exact consecutive-vertex linear segments already present in the source path.

## Excluded-side semantics
0086c may claim an excluded region only if the exact source-native text/fill/legend establishes which side of the materialized boundary is excluded for the unbroken-B-L scenario. If the curve is identifiable but the excluded side is not, return `PASS_NA64_B_L_VECTOR_CURVE_GEOMETRY / BLOCKED_NA64_B_L_EXCLUDED_SIDE_SEMANTICS`; do not infer the side from generic coupling intuition.

## Acceptance taxonomy
- `PASS_NA64_B_L_VECTOR_GEOMETRY_AUTHORITY`: axes, current-NA64 curve identity, coordinates, support, and excluded-side semantics all pass.
- `PASS_NA64_B_L_VECTOR_CURVE_GEOMETRY / BLOCKED_NA64_B_L_EXCLUDED_SIDE_SEMANTICS`: curve geometry passes but excluded side is not source-authorized.
- `BLOCKED_NA64_B_L_VECTOR_AXIS_CALIBRATION`: tick/axis mapping is insufficient or ambiguous.
- `BLOCKED_NA64_B_L_VECTOR_CURVE_IDENTITY`: current-NA64 curve cannot be uniquely bound to a vector object.
- `SCIENTIFIC_FAIL_NA64_B_L_VECTOR_INTEGRITY`: exact PDF contradicts the 0086b vector/no-raster or 0086a same-scenario authority assumptions.
- infrastructure/parser failure must remain distinct from all scientific classifications.

## Scope guards
0086c does not compose NA64 with CEvNS, stellar/SN, cosmology or fifth-force constraints. It does not unlock BSM response. It does not compute a global surviving region, detector enhancement, or discovery claim.

If 0086c PASSes, the next gate must be separately preregistered for cross-family B-L composition/completeness and only then may NMIR test whether a nontrivial surviving corridor overlaps a neutrino-matter-response optimum.
