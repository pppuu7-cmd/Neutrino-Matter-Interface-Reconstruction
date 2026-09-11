# NMIR 0105a q7 — prospective LAr primary-version-history test for F7

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Scope: F7 only; NONDISCOVERY authority audit.

## Frozen motivation

NMIR 0105a F7 asks for the exact semantic role/precedence of `3152` versus `3154` for the COHERENT CENNS-10 LAr Analysis-A steady-state-background input. Current primary sources inspected before this q7 freeze establish that the current COHERENT LAr data-release document and later arXiv paper versions use `3152 +/- 25`, while collaboration presentations visible in public metadata preserve `3154 +/- 25`. The arXiv submission history for COHERENT arXiv:2003.10630 labels version 4 with the author comment `fix typo in table 1`.

The target content of arXiv:2003.10630v3 has not been inspected for q7 before this freeze.

## Frozen authority chain

1. COHERENT Collaboration primary paper arXiv:2003.10630 version history.
2. arXiv:2003.10630v3 Table I (pre-v4 target).
3. arXiv:2003.10630v4 Table I (first version after the author-declared table-1 typo fix).
4. Final/current primary paper version only as a persistence check, not as a criterion-changing source.
5. COHERENT LAr data-release arXiv:2006.12659 only as an independent primary persistence check.

## Frozen PASS criterion for F7

`PASS_0105A_Q7_F7_PRIMARY_VERSIONED_PRECEDENCE_LOCATED_NONDISCOVERY` only if all are true:

1. v3 Table I explicitly contains `3154 +/- 25` for Analysis-A steady-state background (`SS`/`NSS`),
2. v4 Table I explicitly changes that same field to `3152 +/- 25`,
3. the arXiv version history explicitly identifies v4 as fixing a typo in Table I,
4. the corrected `3152 +/- 25` persists in the final/current primary paper and/or the collaboration LAr data release.

If all four conditions hold, F7 is resolved prospectively as: `3154` = pre-correction typo/obsolete value; `3152` = corrected authoritative Analysis-A steady-state-background input.

If any condition fails, F7 remains `BLOCKED_0105A_Q7_F7_PRIMARY_VERSIONED_PRECEDENCE_INCOMPLETE`.

Chronology alone, numerical agreement, presentations alone, or choosing the value that improves reproduction are explicitly insufficient.

## No-post-hoc guard

After this commit, v3 target content may be inspected. The four conditions above must not be weakened or reinterpreted in response to the result.
