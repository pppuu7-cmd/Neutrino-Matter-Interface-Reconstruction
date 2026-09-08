# Preregistration 0090b — G9 endpoint-regularized displaced-disk radial-measure authority

Date frozen: 2026-09-08
Parent: 0090a-r3 `BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE`, immutable result record `research/iterations/0090a_r3_g9_radial_source_measure_blocked.md`.

## Scientific/numerical question
Can the exact displaced-uniform-disk radial source measure itself be certified to the existing normalization standard by an endpoint-regularized one-dimensional formulation that is mathematically distinct from 0090a's direct Gauss-Legendre integration in `u`?

0090b is a source-measure authority gate only. It contains no solar-lens accepted-area integral, no receiver convolution, no `mu_real`, no survivor claim, no named source and no duty/positioning calculation. A PASS can authorize only a separately preregistered finite-source quadrature-method gate.

0090a remains immutable BLOCKED. No 0090a order, interval, sentinel or tolerance is changed or reinterpreted.

## Frozen provenance and source geometries
Use the same physical source semantics and exact controls as 0090a:
- Model-S source commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`, Git blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f` only to reproduce the already frozen observer distances;
- `Rsun = 6.96e10 cm`;
- observer controls `x0={0.020,0.024,0.030}` with their frozen `z=F(x0)` values from the 0089b/0089c authority chain;
- theta indices `k={0,6,12,18,24}` from the existing class grid `theta_s=10^(-18+k/2) rad`;
- offsets `d=delta_y={0,0.01,0.1,1,10,100} m`;
- projected source radius `s=z*AU_CM*theta_s`.

The authoritative physical test set is therefore the 90 unique source geometries `3 observer controls x 5 theta indices x 6 offsets`. Receiver radius is intentionally absent because normalization of the source measure cannot depend on the receiver.

## Exact displaced-disk radial measure
Retain the same geometry as 0090a:

`Omega(u;s,d)=2*pi` for `d<s` and `0<=u<=s-d`;

`Omega(u;s,d)=2*acos((u^2+d^2-s^2)/(2*u*d))` on the partial-overlap interval `|s-d|<u<s+d` for `d>0`;

zero elsewhere, and for `d=0`, `Omega=2*pi` on `0<=u<=s`.

`p(u;s,d)=u*Omega(u;s,d)/(pi*s^2)`.

The exact measure identity is

`integral p(u;s,d) du = 1`.

## Endpoint-regularized transformation frozen before calculation
For `d=0`, evaluate the normalization analytically from `p=2u/s^2`; no numerical quadrature is needed and the value is exactly 1 up to floating representation.

For `d>0`, define

`u(t) = sqrt(d^2 + s^2 - 2*d*s*cos(t))`, `0 <= t <= pi`.

This maps the complete partial-overlap radial interval monotonically from `|d-s|` to `d+s`, with

`du/dt = d*s*sin(t)/u(t)`.

Therefore the partial-overlap normalization is evaluated as

`N_partial = d/(pi*s) * integral_0^pi Omega(u(t);s,d) * sin(t) dt`.

If `d<s`, add the full-ring contribution analytically,

`N_full = (s-d)^2/s^2`.

If `d>=s`, `N_full=0`.

Then

`N_reg = N_full + N_partial`.

The transformed integration variable is `t`; **direct numerical Gauss-Legendre integration of `p(u)` in `u` is forbidden in 0090b scientific authority**. This prevents 0090b from becoming a post-hoc higher-order rerun of 0090a.

## Frozen numerical replicas
Use deterministic `numpy.polynomial.legendre.leggauss` on the single fixed interval `t in [0,pi]` for the partial contribution.

Two fixed replicas are frozen prospectively:
- L: order 32 in `t`;
- H: order 64 in `t`.

No adaptive quadrature, no result-selected interval splitting, no extra nodes, no order escalation and no per-tuple special casing after result inspection.

## Independent analytic controls
Before the 90 physical source geometries, the implementation must pass all of these fixed geometry controls:
1. centered disk `d=0` for `s={1e-6,1,1e6} cm`: exact normalization 1;
2. internally offset disk `d/s={0.1,0.5,0.9}` at `s=1 cm`;
3. tangent case `d/s=1` at `s=1 cm`;
4. externally offset disk `d/s={1.1,2,10}` at `s=1 cm`;
5. scale replicas for `d/s=2` at `s={1e-6,1,1e6} cm` to test dimensionless scale invariance.

These controls are fixed before any 0090b output and do not select tuples from the failed 0090a payload.

## Frozen validation criteria
H0 provenance/finite geometry:
- exact Model-S blob match when reconstructing frozen observer distances;
- observer focal-distance relative drift `<=2e-11` relative to the frozen controls;
- every `s>0`, `d>=0`, transformed `u(t)` finite/non-negative and monotone on a fixed 257-point diagnostic grid;
- `0<=Omega<=2*pi` everywhere on fixed diagnostic nodes.

H1 exact normalization authority:
- for every non-centred analytic control and every one of the 90 physical source geometries, both L and H must satisfy `abs(N_reg-1) <= 2e-10`;
- centred cases must equal 1 to absolute `<=2e-14` using the analytic branch.

H2 independent replica agreement:
- `abs(N_L-N_H) <= 2e-10` for every non-centred control and physical geometry.

H3 dimensionless scale invariance:
- the three `d/s=2` scale replicas must agree pairwise in L and H to absolute `<=2e-12`.

## Frozen classifications
- `PASS_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE_AUTHORITY`: H0-H3 pass for all fixed controls and all 90 physical source geometries.
- `BLOCKED_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE`: H0 is valid but fixed L/H endpoint-regularized quadrature cannot certify H1/H2/H3 under the frozen orders/tolerances.
- `SCIENTIFIC_FAIL_G9_RADIAL_MEASURE_GEOMETRY`: an exact geometry/provenance/invariant condition in H0 fails.
- `INFRASTRUCTURE_FAIL_G9_0090B`: source/runtime/dependency/artifact failure before scientific classification.

## Infrastructure-versus-science taxonomy
A dependency, checkout, unavailable pinned source, process/runtime, missing artifact or malformed output before evaluating the fixed set is infrastructure failure. A finite completed evaluation that violates H1-H3 is scientific BLOCKED. It must not be relabelled infrastructure and its criterion must not be weakened.

## Exact next actions
- On PASS: freeze a separate 0090c finite-source lens-convolution method preregistration that uses the endpoint-regularized source coordinate prospectively; 0090b itself gives no magnification result.
- On BLOCKED: keep 0090b immutable and move to another independent actionable G9 formulation or the next actionable funnel family; do not increase orders post hoc.
- On SCIENTIFIC_FAIL: close the affected source-measure formulation in its stated scope and audit upstream geometry.
- On INFRASTRUCTURE_FAIL: repair infrastructure only without changing scientific criteria.

## Guards
No full 1350-point map. No `mu>=2` claim. No named-source or duty-cycle calculation. No post-hoc promotion of 0090 or 0090a. No result-selected orders/intervals/tolerances. No BSM response/enhancement; BSM remains LOCKED.
