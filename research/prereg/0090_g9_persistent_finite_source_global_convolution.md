# Preregistration 0090 — G9 persistent known-direction finite-source global convolution

Date frozen: 2026-09-08
Parents: 0075 `BLOCKED_G9_PERSISTENT_GEOMETRY`; 0089b `PASS_G9_CONTINUOUS_PIECEWISE_LINEAR_PROJECTION_AUTHORITY`; 0089c `PASS_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION`; 0089e-r2 `PASS_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA`.

## Scientific question

After replacing the invalid local one-ring support of 0075 by the now-certified global continuous transparent-Sun branch geometry, does the **same generic persistent/known-direction class** contain a nonzero finite region in which receiver-integrated real-lens magnification remains `mu_real >= 2` after finite angular source size and an explicit transverse positioning-error budget are included?

This gate is geometric/focusing authority only. It does not name an astrophysical source, does not assign occurrence probability, does not claim active-positioning realizability, and does not multiply focusing by detector/material/BSM gains.

## Inherited physics and semantics — frozen unchanged

- pinned Model-S source commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`, Git blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`;
- continuous piecewise-linear density/projection semantics accepted by 0089b;
- global monotone branch/turning-root semantics accepted by 0089c and independently mesh-free replicated by 0089e;
- distant-source limit `D_s >> z`, so projected source radius is `s=z*theta_s`;
- source is a uniform circular disk;
- `delta_y` is a deterministic transverse centre-offset magnitude/error budget, not a probability distribution;
- receiver is a circular disk of radius `a`;
- event/fluence magnification is relative to the same receiver and source without lens alignment; it is not microscopic interaction gain or neutrino-energy gain;
- occurrence probability is not applied for this persistent/known-direction class;
- any `duty=1` result is explicitly only an instantaneous/best-case geometric upper control. Active-positioning dynamics/time averaging are outside 0090.

## Frozen class-level parameter map

Receiver radii, inherited exactly from 0075:
`a = {1, 10, 100} m`.

Transverse centre offsets, inherited exactly from 0075:
`delta_y = {0, 0.01, 0.1, 1, 10, 100} m`.

Angular source radii: the 0075 prereg froze a logarithmic span `1e-18 ... 1e-6 rad` but not the count. Before any 0090 result is evaluated, this contract resolves it deterministically to half-decade spacing:
`theta_s = 10^(-18 + k/2) rad`, `k=0,...,24` (25 values, endpoints included).

Observer controls / generating rings are the three already frozen G9 controls:
`x0=b/Rsun = {0.020, 0.024, 0.030}`,
with `z=F(x0)` computed from the accepted continuous 0089b map. No observer/ring may be added after seeing 0090 output.

The zero-offset row is an ideal mathematical upper control, not a realizability claim.

## Frozen global finite-source convolution

For each observer control, use the full certified monotone partition of the radial signed map
`y0(b)=b*Rsun*(1-z/F(b))`.

For a source point / centre-offset vector whose projected magnitude is `u`, axisymmetry permits fixing its direction. For a ring with image radius `|y0|`, the accepted azimuth fraction is the exact circle-overlap fraction already used in 0075:

`f_phi(y,u,a)=1` when the whole ring is inside the receiver,
`0` when disjoint,
and otherwise
`acos((y^2+u^2-a^2)/(2*y*u))/pi`.

The incident annular contribution is integrated over **all certified monotone branches** without double counting:
`dA = 2*pi*Rsun^2*b db` weighted by `f_phi`.

The uniform source disk is averaged using deterministic equal-area polar quadrature. The baseline comparison is kept separate, so
`mu_real = 1 + A_accepted/(pi*a^2)`.

No local branch continuation through a turn, scan-grid crossing discovery, fixed global indicator mesh, or result-selected node insertion is permitted.

## Frozen quadrature / convergence controls

Primary source quadrature: `n_radial=12`, `n_azimuth=24`.
Independent refinement replica: `n_radial=24`, `n_azimuth=48`.

Within each certified monotone branch and for each source-offset sample, split the b-domain at analytically relevant acceptance transitions by solving, where present, `|y0(b)|=|u-a|` and `|y0(b)|=u+a` by branch-local bisection. Integrate only the resulting smooth subintervals. A deterministic composite Simpson refinement may be used for the remaining smooth azimuth-fraction integral, starting at 8 panels and doubling to at most 4096 panels per subinterval. It must converge by successive-estimate relative/absolute criterion `<=1e-8` for the subinterval contribution; exhaustion is `BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS`, not permission to relax the tolerance.

The primary-vs-refined **final `mu_real-1` excess** must agree to relative `<=0.005` wherever the larger excess is `>=1e-10`; otherwise classify BLOCKED. For smaller excesses require absolute magnification agreement `<=1e-10`.

## Frozen independent controls / invariants

1. All projected masses, focal distances, branch boundaries, accepted areas and magnifications finite and non-negative.
2. No accepted b-interval overlap/double count across the certified branch partition.
3. For `theta_s=0` (implemented as a dedicated point-source control, not part of the logarithmic source grid), `delta_y=0`, and each `a`, reproduce the 0089e mesh-free aligned cumulative area/magnification at the same observer/radius to relative `<=0.005`.
4. `mu_real <= mu_upper`, with impossible whole-solar-aperture ceiling `mu_upper = 1 + (Rsun/a)^2` at every point.
5. Refined source quadrature convergence as frozen above.
6. Source-disk rotational symmetry: rotating the deterministic centre-offset direction cannot change the result beyond `1e-12` relative (analytic axisymmetry control).
7. Large-blur control: using the existing aperture-only bound, the focused excess must be bounded by a quantity tending to zero as projected source/offset scale grows; no point-caustic divergence is permitted.
8. The 0075 historical local one-ring output is **not** a numerical authority for 0090 except for unit/toy semantics; 0090 must not be tuned to reproduce its blocked branch.

## Frozen prospective outputs

Machine-readable output for every (`x0`,`a`,`theta_s`,`delta_y`) point:
- `z_au`, projected `s_cm`;
- primary and refined `mu_real`;
- real-lens convergence discrepancy;
- impossible aperture `mu_upper`;
- whether `mu_real >= 2`, `10`, `1e3`;
- finite source/offset tolerance summaries: largest frozen `theta_s` and `delta_y` retaining each threshold, if any;
- branch-level accepted-area contributions and invariant flags.

Also report the fraction/count of the frozen finite grid satisfying `mu_real>=2` only as a descriptive class-map statistic, not as a probability measure.

## Frozen classifications

- `PASS_G9_PERSISTENT_KNOWN_DIRECTION_GLOBAL_SURVIVOR`: all invariants/convergence controls pass and at least one **finite nonzero-source, finite nonzero-position-error** grid point (`theta_s>0`, `delta_y>0`) has real-lens `mu_real>=2`. This establishes only a geometric survivor class and authorizes a separately preregistered real-source/active-positioning feasibility audit.
- `PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_PERSISTENT_GLOBAL`: all invariants/convergence controls pass, aligned focusing exists, but no finite nonzero-source/nonzero-error frozen grid point reaches `mu_real>=2`.
- `BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS`: global geometry is available but the prospectively frozen convolution/refinement controls cannot be certified without a new numerical method.
- `SCIENTIFIC_FAIL_G9_PERSISTENT_GLOBAL_INVARIANT`: positivity, no-double-counting, aperture ceiling, point-control, or another frozen invariant fails.
- `INFRASTRUCTURE_FAIL_G9_0090`: source/runtime/dependency/artifact failure before scientific classification.

## Guards

No occurrence-rate penalty in 0090. No `duty=1` realizability claim. No named source selection. No detector/material/interaction/BSM multiplication. No source brightness or flux normalization needed to decide this dimensionless geometry gate. No result-selected source sizes, observer rings, offsets, b-nodes or tolerances. No retroactive promotion of 0075/0076/0077/0089d.

Only a PASS survivor may open a separate real persistent-source + active-positioning/duty audit. A strong-negative result closes only the frozen generic class map, not arbitrary source models outside its preregistered range.