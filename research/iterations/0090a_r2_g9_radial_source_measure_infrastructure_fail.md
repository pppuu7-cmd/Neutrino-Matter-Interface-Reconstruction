# Iteration 0090a-r2 — preflight infrastructure failure before scientific shards

Date: 2026-09-08
Parent prereg: `research/prereg/0090a_g9_radial_source_measure_quadrature_authority.md`, frozen commit `fb4aad7d1ffe23fb4863d09e26c0c3b20f47364c`.
Execution head: `b83a1fd9735968cfe51d2a56796f1659745d8251`.
Run: `34259349490`.
Preflight job: `102173102348`.
Aggregate job: `102173177050`.
Aggregate artifact: `10069211847`.

## Classification
`INFRASTRUCTURE_FAIL_G9_0090A`.

No scientific shard executed; the shard matrix was skipped after preflight failure. Consequently H0-H3 have no scientific classification in r2.

## Raw preflight evidence
Dedicated tests: `1 failed, 5 passed`.
The arbitrary non-sentinel offset normalization smoke test failed at `(s,d,a)=(1.0,2.0,0.4)`: order-64 result `1.000001887844265`, absolute error `1.8878442649139515e-06`, larger than the provisional non-scientific smoke threshold `1e-6`.

This tuple is not one of the frozen 270 scientific sentinels. The numerical diagnostic is retained but has no authority to classify scientific H1.

## Raw aggregate evidence
- `status = INFRASTRUCTURE_FAIL_G9_0090A`
- `reason = missing/duplicate shards: got=[] count=0`
- `shard_count = 0`
- `max_normalization_abs_error = null`
- `max_lh_discrepancy = null`
- `max_point_control_relative_error = null`
- aggregate JSON SHA256 from raw job log: `f3d72c0aafea7d8a443275b5527871850a03053616542ad4c674ca83e5184a1d`.

## Independent artifact verification
Artifact `10069211847` was independently downloaded.
- ZIP SHA256: `81b0116ca717229fce7a4128fa587129dca56c36c08b23f2c946f491eeaa72ee`, exactly matching the Actions upload digest.
- inner `g9_0090a_result.json` SHA256: `f3d72c0aafea7d8a443275b5527871850a03053616542ad4c674ca83e5184a1d`, exactly matching the raw aggregate log.

## Prospective correction
Before any next execution, amendment 2 was frozen at `research/prereg/0090a_amendment2_preflight_no_accuracy_gate.md`: arbitrary preflight tuples are code-path sanity only and may assert finite/positive output, but no non-scientific accuracy-to-unity threshold. Scientific `2e-10` normalization, 32x32/64x64 orders, sentinel set, convergence threshold and taxonomy remain unchanged in `run_shard`.

## Next gate
Apply only the preflight correction from amendment 2 and allow the frozen scientific shard set to execute. Consume every shard raw log and aggregate artifact before classification. Any frozen-sentinel normalization miss above `2e-10` remains a scientific BLOCKED condition; it must not be reclassified as infrastructure or relaxed.
