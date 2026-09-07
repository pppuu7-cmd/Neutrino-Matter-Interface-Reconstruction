# NMIR iteration 0083a — Hong B-L analytical branch/scope identity

Date: 2026-09-08
Parent preregistration: `research/prereg/0083a_hong_bl_branch_scope_identity.md`.
Parser-conformance amendment: `research/amendments/0083a_parser_scope_binding_correction.md`.
Final authoritative classification: **PASS_HONG_B_L_BRANCH_SCOPE_IDENTITY**
`NMIR_READINESS: 95%`.

## Scientific question
Can the distinct exact-source Hong–Shin–Yun `2012.05427v3` B-L numerical statements found in 0083 be deterministically separated into source-native physical branches, rather than being collapsed into one unconditional coupling bound?

Frozen source archive SHA256: `6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc`.

## Authoritative hosted provenance
Final conformance run:
- run `34169565633`
- head commit `8ca9c27971ff35ce4a9208a9a23467e136465e33`
- artifact `10035252686`
- GitHub artifact ZIP digest `sha256:25ad4efa8601239bc6d963a023ccf741f4ff3966e3884839ecc96bc825b1e056`
- independently downloaded ZIP SHA256 `25ad4efa8601239bc6d963a023ccf741f4ff3966e3884839ecc96bc825b1e056`
- raw JSON SHA256 `6b8244893c75611ea6a2fb1b7f22d4fd30d0133b7e2555f9ed624a22a33fb102`

Hosted workflow conclusion: `success`. Dedicated tests passed, scientific audit passed, artifact upload passed, and frozen classification enforcement passed.

Raw audit summary:
- `record_count = 7`
- `unresolved_count = 0`
- `constraint_branch_count = 3`
- `contradictions = []`

## Historical implementation failures retained
The first 0083a run `34169355131`, job `101886553079`, artifact `10035192991` returned a provisional `BLOCKED_*` string, but raw inspection showed source-statement scope-binding defects: semicolon truncation, missing LaTeX `\eta`, broad-context `eta` leakage and wrong precedence between conditional exclusion, compatibility and hint wording. Per the frozen preregistration this is retained as **INFRASTRUCTURE_FAIL_PARSER_SCOPE_BINDING**, not scientific authority.

The first conformance run `34169491112`, job `101886924553` stopped at regression tests before the scientific audit because the sentence splitter treated the decimal point in `0.1` as terminal punctuation. It produced no scientific artifact and is retained as infrastructure failure. The repair only excluded decimal points from sentence-terminal detection; no scientific criterion or number changed.

## Authoritative branch map
### A. General young-neutron-star low-mass constraint
- relation: `e' < 5e-13`
- observation scope: `general_young_NS`
- role: `constraint_bound`
- mass wording: `mass is lower than O(0.1 MeV)`
- no exact finite-mass endpoint is authorized.

### B. Cas A possible hint
- relation: `e' ~ 1e-13`
- observation: `Cas A`
- role: `possible_hint`
- mass wording: `mass around eV`
- this is explicitly not an exclusion.

### C. Cas A equation-level bound
- relation: `e' < 1e-13`
- observation: `Cas A`
- role: `constraint_bound`
- source label: `eq:B-L_keyresult`
- explicit condition: `eta = 1e-13`
- mass wording: `m_{gamma'} < T_c(n^3 P_2) = O(0.1 MeV)`.

### D. Cas A conservative bound
- relation: `e' < 5e-13`
- observation: `Cas A`
- role: `constraint_bound`
- source label: `eq:B-L_keyresult_conserv`
- no same-statement `eta` condition
- mass wording: `m_{gamma'} < T_c(n^3 P_2) = O(0.1 MeV)`.

### E. Cas A conditional additional exclusion
- relation: `1e-13 < e' < 5e-13`
- observation: `Cas A`
- role: `conditional_additional_exclusion`
- source label where present: `eq:B-L_keyresult_hint`
- explicit condition: `eta < 1e-11`
- source's otherwise/evidence wording remains a guard against treating the interval as an unconditional exclusion.

### F. Cas A standard-cooling compatibility statement
- relation: `e' < 5e-13`
- observation: `Cas A`
- role: `standard_cooling_compatibility`
- low-mass wording remains approximate `O(0.1 MeV)`
- this statement is not promoted to a new strict exclusion.

The source contains repeated conclusion-level conditional-exclusion wording consistent with branch E; no contradiction is created.

## Scientific consequence
0083a closes the ambiguity that prevented the two source-native numerical scales `1e-13` and `5e-13` from entering the ledger with correct qualifiers. They are **not contradictory** after the explicit observation/role/`eta` scopes are retained.

The strongest source-defined Cas A equation-level branch is therefore usable only as the qualified analytical statement `e' < 1e-13` under its source-native low-mass and `eta=1e-13` conditions. The conservative Cas A branch is `e' < 5e-13`. Neither produces finite excluded area because 0083 already established that the mass endpoint is only approximate `O(0.1 MeV)`.

`NMIR_READINESS` advances from 94% to 95% because a material external-constraint ambiguity class was reproducibly closed with exact primary-source branch identity. This is funnel maturity only, not probability of new physics or publication success.

## Exact next gate
Audit Shin–Yun `2110.03362v2` source text prospectively for the exact revision/supersession scope of SN1987A/NS1987A B-L constraints. The gate must determine which older branches are revised, what numerical relations and mass domains are source-text authoritative, and whether any statement applies to Cas A. No blanket Hong/Cas-A supersession is permitted without explicit primary-source authority.

## Guards
No raster/OCR/manual contour reading. No `O(0.1 MeV) -> 0.1 MeV` replacement. No unconditional use of the conditional Cas A interval. No hint-to-exclusion promotion. No cross-paper coupling conversion/union or blanket supersession. No BSM response/enhancement scan until the external envelope is separately unlocked.
