# 0105a6o1 — Ar Tier-B optimizer convergence diagnostic

Status: **PREREGISTERED / NUMERICAL DIAGNOSTIC ONLY / NONDISCOVERY**

Parent result: 0105a6o is frozen BLOCKED because its L-BFGS-B multi-start agreement threshold failed before publication-target comparison.

## Purpose

Determine whether the 0105a6o block is caused by ordinary finite-difference optimizer stopping tolerance on a single convex optimum, or by a deeper objective/implementation/identifiability problem.

This gate does **not** relax or reclassify 0105a6o. It does not compare against BSM models and does not inspect an observed residual.

## Frozen inputs/objective

Use the exact 0105a6p central bytes and exactly the 0105a6o central objective, bounds, R3152/R3154 anchors and four deterministic starting vectors. No likelihood family, nuisance constraint or data/template convention may change.

## Convexity identity to verify

For positive expected bin counts, with parameter-to-bin design matrix `A = [S,P,D,B]`, the frozen objective Hessian is

`H = 2 A^T diag(n_i / mu_i^2) A + diag(0, 2/160^2, 2/33^2, 2/25^2)`.

This is positive semidefinite analytically. The diagnostic must compute the numerical symmetric Hessian from this closed form at every retained candidate solution and record its minimum eigenvalue.

## D1 — reproduce original finite-difference behavior without fail-fast

For each anchor and each original 0105a6o start, run the same finite-difference L-BFGS-B settings and **retain all finite successful solutions** instead of raising on disagreement.

Record pairwise/max spreads in:

- each normalization;
- Q;
- analytic gradient infinity norm.

## D2 — analytic-gradient rerun

Use the exact analytic gradient

`grad Q = 2 A^T (1 - n/mu) + [0, 2(NP-497)/160^2, 2(ND-33)/33^2, 2(NB-B0)/25^2]`

with L-BFGS-B, the same bounds and same four starting vectors.

Frozen analytic-gradient settings:

- `ftol=1e-15`;
- `gtol=1e-11`;
- `maxiter=50000`.

## D3 — independent high-accuracy cross-check

Starting from the minimum-Q analytic-gradient solution, run `scipy.optimize.minimize(method='SLSQP')` with the same non-negative bounds, analytic gradient, `ftol=1e-12`, `maxiter=50000`.

## Frozen diagnostic classification

Classify

`PASS_0105A6O1_SINGLE_CONVEX_OPTIMUM_NUMERICAL_TOLERANCE_ONLY_NONDISCOVERY`

only if, for **both** R3152 and R3154:

1. at least 3/4 original finite-difference starts are successful and finite;
2. all retained original solutions differ in Q by `<= 1e-4` from the best original solution;
3. every original solution has analytic-gradient infinity norm `<= 5e-3`;
4. all four analytic-gradient L-BFGS-B starts are successful and finite;
5. analytic-gradient solutions agree within `1e-5` event in every normalization and `1e-9` in Q;
6. every analytic-gradient solution has gradient infinity norm `<= 1e-6`, except an active lower-bound component may satisfy the KKT one-sided condition instead;
7. the minimum Hessian eigenvalue at the chosen optimum is `>= -1e-10`;
8. SLSQP agrees with the chosen analytic-gradient optimum within `1e-4` event in every normalization and `1e-8` in Q.

Otherwise classify

`BLOCKED_0105A6O1_OPTIMIZER_OR_OBJECTIVE_DIAGNOSTIC_UNRESOLVED`.

These thresholds are frozen before the individual 0105a6o start solutions are inspected.

## Consequence

A diagnostic PASS authorizes a **new prospectively preregistered numerical reproduction gate** using the analytic-gradient implementation. It does not authorize retroactive modification of 0105a6o and does not itself establish publication agreement.

A diagnostic BLOCKED requires investigation of the objective/parameterization before any further null-reproduction claim.

## Hard ceilings

- no publication-target PASS/FAIL classification in this diagnostic;
- no systematic-excursion execution;
- no observed BSM/model-agnostic residual;
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`.
