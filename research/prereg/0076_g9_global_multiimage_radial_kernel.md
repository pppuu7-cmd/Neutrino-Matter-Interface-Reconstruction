# Preregistration 0076 — G9 global multi-image transparent-Sun radial kernel

Date frozen: 2026-09-07
Parent: 0075 `BLOCKED_G9_PERSISTENT_GEOMETRY` because the local one-ring monotone branch turns before the largest frozen finite-source/position blur is covered.

## Scientific question
Can the already pinned extended-Sun Model-S lens be converted into a **global, non-double-counted multi-image radial response kernel** across the full transparent solar aperture, so later persistent-source finite-blur calculations do not extrapolate a local focal branch through radial turning points?

This is a geometry/method validation gate only. It must not inspect or classify the 0075 `mu>=2` utility map, and it must not select a named source.

## Frozen authority and scope
Reuse without modification:
- pinned Model-S payload commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`, Git blob `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`;
- solar radius `R_sun = 6.96e10 cm` and `gravity_extended.py` projected-mass/focal-distance implementation validated in 0029-0030/0061;
- distant-source radial observer mapping `y(b;z)=b R_sun [1-z/F(b)]` for `0<b/R_sun<=1`.

Observer-distance controls are frozen to the same three rings introduced before the 0075 result: `b0/R_sun = 0.020, 0.024, 0.030`, with `z=F(b0)` computed from the pinned model.

No new solar density model, geometric-optics correction, detector model, source flux, or BSM interaction is allowed.

## Frozen global-preimage algorithm
For each observer distance `z`:
1. scan the full validated impact domain `1e-4 <= b/R_sun <= 1` using the existing `combined_scan_grid()`;
2. find every zero of the signed map `y(b;z)` by sign-change bracketing plus explicit inclusion of the generating ring `b0`; refine each zero by bisection;
3. for a requested output radius `r`, form `h(b)=|y(b;z)|-r`; insert the refined zero roots into the global scan so narrow accepted intervals cannot be missed; find/refine every `h=0` crossing; classify each consecutive interval by a midpoint and sum each accepted impact annulus exactly as `pi R_sun^2 (b_hi^2-b_lo^2)`;
4. every impact-parameter interval may be counted at most once. Radial turns are not extrapolated or relabeled as a local branch.

The machine-readable global kernel is the cumulative accepted incident area `A(<r)` and corresponding receiver ratio `mu_aperture(r)=A(<r)/(pi r^2)` for logarithmic `r = 1e0...1e9 cm` at decade spacing plus exact receiver controls `r=100,1000,10000 cm`.

## Prospective validation criteria
All criteria are frozen before any 0076 numerical result:

1. **Root recovery:** for each control distance the generating root must be recovered with `|b_root-b0| <= 1e-10`; all roots must lie in `(1e-4,1]` and be unique to `1e-9` in `b/R_sun`.
2. **Area invariants:** every cumulative area is finite/non-negative, `A(<r)` is non-decreasing with `r`, and never exceeds `pi R_sun^2` by more than `1e-10` relative.
3. **Local-authority containment:** at `b0=0.024` and receiver radii `1,10,100 m`, global `A(<a)/(pi a^2)` must be >= the already validated exact one-ring contribution from `annular_point_source_receiver_mu`; the recovered interval containing `b0` must reproduce that exact one-ring annulus ratio within **0.5%**.
4. **Grid refinement:** repeat the global crossing search with every interval of the base `combined_scan_grid` bisected once. For all frozen radii, cumulative `A(<r)` must agree with the base result within **0.5%** relative (absolute comparison used only if both are zero).
5. **No hidden local continuation:** if any requested crossing cannot be bracketed/refined on the global domain, classify BLOCKED/FAIL rather than extending a branch by assumption.

## Frozen classifications
- `PASS_G9_GLOBAL_MULTIIMAGE_KERNEL`: all three observer-distance controls produce a complete global preimage kernel and all prospective validation criteria pass.
- `BLOCKED_G9_GLOBAL_MULTIIMAGE_KERNEL`: the pinned model/domain cannot uniquely bracket the required roots/crossings without an additional physical assumption.
- `SCIENTIFIC_FAIL_G9_GLOBAL_MULTIIMAGE_KERNEL`: root, area, local-authority containment, no-double-counting, or refinement criteria fail.
- `INFRASTRUCTURE_FAIL`: runtime/fetch/artifact failure before scientific classification.

## Reproducibility
Add the smallest reusable global-preimage module, dedicated tests, machine-readable benchmark, and hosted fail-closed workflow. Preserve run/job/artifact/hash and immutable iteration note. Green CI alone is not PASS.

## Next action
- PASS -> only then preregister a new persistent-source convolution gate using this global kernel; do not reuse 0075 local-branch results.
- BLOCKED/FAIL -> close this geometry route at the exact failure and return to the remaining funnel; do not lower tolerances after seeing output.
