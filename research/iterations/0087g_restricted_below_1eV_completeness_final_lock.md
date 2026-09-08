# NMIR Iteration 0087g — restricted-below-1-eV completeness/final-lock audit

Date: 2026-09-08
Classification: `BLOCKED_RESTRICTED_BELOW_1EV_COMPLETENESS`
Preregistration: `research/prereg/0087g_restricted_below_1eV_completeness_final_lock.md`, frozen commit `6d844c292d902fc3f492f827d981e5760aa003c4` before the result-dependent audit.

## Scope
This gate asked whether the strongest currently accepted B-L authority can certify a precisely scoped allowed statement below 1 eV without silently treating source-authority blockers as null constraints. It did not introduce new exclusion geometry, interpolate blocked families, combine Majorana/Dirac or transverse/longitudinal scenarios, or authorize BSM response scanning.

Frozen domain: `6.845530367110015e-6 <= m_V < 1.0 eV`.

## Frozen classification result
The gate is BLOCKED under its preregistered completeness criterion.

Accepted authority establishes:
- NA64 is provably mass-disjoint from the 0087b low-mass target.
- The localized BBN support overlap identified by 0087b begins at 1 eV, so it does not overlap the strict below-1-eV subdomain.

However, three constraint families remain source-authority unresolved and no accepted authority proves them mass-disjoint or irrelevant on the strict below-1-eV domain:
- Cerdeño: `BLOCKED_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY`.
- COHERENT: `BLOCKED_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY`.
- finite-mass fifth force: `BLOCKED_FIFTH_FORCE_FINITE_MASS_SUPPORT_AUTHORITY`.

Therefore the accepted geometry may be described only as a restricted below-1-eV **partial-authority topology**. It is not a certified complete allowed component, not a global external envelope, and not an authorization for BSM response/enhancement calculations. No blocked family was set to zero.

## Hosted reproducibility evidence
Implementation commit: `e677dfa5a0dca83e068681b72455b108171a2283`.
Regression-tests commit: `9e8e804ba8c0041dbfe4ca8fb958c05d25d974ab`.
Workflow commit/head: `ee2b13df711da6a720c0b377dad9dc68e2c2d87b`.
Run/job: `34191935749 / 101951601761`.
Artifact: `10042503439`, `nmir-0087g-restricted-below-1ev-completeness`, 804 bytes.
Artifact ZIP SHA256: `3804d491f748c7e45de348e2010bc76a985d55b23400dc0d91e8862b3b34fd28`.
Raw JSON SHA256: `66b9e68296ef6dbffd2464506b17623e390750d83864a8e94652ecf9e0174d9a`.
Dedicated regression suite: `4 passed in 0.02s`.

The raw job log was inspected directly. The artifact ZIP was independently downloaded and hashed; its digest exactly matched GitHub artifact metadata and the upload log. The extracted JSON independently reproduced the workflow SHA256. Green CI alone was not treated as scientific evidence.

## Scientific interpretation
0087g closes the attempted B-L completeness/final-lock route negatively but cleanly. It does not disprove the partial low-mass topology; it proves that the current authority set is insufficient to certify it as complete even after restricting to masses below 1 eV. The missing-family caveats are therefore structural scientific blockers rather than documentation debt.

BSM response/enhancement remains `LOCKED`.

NMIR_READINESS remains 98% because this iteration localizes a completeness blocker but adds no new exclusion object and does not unlock a physical branch.

## Frozen next action
Return to another physically actionable NMIR frontier rather than manufacturing missing B-L constraints. Before any result-dependent calculation on that frontier, prospectively preregister the exact target, accepted inputs, formulas/units, PASS/BLOCKED/FAIL criteria, and scientific-versus-infrastructure taxonomy.