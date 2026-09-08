# NMIR preregistration 0086b — NA64 2026 B-L numerical asset/materialization audit

Date frozen: 2026-09-08
Status: PROSPECTIVE
Parent: iteration 0086a `PASS_B_L_COLLIDER_FIXED_TARGET_PRIMARY_AUTHORITY`.

## Scientific question
Does NA64 arXiv `2606.17320v2` provide source-native numerical, tabulated, code, or vector-geometry authority sufficient to materialize its B-L fixed-target exclusion reproducibly in `(m_V,g_BL)` without raster/OCR/manual digitization, while preserving source scenario and confidence-level semantics?

## Frozen source
Primary source: NA64 Collaboration, “Improved limits on a new Z' in B-L scenarios with the NA64 experiment at CERN”, arXiv `2606.17320v2`, revised 2026-06-30, report `CERN-EP-2026-166`.

Use the stable arXiv source and, if downloadable, freeze exact source/PDF ancillary bytes and SHA256 before interpreting geometry. If source files cannot be obtained through the available connector, stable primary URLs may establish semantics but cannot substitute for uninspected numerical assets.

## Frozen model/scenario rules
- `g_BL = g_{B-L} = g_{Z'}` only under the source's explicit B-L current convention.
- Preserve unbroken B-L/Dirac + three light RHN assumptions separately from broken/Majorana or dark-sector invisible variants.
- Do not post-hoc choose the strongest scenario.
- Preserve the confidence level and excluded-side semantics stated by the source.

## Asset search order
1. official ancillary/data/code linked by the primary source;
2. arXiv source archive for tables, explicit point arrays, plotting data, vector EPS/PDF/SVG paths or generated-data files;
3. machine-readable tables in the manuscript/source;
4. analytical/tabulated bounds explicitly stated in text.

A raster-only figure is not numerical authority under this gate.

## Acceptance criteria
`PASS_NA64_B_L_NUMERICAL_ASSET_AUTHORITY` if at least one source-native object supplies reproducible numerical B-L limit geometry over nonzero mass support, with exact scenario and CL/side semantics.

`PASS_NA64_B_L_ANALYTICAL_LIMIT_AUTHORITY` if exact/tabulated analytical pointwise limits are sufficient without figure extraction.

`BLOCKED_NA64_B_L_RASTER_ONLY_GEOMETRY` if the applicable primary limit exists but only raster/visually readable geometry is available.

`BLOCKED_NA64_B_L_ASSET_ACCESS` if source-native assets are plausibly available but cannot be obtained/verified in the current infrastructure; do not replace access failure with manual reading.

`SCIENTIFIC_FAIL_NA64_B_L_SCENARIO_MAPPING` only if the primary material contradicts the 0086a frozen same-convention/scenario interpretation.

## Numerical-materialization rule
0086b is an asset-authority audit. If a vector or point-table object is found, freeze its exact hash and topology/axis/CL identity first. A child 0086c must be preregistered before transforming coordinates, interpolating curves, computing excluded areas, or composing with other families.

## Guards
No raster/OCR/manual digitization. No screenshot coordinate reading. No generic dark-photon epsilon contour substitution unless the exact source object is explicitly the B-L result and the source mapping applies to the complete production+decay likelihood. No cross-family union. No BSM response calculation.

## Next action
On asset-authority PASS, preregister 0086c exact NA64 B-L geometry/limit materialization. On BLOCKED, record exact missing asset/access and return to the completeness ledger without pretending collider/fixed-target numerical coverage is complete.
