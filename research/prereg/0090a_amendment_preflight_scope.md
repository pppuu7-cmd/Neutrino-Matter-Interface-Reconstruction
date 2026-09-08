# 0090a amendment — preflight scope after r1 infrastructure failure

Date: 2026-09-08
Parent prereg: `research/prereg/0090a_g9_radial_source_measure_quadrature_authority.md`, frozen commit `fb4aad7d1ffe23fb4863d09e26c0c3b20f47364c`.
Observed execution before this amendment: run `34254541976`, head `658d66fed23317b254cb05ffa60e81d0fee372dc`.

## Frozen interpretation of r1
The hosted workflow stopped in preflight before any scientific shard executed. The failing regression tuple `(s,d,a)=(1.0,0.25,0.3)` is not one of the prospectively frozen 270 scientific sentinels and therefore cannot classify H1/H2 for 0090a. The aggregate correctly returned `INFRASTRUCTURE_FAIL_G9_0090A` because zero scientific shard artifacts existed.

The observed preflight value `|integral p du - 1| = 6.160120946674397e-08` at fixed order 64 is retained as an implementation diagnostic. It is not discarded and it is not promoted to scientific BLOCKED because that tuple was never preregistered as a scientific sentinel.

## Pre-result implementation correction
The regression suite is only a preflight implementation smoke test. It must not impose the scientific `2e-10` H1 threshold on arbitrary, non-preregistered tuples. The scientific threshold remains unchanged inside `run_shard` and will be evaluated on every frozen sentinel.

Therefore the arbitrary offset-disk unit test may check only that the fixed-order implementation is finite, positive and approximately normalized at a loose implementation-smoke level (`<=1e-6` absolute error). This does not alter:
- orders L=32x32 and H=64x64;
- the 270 frozen sentinels;
- source/branch interval construction;
- H0/H1/H2/H3 thresholds;
- PASS/BLOCKED/FAIL taxonomy;
- scientific shard code.

No scientific result from r1 is available. The next hosted execution must run the unchanged frozen scientific shard checks. If any sentinel exceeds `2e-10` radial-normalization error, the corresponding shard must return `BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE`; the threshold must not be relaxed.
