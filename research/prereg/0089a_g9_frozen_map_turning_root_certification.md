# NMIR prereg 0089a — G9 frozen-map piecewise turning-root certification

Date frozen: 2026-09-08
Parent authority: 0089 `PASS_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY`, immutable commit `554a3b6d29804877915dc1fd524c4932c3d3a8b5`.

## Scientific question
Can the turning structure of the already frozen Model-S signed focusing map be numerically certified piece-by-piece using the exact derivative authority established in 0089, without smoothing across Model-S knots, adding result-selected nodes, or computing any focusing area/utility quantity?

This gate certifies roots/turning structure only. It does **not** compute `y=0`, `y=±r`, accepted annular area, a multiimage kernel, one-ring reproduction, finite-source effects, alignment duty cycle or persistent-source gain.

## Frozen provenance / physics
Reuse without modification:
- Model-S source commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`, git blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`;
- frozen `gravity_extended.py` map blob SHA1 `f8d48fb4eae87ff9c1f98ef543dae27c5f359e9c`;
- accepted exact derivative implementation from 0089, `src/nmir/g9_discrete_map_derivative.py`;
- `R_sun=6.96e10 cm`, `G=6.67430e-8 cgs`, `c=2.99792458e10 cm/s`, `AU=1.495978707e13 cm`;
- signed map `y(x;z)=x R_sun [1-z/F(x)]`, `x=b/R_sun`;
- derivative-control distances generated from `x0={0.020,0.024,0.030}` by `z=F(x0)` using the frozen map;
- root-certification domain `1e-4 <= x <= 1`;
- all fixed Model-S radial knots are immutable piece boundaries and no derivative is defined through a knot.

No 0089a derivative signs, candidate roots or root counts have been inspected in setting the criteria below.

## Frozen signed-map derivative
For the frozen map `F(x) ∝ x^2/M(x)`, with accepted exact `M'(x)` from 0089, evaluate on each open knot interval

`D(x;z) = (1/R_sun) dy/dx = 1 + q - x*q*M'(x)/M(x)`,

where `q=z/F(x)`, and `M(x)` is the authoritative frozen projected mass. This expression is used only at interior points. Exact knots are never assigned a derivative.

## Deterministic piecewise audit
For every positive-width Model-S knot interval `(a,b)` intersecting `[1e-4,1]`, clip only to the global domain and then use these result-independent interior fractions:

`Q32 = {j/32 | j=1,...,31}`

plus boundary probes

`qL={2^-16,2^-14,2^-12}` and `qR={1-2^-12,1-2^-14,1-2^-16}`.

All probes are relative to that interval. No interval may be removed after seeing results.

### R1 — finite derivative/sign audit
At every frozen probe for all three `z` controls:
- `D` must be finite;
- define numerical sign only when `|D| > tau_D`, with frozen scale-aware threshold

`tau_D = 2e-10 * max(1, |1+q|, |x*q*M'/M|)`.

Any required probe with `|D| <= tau_D` that cannot be associated with a stably isolated root below is `BLOCKED_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION`; do not lower `tau_D`.

### R2 — sign-changing root isolation inside a fixed piece
Every adjacent pair in the ordered frozen probe set with opposite certified signs defines a candidate bracket. Refine each bracket by deterministic bisection on the accepted exact `D` until bracket width `<=1e-12` in x. The reported root is the midpoint.

Repeat the refinement after adding the fixed dyadic half-step mesh `Q64={j/64 | j=1,...,63}`. Root sets from Q32 and Q64 must match one-to-one within `2e-10` in x. A new unmatched Q64 sign-changing root is BLOCKED rather than a reason to add further result-selected nodes.

If Q64 shows more than one sign-changing bracket inside a Q32 bracket, or any ambiguous near-zero probe not uniquely associated with one matched root, classify BLOCKED.

### R3 — knot-boundary turning semantics
For every fixed knot `k` inside `(1e-4,1)`, compare the innermost preregistered left/right boundary probes from its adjacent pieces (`2^-16` relative offsets). The knot itself remains derivative-undefined.

Classify diagnostically:
- same certified sign: no boundary turn;
- opposite certified signs: `KNOT_BOUNDARY_TURN` at the exact source knot;
- either side near-zero/nonfinite or not stable against the `2^-14` and `2^-12` probes: BLOCKED.

A knot-boundary turn is a legitimate source-fixed partition boundary but is not an interior derivative root and must remain labelled separately.

### R4 — independent original-map finite-difference confirmation
Every interior candidate root must be confirmed using the original signed map, not the analytic derivative evaluator. For the containing piece width `w=b-a`, use symmetric finite-difference half-steps

`h = w/{4096,8192,16384}`

at points that remain inside the same piece. For each scale, independently bracket the derivative sign reversal around the analytic candidate using offsets `±8h`, then bisect a finite-difference derivative surrogate to width `<=5e-11`.

All three original-map confirmations must agree with the exact-derivative root within `5e-9` in x and must have the same orientation. Failure is `SCIENTIFIC_FAIL_G9_FROZEN_MAP_ROOT_CONFIRMATION` if both evaluators are finite/stable but disagree; numerical inability to remain inside the piece or an unresolved near-zero ambiguity is BLOCKED.

For every `KNOT_BOUNDARY_TURN`, confirm the left/right orientation independently from original-map one-sided secants at relative offsets `2^-12,2^-14,2^-16`. All three scales must agree with the exact-derivative side signs; otherwise FAIL/BLOCKED under the same taxonomy.

### R5 — no-missed-root stress audit
The Q64 mesh is the frozen stress replica. Additionally, at each Q64 subinterval midpoint evaluate the original-map finite-difference derivative at `h=w/16384` when the stencil remains inside the source piece. Its sign must match the exact `D` sign at that midpoint unless the point lies inside the final certified bracket of a matched root.

Any unexplained sign disagreement, additional sign reversal, or near-zero ambiguity is BLOCKED. This is a numerical certification criterion, not a theorem excluding arbitrarily fine even-multiplicity stationary points beyond the frozen audit resolution; the iteration note must preserve that scope.

## Frozen controls
For each `x0={0.020,0.024,0.030}` the generating point must be recovered as a root of `y(x;F(x0))=0` by the frozen authoritative map to `<=1e-12` in x. This is a map-consistency control, not a turning-root criterion and does not authorize area computation.

All reported interior roots must be unique to `1e-10` in x after de-duplication; knot-boundary turns are kept separate from interior roots.

## Prospective classification
- `PASS_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION` iff R1–R5 and all generating-map controls pass for all three observer controls.
- `SCIENTIFIC_FAIL_G9_FROZEN_MAP_ROOT_CONFIRMATION` if the accepted exact derivative and stable original-map finite-difference evidence contradict one another beyond the frozen tolerances, or the generating-map control fails.
- `BLOCKED_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION` if an unresolved near-zero, unmatched Q32/Q64 root, unstable knot-boundary orientation, ambiguous multiple root, or stencil/piece-boundary ambiguity prevents certification without an additional assumption.
- source/hash/runtime/test/artifact failure before scientific evaluation is `INFRASTRUCTURE_FAIL_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION`.

No criterion may be weakened after results are seen.

## Reproducibility
When practical add:
1. reusable root-certification code separate from the 0089 derivative authority;
2. deterministic toy maps covering one interior turn, multiple separated turns and a source-fixed boundary turn;
3. dedicated tests;
4. machine-readable benchmark containing all root positions/orientations and failure details;
5. fail-closed hosted workflow;
6. raw run/job/artifact IDs and independent artifact/hash verification before classification.

## Forbidden in 0089a
- changing 0089 derivative semantics;
- smoothing/interpolating through a Model-S knot;
- result-selected extra scan nodes;
- changing `tau_D`, Q32/Q64, boundary offsets or confirmation tolerances after seeing results;
- solving `y=±r` or computing accepted area/kernel/one-ring metrics;
- finite-source/alignment/persistent-source convolution;
- reusing 0075 utility values;
- BSM response/enhancement work.

## Frozen next actions
PASS -> only then preregister a separate G9 kernel reconstruction gate using the certified interior roots + labelled knot-boundary turns and the unchanged authoritative signed map. That later gate must re-freeze area/no-double-counting/one-ring/replica criteria before calculation.

BLOCKED/FAIL -> close 0089a at the exact failure. Do not patch 0077/0088/0089a post hoc; return to another NMIR frontier unless a genuinely new mathematical construction is prospectively preregistered.

BSM response/enhancement remains LOCKED.
