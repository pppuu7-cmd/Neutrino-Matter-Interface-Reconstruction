# Iteration 0090b-r1 — pre-authority orchestration failure

Date: 2026-09-08
Parent prereg: `research/prereg/0090b_g9_endpoint_regularized_radial_measure_authority.md`, frozen commit `c46110eecf6fae9719d37f8f3a378206c2706324`.
Execution head: `c4866c8f978e26aa28069e32bfd7e1017d24568e`.
Run: `34265503415`.
Job: `102193714710`.

## Classification
`INFRASTRUCTURE_FAIL_G9_0090B`.

This run did not execute the authority calculation and produced no `g9_0090b_result.json` artifact. Therefore it has no scientific PASS/BLOCKED/FAIL authority for 0090b.

## Observed failure
The dedicated pytest stage executed the preregistered scientific H1/H2 threshold through `evaluate_pair` before the authority script. It stopped on the fixed analytic control `s=1 cm, d/s=1.1` with:

`Blocked: endpoint-regularized normalization exceeds frozen threshold: unit-control`.

Pytest summary: `1 failed, 3 passed`.
The subsequent authority step was skipped, hash step found no result JSON, and artifact upload failed because the file did not exist.

The diagnostic is retained, but it is not promoted to a scientific BLOCKED classification because the workflow never produced the preregistered authority payload.

## Interpretation
The failure is orchestration/preflight scope, not a justification to change the science contract. Unit tests were allowed to preempt the authority evaluator by enforcing H1/H2 directly. This repeats the class of separation problem already encountered in 0090a preflight.

No scientific setting is changed by this record: orders remain L=32/H=64, normalization and L/H thresholds remain `2e-10`, scale threshold remains `2e-12`, all analytic controls and all 90 physical source geometries remain fixed, and the PASS/BLOCKED/FAIL taxonomy is unchanged.

## Next action
Freeze a prospective orchestration-only amendment before the next execution. Preflight may test finite/positive code-path and exact algebraic endpoint/support identities but must not carry H1-H3 authority. The unchanged authority script must be allowed to execute and write its payload; any H1-H3 miss there is then `BLOCKED_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE`, not infrastructure failure.
