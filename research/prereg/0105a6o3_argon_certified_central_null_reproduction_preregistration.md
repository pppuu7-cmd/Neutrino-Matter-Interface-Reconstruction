# 0105a6o3 — Ar Tier-B certified central/null reproduction

Status: **PREREGISTERED / NUMERICAL NULL REPRODUCTION / NONDISCOVERY**

Parent certificate: `PASS_0105A6O2_STRICT_CONVEX_UNIQUE_HIGH_PRECISION_OPTIMUM_NONDISCOVERY`.

The historical 0105a6o and 0105a6o1 results remain immutable BLOCKED under their original optimizer-coordinate requirements. This new gate does not reclassify them.

## Purpose

Execute the COHERENT CENNS-10 Analysis-A Tier-B central/null numerical reproduction using the unique central optimum certified independently by 0105a6o2, then adjudicate it against the **unchanged** publication and dual-anchor thresholds prospectively frozen in original preregistration commit `a94cbdf5a65618545bd4b1fb4f9fd6c120ae340e` before any fit result existed.

No threshold below is inferred from 0105a6o1 or 0105a6o2 fitted coordinates.

## Frozen authority prerequisites

1. Exact official central bytes must be recovered only from 0105a6p artifact `10160794369`, ZIP SHA256 `a66b3408b22b14575f156c0be7c389589dd9865ada1f4769fe8366a1df65ec82`, manifest SHA256 `5b1df47a50dd4dbb2a7fbd5ee64346c2854bdbad0540bfa6f16637eb10b6bada`.
2. Parent 0105a6o2 artifact `10163470626` must match ZIP SHA256 `8ca17ecfeeabe05bee6305a3bbb2dc6ac2eb5877ffeb67a14e74df165c2dbcc0` and inner result SHA256 `e3790cb7e2459ef900fda2cfe430be8d47fe497c1365f9c12762bef3f9599d73` and must classify `PASS_0105A6O2_STRICT_CONVEX_UNIQUE_HIGH_PRECISION_OPTIMUM_NONDISCOVERY`.
3. Exact central file identities, 960-bin coordinate-token equality and nominal-sum checks remain those frozen in 0105a6o and 0105a6p. No numeric-equivalent substitute is permitted.

## Frozen central objective

Identical to 0105a6o/0105a6o2:

`Q = 2 sum_i [mu_i - n_i ln(mu_i)] + ((NP-497)/160)^2 + ((ND-33)/33)^2 + ((NB-B0)/25)^2`,

`mu_i = NC*S_i + NP*P_i + ND*D_i + NB*B_i`,

with nonnegative normalizations and two mandatory branches:

- R3152: `B0=3152`;
- R3154: `B0=3154`.

Central best-fit coordinates must be taken from or independently reproduce the 0105a6o2 P200 certified root. Any independent recomputation used by this gate must agree with the parent P200 root within `1e-30` event in every normalization; otherwise execution is BLOCKED.

## Frozen conditional background profiling

For a fixed `NC >= 0`, minimize the exact same Q over `(NP,ND,NB)` using arbitrary-precision damped Newton at `mp.dps=100` from the deterministic provider-center start `[497,33,B0]`.

- exact analytic three-parameter gradient/Hessian obtained by deleting the fixed-NC coordinate from the full derivatives;
- Newton equation `H delta = -g`;
- full step first; halve while any background normalization is `<=0` or Q fails to decrease;
- fail if step factor `<2^-80`;
- maximum 200 iterations;
- convergence requires background-gradient infinity norm `<=1e-50`;
- all leading principal minors of the 3x3 Hessian must be positive at convergence.

The three background Gaussian penalties make every fixed-NC profiling problem strictly convex on the positive-mu interior; therefore a converged interior stationary point is the unique conditional minimum.

## Null statistic

Null fit: set `NC=0` and profile `(NP,ND,NB)` by the frozen conditional solver.

Define exactly as in 0105a6o:

`q0 = Q_null - Q_best`,

`Z_stat = sqrt(max(q0,0))`.

No look-elsewhere correction or alternative statistic is introduced.

## CEvNS profile statistical interval

For each branch define

`F(NC) = Q_profile(NC) - Q_best - 1`.

Lower side:

- evaluate `F(0)`;
- if `F(0) <= 0`, report lower boundary `NC=0`;
- otherwise bisect the unique lower crossing on `[0, NC_best]`.

Upper side:

- initial upper bracket `2*NC_best`;
- if `F(upper) <= 0`, double the upper endpoint, at most 20 times, until a positive value is obtained;
- then bisect the unique crossing on `[NC_best, upper]`.

Bisection terminates when bracket width is `<=1e-6` event, exactly matching the original 0105a6o root-tolerance scale. Report

`sigma_profile = (upper - lower)/2`.

No negative-NC extrapolation is allowed.

## Unchanged publication acceptance targets from 0105a6o Stage 6

Each R3152 and R3154 branch must independently satisfy **all**:

- `|NC - 159| <= 2.0` events;
- `|NP - 553| <= 3.0` events;
- `|ND - 10| <= 3.0` events;
- `|NB - 3131| <= 3.0` events;
- `|sigma_profile - 43| <= 2.0` events;
- `|Z_stat - 3.9| <= 0.15`.

These are copied without modification from preregistration commit `a94cbdf5a65618545bd4b1fb4f9fd6c120ae340e`.

## Unchanged dual-anchor robustness thresholds from 0105a6o Stage 7

Only after both branches independently pass publication targets, require:

- `|Delta NC| <= 1.0` event;
- `|Delta NP| <= 1.0` event;
- `|Delta ND| <= 1.0` event;
- `|Delta Z_stat| <= 0.05`;
- `|Delta sigma_profile| <= 0.5` event.

No post-result selection between R3152 and R3154 is permitted.

## Frozen classification

If authority/structure/parent certificate and all numerical solves succeed, both branches satisfy every unchanged publication target, and every unchanged dual-anchor threshold passes:

`PASS_0105A6O3_TIERB_ARGON_CERTIFIED_CENTRAL_NULL_REPRODUCTION_NONDISCOVERY`.

If numerical reproduction completes but a publication target fails:

`BLOCKED_0105A6O3_PUBLICATION_TARGET_MISMATCH`.

If both branches pass individually but dual-anchor robustness fails:

`BLOCKED_0105A6O3_DUAL_ANCHOR_SENSITIVITY`.

If parent/authority/structure/solver certification fails:

`BLOCKED_0105A6O3_AUTHORITY_OR_NUMERICAL_CERTIFICATE_FAILURE`.

## Consequence

A PASS authorizes only the separate prospectively frozen Analysis-A **shape-systematic excursion reproduction** described by 0105a6o Stage 8. It does not yet authorize a nuisance-cleaned observed residual.

The full release-consistent Tier-B SM/null layer is not considered closed until the systematic-excursion layer is independently classified.

## Hard ceilings

- Tier-A exact collaboration-internal likelihood remains BLOCKED;
- no observed nuisance-cleaned residual in this gate;
- no BSM/model-family scan;
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`.
