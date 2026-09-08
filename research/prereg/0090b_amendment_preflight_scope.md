# 0090b amendment — separate preflight sanity from H1-H3 authority

Date frozen: 2026-09-08
Parent prereg: `research/prereg/0090b_g9_endpoint_regularized_radial_measure_authority.md`, frozen commit `c46110eecf6fae9719d37f8f3a378206c2706324`.
Observed prior execution: run `34265503415`, head `c4866c8f978e26aa28069e32bfd7e1017d24568e`.
Immutable r1 record: `research/iterations/0090b_r1_g9_endpoint_regularized_infrastructure_fail.md`.

## Frozen interpretation of r1
The hosted run stopped in pytest before the authority script. No authority result JSON or artifact existed. Hence r1 is `INFRASTRUCTURE_FAIL_G9_0090B`, even though the test exposed a numerical diagnostic on the fixed `d/s=1.1` analytic control. That diagnostic cannot be promoted to scientific BLOCKED outside the preregistered authority payload.

## Prospective orchestration-only correction
Preflight regression tests must test implementation/code-path sanity only and MUST NOT call a helper that raises `Blocked` from H1/H2/H3 thresholds before the authority evaluator runs.

Allowed preflight checks include:
- exact centred branch returns finite normalization 1;
- transformed `u(t)` maps the frozen support endpoints and is monotone within roundoff;
- representative endpoint-regularized evaluations are finite and positive;
- dimensionless geometry algebra is finite and support-preserving.

Preflight MUST NOT assert the scientific `2e-10` normalization or L/H agreement thresholds and MUST NOT assert the `2e-12` scale-invariance criterion. Those remain exclusively authoritative inside the 0090b evaluator.

## Scientific contract unchanged
This amendment changes no scientific/numerical criterion. In particular the following remain immutable:
- endpoint transformation and displaced-disk source geometry from the parent prereg;
- L/H Gauss-Legendre orders `32/64`;
- all fixed analytic controls;
- all 90 physical source geometries;
- H1 normalization threshold `2e-10` for both L and H on every non-centred geometry;
- centred tolerance `2e-14`;
- H2 L/H agreement threshold `2e-10`;
- H3 scale-invariance threshold `2e-12`;
- H0 provenance/geometry conditions and classification taxonomy.

The next hosted execution must run the unchanged authority evaluator and write/upload its raw payload. If the fixed `d/s=1.1` control or any other frozen geometry violates H1-H3 there, the result is scientific `BLOCKED_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE`; it must not be relabelled infrastructure or repaired by increasing order or relaxing tolerance.
