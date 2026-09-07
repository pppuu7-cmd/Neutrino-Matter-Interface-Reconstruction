# Preregistration 0074c — COHERENT CsI+Ar combined-likelihood benchmark authority audit

## Purpose

Iteration 0074a validated the independent Ar SM normalization and 0074b validated the independent CsI first-observation SM response. The next scientific dependency is the exact combined CsI+Ar SM/background likelihood used by the frozen B−L route. Before writing or executing that likelihood, this iteration freezes a **documentary primary-authority audit** whose only job is to identify an external, non-circular numerical benchmark and the exact likelihood conventions that a later reproduction must satisfy.

No likelihood minimization and no B−L scan are permitted in 0074c.

## Frozen scope

Use only the already hash-pinned COHERENT primary packages frozen by iteration 0074 plus the primary Cadeddu et al. analysis authority already recorded by the parent 0074 ledger. Audit both detector branches:

- CsI first-observation analysis, released PE support `6 <= PE < 30`, with the already frozen response convention validated in 0074b;
- Ar Analysis A, released `0 <= Eee < 120 keVee` support in 12 ten-keVee bins, with the SM normalization chain validated in 0074a.

The audit must record, with primary provenance, the exact observed-data binning, signal/background templates used by the intended combined fit, nuisance parameters and their widths/correlation assumptions, and the test statistic/minimization convention.

## Required benchmark authority

Before any reproduction result is computed, identify at least one **external numerical SM/background benchmark** from primary authority that is sensitive to the likelihood implementation rather than merely repeating an input normalization. Preferred forms, in order:

1. published SM best-fit or minimum chi-square / likelihood value with sufficient definition to reproduce it;
2. published profiled nuisance best-fit values plus a total/binwise expectation sufficient for an independently frozen tolerance;
3. an official collaboration example-code output or official numerical likelihood reference point from the same data release.

The fitted CsI excess `134 ± 22` and the standalone SM-normalization targets already used in 0074a/0074b are **not** acceptable as the combined-likelihood benchmark because they would not validate the profile-likelihood machinery.

If no same-analysis primary numerical benchmark can be identified after the primary paper/supplement, official release companion/code, and author/publisher numerical routes are exhausted, classify `BLOCKED_COMBINED_LIKELIHOOD_BENCHMARK_AUTHORITY`; do not invent a tolerance and do not use a secondary reproduction as scientific authority.

## Exact audit criteria

`PASS_COMBINED_LIKELIHOOD_BENCHMARK_AUTHORITY_FROZEN` requires all of:

1. exact CsI and Ar fit supports/binnings are pinned to primary authority;
2. all signal/background components needed by the intended combined fit are mapped to hash-pinned official inputs or an explicit primary analytic construction;
3. every nuisance parameter used by the combined likelihood has a primary provenance, width, and correlation/independence statement;
4. the exact likelihood/test-statistic formula and profiling domain are pinned;
5. at least one non-circular primary numerical benchmark is pinned with an explicit numerical tolerance **before** any reproduction is executed;
6. scientific-vs-infrastructure failure semantics and PASS/FAIL next action are written into the later calculation prereg before execution.

Any missing item gives `BLOCKED_COMBINED_LIKELIHOOD_BENCHMARK_AUTHORITY` unless the missing information is demonstrably a transient infrastructure-access failure, in which case the iteration remains in progress.

## Guards

- No B−L mass/coupling point is evaluated in this iteration.
- No benchmark tolerance may be chosen after seeing an NMIR reproduction result.
- Do not transfer nuisance conventions between CsI generations or between Ar analyses without same-analysis primary provenance.
- Do not treat a green CI run as a scientific likelihood PASS.
- Do not use 0074a/0074b standalone normalization agreement as proof that the combined likelihood is correct.

## Next action

- PASS → prospectively freeze 0074d combined CsI+Ar SM/background likelihood reproduction with the numerical benchmark and tolerance identified here, then execute it fail-closed.
- BLOCKED → retire the exact combined-likelihood B−L route unless a genuinely new primary data/authority source changes the missing-input assumption; B−L response remains prohibited.
