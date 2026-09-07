# NMIR preregistration 0084b — Shin–Yun SN1987A analytical geometry/convention authority

Date frozen: 2026-09-08
Parent authority: 0084a `PASS_SHIN_YUN_SN1987A_BAND_SEMANTICS`.

## Scientific question
Can the exact Shin–Yun source-native low-mass SN1987A exclusion be mapped into reproducible finite-area analytical geometry without raster/manual digitization, post-result convention changes, or extrapolation beyond the domain where both exclusion boundaries are explicitly source-authorized?

## Frozen inputs/provenance
- Primary source: Shin & Yun, arXiv `2110.03362v2`.
- Exact source archive SHA256: `7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd`.
- Parent semantic authority: 0084a immutable record `research/iterations/0084a_shin_yun_sn1987a_band_semantics.md`.
- Global NMIR F8 mass clip remains `1e-6 eV <= m_V <= 10 GeV`; geometry may use only the overlap with source-authorized domains.

## Mandatory pre-geometry authority audit
No area calculation may start until all four items below are resolved machine-readably.

1. **Coupling convention.** Extract exact primary-source definition of the `U(1)_{B-L}` coupling `e'` and determine whether the NMIR ledger variable `g_BL` is exactly the same Lagrangian coupling under the repository convention. PASS requires an explicit algebraic identity, not plot proximity or assumed notation. If a non-unit conversion is required, freeze it prospectively from source equations.

2. **Electron-mass constant.** If BODY_NATIVE `<2m_e` is converted to MeV, use an externally authoritative electron rest-energy value frozen before geometry. The implementation must store source, numerical value and units. No rounded `2m_e=1 MeV` substitution is allowed for BODY_NATIVE.

3. **Source-domain variants.** Compute and retain two distinct variants rather than silently selecting one:
   - `BODY_NATIVE`: high-coupling branch valid only for `m_V < 2m_e` using the frozen electron-mass constant;
   - `CONCLUSION_SUMMARY`: high-coupling branch valid only for `m_V < 1 MeV` exactly as summarized by the source.
   They may be compared, but may not be merged into one authority in 0084b.

4. **No high-mass extrapolation.** For `m_V` above the respective low-mass high-coupling-domain endpoint and below `20 MeV`, exact source text states the lower/high-coupling bounds weaken. Therefore 0084b must not close a polygon there and must not extend the constant/product high boundary to `20 MeV`.

## Frozen analytical geometry
Only after the authority audit passes:

### Transverse
Within each variant's authorized low-mass domain, the source explicitly supplies a low/free-streaming boundary `e'=1e-11` and a high-coupling allowed boundary `e'=1.5e-8`. The finite excluded strip is the open interior between those boundaries, clipped only by the variant mass interval and NMIR global mass clip.

### Longitudinal
Within each variant's authorized low-mass domain, source text supplies the allowed low side `e' m_V < 7.4e-10 MeV` and allowed high side `e' m_V > 1.2e-5 MeV`. The finite excluded strip is the interior between the two product boundaries, with `m_V` expressed in MeV for these source-native products. No transverse/longitudinal union is authorized by 0084b; report them separately.

## Frozen outputs
For both BODY_NATIVE and CONCLUSION_SUMMARY, and separately for T and L:
- exact mass interval used, in eV and MeV;
- exact boundary formulas in source coupling and mapped NMIR coupling;
- finite log10-area in `decade^2` after NMIR global clip;
- polygon validity/non-self-intersection;
- boundary ordering at both mass endpoints;
- analytic area and independently sampled/numerical area cross-check, relative difference <= `1e-8` for straight/log-affine boundaries.

## PASS criteria
`PASS_SHIN_YUN_SN1987A_PARTIAL_ANALYTICAL_EXCLUDED_GEOMETRY` requires:
- source coupling convention resolved with no ambiguity;
- authoritative electron-mass provenance frozen if BODY_NATIVE is numerical;
- both domain variants retained separately;
- T and L geometries retained separately;
- no extrapolation above variant high-boundary domain;
- all polygons valid and positive-area;
- analytic-vs-numerical area relative difference <= `1e-8`;
- no boundary-order reversal inside authorized intervals.

## BLOCKED criteria
`BLOCKED_SHIN_YUN_SN1987A_ANALYTICAL_GEOMETRY_AUTHORITY` if coupling convention cannot be proven, electron-mass provenance cannot be frozen, or source semantics are insufficient to define a finite low-mass strip without an unregistered assumption.

## SCIENTIFIC_FAIL
Use only if the prospectively defined analytical region is internally inconsistent, e.g. high/low boundaries reverse inside the authorized domain, after units and convention are validated. Infrastructure/parser failures are not scientific FAIL.

## Guards
- No raster/OCR/manual digitization.
- No post-result choice between BODY_NATIVE and CONCLUSION_SUMMARY.
- No treating source rounded `2m_e \simeq 1 MeV` as exact identity.
- No high-coupling-bound extrapolation from `<2m_e`/`<1MeV` to `20MeV`.
- No T/L union.
- No union with Hong, cosmology, solar CEvNS, fifth-force, COHERENT or Wagner in this gate.
- No global B-L envelope claim and no BSM response/enhancement scan.

## Frozen next action
PASS -> record immutable 0084b partial finite-area authorities for the four separate branches/variants, then choose the next missing 0071 class-level authority; any later envelope composition requires a separate preregistered union/coverage audit. BLOCKED/FAIL -> retain 0084/0084a analytical semantics only and move to another missing 0071 family.
