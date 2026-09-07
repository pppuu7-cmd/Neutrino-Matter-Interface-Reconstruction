# NMIR iteration 0084a — Shin–Yun SN1987A analytical excluded-band semantics

Date: 2026-09-08
Prospective contract: `research/prereg/0084a_shin_yun_sn1987a_band_semantics.md`, frozen commit `e3162927be26ca7e72b4a20440dbe6754393705a` before any 0084a result.
Final classification: **PASS_SHIN_YUN_SN1987A_BAND_SEMANTICS**.
`NMIR_READINESS: 96%`.

## Authoritative hosted evidence
Final run/job: `34171720462 / 101893145840`.
Head: `891db67c2af53fcf2f33713d7a8f509e4fdceb75`.
Artifact: `10035914608`, 2652 bytes.
GitHub artifact ZIP SHA256: `8ab3fd02571aa755a9303570fac907bc0be88d5a9cbf03e5e7a76c9a8e0b8aee`.
Independently downloaded ZIP SHA256: identical.
Raw JSON SHA256: `5e964a12dd8e54e6f94346cb07f489ec6b23f5ccac6ec94e71f2e02878e3f947`.
Independently extracted inner JSON SHA256: identical.
Regression suite: `3 passed in 0.03s`.
Frozen source archive SHA256: `7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd`.

All frozen semantic checks passed in the raw result: explicit SN1987A excluded-region wording; explicit reabsorption; transverse and longitudinal low/free-streaming values; transverse and longitudinal high-coupling values; body `<2m_e` allowed-domain statement; conclusion revision statement; conclusion high-coupling values; conclusion `<1 MeV` domain; and explicit `allowed` wording.

## Scientific result
The source does **not** define a one-sided “all larger coupling excluded” constraint. It defines a band-like SN1987A topology with a low/free-streaming side and a high-coupling reabsorbed/trapped allowed side.

Transverse source-native statements:
- low/free-streaming boundary: `e' < 1e-11` for `m_gamma' < 20 MeV`;
- high-coupling allowed side in body: `e' > 1.5e-8` allowed for `m_gamma' < 2 m_e`;
- conclusion summary: same coupling boundary `e' > 1.5e-8`, with mass wording `<1 MeV`.

Longitudinal source-native statements:
- low-side allowed/boundary: `e' m_gamma' < 7.4e-10 MeV` for `m_gamma' < 20 MeV`;
- high-coupling allowed side in body: `e' m_gamma' > 1.2e-5 MeV` allowed for `m_gamma' < 2 m_e`;
- conclusion summary: same product boundary, with mass wording `<1 MeV`.

The source body itself writes `2m_e \simeq 1 MeV`; however 0084a prospectively prohibited numerical conversion or choosing one formulation as the universal endpoint. Therefore the body `<2m_e` and conclusion `<1 MeV` remain two source-statement-conditioned domain descriptions until a separate gate freezes the electron-mass constant/convention policy.

Transverse and longitudinal branches remain separate. The product relation for longitudinal polarization may not be collapsed into the transverse coupling-only branch.

## Historical implementation-invalid runs
Run/job `34171573790/101892735690`, artifact `10035869701`, raw JSON SHA256 `31e5c3d3d0353c01f2c2bb015cc27823c5ed444825f5f5d953f03c1a12e7726e`, ZIP SHA256 `e426f2c3c38070883e75c8226fbb6615d954d641d40699933930f8c9339379be`: `IMPLEMENTATION_INVALID_TEX_CLAUSE_FALSE_NEGATIVE`. Raw output already contained controlling high-coupling tokens; regex clause-distance missed conclusion binding.

Run/job `34171635267/101892904188`, artifact `10035887716`, raw JSON SHA256 `04cf41ae826767d150b20e0a8cddeb72c12c92353e7bd2de3ed1db4c6763f2eb`, ZIP SHA256 `3b3c740c9d66b5d611807d62337414468880b8ef9405e6559b48163cf285ec58`: `IMPLEMENTATION_INVALID_CONCLUSION_BLOCK_FALSE_NEGATIVE`. Exact prose was present; parser anchor overfit TeX math markup. Scientific contract was unchanged.

## Consequence
0084a closes the excluded-side/topology ambiguity needed before any analytical finite-area materialization. It does **not** itself create a polygon or advance the global B-L envelope area. In particular, exact text alone does not supply a closed high-coupling branch all the way to 20 MeV: the source says the lower/high-coupling bounds weaken above the `2m_e` threshold. Therefore any later source-text-only polygon must restrict itself to a prospectively frozen domain where both sides are explicit, rather than extrapolating the high-coupling branch to 20 MeV.

Compact authority ledger: `data/shin_yun_band_semantics_0084a_authority.json`, commit `edbe1d8310842671d7974b61226fbd078f68ebad`.

## Exact next gate
Prospectively freeze 0084b before any finite-area computation. 0084b must audit/freeze: (i) exact source coupling convention `e'` versus NMIR `g_BL`; (ii) authoritative electron-mass constant provenance if `2m_e` is converted to MeV; (iii) separate BODY_NATIVE and CONCLUSION_SUMMARY mass-domain variants rather than silently selecting one; (iv) exact low-mass domain where both low and high boundaries are source-authorized; and (v) any plotting/global clip. Only then may a partial low-mass SN1987A analytical excluded-region geometry be computed.

## Guards
No raster/OCR/manual geometry. No extrapolation of the high-coupling branch to 20 MeV. No `2m_e -> 1 MeV` equality without separately frozen constant/tolerance policy. No source `e' -> g_BL` identity without convention authority. No branch merger, cross-family union, global envelope claim, or BSM response/enhancement scan.
