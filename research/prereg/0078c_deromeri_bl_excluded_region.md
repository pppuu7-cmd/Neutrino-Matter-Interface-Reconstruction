# Preregistration 0078c — De Romeri et al. combined solar-CEvNS B-L excluded region

Date frozen: 2026-09-07
Parent PASS: 0078b `PASS_COMBINED_SOLAR_CEVNS_B_L_VECTOR_CALIBRATION`, run/job `34154728073/101844079794`, head `0624c8d0fc4ad1c035dc7bc29b14876c3ab96443`, artifact `10030555477`, raw JSON SHA256 `785605b660efeabf13d1825bf8f66fa4a1e4d4f8675514c45f76cd036a5171de`.

## Frozen authority

Primary arXiv source `2603.00554` identifies the right-panel vector `B-L` **magenta shaded region** as the combined XENONnT + PandaX-4T + LZ 90% CL excluded region. Therefore 0078c does not infer `above` or `below` a line from geometry: the primary filled vector region itself is the excluded-side authority.

Frozen source archive SHA256:
`09ab22f753ac3f5fbde5be65ac50926de67b0638550366d158aadcfde8e92564`.

Frozen asset `vector_BL_PnX_XnT_LZ_combined.pdf` SHA256:
`ace761499623535907263e780a6e96a17474adf418d3f9363dae8e28bc5e7a39`.

Frozen 0078b affine calibration, not to be refit in 0078c:

- `log10(m_V/GeV) = 0.013440860603931617 * x_pdf - 6.171186200127133`
- `log10(g_BL) = -0.01803751809647103 * y_pdf - 1.3913180812870007`

Frozen physical plot domain:
`-5 <= log10(m_V/GeV) <= 1`, `-8 <= log10(g_BL) <= -2`.

Frozen magenta class is unchanged from 0078b: HSV hue `[285,345] deg`, saturation `>=0.35`, value `>=0.35`.

0078b observed exactly two scientific magenta drawings under that prospectively frozen class: one filled+stroked drawing and one stroke-only drawing. For 0078c, only filled scientific magenta geometry is eligible to define excluded area; the stroke-only object is a boundary-control object and is never used to choose excluded side.

## Scientific question

Can the primary filled magenta vector object be converted reproducibly into one or more closed excluded-region polygons in `(log10 m_V/GeV, log10 g_BL)` and clipped to the frozen plotted domain without manual interpretation or topology repair?

## Frozen reconstruction

1. Redownload and hash-check the exact source and asset.
2. Use the frozen 0078b affine calibration coefficients verbatim; do not refit ticks.
3. Enumerate vector drawings and select scientific magenta drawings using the same frozen HSV rule and the same 0078b scientific-span requirement (`>=2.0` decades in mass or `>=1.0` decade in coupling).
4. Require exactly one eligible scientific magenta drawing with non-null magenta fill. Zero or more than one is `PARTIAL_EXCLUDED_REGION_TOPOLOGY` unless primary semantics independently distinguish them without geometry-based choice.
5. Reconstruct ordered subpaths from PDF drawing items. Line segments are exact. Cubic Bezier items are sampled at both 32 and 64 equal parameter subdivisions; rectangles/quads are represented by their explicit corners.
6. A new subpath begins only when the next item start differs from the previous item end by more than `1e-6` PDF points. A candidate fill loop must close within `1e-5` PDF points (or be explicitly closed by the PDF drawing object); no artificial bridge longer than that is allowed.
7. Convert every loop with the frozen affine maps. Build polygons in physical log-space and require finite coordinates, positive area and valid simple polygon topology before clipping. No `buffer(0)`, smoothing, vertex sorting, convex hull, or post-hoc topology repair is allowed.
8. Clip each valid polygon by exact polygon/rectangle intersection to the frozen plot-domain rectangle. Retain polygonal components with positive area only.
9. Re-run the reconstruction with 32 and 64 cubic subdivisions. Require the symmetric-difference area between the clipped unions divided by the 64-subdivision union area to be `<=1e-4` and total clipped-area relative difference `<=1e-4`.
10. Require nonzero excluded area and at least one interior point whose point-in-polygon query is true and whose distance to the plot boundary is positive. Store polygons, areas and representative interior points.
11. Use the stroke-only scientific magenta drawing only as a boundary control: require at least 50% of its in-domain sampled points to lie within `0.05` decade Euclidean distance of the boundary of the filled excluded union. Failure is `PARTIAL_EXCLUDED_REGION_TOPOLOGY`, not permission to reassign the stroke.

## Combination audit in the same iteration

After the new solar-CEvNS excluded region is materialized, inspect existing primary B-L authorities already frozen in NMIR. A pre-existing family may be combined only if the repository already contains both reproducible physical geometry/numerics **and** explicit excluded-side authority in the same `(m_V,g_BL)` convention. A mere constraint line, a blocked likelihood route, or a family with unresolved semantic identity may not be promoted by assuming `above the line is excluded`.

Therefore 0078c can produce a **partial external envelope** even if the global 0071 envelope remains blocked.

## Prospective classifications

- `PASS_SOLAR_CEVNS_B_L_EXCLUDED_REGION`: filled primary magenta geometry passes closure/validity/clipping/subdivision/boundary-control gates and yields a machine-readable 90% CL excluded region.
- `PASS_PARTIAL_B_L_EXTERNAL_ENVELOPE`: additionally, the new region is combined with every previously materialized family that independently satisfies the geometry+side-authority requirement; this does not imply the full 0071 global envelope is complete.
- `PARTIAL_EXCLUDED_REGION_TOPOLOGY`: filled region is present but one frozen topology/boundary-control criterion prevents unambiguous materialization.
- `SCIENTIFIC_FAIL_EXCLUDED_REGION_TOPOLOGY`: exact primary fill cannot produce any valid nonzero excluded polygon under the frozen reconstruction despite successful source access.
- `INFRASTRUCTURE_FAIL`: source/package/runtime failure before scientific classification.

## Decision tree

PASS new region / partial envelope -> record `PASS_NEW_EXECUTABLE_SURVIVOR_BSM` as closed for this solar-CEvNS family, update recovery, and prospectively choose the next missing primary family needed for the global 0071 envelope. **Do not run any BSM response/enhancement calculation yet.**

PARTIAL/FAIL -> do not manually digitize or assume excluded side; retain the 0078b calibrated contour as the highest valid authority.
