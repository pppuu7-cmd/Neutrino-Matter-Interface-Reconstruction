# NMIR iteration 0084 — Shin–Yun B-L source-text revision/supersession authority

Date: 2026-09-08
Prospective contract: `research/prereg/0084_shin_yun_bl_source_text_revision_scope.md`, frozen commit `f846cdaa01d7d42628549330823109061c46461a`.
Final authoritative classification: **PASS_SHIN_YUN_B_L_REVISION_SCOPE_AUTHORITY**
`NMIR_READINESS: 96%`.

## Scientific question
Can exact primary-source text in Shin & Yun `2110.03362v2` provide non-raster numerical B-L constraints for SN1987A/NS1987A and explicit revision/supersession scope suitable for the NMIR external-constraint ledger?

Frozen source archive SHA256: `7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd`.

## Hosted provenance
Final authoritative run:
- run `34171357240`
- job `101892123279`
- head `fc42470e0a431361279d0965f26067961308b386`
- artifact `10035801098`
- GitHub artifact ZIP digest `sha256:affa60027833b66607c08d6291f82bd5eb06a7ad4a15b5d38a07c8e6ddb637e2`
- independently downloaded ZIP SHA256 `affa60027833b66607c08d6291f82bd5eb06a7ad4a15b5d38a07c8e6ddb637e2`
- raw JSON SHA256 `6af4872374b8f0090d02476843e7a2fa79505c812f183129b7446e2a6c514db9`
- regression tests: `3 passed`.

Raw hosted audit summary:
- `record_count = 86`
- `coupling_record_count = 11`
- `bound_record_count = 11`
- `revision_record_count = 41`
- `unresolved_coupling_record_count = 0`.

The uploaded artifact was downloaded after the run, its ZIP SHA256 independently matched GitHub metadata, and the inner JSON independently matched the raw SHA256 printed by the job.

## Historical infrastructure/parser failures retained
1. Run/job `34171230773/101891766367` failed before any scientific audit because the fresh Python environment lacked `pytest`. No scientific result was produced. Classification: `INFRASTRUCTURE_FAIL_TEST_DEPENDENCY`.
2. Run/job `34171272174/101891883549`, artifact `10035775014`, produced a provisional `BLOCKED_SHIN_YUN_B_L_SOURCE_TEXT_AUTHORITY`, but raw artifact inspection showed that its two allegedly unresolved numerical records were the unrelated core-density value `3×10^14 g/cm^3` repeated in B-L contexts. The frozen contract requires accepted **B-L numerical relations**, not arbitrary nearby physical numbers. This run is retained as `IMPLEMENTATION_INVALID_NUMERIC_SCOPE_FALSE_POSITIVE`, not scientific BLOCKED. The repair narrowed accepted records to explicit source-native coupling relations; no scientific threshold, source, or PASS criterion changed.

## Authoritative source-text findings
### SN1987A — transverse polarization
The body explicitly states that the excluded SN1987A region has a low-coupling boundary

`e' < 1e-11` for `m_gamma' < 20 MeV`.

For masses above 20 MeV the source says the constraint becomes exponentially less stringent. The same source also states a high-coupling/trapping-side allowed branch:

`e' > 1.5e-8` is allowed for `m_gamma' < 2 m_e` in the body,

while the conclusion summarizes this as `m_gamma' < 1 MeV`.

Therefore `e'<1e-11` must **not** be misread as excluding every larger coupling. It is one boundary of a band-like SN1987A exclusion topology.

The conclusion explicitly says the SN1987A B-L constraint is **revisited** and that the transverse result is **an order of magnitude more stringent than the earlier derivation of Knapen et al.** This is source-native revision authority for that earlier SN1987A derivation only. It does not authorize blanket supersession of Hong Cas A or general young-NS branches.

### SN1987A — longitudinal polarization
The source states the low-coupling allowed/boundary relation

`e' m_gamma' < 7.4e-10 MeV` for `m_gamma' < 20 MeV`,

and the high-coupling allowed boundary

`e' m_gamma' > 1.2e-5 MeV`

for `m_gamma' < 2 m_e` in the body, summarized as `<1 MeV` in the conclusion. These product relations remain distinct from the transverse coupling-only branch; no merger or convention conversion is authorized by 0084.

### NS1987A
The source independently states

`e' < 1.5e-12`

for

`m_gamma' <= T_NS1987A = O(10^9 K) = O(0.1 MeV)`,

and explicitly says there is **no lower bound from NS1987A** because of the condensed profile. The cooling-curve discussion uses `eta=1e-7` as a fiducial choice and notes that a relatively large `eta >= 1e-8` is demanded to match the observationally inferred luminosity in the standard-cooling scenario.

The `O(0.1 MeV)` endpoint is approximate and remains forbidden as an exact finite-mass coordinate.

## Scientific consequence
0084 closes the source-text revision/scope uncertainty for the later Shin–Yun paper without raster/manual contour reading. The primary paper provides exact analytical SN1987A boundary relations and an NS1987A analytical bound, while its explicit revision language is scoped to the earlier SN1987A derivation it names. Hong Cas A remains separate.

The result does **not** yet create a global B-L excluded polygon. In particular:
- the SN1987A source has both low-coupling and high-coupling/trapping branches;
- body `<2m_e` versus conclusion `<1 MeV` wording must be handled prospectively before any exact low-mass band materialization;
- NS1987A has only an approximate `O(0.1 MeV)` mass endpoint;
- transverse and longitudinal branches are distinct.

A compact persistent ledger is stored in `data/shin_yun_bl_0084_authority.json`.

## Exact next gate
Prospectively audit the **0084a SN1987A analytical excluded-band semantics/body-vs-conclusion consistency** before computing any area or combining with other B-L families. The gate must determine, from exact source TeX only, whether the body `<2m_e` and conclusion `<1 MeV` lower/trapping-domain statements are compatible summary descriptions, what exact domain can be used without post-hoc strengthening, and which transverse/longitudinal inequalities define allowed versus excluded sides. No polygon area is permitted until that semantic gate passes.

## Guards
No raster/OCR/manual contour reading. No `O(0.1 MeV) -> 0.1 MeV`. No interpretation of the transverse `1e-11` boundary as excluding all larger coupling. No blanket Hong/Cas-A supersession. No transverse/longitudinal merger. No global-envelope union or BSM response/enhancement scan before separate unlock authority.
