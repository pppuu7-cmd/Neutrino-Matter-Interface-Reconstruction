# NMIR iteration 0082 — B-L stellar/SN primary source-asset authority

Date: 2026-09-08
Classification: **PASS_B_L_STELLAR_SN_PRIMARY_SOURCE_ASSET_AUTHORITY**
Prospective contract: `research/prereg/0082_bl_stellar_sn_primary_source_asset_authority.md`, frozen commit `bbf55baeeb013fbd5c273b75490c5e987aeceb81`.

## Result
All three prospectively frozen primary source archives were fetched in exact versioned form, hashed, semantically audited for explicit `U(1)_{B-L}` constraints, and found to contain source-native PDF figure assets referenced from their TeX source. No raster/manual digitization or contour geometry was used.

### Hong–Shin–Yun 2021 — arXiv 2012.05427v3
- Source archive SHA256: `6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc`
- Bytes: `2085288`
- Per-source status: `PASS_SOURCE_AUTHORITY`
- Explicit B-L / constraint semantics: PASS.
- Relevant source-native vector/document candidates include `B-LConstraints.pdf`, `money_teff_CCDK_B-L.pdf`, `money_lum_CCDK_B-L.pdf`, plus supporting neutron-star/cooling assets.
- The paper covers young-neutron-star cooling context including NS1987A/Cas A; exact curve scope is deferred to 0082a.

### Cerdeño et al. 2021 — arXiv 2106.11660v3
- Source archive SHA256: `f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d`
- Bytes: `336509`
- Per-source status: `PASS_SOURCE_AUTHORITY`
- Explicit B-L / SN1987A / medium-effect constraint semantics: PASS.
- Source-native PDF candidates include `Figures/BL_constraints.pdf`, `Figures/medium_effects_BL.pdf`, `Figures/medium_effects_BL_tot.pdf` and supporting vector/scalar comparison assets.

### Shin–Yun 2022 — arXiv 2110.03362v2
- Source archive SHA256: `7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd`
- Bytes: `392986`
- Per-source status: `PASS_SOURCE_AUTHORITY`
- Source-native revisit semantic check: **PASS**. The exact source contains B-L + SN1987A + revisit + transverse + longitudinal semantics required by the frozen contract.
- Source-native PDF candidates include `B-L_Constraints.pdf`, `NS1987A.pdf`, `spectral_SN1987A.pdf`, `NNbrem.pdf`, and `NNbrem_Internal_Contact.pdf`.

## Hosted provenance
- Scientific run/job: `34166836428 / 101879452299`
- Head SHA: `31d991298144f38f75357445397fab192667f74e`
- Artifact: `10034419759`
- Dedicated regression tests: `5 passed in 0.05s`
- Raw JSON SHA256: `f24f6e1d5f3726a1943b59cd298509b1b9304f21ba503defeb860461107467a7`
- Artifact ZIP SHA256: `decf86739ac910ed42cd0a836d8223e34a8ac16e1a9bb15cfa3740a9fbe97b77`
- Artifact bytes were independently downloaded after the run; ZIP and inner JSON hashes matched the hosted log/GitHub digest.
- Baseline CI on the same head SHA: run `34166836976`, `success`.

## Interpretation
This closes a provenance/source-asset uncertainty class: the stellar/SN B-L family has exact primary-source and machine-native figure routes, including the later Shin–Yun update. It does **not** yet create a numerical stellar/SN excluded polygon and does not authorize combining or superseding curves.

## Guards preserved
- No contour geometry was extracted.
- No raster/manual point picking.
- No assumption that a PDF is vector-native until separately inspected.
- No Hong/Cerdeño/Shin–Yun union/intersection.
- No claim that Shin–Yun supersedes all Hong young-NS/Cas-A results.
- No global B-L envelope or BSM response scan.

## Next gate
Prospectively preregister 0082a semantic/scope authority: determine from exact TeX captions/body which B-L constraint figure/curve is controlling for each physical observable, the coupling/mass convention, and the exact limited supersession/revision relationship. Geometry remains forbidden until that gate passes.

`NMIR_READINESS: 94%` — unchanged because no new excluded region has yet been materialized.
