# NMIR preregistration 0087g — restricted-below-1-eV completeness / final-lock audit

Date frozen: 2026-09-08
Status: PROSPECTIVE — frozen after authoritative 0087f classification and before any new restricted-domain completeness calculation or topology claim.

## Scientific question
What is the strongest scientifically defensible statement about the 0087 low-mass B-L partial-authority candidate when restricted to `m_V < 1 eV`, given that 0087f leaves the BBN family unresolved only at `1.0 .. 1.4057345497828417 eV`, while Cerdeño, COHERENT and finite-mass fifth-force support routes remain source-authority BLOCKED rather than cleared?

This is a completeness/final-lock audit, not a new cross-family exclusion construction and not a BSM response scan.

## Frozen inputs / provenance
Use only accepted immutable NMIR authority through 0087f:
- 0087/0087a partial-authority topology/stress results;
- 0087b missing-family mass-support threat ranking and target `6.845530367110015e-6 .. 1.4057345497828417 eV`;
- NA64 `PROVABLY_MASS_DISJOINT` only for the 0087b low-mass target;
- 0087c `BLOCKED_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY`;
- 0087d `BLOCKED_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY`;
- 0087e `BLOCKED_FIFTH_FORCE_FINITE_MASS_SUPPORT_AUTHORITY`;
- 0087f `BLOCKED_BBN_TAIL_ACTIONABILITY_AUTHORITY` with unresolved BBN overlap only `>=1 eV` under the accepted 0087b support statement.

No blocked family is to be treated as zero constraint.

## Frozen criteria
### PASS — scoped certification only
`PASS_RESTRICTED_BELOW_1EV_PARTIAL_AUTHORITY_CERTIFICATION`
may be returned only if the audit proves that a clearly named statement is valid on a precisely stated subdomain below 1 eV using accepted geometries and threat classifications, while explicitly carrying unresolved Cerdeño/COHERENT/fifth-force families as completeness caveats. PASS cannot use the words global, complete external envelope, or fully allowed region unless every applicable family is actually cleared on that subdomain.

### BLOCKED
`BLOCKED_RESTRICTED_BELOW_1EV_COMPLETENESS`
if unresolved family support could overlap the restricted domain and no accepted authority proves disjointness or irrelevance. In that case no complete allowed-region claim is permitted; retain only partial-authority topology language.

### SCIENTIFIC FAIL
`SCIENTIFIC_FAIL_RESTRICTED_AUTHORITY_CONSISTENCY`
only for a direct contradiction among accepted immutable authority under the same definitions.

### INFRASTRUCTURE FAIL
Use `INFRASTRUCTURE_FAIL_*` for missing/corrupt ledgers, inconsistent hashes, parser/runtime errors, or inability to reproduce required accepted inputs.

## Frozen guards
- no blocked-family-as-null assumption;
- no BBN extrapolation below or above source-authorized support;
- no finite-mass extrapolation of fifth-force asymptote;
- no COHERENT or Cerdeño mass-support interpolation from insufficient ticks;
- no raster/OCR/manual digitization;
- no Majorana/Dirac or T/L union;
- no claim of a complete global B-L envelope;
- no BSM response/enhancement unlock.

## Frozen next action
If PASS scoped certification: preserve the exact caveated statement and proceed to a formal BSM-lock status audit, which remains expected to stay LOCKED unless a complete external envelope exists.
If BLOCKED: record that current authority supports only partial-authority topology, not a complete allowed component, and return to other physically actionable NMIR frontiers rather than manufacturing missing constraints.
If SCIENTIFIC FAIL: reconcile the conflicting immutable authority before further work.
