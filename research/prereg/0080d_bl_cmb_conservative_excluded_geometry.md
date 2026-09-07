# Preregistration 0080d — conservative current-CMB excluded-region geometry

Date frozen: 2026-09-07
Parents: 0080a `PASS_COSMOLOGY_B_L_VECTOR_INTEGRITY`; 0080b `PASS_COSMOLOGY_B_L_CMB_AXIS_CALIBRATION`; 0080c `PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_95CL_SEMANTICS`.

## Question
Can the **hard current-CMB excluded regions** (`Delta N_eff >= 0.4` at 95% C.L.) be materialized reproducibly and separately for the Majorana and Dirac Esseili–Kribs panels from native vector geometry, without raster/manual digitization or post-result topology repair?

## Frozen inputs and provenance
Primary source: Esseili & Kribs, arXiv `2308.07955v2`, source archive SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`.

CMB PDFs:
- Majorana `Presentation/CnstrntPlotMajoranaNeff.pdf`, SHA256 `8b5c5839fada534ed10d79768335050814765a6ec00bddcb51e75cc0f64e7837`.
- Dirac `Presentation/CnstrntPlotDiracNeff.pdf`, SHA256 `c06b66e5cb35c3b1cae341da393e9b638d3f3f536cef09a3ca5431600fb2ed4a`.

0080b frozen transforms:
- `log10(m_X/MeV) = 0.014151317772708815*x_pdf - 6.9932501456724525`
- `log10(g_X) = -0.0329969798924973*y_pdf - 2.6510803066554596`

0080c frozen observational semantics:
- hard excluded: light blue (`Delta N_eff >= 0.4`) plus dark blue (`>=0.5`), 95% C.L.;
- green (`0.3 <= Delta N_eff < 0.4`) is **not** hard excluded and must not enter the geometry.

Majorana and Dirac are alternative neutrino-nature scenarios. They must remain separate outputs in this gate.

## Frozen vector-selection method
For each PDF independently:
1. verify pinned PDF SHA256;
2. inspect native vector drawing objects only; zero raster/manual coordinate input is allowed;
3. inventory exact source-native fill/stroke RGB tuples and drawing-object counts before selecting any exclusion object;
4. identify the light-blue and dark-blue region objects by exact source-native color identity, cross-checked against the primary caption ordering fixed in 0080c. Selection must be algorithmic and recorded in the raw JSON; no object may be chosen by visual proximity to an expected contour;
5. flatten selected vector curves with deterministic recursive Bezier subdivision. Use two frozen chord-error tolerances in PDF user-space: base `0.02 pt`, refined `0.01 pt`;
6. map all vertices to `(log10(m_X/GeV), log10(g_X))` using the 0080b transforms (`log10(m_X/GeV)=log10(m_X/MeV)-3`);
7. clip only to the physical plotting rectangle recovered from 0080b major tick extrema: `-9 <= log10(m_X/GeV) <= 0` and `-17 <= log10(g_X) <= -3`. Clipping to this already-published panel support is allowed; no other clipping/window selection is allowed;
8. construct the union of light-blue and dark-blue filled regions **within each scenario only**. Standard polygon union/intersection with the frozen plotting rectangle is allowed. Topology repair operations such as `buffer(0)`, convex hull, smoothing, manual node insertion/deletion, or result-selected snapping are forbidden;
9. record component count, validity, area in decade^2, bounds, selected source object IDs/colors, and boundary coordinates for both base and refined subdivision.

If the source vector encoding represents nested threshold regions as overlapping fills, their mathematical union is the hard-excluded region. If instead exact color identity does not determine the relevant native vector objects uniquely, classify BLOCKED rather than infer from shape.

## Frozen acceptance criteria
`PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_EXCLUDED_GEOMETRY` iff BOTH Majorana and Dirac satisfy all of:
- exact PDF SHA matches;
- selected light-blue/dark-blue source objects are uniquely identified by exact native color identity and caption semantics;
- at least one non-zero-area excluded polygon is produced;
- every output polygon is valid without forbidden repair;
- base vs refined total area relative difference <= `0.005` (0.5%);
- base vs refined symmetric-difference area divided by refined union area <= `0.005`;
- every refined boundary-control point transformed back to PDF coordinates lies within `0.02 pt` of the native selected path set;
- no green/pink/red/orange object enters the selected hard-excluded geometry;
- no raster/manual coordinate was used.

`BLOCKED_COSMOLOGY_B_L_CMB_VECTOR_COLOR_IDENTITY` if exact source-native vector color/object identity is ambiguous or does not uniquely select the hard-excluded objects.

`SCIENTIFIC_FAIL_COSMOLOGY_B_L_CMB_EXCLUDED_GEOMETRY` if identity is deterministic but any frozen topology/refinement/boundary criterion fails.

`INFRASTRUCTURE_FAIL` only for source acquisition/parser/runtime failure before scientific classification.

## Forbidden
No green-region inclusion; no interpolation between `Delta N_eff=0.3` and `0.4`; no Majorana/Dirac union, intersection, preference, or weighting; no BBN geometry; no union with 0078c/0079a/other B-L families; no global-envelope claim; no BSM response/enhancement scan; no post-result tolerance change.

## Next action
PASS permits a separately preregistered **scenario-semantics/envelope gate** deciding how Majorana and Dirac alternatives should be represented in the external B-L ledger, before any cosmology/global union. BLOCKED/FAIL retires this vector-geometry route unless a genuinely new primary machine-readable representation changes the assumptions.
