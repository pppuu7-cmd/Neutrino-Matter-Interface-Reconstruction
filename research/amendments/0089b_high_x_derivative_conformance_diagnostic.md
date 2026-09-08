# NMIR amendment 0089b — high-x derivative conformance diagnostic

Date frozen: 2026-09-08
Parent preregistration: `5d99cd6cd4d3a5f1f9defecfbd7f4036c93b8636`.
Current recovery front: 0089b remains scientifically unclassified after implementation/reference-conformance retries.

## Trigger
The latest validated retry `34212522107/102016600507`, artifact `10050421483`, independently verified ZIP SHA256 `115791057578a5328c4f73cf60730ab103b6e3111501fd31abb635ba512ae6da`, reaches frozen V1 point `x=0.99999825` with:
- mass relative mismatch `2.7517694270327773e-17` (PASS against frozen `1e-10` mass criterion),
- derivative relative mismatch `3.6792373931063796e-08` (FAIL against frozen `1e-9` derivative criterion).

No V2/V3 value has been produced or inspected. This diagnostic is frozen before any alternative derivative value is computed.

## Scope
Diagnose only the already observed V1 derivative mismatch at exactly `x=0.99999825`. Do not change production code, V1/V2/V3 thresholds, Model-S bytes/parser/constants, or the set of V1 points. Do not compute V2, V3, turning roots, areas, kernels, or persistent-source quantities.

## Exact provenance
- Model-S commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`.
- Expected Model-S git blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`.
- `R_sun = 6.96e10 cm` and same parser semantics as 0089b.
- Production value is taken from unchanged `continuous_projected_mass_derivative_g_per_x` on repository head used by the diagnostic.

## Frozen independent references
Use `mpmath` with `mp.dps=100` and compute the full derivative

`dM/dx = 4*pi*R^3*x * integral_x^1 u*rho(u)/sqrt(u^2-x^2) du`

by two independent routes on the same piecewise-linear density:

### Reference A — theta-space direct numerical integral
For each source interval above x, set `u=x/cos(theta)`. Then

`x * u*rho(u)/sqrt(u^2-x^2) du = x^2*rho(x/cos(theta))/cos(theta)^2 dtheta`.

Integrate each interval with `mp.quad` at 100 digits, splitting exactly at source-interval boundaries. No production primitive is reused.

### Reference B — t-space direct numerical integral
Set `t=sqrt(u^2-x^2)`, so `du=t/u dt`. Then

`x * u*rho(u)/sqrt(u^2-x^2) du = x*rho(sqrt(x^2+t^2)) dt`.

Integrate each source interval with `mp.quad` at 100 digits between its exact transformed endpoint values. No theta transform and no production primitive is reused.

Both references include the common `4*pi*R^3` factor only after summing interval integrals.

## Frozen diagnostic checks
D0 source/blob/parser checks must pass.

D1 high-precision reference agreement:
`abs(A-B)/max(abs(A),abs(B),1e-100) <= 1e-20`.
If not, classify `INFRASTRUCTURE_FAIL_G9_0089B_HIGH_X_REFERENCE_DISAGREEMENT`.

D2 production-vs-reference mismatch is evaluated with the original V1 symmetric relative definition. No threshold changes:
- if production agrees with the consensus reference at `<=1e-9`, classify `PASS_G9_0089B_HIGH_X_DERIVATIVE_CONFORMANCE_DIAGNOSTIC` (diagnostic PASS only; this does not make 0089b PASS and requires rerunning the original V1 gate);
- if A/B agree but production differs by `>1e-9`, classify `DIAG_G9_0089B_PRODUCTION_DERIVATIVE_STABILITY_DEFECT`.

D3 cancellation observability only: for every active source interval, record the double-precision production decomposition `a*DeltaJ_A`, `b*DeltaJ_B`, their sum, and `(|term_A|+|term_B|)/max(|sum|,1e-300)`. This ratio is diagnostic only and has no PASS/BLOCKED threshold.

## Taxonomy / permitted next action
This diagnostic cannot create a scientific PASS/BLOCKED/FAIL for G9.
- `DIAG_G9_0089B_PRODUCTION_DERIVATIVE_STABILITY_DEFECT` permits a **new prospectively frozen algebraically equivalent production-stability amendment only**; all scientific thresholds remain unchanged.
- reference disagreement permits no production change and requires a separately frozen reference diagnostic.
- diagnostic PASS permits only a clean rerun of the unchanged original 0089b V1-V3 contract.

No result-selected tolerances, points, shell deletion, smoothing, quadrature in production, or scientific-threshold relaxation is permitted.
