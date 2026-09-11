# 0105a6q5e — Argon semantic-contract adjudication preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5E`
Scope: authority/semantic adjudication only; NONDISCOVERY.

## Prospective timing and parent

This adjudication is preregistered **before inspection of the hosted q5d semantic-evidence artifact**. Execution is contingent on q5d validating as `PASS_0105A6Q5D_BOUNDED_SEMANTIC_EVIDENCE_INVENTORY_COMPLETE_NONDISCOVERY`. Parent four-file byte identity is the immutable q5c1 PASS record commit `908038bcff4f6f1c6554dbb03c1ce339546d9173`.

q5e may use only the complete q5d preregistered E1–E6 evidence inventory from all four exact q5c1 files. It may not introduce new lexical searches or inspect additional release files after seeing q5d.

## Frozen questions

The gate adjudicates four previously unresolved implementation questions independently; absence or ambiguity is BLOCKED, never filled by convention.

### F1 — elementary observation/count law
PASS only if the bounded authority evidence explicitly and uniquely specifies or implements the elementary statistical law for the Analysis-A observation/pseudo-data count construction (e.g. Poisson vs fixed-total/multinomial or another explicit law) sufficiently to distinguish total-count fluctuation behavior. Merely mentioning `extended`, RooFit, a likelihood, a generator, or event counts without an explicit law is insufficient.

### F4 — shape-systematic application contract
PASS only if the evidence explicitly specifies or implements how the published ±1σ shape alternatives enter the analysis: discrete external alternate fits/ensembles versus continuous interpolation/morphing, including enough direction/selection semantics to reproduce that treatment. Presence of shape/PDF/systematic labels alone is insufficient.

### F6 — simultaneous/correlation contract
PASS only if the evidence explicitly specifies or implements whether relevant nuisance/shape directions are fitted jointly/simultaneously with correlations/covariance, independently, or as separate external excursions, with enough information to avoid inventing correlation structure. Silence is BLOCKED.

### F7 — central-count anchor/precedence contract
PASS only if the evidence explicitly supplies a unique precedence/role rule sufficient to resolve any competing central CEvNS count anchors such as `3152` and `3154` when both are present. Numerical occurrence alone is insufficient; if no conflict is actually present in the complete evidence, this item may be `NOT_APPLICABLE_NO_COMPETING_ANCHORS` rather than inferred PASS.

## Frozen overall classes

For each F1/F4/F6 return exactly one of `PASS_EXPLICIT`, `BLOCKED_INCOMPLETE_OR_AMBIGUOUS`. For F7 allow those plus `NOT_APPLICABLE_NO_COMPETING_ANCHORS`.

Overall:
- `PASS_0105A6Q5E_ARGON_RELEASE_SEMANTIC_CONTRACT_SUFFICIENT_NONDISCOVERY` iff F1, F4 and F6 are all `PASS_EXPLICIT`, and F7 is either `PASS_EXPLICIT` or `NOT_APPLICABLE_NO_COMPETING_ANCHORS`.
- `BLOCKED_0105A6Q5E_ARGON_RELEASE_SEMANTIC_CONTRACT_INCOMPLETE` otherwise.
- `BLOCKED_0105A6Q5E_PARENT_EVIDENCE_INVALID` if q5d is not independently validated PASS or q5d/q5c1 provenance does not match.

No partial item PASS may be promoted to overall PASS if another required item remains incomplete.

## Evidence discipline

Every item judgment must cite exact q5d file + line/context-window identifiers used. No evidence outside q5d may be used. No code behavior may be inferred from variable names alone when the operative statistical rule is absent. No RooFit default, HEP convention, generic Wilks assumption, nuisance independence, morphing rule, or normalization precedence may be supplied manually.

## Authorization consequence

Even an overall q5e PASS would authorize only a separately prospectively preregistered standalone Ar null/systematics implementation gate. It does **not** authorize observed BSM residual inspection, model-family scans, or discovery claims.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`