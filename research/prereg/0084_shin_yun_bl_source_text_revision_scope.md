# NMIR preregistration 0084 — Shin–Yun B-L source-text revision/supersession authority

Date frozen: 2026-09-08
Parent authority: 0083a `PASS_HONG_B_L_BRANCH_SCOPE_IDENTITY`.

## Scientific question
Does exact primary-source text in Shin & Yun, arXiv `2110.03362v2`, provide machine-readable numerical B-L constraints for SN1987A/NS1987A and explicit revision/supersession semantics sufficient to update the NMIR external-constraint ledger without raster/manual contour reading?

## Frozen source and provenance
- Primary source: Shin & Yun, arXiv `2110.03362v2`.
- Exact source archive SHA256: `7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd`.
- Permitted evidence: exact source-native TeX/text files extracted from this archive only.
- Forbidden evidence: raster/OCR/manual figure reading, public-summary paraphrase used in place of source text, and post-result cross-paper convention repair.

## Frozen audit scope
The audit must inventory all source statements relevant to B-L constraints and bind each accepted numerical statement to the following tuple:
1. exact numerical relation as written by the source;
2. observation identity: `SN1987A`, `NS1987A`, both, or another source explicitly named in the same local context;
3. mediator mass-domain wording, retaining `O(...)`, approximate, inequality, or range semantics exactly as written;
4. assumption/scenario qualifiers explicitly stated in the local source context;
5. confidence/statistical qualifier if explicitly stated;
6. role: `constraint_bound`, `excluded_interval`, `possible_hint`, `compatibility_statement`, or another source-native role;
7. revision/supersession relation: whether the paper explicitly says an earlier bound is revised, weakened, strengthened, replaced, superseded, retained, or merely compared.

## Frozen scientific criteria
### PASS_SHIN_YUN_B_L_REVISION_SCOPE_AUTHORITY
Requires all of:
- exact source archive hash matches the frozen SHA256;
- at least one explicit B-L numerical constraint relation is found in source TeX;
- every accepted numerical relation has deterministic observation identity and local assumption/mass-domain binding;
- any claimed revision/supersession is supported by explicit source language, not inferred from chronology or curve placement;
- unresolved or contradictory branch assignments are zero for statements promoted to authority.

PASS may authorize only the scenario-qualified source-text anchors and explicit supersession scope stated by Shin–Yun. It may not create finite-area geometry by itself.

### PASS_SHIN_YUN_B_L_ANALYTICAL_ANCHOR_ONLY
If source-native numerical constraints are explicit and branch-resolved but revision/supersession wording is absent or insufficiently explicit, retain the analytical anchors while classifying cross-paper supersession as BLOCKED.

### BLOCKED_SHIN_YUN_B_L_SOURCE_TEXT_AUTHORITY
Use when exact source text lacks sufficient numerical/observation/assumption binding for a non-ambiguous analytical ledger entry, or when contradictory candidate mappings cannot be resolved without figure/manual interpretation.

### SCIENTIFIC_FAIL
Use only if the source explicitly contradicts a required physical/source premise of this gate after exact-source verification. Parser/network/archive failures are not scientific FAIL.

## Infrastructure vs scientific failure
- archive download/hash mismatch, extraction failure, parser crash, serialization failure, or regression-test failure before a valid audit result -> `INFRASTRUCTURE_FAIL`;
- parser false negative demonstrated by raw source context -> implementation defect, not scientific BLOCKED/FAIL; fix parser without changing this contract and rerun;
- green workflow alone is not PASS; raw log and artifact must be inspected against this preregistration.

## Guards
- No raster/OCR/manual contour reading.
- No conversion of approximate mass wording such as `O(...)` into an exact endpoint.
- No blanket supersession of Hong Cas A, general young-NS, or any Cerdeño branch unless Shin–Yun explicitly names that scope.
- No promotion of hints or compatibility language to exclusions.
- No post-result convention factor or coupling remapping.
- No finite-mass polygon or global envelope union/intersection in 0084.
- BSM response/enhancement remains locked.

## Frozen next action
- PASS with explicit revision scope -> record immutable 0084 result; update ledger/recovery; then preregister the next missing 0071 family or, only if exact finite-mass source authority exists, a separate geometry/materialization gate.
- analytical-anchor-only PASS -> record anchors, keep supersession BLOCKED, and move to the next missing 0071 family.
- BLOCKED/FAIL -> preserve all earlier Hong/Cerdeño authority unchanged and move to the next missing executable 0071 family.
