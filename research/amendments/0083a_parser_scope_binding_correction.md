# NMIR 0083a post-run parser scope-binding correction

Date: 2026-09-08
Status: **INFRASTRUCTURE/PARSER CORRECTION ONLY; 0083a SCIENTIFIC CONTRACT UNCHANGED**
Parent preregistration: `research/prereg/0083a_hong_bl_branch_scope_identity.md`.
Affected first run: `34169355131`, job `101886553079`, artifact `10035192991`.

## Why the first 0083a classification is not scientific authority
The first hosted executable returned `BLOCKED_HONG_B_L_BRANCH_SCOPE_IDENTITY` with `contradictions=[]`, but raw-record inspection shows deterministic implementation errors in source-local scope binding:

1. The sentence splitter treated semicolon `;` as a terminal sentence boundary. In the exact Hong TeX, the conclusion statement containing `e' < 5e-13` continues after the semicolon to say that the volume emission causes little alteration of the standard cooling curve that fits Cas A. Truncating at the semicolon removed both the observational identity and the correct `standard_cooling_compatibility` role.
2. The `eta` extractor searched for literal `eta` but the source uses LaTeX `\eta`; therefore the explicit `\eta = 10^-13` condition attached to `eq:B-L_keyresult` was missed.
3. `eta_scope` was harvested from a broad context window after the local statement. This incorrectly attached unrelated nearby `eta > ...` conditions to `eq:B-L_keyresult_conserv`, whose own conservative inequality is stated without such an `eta` condition.
4. Role fallback used broad-context words such as `constraint`, which promoted the truncated standard-cooling compatibility sentence to `constraint_bound` even though its own wording says only that the new emission makes little alteration to the standard cooling curve.
5. For the interval `1e-13 < e' < 5e-13`, the implementation tested hint language before the explicit phrase `can be further excluded ... if eta < 1e-11`, causing the exclusion branch to be labelled `possible_hint` instead of retaining the source's conditional-exclusion role and its otherwise-hint wording.

These are parser/scope-binding implementation defects, not evidence that the source itself lacks branch identity. Under the frozen preregistration, parser failure is infrastructure failure. Therefore run `34169355131` is retained as **INFRASTRUCTURE_FAIL_PARSER_SCOPE_BINDING** and its `BLOCKED_*` string is not promoted to scientific authority.

## Frozen conformance repair 0083a-r1
The scientific question, source archive/hash, branch categories and PASS/BLOCKED/FAIL criteria remain unchanged. Permitted implementation repairs only:

- Define a source statement using `.`, `!`, or `?` as terminal punctuation; do not treat semicolon as a terminal boundary.
- Read observational identity and role from that full source statement first; only use a broader context to assign `general_young_NS` when the statement is an abstract-level general result and local preceding text explicitly establishes the young-NS scope.
- Parse both `eta` and LaTeX `\eta`, but attach `eta` conditions only when they occur in the same source statement as the numerical relation.
- Give explicit conditional-exclusion language (`can be further excluded`, `excluded ... if`) precedence over `otherwise ... evidence/hint`; preserve the otherwise/hint text as a guard, never as an unconditional exclusion.
- `standard_cooling_compatibility` takes precedence over broad-context constraint words when the same statement explicitly says the parameter choice causes little/no alteration and fits standard cooling.
- Equation labels remain source-native identifiers only; section labels must not be mistaken for equation labels.

No numerical threshold, scientific classification rule, source choice, mass endpoint, coupling convention or excluded-side interpretation may change.

## Guards
No raster/OCR/manual reading. No figure-path semantics. No `O(0.1 MeV) -> 0.1 MeV`. No cross-paper conversion, union or supersession. No BSM response calculation.

`NMIR_READINESS` remains 94% until a valid 0083a scientific classification is obtained.
