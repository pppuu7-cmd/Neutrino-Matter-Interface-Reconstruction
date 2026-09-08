# NMIR iteration 0084b — Shin–Yun SN1987A analytical geometry authority

Date: 2026-09-08
Prospective contract: `research/prereg/0084b_shin_yun_sn1987a_analytical_geometry_authority.md`, frozen commit `6dd35ebe3b23846c30380e47b3cf14801fcd7313`.
Pre-geometry input freeze: `research/inputs/0084b_shin_yun_geometry_authority_freeze.md`, commit `3a1090d51c04b4a650065b5b104d2d29cd77c7bd`.
Final authoritative classification: **PASS_SHIN_YUN_SN1987A_ANALYTICAL_GEOMETRY_AUTHORITY**
`NMIR_READINESS: 97%`.

## Scientific question
Can the exact low-mass SN1987A B-L exclusion from Shin & Yun `2110.03362v2` be converted into reproducible finite log-plane geometry without raster/manual digitization, convention guessing, rounded `2m_e=1 MeV`, polarization merging, or extrapolation of the high-coupling branch toward 20 MeV?

## Authority frozen before geometry
### Coupling convention
The NMIR 0071 ledger defines

`L_int = g_BL V_mu J_{B-L}^mu`

with standard B-L charges. Shin & Yun Eq. (1) defines the source interaction coefficient as `e' A'_mu J'^mu`, defines `J'^mu` as the dark-current sum over charged fermions, and explicitly specializes the scenario used for the constraints to the anomaly-free B-L current. Therefore the prospective identity is

`g_BL = e'`

with exact multiplicative conversion factor `1` under the same canonical vector/current normalization. The hosted audit re-verified both source and NMIR-ledger identities before constructing geometry.

### Electron mass
The BODY_NATIVE endpoint uses the NIST/CODATA 2022 electron mass energy equivalent

`m_e c^2 = 0.51099895069(16) MeV`,

so the frozen deterministic central endpoint is

`2m_e = 1.02199790138 MeV = 1.02199790138e6 eV`.

The CONCLUSION_SUMMARY endpoint remains separately exactly `1 MeV`; the two variants are not merged or treated as identical.

## Hosted provenance
Authoritative run:
- run `34173289135`
- job `101897646086`
- head commit `d8a3cd6845ab39284aa3dbce8454f77c956b3d1d`
- artifact `10036398152`
- GitHub artifact ZIP digest `sha256:03a5566ccafec2e6dda99927b7abd63a0e5188b39b0b5d5d96ed06d95f7ff5ed`
- independently downloaded ZIP SHA256 `03a5566ccafec2e6dda99927b7abd63a0e5188b39b0b5d5d96ed06d95f7ff5ed`
- raw JSON SHA256 `483f6ad0864e10aee6fb16b6ab78ad97fbfb2a904bbd155d54fb51848ee0be7b`

All dedicated regression tests passed. The exact source-authority audit passed, the geometry calculation passed, the artifact uploaded successfully, and fail-closed classification enforcement passed.

## Source semantics carried from 0084/0084a
The excluded SN1987A region is band-like and must remain polarization-separated.

Transverse (`T`):
- low/free-streaming boundary: `g_BL = 1e-11`;
- high/trapping-side allowed boundary: `g_BL = 1.5e-8`;
- excluded interior lies strictly between them.

Longitudinal (`L`), with `m` in MeV:
- low/free-streaming boundary: `g_BL m = 7.4e-10 MeV`;
- high/trapping-side allowed boundary: `g_BL m = 1.2e-5 MeV`;
- excluded interior lies strictly between the corresponding curves.

The low-coupling source relations are stated below 20 MeV, but the high-coupling branch is only source-authorized below `2m_e` in the body and below `1 MeV` in the conclusion summary. Therefore 0084b closes finite polygons only inside the smaller high-coupling domain. No branch is extrapolated to 20 MeV.

## Authoritative finite geometry
Common lower clip: `m_V = 1e-6 eV`, inherited from the global 0071 interval.

### BODY_NATIVE — transverse
Mass interval:
`1e-6 eV <= m_V <= 1.02199790138e6 eV`.

Mass width:
`12.009450003998282 decades`.

Excluded area:
`38.14310918376516 decade^2`.

Independent sampled area:
`38.14310918376452 decade^2`.

Polygon/shoelace area:
`38.14310918376516 decade^2`.

Ordering is valid at both mass endpoints and numerical/analytic agreement is better than the frozen `1e-8` relative tolerance.

### BODY_NATIVE — longitudinal
Same mass interval and mass width.

Excluded area:
`50.559178355656044 decade^2`.

Independent sampled area:
`50.5591783556483 decade^2`.

Polygon/shoelace area:
`50.559178355656044 decade^2`.

The two product boundaries remain ordered at both endpoints; geometry is positive and valid.

### CONCLUSION_SUMMARY — transverse
Mass interval:
`1e-6 eV <= m_V <= 1e6 eV`.

Mass width:
`12.0 decades`.

Excluded area:
`38.113095108668176 decade^2`.

Independent sampled area:
`38.1130951086621 decade^2`.

Polygon/shoelace area:
`38.113095108668176 decade^2`.

### CONCLUSION_SUMMARY — longitudinal
Same mass interval and 12-decade width.

Excluded area:
`50.51939431579979 decade^2`.

Independent sampled area:
`50.519394315808036 decade^2`.

Polygon/shoelace area:
`50.51939431579979 decade^2`.

## Interpretation
0084b is the first reproducible finite-area Shin–Yun SN1987A materialization in the NMIR B-L ledger obtained entirely from analytical source statements rather than figure digitization.

The BODY_NATIVE and CONCLUSION_SUMMARY areas differ only because their upper mass endpoints are genuinely different source statements (`2m_e` versus `1 MeV`). The difference is preserved rather than optimized away. T and L are also retained as alternative polarization-specific exclusion objects; their areas must not be added or unioned absent a separate source-authorized composition gate.

This result closes a material stellar/SN geometry uncertainty class, so `NMIR_READINESS` advances from 96% to **97%**. This percentage measures funnel/reproducibility maturity, not probability that B-L new physics exists and not publication probability.

## What remains open
The global 0071 B-L envelope is still incomplete. In particular:
- no T/L union or cross-family union has yet been authorized;
- Hong exact finite-mass geometry remains blocked by approximate `O(0.1 MeV)` endpoints;
- Cerdeño vector geometry remains blocked/retired under the frozen no-raster contract;
- BBN geometry remains blocked;
- finite-mass continuation of the long-range fifth-force bound remains unauthorized;
- COHERENT benchmark/global contour authority remains incomplete;
- the previously identified Wagner/global-side authority remains unresolved.

BSM response/enhancement calculations therefore remain locked.

## Exact next gate
Advance F8 to the next reproducible missing family rather than prematurely composing partial regions. Highest value is to resolve the **Wagner/global-side B-L authority** (or, if source-native materialization remains impossible, explicitly retire that route) because the global envelope cannot be declared complete while its allowed/excluded-side semantics remain unresolved. Any later cross-family envelope composition must receive its own prospective contract after the surviving families are independently authoritative.

## Guards
No raster/OCR/manual contour reading. No post-result convention factor. No `2m_e = 1 MeV` exact identity. No high-coupling extrapolation to 20 MeV. No T/L union. No BODY_NATIVE/CONCLUSION_SUMMARY post-hoc selection. No union with Hong/Cerdeño/cosmology/fifth-force/direct-detection constraints in 0084b. No global B-L envelope claim and no BSM response/enhancement scan until separately unlocked.
