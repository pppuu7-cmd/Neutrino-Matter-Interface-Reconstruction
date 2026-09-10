# 0105a6o2 — Ar Tier-B strict-convexity and high-precision optimum certificate

Status: **PREREGISTERED / OPTIMIZER-PRECISION CERTIFICATE / NONDISCOVERY**

Parent: 0105a6o1 is frozen `BLOCKED_0105A6O1_OPTIMIZER_OR_OBJECTIVE_DIAGNOSTIC_UNRESOLVED` solely because the four analytic-gradient L-BFGS-B solutions differ in the unpenalized CEvNS normalization by about `3e-5` event, exceeding the frozen `1e-5` coordinate-spread criterion. The parent threshold is not changed or reinterpreted.

## Purpose

Determine whether the exact 0105a6o central objective has a unique interior global minimum that can be certified independently of ordinary double-precision optimizer stopping coordinates.

This gate performs **no publication-target comparison**, no shape-systematic excursion, and no observed BSM/model-agnostic residual analysis.

## Frozen inputs and objective

Use only the exact official central bytes carried by 0105a6p artifact `10160794369`, whose ZIP SHA256 is

`a66b3408b22b14575f156c0be7c389589dd9865ada1f4769fe8366a1df65ec82`

and whose `manifest.json` SHA256 is

`5b1df47a50dd4dbb2a7fbd5ee64346c2854bdbad0540bfa6f16637eb10b6bada`.

Use exactly the 0105a6o central objective, nonnegative normalization domain, and both frozen steady-state anchors `B0=3152` and `B0=3154`:

`Q(theta) = 2 sum_i [mu_i - n_i log(mu_i)] + ((NP-497)/160)^2 + ((ND-33)/33)^2 + ((NB-B0)/25)^2`,

with

`mu_i = NC*S_i + NP*P_i + ND*D_i + NB*B_i`,

where each S/P/D/B is the corresponding exact central template normalized by its exact decimal-text sum.

The decimal tokens in the provider text files must be parsed directly into arbitrary-precision numbers. Binary double values from 0105a6o1 may not be used as the high-precision input representation.

## C1 — algebraic strict-convexity certificate

For every positive-`mu` interior point,

`v^T H v = 2 sum_{i:n_i>0} n_i (a_i dot v)^2 / mu_i^2 + 2 v_P^2/160^2 + 2 v_D^2/33^2 + 2 v_B^2/25^2`.

A machine certificate must verify from the exact central data/templates that:

1. all data/template values are nonnegative and all required exact SHA256 identities match;
2. at least one bin has simultaneously `n_i > 0` and `S_i > 0`;
3. therefore `v^T H v = 0` implies first `v_P=v_D=v_B=0` from the positive Gaussian penalty terms and then `v_C=0` from a positive-count/nonzero-signal bin.

If these conditions hold, the objective is strictly convex throughout its positive-`mu` interior. Hence any interior stationary point is the unique global interior minimizer. This algebraic implication is frozen before execution and must not be replaced by a sampled Hessian argument.

## C2 — deterministic arbitrary-precision Newton certificate

For each anchor independently, solve `grad Q = 0` using a custom damped Newton method with the exact analytic gradient and Hessian in `mpmath` arithmetic.

Frozen starting vectors, chosen independently of 0105a6o1 fitted coordinates:

- `S0 = [128, 497, 33, B0]` (provider prediction center);
- `S1 = [256, 497, 33, B0]` (fixed doubled-signal stress start).

Frozen Newton rule:

- solve `H delta = -g` at every iteration;
- initial step factor `alpha=1`;
- if any candidate normalization is `<=0` or Q does not decrease, halve `alpha` repeatedly;
- fail if `alpha < 2^-80`;
- maximum 200 Newton iterations;
- no coordinate clipping, rounding, smoothing, or tolerance repair.

Run the complete solve twice:

- precision P80: `mp.dps=80`;
- precision P120: `mp.dps=120`.

Precision-derived convergence tolerances are frozen as:

- P80 gradient infinity norm `<= 1e-50`;
- P120 gradient infinity norm `<= 1e-80`.

These thresholds are tied to the declared arithmetic precision rather than to any previously observed fit coordinate.

## C3 — precision/starter invariance

For each anchor, require:

1. both S0 and S1 converge at P80 and P120;
2. the two P120 roots agree in every normalization within `1e-60` event;
3. each P80 root agrees with the corresponding P120 root within `1e-40` event;
4. all four certified roots are strictly interior: every normalization `> 0`;
5. the exact-arithmetic symmetric Hessian at each P120 root is positive definite by an LDL/Cholesky-compatible principal-minor or eigenvalue calculation at P120 precision; no negative/zero curvature is permitted;
6. the P120 objective values from the two starts agree within `1e-70`.

## C4 — double-precision diagnosis, report-only

For provenance only, the gate may evaluate the frozen 0105a6o1 analytic-gradient solutions at the P120 objective/gradient and report their distance to the certified root if those coordinates are supplied from the immutable 0105a6o1 artifact. These report-only diagnostics cannot affect PASS/BLOCKED classification and cannot be used to weaken 0105a6o1.

## Frozen classification

PASS only if C1, C2 and C3 all pass for both anchors:

`PASS_0105A6O2_STRICT_CONVEX_UNIQUE_HIGH_PRECISION_OPTIMUM_NONDISCOVERY`.

Otherwise:

`BLOCKED_0105A6O2_HIGH_PRECISION_OR_UNIQUENESS_CERTIFICATE_UNRESOLVED`.

Transport/hash/runtime failure is separately:

`BLOCKED_0105A6O2_SOURCE_OR_RUNTIME_FAILURE`.

## Consequence

A PASS authorizes a **new prospectively recorded Tier-B central/null reproduction gate** that may use the certified deterministic optimum machinery while reusing the already-frozen 0105a6o publication targets, dual-anchor robustness thresholds and profile/null definitions *unchanged*. The original 0105a6o and 0105a6o1 classifications remain historical and immutable.

A BLOCKED result requires further numerical/objective investigation before publication-target reproduction.

## Hard ceilings

- no publication-target PASS/FAIL classification in 0105a6o2;
- no systematic-excursion execution;
- no nuisance-cleaned observed residual;
- no BSM/model-family scan;
- Tier-A collaboration-internal likelihood remains BLOCKED;
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`.
