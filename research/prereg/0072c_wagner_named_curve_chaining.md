# NMIR 0072c preregistration — Wagner named B-L curve chaining and physical transform

Date frozen: 2026-09-07
Parent: 0072/0072a primary Wagner vector materialization.
Prerequisite result: 0072b `PASS_WAGNER_AXIS_CALIBRATION`; authoritative transform is `data/wagner_axis_calibration_0072b.json` and must not be refit in this gate.

## Scientific question
Can the named left-panel 95% CL vector-Yukawa B-L upper-bound curves in Wagner et al. Figure 6 be recovered directly and reproducibly from the hash-pinned EPS vector command stream, without raster digitization or secondary-contour authority?

## Frozen source/geometry
- Primary EPS SHA256: `4adafc21e896aa3e19490a586e9249fb9b7c947ad9cbe9efd3416d5e00466882`.
- Left-panel EPS box: `x=[1.681,6.681]`, `y=[0.844,4.844]`.
- Curve stroke width in the primary GRAF EPS: `0.010` EPS units.
- Exact curve colors from primary vector geometry / printed source:
  - EW, EW94, EW99: blue `(0,0,1)`;
  - Princeton: red `(1,0,0)`;
  - Moscow: orange `(1,0.5,0)`;
  - two LLR constraints: magenta `(1,0,1)`.
- Primary caption states these are 95% CL **upper bounds** on `|alpha_tilde|`; excluded sense is above the relevant bound.

## Frozen extraction algorithm
1. Reparse the primary EPS with the already hardened parser; require the EPS SHA match exactly.
2. Retain only two-point stroked segments with line width exactly `0.010` within the left-panel box and one of the four frozen curve colors above. Do not use fill paths, text/glyph strokes, black axes, or any right-panel segment.
3. Preserve original EPS file order. Chain adjacent retained segments only when the previous endpoint and next start point agree to `<=1e-9` EPS coordinate units. Never bridge a discontinuity, even if two pieces look visually close.
4. Drop only chains with fewer than 3 connected segments as non-curve fragments; record every dropped fragment in the machine-readable ledger. No other result-dependent cleanup is allowed.
5. Primary Figure 6 contains seven named left-panel constraints: three blue chains (`EW`, `EW94`, `EW99`), one red (`Princeton`), one orange (`Moscow`), and two magenta (`LLR_precession`, `LLR_inverse_square`). A color family is identity-resolved only if the connected long-chain topology permits this published multiplicity without merging disconnected chains.
6. Blue identity is assigned by pointwise vertical ordering where all three overlap: `EW99` is weakest/highest `|alpha|`, `EW94` intermediate, `EW` strongest/lowest. The assignment must remain order-consistent on their common domain except at exact crossings explicitly present in the source; otherwise identity is ambiguous.
7. The two magenta LLR chains remain separately labelled by the primary caption's geometry: the left-range chain is anomalous lunar-orbit precession and the right-range chain is the earth-moon differential-acceleration/inverse-square-law constraint. Do not merge them.
8. Transform every accepted EPS vertex only with the frozen 0072b affine maps. Then convert with the already frozen relations
   `|g_BL|=2.70463357586823e-19*sqrt(|alpha_tilde|)` and
   `m_V[eV]=1.973269804e-7/lambda[m]`.
9. Round-trip each transformed point back to EPS coordinates and require maximum absolute coordinate residual <= `1e-9` EPS units apart from floating-point serialization.

## Classification
- `PASS_WAGNER_B_MINUS_L_VECTOR_CONTOURS_MATERIALIZED` only if all seven published named constraints are resolved, transformed and round-trip validated under the rules above.
- `PARTIAL_PASS_WAGNER_VECTOR_CURVES` if at least one primary named curve is unambiguous and valid but the full seven-curve identity set is not; only individually validated curves may enter later envelope work.
- `SCIENTIFIC_FAIL_VECTOR_CURVE_IDENTITY` if connected-path topology or ordering cannot support a source-consistent named assignment.
- `INFRASTRUCTURE_FAIL` only for download/parser/runtime failure before scientific topology can be evaluated.

## Envelope guard
This gate does not yet create a global B-L allowed region. On full or partial PASS, a later gate may take the pointwise strongest upper bound only across individually validated primary curves and only within their connected domains. No interpolation across disconnected chains and no secondary curve may fill a gap.

## Next action
On full PASS, record the first primary machine-readable Wagner B-L contour family and advance 0072 to remaining direct-detection/cosmology/stellar families. On partial PASS preserve the valid subset and pursue the independent PandaX/De-Romeri route for missing controlling coverage. On identity FAIL preserve the negative result and switch to that independent route. No NMIR BSM enhancement scan is authorized by this gate.
