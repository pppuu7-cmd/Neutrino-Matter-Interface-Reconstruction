# 0090a amendment 2 — preflight carries no non-scientific quadrature accuracy gate

Date: 2026-09-08
Parent prereg: `research/prereg/0090a_g9_radial_source_measure_quadrature_authority.md`, frozen commit `fb4aad7d1ffe23fb4863d09e26c0c3b20f47364c`.
Prior preflight-scope amendment: commit `7825b28a015a0dca31188f2a5057d83373596c84`.
Observed r2 before this amendment: run `34259349490`, head `b83a1fd9735968cfe51d2a56796f1659745d8251`.

## Frozen interpretation of r2
The hosted workflow again stopped in preflight before any scientific shard. The arbitrary smoke tuple set included `(s,d,a)=(1.0,2.0,0.4)`, for which fixed order-64 radial normalization differed from unity by `1.8878442649139515e-06`, exceeding the provisional non-scientific `1e-6` smoke threshold introduced after r1. This tuple is not part of the prospectively frozen 270 scientific sentinels. Therefore r2 is again `INFRASTRUCTURE_FAIL_G9_0090A`, not scientific PASS/BLOCKED/FAIL.

The repeated failure demonstrates that any numerical accuracy threshold on arbitrary non-sentinel offset tuples can preempt the preregistered scientific experiment and has no authority to classify H1. The observed value is retained as a diagnostic.

## Pre-result correction for the next hosted execution
Preflight must exercise code-path sanity only: for arbitrary offset tuples it may require the radial normalization result to be finite and strictly positive, but MUST NOT impose any accuracy-to-unity threshold. Exact/analytic geometry smoke tests remain allowed.

The scientific test is unchanged and remains exclusively inside `run_shard` on the frozen sentinel set. In particular, all of the following remain immutable:
- L/H orders `32x32` and `64x64`;
- all 270 frozen nonzero-source sentinels and aligned point controls;
- source-support and branch splitting rules;
- scientific radial-normalization threshold `2e-10` on every frozen sentinel;
- L/H convergence threshold `0.5%`;
- inherited geometry and point-control criteria;
- PASS/BLOCKED/FAIL taxonomy.

If any frozen sentinel violates `2e-10`, the scientific shard must return `BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE`. No tolerance relaxation or result-selected refinement is authorized.
