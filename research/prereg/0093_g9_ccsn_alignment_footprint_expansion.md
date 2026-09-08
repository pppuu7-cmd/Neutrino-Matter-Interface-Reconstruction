# Preregistration 0093 — G9 CCSN alignment-footprint expansion

Date frozen: 2026-09-08

## Purpose
Determine how far the already-certified G9 finite-source numerical survivor extends in source-centre offset for the **already frozen generic Galactic CCSN source-size authority**, instead of treating the old 0090f maximum tested offset `100 m` as a physical boundary.

This is a numerical geometry/actionability gate only. It does not repair the independent 0092b-a2 MeV nuclear-channel authority blocker, does not introduce a new source, and does not authorize detector/material/power multiplication.

## Frozen parents
Numerical parent:
- `research/iterations/0090f_g9_full_grid_finite_nonzero_survivors_pass.md`;
- prereg `research/prereg/0090f_g9_full_ray_centric_finite_source_survivor_scan.md`, contract commit `fc277e3695ebeb2628d133b9385e7d7d2e12a5d5`;
- authoritative run/job/artifact `34270367643/102211319629/10073678384`;
- aggregate inner JSON SHA256 `71831e971932c2d347e2f79c4c315c839ae853b2968d75545bb6a3b97ead6083`;
- parent evaluator blob `4bedc9431b428292f1b09613f603bea82597f9b5`;
- 0090f established that every tested nonzero offset through `100 m` survived `mu>=2` and that its global grid minimum was still `157.28015230029052`.

Source parent:
- `data/g9_ccsn_source_authority_0061.json`, Git blob SHA1 `ed2e5ab50375abb1049b86348a2e570b5e7b99f5`;
- benchmark source distance exactly `10.0 kpc` under that authority;
- fiducial neutrino-emission radius `21 km`;
- conservative sensitivity radius `100 km`.

Real-source parent:
- 0091 `BLOCKED_G9_REAL_SOURCE_AUTHORITY` retained the generic 10-kpc CCSN branch as morphology-compatible but alignment/actionability-blocked.

## Frozen lens method and controls
Use exactly the certified 0090e-r1 high method imported without scientific modification:
- exact two-circle overlap;
- angular GL32;
- radial GL64;
- inherited 60-dps disparate-radius overlap branch/fallback;
- same frozen Model-S blob and map;
- same three observer controls and receiver radii `{1,10,100} m`;
- same point-control, map-conformance, whole-aperture and large-source invariants as 0090f.

No adaptive quadrature/order escalation is allowed.

## Frozen CCSN angular sizes
Use the small-angle ratio `theta = R_source / D` with:
- `D = 10,000 pc`;
- `1 pc = (648000/pi) AU`;
- IAU exact `AU = 149597870700 m`;
- source radii exactly `{21,100} km` from the frozen 0061 authority.

The code must record the resulting `theta` and projected source radius `s=z*AU*theta` for each observer control. No result-selected source radius is allowed.

## Map-derived no-overlap ceiling
For each observer/receiver/source-size row family, calculate the frozen ray-map maximum

`y_max = max |y(x)|`

over the exact inherited monotone-absolute-map segment endpoints `{XMIN, turn, x0, XMAX}`. The inherited 0090a segmentation is the authority that `|y|` is monotone on those segments.

For source radius `s` and receiver radius `a`, define the deterministic strict no-overlap ceiling

`d_zero = nextafter(y_max + s + a, +infinity)`.

For any `d >= d_zero`, the minimum possible separation of the ray centre and source centre exceeds `s+a`; hence the exact circle-overlap kernel is zero for every ray and `mu=1`. This ceiling is derived from the frozen map, not chosen after seeing magnification results.

The execution must verify `mu(d_zero)` is numerically equal to 1 within `1e-12` absolute magnification tolerance or classify a scientific/infrastructure failure rather than weakening the ceiling.

## Frozen offset scan
For each of the 18 `(3 observer controls) x (3 receivers) x (2 CCSN radii)` families:
1. start at exactly `d_start = 100 m`, the previous 0090f tested edge;
2. end at that family's `d_zero`;
3. evaluate exactly **257 logarithmically spaced offsets including both endpoints**:

`d_j = exp(log(d_start) + j/256 * (log(d_zero)-log(d_start)))`, `j=0..256`,

with the final node replaced exactly by `d_zero` to avoid transcendental endpoint drift;
4. retain the inherited survivor threshold `mu>=2` unchanged.

This dense scan is a finite-grid topology reconnaissance, not a proof of global monotonicity. The result must explicitly record any sampled re-entry (`mu<2` followed later by `mu>=2`).

## Frozen crossing refinement
For every adjacent logarithmic node pair whose endpoint states straddle `mu=2`, refine that **already prospectively identified bracket** using geometric-midpoint bisection:

`d_mid = sqrt(d_lo*d_hi)`

for exactly 32 iterations, evaluating the same H method.

Record both final endpoints and their `mu` values. Do not assume there is only one crossing. Do not refine intervals that do not straddle the frozen threshold.

## Frozen summary quantities
Per family record:
- all 257 coarse rows;
- `y_max`, `d_zero`;
- number of sampled `mu>=2` rows;
- maximum sampled survivor offset;
- first sampled non-survivor after the start;
- contiguous-prefix last survivor offset starting from 100 m;
- all threshold-straddling refined brackets;
- any sampled re-entry count.

Aggregate record:
- minimum and maximum contiguous-prefix survivor offset across all 18 families;
- minimum and maximum refined first-crossing bracket across all 18 families, where defined;
- corresponding angular misalignment `beta=d/(z*AU)` in rad, microarcsec and arcsec;
- per-observer, per-receiver and per-source-radius summaries.

The **conservative CCSN footprint sentinel** is the minimum lower endpoint of the first refined `mu=2` crossing across all 18 frozen families. This is deliberately conservative and does not assert that every continuous offset below it has been analytically proved monotone; it is the boundary of the sampled contiguous-prefix survivor regime with a refined local crossing.

## Frozen classifications
`PASS_G9_CCSN_ALIGNMENT_FOOTPRINT_EXPANDED` if:
- all 18 families execute with inherited invariants satisfied;
- each starts with `mu(100m)>=2`;
- each reaches the certified no-overlap ceiling with `mu≈1`;
- every family has at least one threshold-straddling bracket;
- the aggregate conservative CCSN footprint sentinel is strictly greater than `100 m`.

`SCIENTIFIC_FAIL_G9_CCSN_ALIGNMENT_FOOTPRINT` if any inherited physical invariant, no-overlap theorem check, or source-authority identity fails.

`BLOCKED_G9_CCSN_ALIGNMENT_TOPOLOGY` if execution is numerically valid but sampled topology is too complex to summarize by the frozen crossing protocol (for example pathological unresolved re-entry requiring a separately preregistered denser/topology-specific gate).

`INFRASTRUCTURE_FAIL_G9_0093` for execution/provenance/runtime failure only.

## Interpretation guards
- `100 m` is a prior tested edge, not a physical alignment tolerance.
- A larger 0093 footprint does not make a generic future CCSN direction known in advance.
- No sky-occurrence probability, warning-time, spacecraft slew, detector event rate, material gain or power claim is authorized in 0093.
- The independent 0092b-a2 MeV nuclear-channel authority blocker remains independent even if 0093 passes.
- No post-hoc source, radius, receiver, threshold or offset-grid change is permitted.
