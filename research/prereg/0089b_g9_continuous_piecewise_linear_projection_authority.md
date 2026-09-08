# NMIR preregistration 0089b — G9 continuous piecewise-linear Model-S projection authority

Date frozen: 2026-09-08
Parent terminal gate: 0089a `BLOCKED_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION` from the completed preregistered PyPy runtime replica, reason `unstable knot-boundary orientation`. No offending knot identity, root position, boundary-turn list, area, kernel or magnification value was inspected before this preregistration.

## Question
Can the already frozen *continuous piecewise-linear density semantics* of Model S be projected analytically, without the moving-point trapezoidal discretization that creates source-knot derivative cusps and without adaptive/composite quadrature, while remaining compatible with the previously authoritative finite map at the existing G9 0.5% numerical-stability scale?

This is a genuinely new mathematical construction. It does not patch 0077, 0088 or 0089a and may not reuse result-selected knots, roots, offsets or tolerances from their outcomes.

## Frozen source / physics semantics
- Model-S source commit: `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`.
- Expected Model-S git blob SHA1: `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`.
- Retain the same parser semantics: sorted `0 <= r/R <= 1`, exact source radii/densities, inserted centre point only if absent, and linear interpolation between adjacent density knots.
- `R_sun = 6.96e10 cm`; retain the same frozen G, c and AU constants from `gravity_extended.py`.
- Domain: `1e-4 <= x=b/R_sun <= 1`.
- This gate changes only the numerical projection of the already frozen linearly interpolated density field. No new solar model, smoothing spline, fitted density, root-selected node, physics parameter or observational input is allowed.

## Exact continuous construction
On every source interval `[r_i,r_{i+1}]`, write
`rho(u)=A_i*u+B_i`,
where `A_i=(rho_{i+1}-rho_i)/(r_{i+1}-r_i)` and `B_i=rho_i-A_i*r_i`.

The continuous projected cylinder mass is
`M_cyl(x)=4*pi*R^3 * integral_0^1 u^2 rho(u) f(x,u) du`,
with `f=1` for `u<=x` and `f=1-sqrt(1-(x/u)^2)` for `u>x`.

For stable exact evaluation above `x`, define `q=sqrt(1-(x/u)^2)` and the frozen antiderivatives

`F_A(u;x) = (u^2*x^2/8) * [2/(1+q)+q] + (x^4/8)*acosh(u/x)`,

`F_B(u;x) = (u*x^2/3) * (1+q+q^2)/(1+q)`.

They satisfy exactly
`dF_A/du = u^3 [1-sqrt(1-(x/u)^2)]`,
`dF_B/du = u^2 [1-sqrt(1-(x/u)^2)]`.

Below `x`, integrate the polynomial exactly:
`P_A(u)=u^4/4`, `P_B(u)=u^3/3`.
Thus every interval contribution is an endpoint difference of these frozen functions, with the interval containing `x` split exactly at `x`. Use deterministic `math.fsum` over interval contributions. No numerical quadrature is permitted in the production evaluator.

The exact continuous derivative is frozen independently as
`dM_cyl/dx = 4*pi*R^3*x * integral_x^1 u*rho(u)/sqrt(u^2-x^2) du`.
For `rho=A*u+B`, use

`J_A(u;x)=0.5*[u*sqrt(u^2-x^2)+x^2*acosh(u/x)]`,
`J_B(u;x)=sqrt(u^2-x^2)`,

so each source interval above `x` contributes
`A*[J_A(hi;x)-J_A(lo;x)] + B*[J_B(hi;x)-J_B(lo;x)]`.
The lower endpoint is `max(x,r_i)`. Use `math.fsum`; no quadrature.

At source density knots the continuous mass and derivative are mathematically defined because density itself is continuous; no `derivative undefined at knot` rule is inherited from the discrete trapezoidal map.

## V0 — generic algebra / toy tests
Before Model-S classification, production helpers must pass deterministic tests on constant and linear toy densities. Required:
- antiderivative endpoint differences agree with direct high-precision numerical integration to relative `<=1e-12` at fixed generic `(x,lo,hi)` tuples that do not come from Model-S results;
- analytic `dM/dx` agrees with an independent high-precision five-point derivative of the continuous analytic `M(x)` to relative `<=1e-9` on fixed toy profiles;
- mass is finite, positive and monotone nondecreasing in x.
Failure before Model-S evaluation is implementation/infrastructure failure, not science.

## V1 — independent high-precision Model-S authority replica
Use `mpmath` at 80 decimal digits only as an independent validator, not as the production map. Freeze validation x-values before any continuous Model-S result:

`X_REF = {1e-4,3e-4,1e-3,3e-3,1e-2,2e-2,2.4e-2,3e-2,5e-2,1e-1,2e-1,4e-1,7e-1,9e-1,9.9e-1}`.

Additionally choose 32 source intervals deterministically by indices `round(j*(N-2)/31)`, `j=0..31`, after parsing and clipping to intervals intersecting the domain; validate each interval midpoint. This index rule is source-order based, not result-selected.

At all V1 points:
- continuous analytic `M_cyl` vs direct 80-digit piecewise numerical integral: relative difference `<=1e-10`;
- continuous analytic `dM/dx` vs 80-digit integral of the frozen derivative integrand: relative difference `<=1e-9`;
- all values finite and positive where physically required.
Any V1 mismatch is `INFRASTRUCTURE_FAIL_G9_CONTINUOUS_PROJECTION_IMPLEMENTATION`; no scientific classification is inferred.

## V2 — source-knot continuity / cusp removal
For every positive Model-S source knot `k` inside the domain, evaluate the exact continuous derivative at `k` and one-sided points at frozen offsets `2^-12`, `2^-14`, `2^-16` of their respective adjacent source-interval widths.

Required:
- exact derivative at the knot is finite;
- left/right values remain finite;
- for each side, absolute distance to the exact-knot value must decrease monotonically (allow `1e-13 * max(1,|D_k|)` additive roundoff slack) as the offset shrinks from `2^-12` to `2^-16`;
- the smallest-offset left and right values must each agree with the exact-knot derivative to scale-aware relative/absolute error `<=2e-5`, using denominator `max(1,|D_k|)`.

This is a continuity test only. It does not search for turning roots. A near-zero exact derivative is allowed and is merely recorded for a later prospectively registered root gate.
Failure is `BLOCKED_G9_CONTINUOUS_PROJECTION_KNOT_CONTINUITY`; no offset may be changed after seeing the result.

## V3 — compatibility with the previously frozen discrete map
Use the already frozen `combined_scan_grid()` only; do not add result-selected points.
At every grid x in `1e-4..1` compare:
- continuous analytic projected mass to `gravity_extended.projected_mass_g`;
- continuous analytic focal distance to the old frozen focal distance.

Require maximum symmetric relative difference
`abs(a-b)/max(abs(a),abs(b),1e-300) <= 0.005`
for both mass and focal distance. Record RMS and maxima and the x locations of maxima, but do not tune from them.

The 0.5% criterion is inherited prospectively from the existing G9 numerical-stability standard; it is not chosen from 0089a data.
If V0-V2 pass but V3 exceeds 0.5%, classify `BLOCKED_G9_CONTINUOUS_PROJECTION_DISCRETE_COMPATIBILITY`. The continuous reconstruction is then not allowed to inherit the previous G9 numerical authority without a new independently motivated gate.

## Classification
`PASS_G9_CONTINUOUS_PIECEWISE_LINEAR_PROJECTION_AUTHORITY` iff V0-V3 all pass.

Fail closed as:
- `INFRASTRUCTURE_FAIL_G9_CONTINUOUS_PROJECTION_IMPLEMENTATION` for code/source/hash/high-precision-replica failures;
- `BLOCKED_G9_CONTINUOUS_PROJECTION_KNOT_CONTINUITY` for V2 continuity failure;
- `BLOCKED_G9_CONTINUOUS_PROJECTION_DISCRETE_COMPATIBILITY` for V3 >0.5% after V0-V2 pass.

## Scope / prohibition
A PASS authorizes only a separately preregistered continuous-map turning-root certification gate. 0089b itself must not output or promote turning-root positions, caustic partitions, y=+-r boundaries, annular areas, magnification, one-ring controls, finite-source convolution, persistent-source convolution, detector gain or BSM quantities.

No post-result smoothing, knot deletion/addition, fitted spline, quadrature tolerance relaxation, result-selected validation point or altered 0.5% criterion is permitted.