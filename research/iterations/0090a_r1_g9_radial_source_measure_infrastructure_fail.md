# Iteration 0090a-r1 — G9 radial-source-measure authority preflight infrastructure failure

Date: 2026-09-08
Parent prereg: `research/prereg/0090a_g9_radial_source_measure_quadrature_authority.md`, frozen commit `fb4aad7d1ffe23fb4863d09e26c0c3b20f47364c`.
Execution head: `658d66fed23317b254cb05ffa60e81d0fee372dc`.
Run: `34254541976`.
Preflight job: `102156896866`.
Aggregate job: `102156980216`.
Artifact: `10067317090` (`nmir-g9-0090a-radial-source-measure`).

## Classification
`INFRASTRUCTURE_FAIL_G9_0090A`.

No scientific shard executed, so H0-H3 were not scientifically classified. The shard matrix was skipped after preflight failure. The aggregate found zero shard artifacts and correctly emitted the preregistered infrastructure class.

## Raw evidence
Dedicated preflight regression tests: `1 failed, 5 passed`. The failure was the arbitrary non-sentinel offset-disk normalization smoke case `(s,d,a)=(1.0,0.25,0.3)`: fixed order 64 returned `1.0000000616012095`, absolute normalization error `6.160120946674397e-08`, while that unit test had incorrectly applied the scientific H1 threshold `2e-10` to an arbitrary tuple.

Aggregate payload:
- `status = INFRASTRUCTURE_FAIL_G9_0090A`
- `reason = missing/duplicate shards: got=[] count=0`
- `shard_count = 0`
- `max_normalization_abs_error = null`
- `max_lh_discrepancy = null`
- `max_point_control_relative_error = null`.

## Artifact verification
GitHub-reported/upload-log ZIP SHA256: `7ad9d98d09e54d265ebded34cace0adf7c0a331d5b05e6810b384d322f98872f`.
Independent downloaded ZIP SHA256: `7ad9d98d09e54d265ebded34cace0adf7c0a331d5b05e6810b384d322f98872f`.
Inner `g9_0090a_result.json` SHA256: `3e9af10c702884d678e1bd53c588a8af967f209f0e94f8c92e2ecd9d72b59d1b`, matching raw aggregate log.

## Interpretation
This run is not scientific PASS, BLOCKED or FAIL for the 0090a method-authority question because no frozen sentinel was evaluated. The preflight test itself used a tuple outside the frozen 270-sentinel set. Its numerical miss is retained as a diagnostic, not hidden.

A prospective preflight-scope amendment was frozen before correction: `research/prereg/0090a_amendment_preflight_scope.md`. It permits only a loose arbitrary-tuple smoke assertion while preserving the exact scientific H1 `2e-10` threshold in `run_shard` for every frozen sentinel. Orders, intervals, sentinels, H0-H3 thresholds and scientific taxonomy are unchanged.

## Next gate
Correct only the preflight regression scope per the prospective amendment, rerun hosted 0090a, and classify solely from frozen scientific shard outputs plus raw logs and independently verified aggregate artifact.
