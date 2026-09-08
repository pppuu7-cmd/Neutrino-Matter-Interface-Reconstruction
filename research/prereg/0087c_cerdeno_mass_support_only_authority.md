# NMIR prereg 0087c — Cerdeño mass-support-only authority

Date: 2026-09-08

## Motivation
0087b localizes the robust low-mass topology candidate to
`6.845530367110015e-6 <= m_V <= 1.4057345497828417 eV` at the inward stress ceiling `log10(g_BL)=-5` and leaves Cerdeño stellar/SN transport as `UNRESOLVED_MASS_SUPPORT_THREAT`.

0082c retired the **full 2D vector contour route** because both-axis source-native calibration did not satisfy its frozen contract, especially the y axis. That does not logically imply that the x/mass support alone is unrecoverable. This gate asks the narrower question prospectively and does not reopen 0082c.

## Frozen primary bytes
- source: Cerdeño et al., arXiv `2106.11660v3`;
- archive SHA256: `f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d`;
- exact vector asset: `Figures/BL_constraints.pdf`;
- asset SHA256: `6557571159bd7d279e9b78e026c79c2974fd487db86dcf3f60b566e54318d07f`.

## Pre-existing facts, frozen before 0087c
0082b established that the asset is a one-page source-native vector PDF with no image XObjects and that a mediator-mass axis identity exists. 0082c-r1 did **not** promote its provisional x candidate set because the broader two-axis contract retained residual exponent-fragment/sign ambiguity; the y axis independently blocked the full route. No provisional 0082b/0082c numerical x endpoints are imported into 0087c.

## Scientific question
Can the exact primary source certify a finite mediator-mass support interval for the published B-L constraints **without using y-axis information, curve/path/color identity, raster/OCR/manual reading, or visual sign recovery**?

## Frozen authority routes
Evaluate the routes in this order and report both independently.

### Route A — explicit source-text mass interval
Search exact TeX source members after comment stripping for a statement that explicitly gives both lower and upper mediator-mass endpoints for the B-L constraint figure/analysis, with unambiguous units. PASS_A requires:
1. both finite positive endpoints are explicitly present in source text;
2. the text/caption context identifies the B-L constraint figure or the same B-L mediator parameter;
3. no endpoint is inferred from qualitative words such as `light`, `small`, `below`, `up to` unless a numerical bound with unit is syntactically attached;
4. no cross-paper conversion is required.

### Route B — source-native x-axis/frame authority
If Route A does not PASS, use only PyMuPDF text spans plus vector geometry of the plot frame, under these frozen rules:
1. source-native mass-axis identity must be present in PDF text and include the mediator-mass symbol plus a physical mass unit;
2. select candidate major ticks only from a bottom horizontal band `yc >= 0.75*page_height` and central plot-width band `0.05W <= xc <= 0.95W`;
3. reconstruct powers of ten only from source-native adjacent text fragments using geometric adjacency; do not use raster/OCR or vector strokes to synthesize a missing sign;
4. require at least 3 distinct signed major tick anchors spanning at least 2 decades;
5. fit `log10(m/unit)=a*x+b` with positive slope and max absolute residual <= `0.015` decade;
6. require a source-native rectangular/scientific plot-frame candidate whose left/right x coordinates match the leftmost/rightmost accepted major tick anchors within `1.5` PDF points; alternatively an explicit source-text statement may identify that the plotted x range terminates at those anchors;
7. the finite support is exactly the two outer accepted frame-anchored x ticks, converted to eV by the explicit axis unit;
8. no use of y positions except to select the bottom x-axis band; no y tick values, curve paths/colors, legends, excluded sides or contour identities.

If multiple incompatible frame/tick solutions satisfy all criteria, Route B is BLOCKED rather than selected by visual plausibility.

## Threat comparison frozen before result
If a finite Cerdeño mass support `[a,b]` is certified, compare it to the 0087b target `[6.845530367110015e-6, 1.4057345497828417] eV` using the exact 0087b rule:
- `PROVABLY_MASS_DISJOINT` iff `b < target_min` or `a > target_max`;
- otherwise `MASS_OVERLAP_THREAT`, including endpoint contact.
Report logarithmic separation or overlap width.

## Classification
- `PASS_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY` if Route A or Route B uniquely certifies a finite positive interval and the threat comparison is computed.
- `BLOCKED_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY` if neither route supplies sufficient source-native authority or if multiple incompatible solutions remain.
- `SCIENTIFIC_FAIL_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY` only for an internal source inconsistency (e.g. independently authoritative A/B intervals contradict beyond tolerance), not for insufficient metadata.
- network/archive/parser/test failures before source evaluation are infrastructure failures, not scientific classifications.

## Guards
No resurrection of the 0082c 2D contour. No y-axis calibration. No curve/path/color/legend identity. No excluded-side assignment. No raster/OCR/manual digitization or visual sign recovery. No use of provisional 0082b endpoints. No cross-paper union or coupling conversion. No global B-L allowed-region claim. No BSM response/enhancement scan.
