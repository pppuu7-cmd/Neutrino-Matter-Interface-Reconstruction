# NMIR iteration 0086c — NA64 unbroken-B-L vector geometry materialization

Date: 2026-09-08
Prospective contract: `research/prereg/0086c_na64_b_minus_l_vector_geometry_materialization.md`, frozen commit `e90f0cc7d9f79622f00c8cde2c1c5055ffa1aa7c` before inspecting vector path coordinates.
Final classification: **BLOCKED_NA64_B_L_VECTOR_AXIS_CALIBRATION**.
`NMIR_READINESS: 98%`.

## Exact frozen object
- arXiv archive `2606.17320v2`, SHA256 `4981fbe374836ed52c24c26955f90fa118295ff86aeab69f9f5f3449e60a3b9e`
- target `bminusl_unbroken.pdf`, SHA256 `d4b0ba8aa1cb05dad76f12c1fc6c8f98eb5c6e72dd53a6d47402b9d21b023393`
- source scenario: unbroken U(1)_{B-L}, Dirac neutrinos / three light RHNs, combined 2016–2022 NA64 dataset, 90% C.L.

## Diagnostic execution
The first diagnostic run failed before scientific inspection because PyMuPDF returned `width=None` for some drawing objects and the serializer attempted `float(None)`. This is classified **INFRASTRUCTURE_FAIL_VECTOR_PARSER_CONFORMANCE**, not a scientific result. Only `None -> safe numeric serialization` was changed; the frozen 0086c scientific contract was not altered.

Authoritative corrected diagnostic:
- head commit `0101f88bc0c835c7078e5e8c8d9f313b9e020615`
- run `34177656938`
- job `101910174970`
- artifact `10037802840`
- artifact ZIP SHA256 `e34cc96b9c75f910a91302d3527fbd30929f336579d1705773f4bdb6ce57cd52`
- raw JSON SHA256 `4c19f7e47c38b0844d53b3952a7faac85fe474be9f30345674e42ae098ac9c16`
- exact PDF structural inventory: 61 text spans, 51 drawing objects, 0 embedded images.

The corrected diagnostic itself performs no scientific classification, coordinate transform, interpolation, rasterization, OCR, or manual digitization.

## Source-native numerical tick anchors
The prospectively frozen rule requires at least **three distinct numerical tick anchors per axis** before an affine log-coordinate calibration can PASS.

The exact PDF text provides three major numerical x-axis anchors:
- `10^-2 GeV`, centered at PDF x ~= `71.1403541565`;
- `10^-1 GeV`, centered at PDF x ~= `238.5044631958`;
- `10^0 GeV`, centered at PDF x ~= `405.8685913086`.

Thus the x-axis satisfies the preregistered anchor-count requirement.

The exact PDF text provides only two major numerical y-axis anchors:
- `10^-5`, centered at PDF y ~= `260.0417175293`;
- `10^-4`, centered at PDF y ~= `119.5019645691`.

The PDF contains source-native minor y tick marks, but they do not carry printed numerical labels. They therefore cannot be promoted to additional **numerical tick anchors** under the frozen contract.

## Scientific classification
Because only two printed numerical y-axis anchors exist, the preregistered minimum of three is not met. Therefore 0086c must stop at:

**BLOCKED_NA64_B_L_VECTOR_AXIS_CALIBRATION**.

No post-result weakening from three anchors to two is allowed. Two points are mathematically sufficient to define an affine map, but using that fact now would alter the prospectively frozen validation criterion after observing the source object.

Curve-path identity and excluded-side materialization are not promoted to PASS because axis calibration is a mandatory upstream condition. No `(m_V,g_BL)` NA64 curve coordinates are accepted from 0086c.

## What this blocker means
This is not evidence against the NA64 B-L constraint and not a physics no-go. 0086b already proves the figure is a genuine source-native vector object. The blocker is narrower: the frozen high-redundancy axis-validation rule cannot be satisfied from this PDF alone.

A scientifically independent route remains legitimate if an official machine-readable table, collaboration data release, plotting data/code, HEPData record, or source statement supplies numerical coordinates/axis authority without relaxing 0086c.

## Guards preserved
- no raster/OCR/manual digitization;
- no visual clicking;
- no two-anchor post-hoc calibration;
- no interpolation/extrapolation;
- no scenario union;
- no cross-family composition;
- no BSM response scan.

## Next action
Audit independent official numerical-data channels for the exact NA64 unbroken-B-L 90% C.L. curve. If no independent source-native coordinates exist, retain collider/fixed-target as primary-authority-covered but numerically BLOCKED and proceed to a composition design that explicitly treats unavailable numerical families as non-composable rather than inventing coverage.
