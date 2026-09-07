# NMIR prereg 0083a — Hong B-L analytical branch/scope identity

Date frozen: 2026-09-08
Status: **PROSPECTIVE / NO 0083a CLASSIFICATION INSPECTED**
Parent: 0083 `PASS_HONG_B_L_SOURCE_TEXT_ANALYTICAL_ANCHOR / BLOCKED_HONG_B_L_EXACT_FINITE_MASS_TEXT_AUTHORITY`.

## Frozen authority
Use only Hong, Shin & Yun arXiv `2012.05427v3`, source archive SHA256 `6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc`, source-native `.tex` text only.

0083 established that exact source TeX contains at least the numerical B-L levels `1e-13` and `5e-13`, but does not authorize collapsing them into one unconditional global bound. 0083a asks whether those statements can be deterministically separated into source-native physical branches.

## Frozen extraction universe
Inspect every exact-source textual occurrence that contains an explicit B-L `e'` numerical inequality/range or an explicit `e' ~ ...` hint near B-L/Cas A/NS1987A cooling context. Bibliography-only occurrences are excluded. Figure geometry, raster/OCR/manual reading and values imported from another paper are forbidden.

For each candidate statement preserve the source excerpt and extract, when explicitly present:
1. numerical relation: upper bound, lower+upper interval, or approximate/hint value;
2. observational identity: `Cas A`, `NS1987A`, `SN1987A`, or `general_young_NS`;
3. role from the source wording:
   - `constraint_bound` — explicitly called a constraint/bound/exclusion;
   - `conditional_additional_exclusion` — a parameter interval excluded only under an explicit condition;
   - `standard_cooling_compatibility` — stated to cause little/no alteration or remain compatible with standard cooling, without treating that sentence alone as a new exclusion;
   - `possible_hint` — source says hint/implication/possibility rather than exclusion;
4. explicit `eta` condition/value/range if present in the same local statement;
5. mass-domain wording exactly as source text, including whether it is approximate `O(...)`, `~`, `lesssim`, or an exact inequality;
6. source equation label if an inequality is source-labelled.

## Frozen identity rules
A numerical B-L statement is **branch-resolved** only if the source text gives enough local information to assign its observational identity and role without looking at a figure.

The `1e-13` and `5e-13` levels may coexist without contradiction only if the source text explicitly distinguishes them by at least one branch key: observation, `eta` condition, role, or another stated physical assumption. Do not prefer the tighter number merely because it is smaller.

A `possible_hint` is never promoted to an exclusion. A `standard_cooling_compatibility` statement is never promoted to a strict exclusion unless the source explicitly says so in that same branch. Conditional exclusions retain their conditions.

## PASS/BLOCKED/FAIL
`PASS_HONG_B_L_BRANCH_SCOPE_IDENTITY` requires:
- every source-native numerical B-L statement relevant to the 0083 low-mass cooling anchor to be assigned a deterministic branch tuple;
- all distinct numerical levels to be mutually consistent after their branch conditions/roles are retained;
- at least one explicit source-defined `constraint_bound` branch suitable for a scenario-qualified analytical ledger anchor.

`BLOCKED_HONG_B_L_BRANCH_SCOPE_IDENTITY` if one or more distinct numerical levels cannot be assigned a unique observational/role/condition scope from source text alone, or if a figure is required to decide which branch a number belongs to.

`SCIENTIFIC_FAIL_HONG_B_L_BRANCH_SCOPE_IDENTITY` only if exact source text gives irreconcilably contradictory numerical statements under the same explicit branch tuple.

Parser/network/archive failure is infrastructure failure.

## Consequences
PASS -> record only scenario-qualified analytical Hong anchors. No exact excluded area is created because 0083 already blocked exact finite-mass materialization. Then prospectively audit Shin–Yun `2110.03362v2` source text for the exact revision/supersession scope of SN1987A/NS1987A branches, without assuming Cas A supersession.

BLOCKED/FAIL -> retain 0083 as source-text evidence but do not add a numerical Hong anchor to the global envelope; move directly to the later Shin–Yun primary source or another missing 0071 family.

## Guards
No raster/manual contour reading. No `O(0.1 MeV) -> 0.1 MeV` replacement. No cross-paper coupling conversion. No Hong/Cerdeño/Shin–Yun union/supersession claim. No BSM response scan.

`NMIR_READINESS: 94%` until a material uncertainty class is reproducibly closed.
