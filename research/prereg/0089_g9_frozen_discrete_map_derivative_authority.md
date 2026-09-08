# NMIR prereg 0089 — G9 frozen-discrete-map exact derivative authority

Date: 2026-09-08

## Motivation
0077 is `BLOCKED_G9_TURNING_POINT_KERNEL`. 0088 independently attacked the turning-root problem with a continuous interpolated-density projected-mass derivative and ended terminally as `BLOCKED_G9_ROOT_CERTIFICATION` at `RuntimeError('composite Simpson convergence exhausted')`. The 0088 prereg explicitly closes that route on BLOCKED/FAIL; 0089 is **not** an 0088 repair and may not change its quadrature/tolerance/node choices.

The authoritative G9 signed map still uses `src/nmir/gravity_extended.py::projected_mass_g`. That function does not numerically integrate a continuous radial integrand by Simpson. It evaluates the shell-cylinder fraction at the parsed Model-S radial knots, inserts the moving split point `x=b/R` when it is not already a knot, and applies a finite trapezoidal sum. Therefore its exact piecewise derivative can be derived algebraically with no quadrature.

0089 asks only whether that derivative evaluator is mathematically and numerically authoritative for the **frozen discrete map**. It does not search roots or construct a kernel.

## Frozen source / code authority
- Model-S source commit: `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`;
- Model-S git blob SHA1: `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`;
- frozen map implementation: `src/nmir/gravity_extended.py` blob SHA1 `f8d48fb4eae87ff9c1f98ef543dae27c5f359e9c` as inspected at 0088 final head `902864b8dd40c4781de253fb3ef8920889c8e3ea`;
- parser semantics: linearly interpolated density; centre point inserted by constant extrapolation if absent; fixed radius knots sorted centre-to-surface;
- `R_sun = 6.96e10 cm`;
- domain for derivative authority: open intervals between adjacent parsed Model-S radial knots inside `0 < x < 1`.

No Model-S values, knot positions, derivative signs or turning roots have been numerically inspected in defining the acceptance criteria below.

## Frozen finite-sum map identity
Let dimensionless radius be `u=r/R`, let `rho(u)` be the same piecewise-linear density used by `_interp_density`, and define

`g(u) = u^2 rho(u)`.

For shell-cylinder fraction

- `f(x,u)=1` for `u <= x`;
- `f(x,u)=1-sqrt(1-(x/u)^2)` for `u > x`,

the frozen trapezoidal map can be written

`M_trap(x) = 2*pi*R^3 * sum_j (p_{j+1}-p_j) [ g(p_j) f(x,p_j) + g(p_{j+1}) f(x,p_{j+1}) ]`,

where `{p_j}` is the parsed fixed radial-knot set augmented by `x` when `x` is not already a knot. This is algebraically equivalent to the physical-radius `_trapz` implementation in `projected_mass_g`.

## Frozen exact derivative on an open knot interval
For adjacent fixed knots `a < x < b`, define the piecewise-linear density slope

`s = [rho(b)-rho(a)]/(b-a)`,

`rho_x = rho(a) + s (x-a)`,

`g_x' = 2 x rho_x + x^2 s`.

For any fixed `u>x`,

`f_x'(x,u) = x / [u^2 sqrt(1-(x/u)^2)]`.

The derivative of the two trapezoids that contain the moving inserted point `x` is frozen as

`H_split' = g(a) - g(b) f(x,b) + (b-a) g_x' + (b-x) g(b) f_x'(x,b)`.

Every fully external fixed interval `[u_j,u_{j+1}]` with `u_j >= b` contributes

`(u_{j+1}-u_j) [ g(u_j) f_x'(x,u_j) + g(u_{j+1}) f_x'(x,u_{j+1}) ]`.

Thus

`dM_trap/dx = 2*pi*R^3 [ H_split' + sum_external(...) ]`.

Intervals wholly below `a` have zero x derivative. This formula is the only 0089 derivative candidate.

## Knot-boundary semantics
At an exact fixed Model-S radial knot, the augmented-grid topology changes and the source implementation may have a cusp / non-smooth one-sided derivative because the shell fraction contains a square-root edge at a sampled fixed knot. 0089 must **not** invent a derivative through a knot.

Every exact parsed radial knot is frozen as an explicit derivative piece boundary. 0089 authority, if PASS, applies only inside open intervals. One-sided behavior may be reported diagnostically but cannot be smoothed, bridged or used to select extra nodes.

## Prospective validation suite
All point selection is deterministic and result-independent.

### V1 — finite-sum mass identity over every interval
For every positive-width parsed knot interval `(a,b)`, evaluate at the three fixed fractions

`x = a + q (b-a)`, `q in {1/4, 1/2, 3/4}`.

Compare the independently coded dimensionless finite-sum `M_trap(x)` with the authoritative `gravity_extended.projected_mass_g(profile,x,R)`.

PASS_V1 requires:
- all values finite and positive;
- maximum symmetric relative discrepancy `<= 5e-13`.

No interval may be removed after seeing the result.

### V2 — high-precision independent derivative reference
Use an independent high-precision implementation of the same **finite trapezoidal map**, not the analytic derivative formula. Convert the parsed float knot/density values from their round-trip decimal representations and evaluate with at least 80 decimal digits.

Select a deterministic stratified subset of at most 64 radial intervals:
- always the first 4 and last 4 positive-width intervals;
- intervals containing or immediately neighboring the control radii `x={0.020,0.024,0.030}`;
- fill remaining slots by uniformly spaced interval indices from the full ordered interval list, de-duplicated before evaluation.

Within every selected interval use `q={1/4,1/2,3/4}`. At each point compute an independent 5-point central numerical derivative of high-precision `M_trap` at

`h=(b-a)/1024`

and a replica at `h/2`. Both stencils remain inside the same open interval by construction.

PASS_V2 requires:
- the two high-precision numerical derivative replicas agree to symmetric relative discrepancy `<= 1e-8`;
- the analytic 0089 derivative agrees with the `h/2` high-precision reference to symmetric relative discrepancy `<= 1e-8`;
- all evaluated derivatives are finite.

The threshold and steps are frozen before source-derived derivative values are inspected.

### V3 — deterministic synthetic profiles
Test the evaluator on at least three preregistered non-result-selected toy profiles spanning:
1. constant density on knots `(0, 0.25, 0.6, 1)`;
2. monotone linear density values `(4,3,2,1)` on the same knots;
3. non-monotone positive density values `(1,3,2,4)` on knots `(0,0.2,0.7,1)`.

At every open toy interval and q=`1/4,1/2,3/4`, require finite-sum mass identity `<=5e-13` and 80-digit numerical-derivative agreement `<=1e-8` using the same stencil rules.

### V4 — piece-boundary integrity
The evaluator must explicitly reject exact fixed radial knots as derivative points rather than silently choosing a side. The authoritative mass itself must remain finite/positive at every positive fixed knot. No continuity or differentiability through a knot is required for PASS.

## Classification
- `PASS_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY` iff V1–V4 all pass.
- `SCIENTIFIC_FAIL_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY` if the frozen analytic derivative or finite-sum identity disagrees with the authoritative map/reference beyond any frozen tolerance, or if a required interior derivative is nonfinite.
- `BLOCKED_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY` if the exact map semantics cannot be represented without an additional unpreregistered assumption, or a required piece cannot be certified because the source map itself is ambiguous at an interior point.
- source download/hash/runtime/artifact/test failures before the scientific audit are infrastructure failures, not scientific classifications.

## Scope / guards
0089 is derivative-authority-only.

Forbidden in 0089:
- turning-root search or root count;
- result-selected scan nodes;
- monotone partition construction;
- y=0 or y=±r solving;
- multiimage area/kernel evaluation;
- one-ring acceptance or 0.5% kernel comparison;
- finite-source, positioning-error or persistent-source convolution;
- any 0077/0088 reclassification or patch;
- any BSM response/enhancement scan.

If 0089 PASSes, a separate prospectively preregistered gate may use the map-exact derivative for turning-root certification. If 0089 BLOCKED/FAILs, no root gate based on this derivative may be launched without a genuinely new assumption and preregistration.
