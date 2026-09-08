# Preregistration 0090a — G9 radial-source-measure quadrature authority

Date frozen: 2026-09-08
Parent: 0090 `BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS`, immutable result commit `51dd4e8a904163ba1746790658f53e50fc109b88`.

## Scientific/numerical question
Can an independent, geometry-reduced finite-source integration certify the same continuous transparent-Sun lens convolution without using the 0090 equal-area 2-D source node rule or its composite-Simpson b-integrator?

0090a is a numerical-method authority gate only. It does not retroactively change 0090 and does not yet authorize a full 1350-point survivor/strong-negative classification.

## Frozen provenance and physical semantics
Unchanged from 0090:
- pinned Model-S source commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`, Git blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`;
- continuous piecewise-linear projection semantics from 0089b;
- certified turning roots/global monotone branches from 0089c, independently replicated by 0089e;
- `Rsun = 6.96e10 cm`;
- observer controls `x0={0.020,0.024,0.030}` with their already frozen `z=F(x0)`;
- receiver radii `a={1,10,100} m`;
- uniform circular source, projected radius `s=z*theta_s` in the distant-source limit;
- deterministic centre offset `delta_y`, not a probability distribution;
- baseline-separated magnification `mu_real=1+A_accepted/(pi*a^2)`;
- no occurrence probability, named source, duty realizability, detector/material or BSM gain.

## Independent radial reduction — frozen before calculation
For a uniform source disk of projected radius `s` whose centre is a transverse distance `d=delta_y` from the optical axis, replace the 0090 equal-area polar source node sum by the exact radial measure of the displaced disk.

Let `u` be the distance of a source point from the optical axis. The angular measure of the intersection of the radius-u circle with the source disk is

`Omega(u;s,d)=2*pi` for `d < s` and `0 <= u <= s-d`;

`Omega(u;s,d)=2*acos((u^2+d^2-s^2)/(2*u*d))` for `d>0` and `|s-d| < u < s+d`;

and zero outside the disk-supported ranges. For `d=0`, the first case alone gives the centred disk.

The normalized radial source density is

`p(u;s,d) = u*Omega(u;s,d)/(pi*s^2)`,

with prospective normalization check `integral p(u) du = 1`.

For fixed `u`, retain the exact axisymmetric receiver overlap fraction from 0090,

`f_phi(y,u,a)=1` for whole-ring acceptance, `0` for disjoint rings, and otherwise
`acos((y^2+u^2-a^2)/(2*y*u))/pi`.

Using the certified global signed map `y0(b)`, define

`A(u)=2*pi*Rsun^2 * sum_branches integral b*f_phi(|y0(b)|,u,a) db`,

with every branch split at every present solution of `|y0|=|u-a|` and `|y0|=u+a`. No scan-grid root discovery is allowed.

The finite-source area authority is then the one-dimensional radial convolution

`Abar(s,d)=integral p(u;s,d)*A(u) du`,

and `mu_radial=1+Abar/(pi*a^2)`.

## Frozen quadrature construction
No composite Simpson and no 0090 equal-area source nodes are permitted in 0090a.

Use deterministic Gauss-Legendre quadrature from `numpy.polynomial.legendre.leggauss` on every finite interval after exact geometric splitting.

Two fully independent fixed-order replicas are frozen:
- replica L: source-u order 32 on each source-measure interval and b order 32 on each branch/acceptance subinterval;
- replica H: source-u order 64 and b order 64 on the same prospectively defined intervals.

Source-u intervals are split only at geometry-known boundaries `{0, max(0,s-d), |s-d|, s+d, a}` that lie strictly inside support; duplicates are removed. No point may be inserted after output inspection. The b intervals are split only at certified branch boundaries and the exact acceptance-transition roots defined above.

For `s=0` the finite-source integral degenerates to the already frozen exact point-control annulus construction; it is a control, not part of the nonzero-source sentinel grid.

## Frozen sentinel coverage
0090a does not select failed tuples from 0090. Before any 0090a result, the sentinel set is fixed uniformly from the preregistered class grid:
- all three observer controls;
- all three receiver radii;
- theta indices `k={0,6,12,18,24}` from `theta_s=10^(-18+k/2) rad`;
- all six `delta_y={0,0.01,0.1,1,10,100} m`.

Total nonzero-source sentinel tuples: `3*3*5*6 = 270`, plus the aligned point controls.

## Frozen validation and classifications
H0 provenance/geometry:
- exact Model-S blob match;
- observer focal-distance relative drift `<=2e-11`;
- signed-map batch/scalar conformance `<=2e-11`;
- finite/non-negative areas and magnifications; no branch overlap/double counting; whole-solar-aperture ceiling preserved.

H1 radial-measure authority:
- numerical `integral p du` under replica H must agree with 1 to absolute `<=2e-10` for every nonzero-source sentinel;
- centred (`d=0`) radial measure must agree with analytic `p=2u/s^2` support semantics to the same normalization tolerance.

H2 independent quadrature convergence:
- compare final excesses `eL=mu_L-1`, `eH=mu_H-1`;
- wherever `max(|eL|,|eH|)>=1e-10`, require relative discrepancy `|eL-eH|/max(|eL|,|eH|) <=0.005`;
- below that scale require absolute magnification discrepancy `|mu_L-mu_H|<=1e-10`.

H3 inherited point control:
- `s=0,d=0` exact-annulus control must reproduce 0089e aligned mesh-free area/magnification to relative `<=0.005` for all three observer controls and all three receiver radii.

H4 cross-method non-authoritative diagnostic:
- where an 0090 equal-area result happens to have been numerically certified before its shard stopped, it may be reported only as a diagnostic and cannot alter any threshold or classification. 0090 BLOCKED remains immutable.

Classifications:
- `PASS_G9_RADIAL_SOURCE_MEASURE_QUADRATURE_AUTHORITY`: H0-H3 pass for all 270 sentinels and point controls. This authorizes only a separately preregistered full-grid radial-convolution gate using the frozen method.
- `BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE`: H0 geometry is valid but L/H quadrature convergence or radial normalization cannot be certified under the frozen orders/tolerances.
- `SCIENTIFIC_FAIL_G9_RADIAL_SOURCE_MEASURE_INVARIANT`: a frozen physical/geometric invariant fails.
- `INFRASTRUCTURE_FAIL_G9_0090A`: source/runtime/dependency/artifact failure before scientific classification.

## Guards
No result-selected orders, intervals, sentinel tuples, source radii, offsets or tolerances. No post-hoc promotion of 0090. No `mu>=2` survivor claim from sentinel coverage. No named-source, duty-cycle, detector/material or BSM calculation. BSM response/enhancement remains LOCKED.
