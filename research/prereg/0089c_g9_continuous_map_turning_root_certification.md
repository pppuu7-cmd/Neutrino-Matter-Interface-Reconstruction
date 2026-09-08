# NMIR prereg 0089c — G9 continuous-map turning-root certification

Date frozen: 2026-09-08
Parent authority: 0089b `PASS_G9_CONTINUOUS_PIECEWISE_LINEAR_PROJECTION_AUTHORITY`, immutable record commit `40f88288c7996d105446918e78cce29aa4c99d83`.

## Scientific question
Can the turning structure of the newly accepted continuous piecewise-linear Model-S signed focusing map be reproducibly certified over the inherited G9 domain, without result-selected refinement and without computing any accepted area, kernel or utility quantity?

This gate is **turning-root certification only**. It does not solve `y=±r`, compute accepted annular area, reconstruct a multiimage kernel, reproduce one-ring metrics, or evaluate finite-source/alignment/persistent-source utility.

No derivative sign, root position or root count for this continuous map has been evaluated in setting this contract.

## Frozen provenance / physics
Reuse exactly:
- Model-S source commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`;
- Model-S git blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`;
- accepted continuous projection implementation `src/nmir/g9_continuous_projection.py` at the 0089b hosted head `e4891230d6fcbdf379dbcda0571d6fc4ca90f5c3` or byte-identical implementation;
- `R_sun=6.96e10 cm`, `G=6.67430e-8 cgs`, `c=2.99792458e10 cm/s`, `AU=1.495978707e13 cm`;
- root-certification domain `1e-4 <= x <= 1`;
- signed map

`y_c(x;z)=x R_sun [1-z/F_c(x)]`,

where `F_c(x)=x^2 R_sun^2 c^2 / [4 G M_c(x)] / AU` and `M_c` is the accepted 0089b continuous projected mass;
- observer controls generated prospectively from `x0={0.020,0.024,0.030}` by `z=F_c(x0)`.

The Model-S source knots remain immutable, result-independent audit anchors, but unlike 0089a they are **not derivative discontinuities**: 0089b V2 established continuous derivative authority across all 2400 positive source knots within the frozen tolerance.

## Frozen signed-map derivative
For the accepted continuous map evaluate

`D_c(x;z) = (1/R_sun) dy_c/dx = 1 + q - x*q*M_c'(x)/M_c(x)`,

with `q=z/F_c(x)`.

`M_c` and `M_c'` must come only from the accepted 0089b analytic evaluators. No numerical derivative is used for the primary root locator.

## Deterministic audit mesh
Construct immutable audit cells from the sorted unique set:
- global endpoints `{1e-4,1}`;
- every Model-S source knot strictly inside the domain.

For every positive-width cell `(a,b)`, evaluate result-independent interior meshes:
- `Q32={j/32 | j=1,...,31}`;
- stress replica `Q64={j/64 | j=1,...,63}`.

Also evaluate `D_c` at every interior source knot itself. No cell, knot or probe may be removed after results are observed.

## R1 — finite/sign audit
At every Q32/Q64 probe and every source-knot anchor for all three observer controls:
- `M_c`, `M_c'`, `F_c`, `D_c` must be finite with `M_c>0`, `F_c>0`, `M_c'>=0`;
- define a certified sign only when

`|D_c| > tau_D`,

with frozen scale-aware threshold

`tau_D = 2e-10 * max(1, |1+q|, |x*q*M_c'/M_c|)`.

A near-zero point is not discarded. It must either be uniquely associated with a root certified below or the gate is `BLOCKED_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION`. `tau_D` may not be lowered.

## R2 — primary sign-changing root isolation
Build the globally ordered Q32 probe sequence including global endpoints only when their derivative is finite and every interior source knot. Every adjacent certified opposite-sign pair defines a primary candidate bracket, regardless of whether a source knot lies at a bracket endpoint.

Refine each bracket by deterministic bisection on analytic `D_c` until width `<=1e-12` in x; midpoint is the reported primary root.

Repeat from the globally ordered Q64 sequence. Q32 and Q64 root sets must match one-to-one within `2e-10` in x and with the same orientation. An unmatched Q64 root, multiple Q64 roots inside one Q32 bracket, or unresolved near-zero ambiguity is BLOCKED; do not add result-selected probes.

A source-knot anchor satisfying `|D_c|<=tau_D` is treated as a root candidate only if fixed neighboring Q64 probes on its two sides have opposite certified signs. Its final root is still obtained by ordinary analytic bisection across those fixed neighbors; it is not assigned to the knot by fiat.

## R3 — source-knot continuity/orientation stress
For every interior source knot `k`, use fixed one-sided relative offsets in its two adjacent source cells:

`delta={2^-12,2^-14,2^-16}`.

At each scale evaluate analytic `D_c` on both sides. Except when a certified R2 root bracket intersects that local neighborhood:
- all three left signs must agree;
- all three right signs must agree;
- left/right signs must agree with the exact-knot sign when the knot is not near-zero.

Any unstable one-sided orientation or finite discontinuity inconsistent with 0089b authority is `SCIENTIFIC_FAIL_G9_CONTINUOUS_MAP_DERIVATIVE_CONTINUITY` when values are finite/stable but contradictory, otherwise BLOCKED.

## R4 — independent signed-map finite-difference confirmation
Every R2 root must be confirmed from the accepted continuous signed map `y_c`, not from analytic `D_c`.

Let `w` be the width of the source cell containing the root, or the minimum adjacent cell width if its bracket crosses a source knot. Freeze symmetric finite-difference half-steps

`h=w/{4096,8192,16384}`.

For each scale evaluate the central derivative surrogate

`D_FD(x;z)=[y_c(x+h;z)-y_c(x-h;z)]/(2 h R_sun)`

where the stencil remains inside `[1e-4,1]`. Use fixed offsets `±8h` around the analytic candidate to obtain an FD sign-changing bracket, then deterministic bisection of the FD surrogate to width `<=5e-11`.

All three FD roots must agree with the analytic root within `5e-9` in x and have the same orientation. Stable finite contradiction is `SCIENTIFIC_FAIL_G9_CONTINUOUS_MAP_ROOT_CONFIRMATION`; inability to form an unambiguous stencil/root without changing the frozen scales is BLOCKED.

## R5 — no-missed-root stress audit
Q64 is the frozen analytic stress replica. Additionally, at every Q64 subinterval midpoint evaluate the independent central finite-difference derivative using local `h=w/16384`, where `w` is that source cell width and the stencil remains in the global domain.

Its certified sign must agree with analytic `D_c` at the same point unless the point lies inside a final certified root bracket. Any unexplained sign disagreement, additional reversal or near-zero ambiguity is BLOCKED.

This is a numerical certification at the preregistered resolution, not a theorem excluding arbitrarily narrow even-multiplicity stationary points.

## R6 — generating-map controls
For each frozen `x0={0.020,0.024,0.030}`:
- generate `z=F_c(x0)` only from the accepted continuous map;
- verify `|y_c(x0;z)|/R_sun <=1e-13`;
- independently solve the local `y_c=0` crossing with a fixed bracket `[x0*(1-2^-10), x0*(1+2^-10)]` clipped to the domain and deterministic bisection;
- recovered root must agree with `x0` within `1e-12` in x.

This is only a map-consistency control, not a turning-root result.

## Prospective classification
- `PASS_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION` iff R1-R6 pass for all three observer controls.
- `SCIENTIFIC_FAIL_G9_CONTINUOUS_MAP_DERIVATIVE_CONTINUITY` for stable contradiction of the accepted continuous derivative across source knots.
- `SCIENTIFIC_FAIL_G9_CONTINUOUS_MAP_ROOT_CONFIRMATION` for stable analytic-vs-signed-map FD contradiction or generating-map control failure.
- `BLOCKED_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION` for unmatched Q32/Q64 roots, unresolved near-zero/multiple-root ambiguity, unstable finite-difference certification or any need for result-selected refinement.
- source/hash/runtime/test/artifact failure before scientific evaluation is `INFRASTRUCTURE_FAIL_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION`.

No criterion may be weakened after results are seen.

## Reproducibility requirements
When practical leave:
1. reusable continuous-map root-certification code;
2. deterministic toy cases covering zero, one and multiple turning roots and a root near a fixed source anchor;
3. dedicated tests;
4. machine-readable result containing z controls, root positions/orientations, Q32/Q64 matching and confirmation residuals;
5. fail-closed hosted workflow;
6. raw run/job/artifact IDs and independent ZIP/inner-result hashes before classification.

## Forbidden in 0089c
- changing the accepted 0089b mass/derivative semantics;
- smoothing/refitting Model-S density;
- result-selected extra nodes or tolerance changes;
- solving `y=±r` or computing accepted area/kernel/one-ring quantities;
- finite-source, alignment duty-cycle or persistent-source convolution;
- reusing 0075 utility values;
- any BSM response/enhancement calculation.

## Frozen next actions
PASS -> only then preregister a separate G9 continuous-map kernel/accepted-area reconstruction gate with area/no-double-counting/one-ring/replica criteria frozen before calculation.

BLOCKED/FAIL -> close 0089c at the exact failure and do not post-hoc tune the mesh/tolerances. Return to another actionable NMIR frontier unless a genuinely new mathematical construction is prospectively preregistered.

BSM response/enhancement remains **LOCKED**.
