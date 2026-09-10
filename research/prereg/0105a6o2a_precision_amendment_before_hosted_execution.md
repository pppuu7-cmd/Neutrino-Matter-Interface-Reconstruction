# 0105a6o2a — pre-execution arithmetic-precision amendment

Status: **PREREGISTERED AMENDMENT BEFORE HOSTED SCIENTIFIC EXECUTION / NONDISCOVERY**

Parent preregistration: `research/prereg/0105a6o2_argon_strict_convexity_high_precision_certificate_preregistration.md`, commit `07a61181b7fb2b8f7041250c3b9bf1de1aeee0e4`.

## Reason for amendment

A local implementation probe performed before any hosted 0105a6o2 execution exposed a generic arithmetic-resolution inconsistency in the parent numerical design, not a physics/result-dependent discrepancy.

The parent required a P120 Newton solve to reach gradient infinity norm `<=1e-80` while accepting a Newton step only if the computed objective Q strictly decreases. Near a nondegenerate Newton optimum, the objective improvement is second order in the gradient, approximately `O(||g||^2)`. A target gradient of order `1e-80` therefore entails objective changes of order `1e-160` up to curvature scales, below the resolving power of a 120-decimal-digit evaluation of an objective with magnitude of order unity or larger. A strict-Q-decrease line search can therefore stall from arithmetic resolution before the unchanged gradient certificate is reached.

This is an implementation-design defect independent of the previously observed 0105a6o1 coordinate spread. No publication target, model residual, or BSM quantity is involved.

## Frozen strengthening

The parent success thresholds are **not weakened**. Instead, arithmetic precision is strengthened:

- keep P80 solve exactly as preregistered: `mp.dps=80`, gradient infinity norm `<=1e-50`;
- replace the parent P120 solve by **P200**: `mp.dps=200`;
- retain the high-precision gradient threshold unchanged at `<=1e-80`;
- retain both starting vectors, Newton equation, backtracking rule, 200-iteration cap, positivity rule, and `alpha < 2^-80` failure rule unchanged;
- wherever the parent says “P120 root/objective/Hessian”, read “P200 root/objective/Hessian” for the hosted certificate;
- retain starter agreement `<=1e-60` event;
- retain P80-to-high-precision agreement `<=1e-40` event;
- retain high-precision objective agreement `<=1e-70`;
- C1 algebraic strict-convexity certificate and all hard ceilings remain unchanged.

The stronger 200-digit arithmetic is solely to make the already-frozen `1e-80` stationarity target numerically resolvable under the already-frozen strict-decrease line search.

## Execution authority

No hosted 0105a6o2 scientific run occurred before this amendment. The next hosted run must cite both the parent preregistration commit and this amendment commit.

Classification names and consequences remain exactly those defined by the parent preregistration.
