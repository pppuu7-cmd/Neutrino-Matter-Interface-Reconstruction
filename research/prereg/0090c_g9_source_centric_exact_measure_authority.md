# Preregistration 0090c — G9 source-centric exact-measure authority

Date frozen: 2026-09-08
Parent: 0090b-r2 `BLOCKED_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE`, immutable record `research/iterations/0090b_r2_g9_endpoint_regularized_radial_measure_blocked.md`.

## Scientific/numerical question
Can the same uniformly bright circular finite source be represented in source-centred coordinates with probability measure normalized by construction, while preserving the displaced-disk geometry over the complete frozen physical source set, without using either 0090a direct radial-u quadrature or 0090b endpoint-regularized radial normalization?

0090c is a source-measure geometry authority gate only. It contains no solar-lens accepted-area integral, no receiver convolution, no `mu_real`, no `mu>=2` survivor classification and no named-source/duty calculation. PASS can authorize only a separately preregistered finite-source lens-convolution method gate.

0090, 0090a and 0090b remain immutable. No order or tolerance from them is changed.

## Frozen provenance and physical source set
Use the same source semantics and controls as 0090b:
- Model-S source commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`, Git blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f` only to reconstruct the frozen observer distances;
- `Rsun = 6.96e10 cm`;
- observer controls `x0={0.020,0.024,0.030}` and their frozen `z=F(x0)` values;
- theta indices `k={0,6,12,18,24}` from `theta_s=10^(-18+k/2) rad`;
- deterministic centre offsets `d=delta_y={0,0.01,0.1,1,10,100} m`;
- projected source radius `s=z*AU_CM*theta_s`.

The authoritative physical set is the same 90 unique source geometries `3 x 5 x 6`. Receiver radius is absent because this gate concerns only the source probability measure and displacement geometry.

## Exact source-centric measure frozen before calculation
For a source-centred polar radius `r` and angle `phi`, define

`q = r^2/s^2`, with `0 <= q <= 1`, `0 <= phi < 2*pi`,

so that

`r = s*sqrt(q)`.

A uniform disk has exact normalized area measure

`dP = dA/(pi*s^2) = dq*dphi/(2*pi)`.

Place the source centre at `(d,0)` relative to the optical axis. A source point maps to

`X = d + r*cos(phi)`,
`Y = r*sin(phi)`,
`u = hypot(X,Y)`.

The sign choice of the cosine is immaterial after full azimuthal integration; the above convention is frozen.

This formulation contains no displaced-radius density `p(u;s,d)` and no numerical normalization integral in `u` or transformed `t`. Scientific use of the 0090a/0090b radial-normalization routines is forbidden in 0090c.

## Frozen deterministic replicas
Use product quadrature directly in the exactly normalized variables:
- replica L: Gauss-Legendre order 16 in `q` mapped to `[0,1]`, and 32 equally weighted azimuthal midpoint nodes `phi_j=2*pi*(j+1/2)/32`;
- replica H: Gauss-Legendre order 32 in `q`, and 64 equally weighted azimuthal midpoint nodes.

The probability weight of each product node is `(w_q/2) * (1/N_phi)`, where `w_q` is the standard Gauss-Legendre weight on `[-1,1]`. No adaptive quadrature, no result-selected nodes and no post-result order escalation are allowed.

## Frozen exact controls and identities
For every replica, the following identities are evaluated as weighted expectations on all 90 physical geometries and on the fixed dimensionless displacement controls `D=d/s={0,0.1,0.5,0.9,1,1.1,2,10,1e6}` at `s=1 cm`:

H1 exact measure normalization:
- `sum(weights) = 1` to absolute `<=2e-14`.

H2 source-centred uniform-disk moments, evaluated in normalized local coordinates `xi=(X-d)/s=sqrt(q)cos(phi)` and `eta=Y/s=sqrt(q)sin(phi)`:
- `E[xi] = 0`, `E[eta] = 0` to absolute `<=2e-14`;
- `E[xi^2] = 1/4`, `E[eta^2] = 1/4` to absolute `<=2e-14`;
- `E[xi*eta] = 0` to absolute `<=2e-14`;
- `E[xi^2+eta^2] = 1/2` to absolute `<=2e-14`.

H3 displaced geometry invariants at every quadrature node:
- `u`, `X`, `Y` finite;
- `r <= s*(1+2e-14)` and `r>=0`;
- triangle support `max(0,d-r)-T <= u <= d+r+T`, with `T=64*eps*max(d,s,1 cm)`;
- recomputation `u^2 = X^2+Y^2` agrees using a scale-normalized residual `abs(u^2-(X^2+Y^2))/max(u^2,X^2+Y^2,1) <= 5e-15`.

H4 replica agreement on fixed geometry diagnostics:
For each geometry compute source-centred moments above and the dimensionless mean squared offset from the source centre `E[(r/s)^2]`. L/H values must agree to absolute `<=2e-14`.

The exact normalization and moment standards are intentionally stricter than 0090a/0090b because these identities are polynomial/constant in the new measure coordinates and do not require resolving endpoint singularities.

## Frozen provenance checks
- exact Model-S blob match;
- reconstructed focal distances relative to frozen controls within `2e-11`;
- exactly 90 physical source geometries and 9 dimensionless controls;
- all source radii finite and strictly positive.

A dependency, source-fetch, checkout, malformed output or missing artifact before evaluating the fixed set is infrastructure failure.

## Frozen classifications
- `PASS_G9_SOURCE_CENTRIC_EXACT_MEASURE_AUTHORITY`: provenance and H1-H4 pass for all fixed controls and all 90 physical geometries.
- `BLOCKED_G9_SOURCE_CENTRIC_EXACT_MEASURE`: provenance/geometry are valid but fixed L/H product quadrature cannot certify one or more H1/H2/H4 numerical identities under frozen thresholds.
- `SCIENTIFIC_FAIL_G9_SOURCE_CENTRIC_GEOMETRY`: an exact displaced-geometry/provenance invariant in H3 fails.
- `INFRASTRUCTURE_FAIL_G9_0090C`: runtime/dependency/source/artifact failure before scientific classification.

## Next actions
- On PASS: prospectively freeze a separate finite-source lens-convolution method gate using this exact-measure `(q,phi)` coordinate system and the already certified global signed lens map. That later gate must have its own fixed quadrature/convergence/sentinel contract before any `mu_real` result.
- On BLOCKED: keep 0090c immutable; do not increase 16x32/32x64 post hoc. Move to another independent actionable formulation or another funnel family.
- On SCIENTIFIC_FAIL: audit source displacement geometry/upstream provenance.
- On INFRASTRUCTURE_FAIL: repair infrastructure only.

## Guards
No full 1350-point scan. No `mu>=2` claim. No lens-area calculation in this gate. No named-source, positioning-probability, duty-cycle, detector/material or BSM calculation. BSM response/enhancement remains LOCKED.
