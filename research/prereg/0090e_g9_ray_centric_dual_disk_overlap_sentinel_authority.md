# Preregistration 0090e — G9 ray-centric dual-disk overlap finite-source sentinel authority

Date frozen: 2026-09-08
Parent: 0090d `BLOCKED_G9_SOURCE_CENTRIC_FINITE_SOURCE_CONVOLUTION`, immutable record `research/iterations/0090d_g9_source_centric_finite_source_convolution_blocked.md`.

## Scientific/numerical question
Can the same finite uniform source disk and receiver disk be convolved with the already certified continuous solar-lens map by exchanging the order of integration and integrating the source exactly through disk-overlap geometry, thereby avoiding all explicit source-point quadrature that blocked 0090d?

This is an independent formulation, not an order escalation of 0090d. The 0090d source replicas `8x16/16x32` are retired inside this gate and must not be used to tune 0090e.

0090e remains a sentinel/method authority gate. It is not the full 1350-point survivor scan.

## Frozen upstream authority
Use without changing physical semantics:
- Model-S blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`;
- continuous signed map / turning-root chain 0089b/0089c;
- mesh-free branch/root geometry 0089e-r2;
- point-source `point_area_exact`, monotone map segments and threshold-root semantics inherited from 0090a;
- finite source is a uniform disk with radius `s=z*AU_CM*theta_s` and centre offset `d`;
- receiver radius `a` and magnification accounting `mu=1+Abar/(pi*a^2)` remain unchanged.

No radial-source density integral, no endpoint-regularized radial normalization, and no `(q,phi)` source tensor quadrature may be used to compute the 0090e scientific result.

## Exact source integration by dual-disk overlap
For a fixed incident-ray image vector `y_vec`, a source point `u_vec` is accepted when

`|y_vec-u_vec| <= a`.

Source points are uniform over the disk `D_s(d_vec)` of radius `s` centred at `d_vec`. Therefore the exact conditional source acceptance fraction for that ray is

`F = Area[D_s(d_vec) intersection D_a(y_vec)] / (pi*s^2)`.

Let `h=|y_vec-d_vec|`. Freeze the standard two-circle overlap area `O(s,a,h)`:
- if `h >= s+a`: `O=0`;
- if `h <= |s-a|`: `O=pi*min(s,a)^2`;
- otherwise
  `O=s^2*acos((h^2+s^2-a^2)/(2*h*s)) + a^2*acos((h^2+a^2-s^2)/(2*h*a)) - 0.5*sqrt((-h+s+a)*(h+s-a)*(h-s+a)*(h+s+a))`.

All acos arguments are clipped only to `[-1,1]` for floating-point roundoff; the square-root radicand may be clipped only at zero for negative roundoff at tangency. No empirical smoothing or renormalization is allowed.

For source-centre offset chosen along the x-axis and a ray ring of image radius `y`, separation is

`h(psi)=sqrt(y^2+d^2-2*y*d*cos(psi))`.

By reflection symmetry the ring-averaged exact-source kernel is

`K(y;s,d,a) = (1/pi) * integral_0^pi O(s,a,h(psi))/(pi*s^2) dpsi`.

For `d=0` or `y=0`, evaluate `K` analytically from the single separation `h=y` or `h=d`; no angular quadrature is used.

## Frozen analytic angular splitting
For `d>0` and `y>0`, split `[0,pi]` at all physical solutions of

`h(psi)=|s-a|` and `h(psi)=s+a`.

For each threshold `t` with `|y-d| <= t <= y+d`, compute

`psi_t = acos((y^2+d^2-t^2)/(2*y*d))`

and include it together with endpoints `0,pi`. Duplicate split points may be merged only at exact/roundoff equality. No result-selected split points.

## Frozen radial/map splitting
The lens radial variable remains incident solar radius fraction `x`. Use the already certified monotone signed-map segmentation from 0089c/0089e.

For each sentinel define overlap thresholds

`t1=|s-a|`, `t2=s+a`.

The angular-overlap topology can change only when image radius `y=|Y(x)|` crosses one of

`|d-t1|`, `d+t1`, `|d-t2|`, `d+t2`.

Prospectively root-split every existing monotone map segment at all finite nonnegative members of this set using the inherited deterministic threshold-root solver. Also retain the inherited turning point, `x0`, `XMIN`, `XMAX`. No scan-grid crossing detection and no result-selected roots.

## Frozen numerical replicas
After exact source integration and all analytic/root splitting, only ray geometry is numerically integrated.

L replica:
- angular Gauss-Legendre order 16 on every nonzero analytic angular subinterval;
- radial `x` Gauss-Legendre order 32 on every nonzero prospectively split map interval.

H replica:
- angular Gauss-Legendre order 32 on every nonzero analytic angular subinterval;
- radial `x` Gauss-Legendre order 64 on every nonzero prospectively split map interval.

Accepted incident area:

`Abar = 2*pi*Rsun^2 * integral x*K(|Y(x)|;s,d,a) dx`.

No adaptive integration, no order escalation after results, no source quadrature, no interpolation of `K`, and no tolerance relaxation.

## Frozen sentinel set
Exactly the same 81 prospectively fixed physical sentinels as 0090d:
- observer controls `x0={0.020,0.024,0.030}`;
- receivers `a={1,10,100} m`;
- theta indices `{0,12,24}` from the existing grid;
- centre offsets `delta_y={0,0.1,100} m`.

Shard by the same 9 `(observer,receiver)` pairs, 9 rows per shard.

## Frozen validation criteria
H0 provenance/map:
- exact Model-S blob match;
- focal-distance relative drift `<=2e-11`;
- batch/scalar signed-map conformance `<=2e-11`;
- exact aggregate cardinalities 9 shards / 81 rows on PASS.

H1 overlap-kernel invariants:
- `0 <= O <= pi*min(s,a)^2*(1+1e-13)`;
- `0 <= K <= min(1,a^2/s^2)*(1+1e-12)` when finite;
- exact disjoint and containment branches on deterministic unit controls;
- symmetry `O(s,a,h)=O(a,s,h)` to relative/absolute `<=2e-14` on fixed nondegenerate controls;
- scale invariance `O(cs,ca,ch)/c^2 = O(s,a,h)` to relative `<=2e-13` on fixed scales `c={1e-6,1,1e6}` where finite.

H2 point/source limit controls:
- inherited aligned point-source `point_area_exact` must match frozen 0089e-r2 reference area for each shard within `0.5%`;
- for smallest-source aligned sentinel `(theta index 0, delta=0)`, H `Abar` must agree with `point_area_exact` within `0.5%` when point area is nonzero.

H3 finite-source replica convergence for every sentinel:
Let `e_L=mu_L-1`, `e_H=mu_H-1`.
- if `max(|e_L|,|e_H|)>=1e-10`, require `|e_L-e_H|/max(|e_L|,|e_H|) <= 0.005`;
- otherwise require `|mu_L-mu_H| <= 1e-10`.

H4 physical/numerical invariants:
- `Abar_L,Abar_H` finite and in `[0,pi*Rsun^2*(1+1e-9)]`;
- `mu_L,mu_H` finite and `>=1`;
- no result-derived normalization factor;
- no 0090d source replica is evaluated as part of classification.

## Frozen classifications
- `PASS_G9_RAY_CENTRIC_DUAL_DISK_SENTINEL_AUTHORITY`: all 9 shards, all 81 sentinels and all H0-H4 checks pass.
- `BLOCKED_G9_RAY_CENTRIC_DUAL_DISK_CONVOLUTION`: exact provenance and invariants hold but one or more frozen H2/H3 convergence/limit checks miss.
- `SCIENTIFIC_FAIL_G9_DUAL_DISK_INVARIANT`: overlap/map/physical invariant fails.
- `INFRASTRUCTURE_FAIL_G9_0090E`: runtime/dependency/source/shard/artifact failure prevents scientific classification.

A finite H2/H3 miss is BLOCKED, not infrastructure.

## Exact next actions
- On PASS: prospectively freeze the full 1350-point G9 finite-source survivor scan using exactly the H ray-centric dual-disk method and a separately frozen survivor criterion; no named-source/duty claim yet.
- On BLOCKED: keep 0090e immutable and do not increase its 16/32 angular or 32/64 radial orders post-result; either derive a further independent analytic reduction or classify the present G9 numerical route currently non-actionable.
- On SCIENTIFIC_FAIL: audit exact overlap or upstream map authority.
- On INFRASTRUCTURE_FAIL: repair infrastructure only.

## Guards
No full 1350 grid in 0090e. No named astrophysical source claim. No detector/material gain. No BSM response/enhancement. No post-hoc promotion of 0090d. BSM remains LOCKED.
