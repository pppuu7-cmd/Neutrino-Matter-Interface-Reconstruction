# NMIR prereg 0085 — Wagner identity-free B-L upper-bound envelope

Date frozen: 2026-09-08
Status: **PROSPECTIVE / NO 0085 NUMERICAL ENVELOPE INSPECTED**
Parent authority: 0072b axis calibration PASS, 0072c partial primary vector materialization, 0072d blue-name identity FAIL, and 0084b current F8 state.
`NMIR_READINESS: 97%` until this gate is classified.

## Scientific question
Can the old 0072d blue-name failure be bypassed without any post-hoc curve naming by constructing an **identity-free pointwise strongest published Wagner B-L upper-bound envelope** directly from every source-native Figure-6 data-curve component whose geometry is independently validated?

This gate does **not** ask which blue path is EW, EW94 or EW99. It asks only whether each retained path is a genuine member of the primary Figure-6 family of 95% CL upper-bound curves and, if so, what the pointwise minimum published upper limit is wherever at least one validated component has support.

## Frozen primary authority
Primary source: Wagner et al., arXiv `1207.2442v1`, Figure 6 left panel.

Source text/caption authority to be verified from the exact arXiv source in the hosted audit:
- the left panel concerns a vector Yukawa interaction coupled to `q-tilde = B-L`;
- it reports **95% CL upper bounds** on the interaction strength as a function of range `lambda`;
- therefore, for the plotted magnitude `|alpha-tilde|`, points above a valid limit curve are excluded by that individual published upper bound and points below are allowed by that individual curve.

Exact source-native vector asset: `WEP_figure6.eps`.
Frozen EPS SHA256 from 0072b/0072c: `4adafc21e896aa3e19490a586e9249fb9b7c947ad9cbe9efd3416d5e00466882`.

Frozen physical-axis transform from `data/wagner_axis_calibration_0072b.json`:
- `log10(lambda/m) = 3.0018224354393763*x_eps - 7.051566622680237`;
- `log10(|alpha_tilde|) = 1.650456736852946*y_eps - 12.69366318007594`.
The calibration file must classify `PASS_WAGNER_AXIS_CALIBRATION` and carry the same EPS SHA256.

Frozen 0072 conversion retained unchanged:
- `m_V[eV] = 1.973269804e-7 / lambda[m]`;
- `|g_BL| = 2.70463357586823e-19 * sqrt(|alpha_tilde|)`.
No new convention factor may be introduced in 0085.

## Frozen curve-membership rules
Re-parse the exact EPS using the already-audited PostScript path parser and the same Figure-6 left-panel box
`(x0,x1,y0,y1) = (1.681,6.681,0.844,4.844)`.

A candidate data-curve segment is admissible only if all of the following hold:
1. source-native stroke color is exactly one of the Figure-6 experiment colors already frozen in 0072c: blue `(0,0,1)`, red `(1,0,0)`, orange `(1,0.5,0)`, magenta `(1,0,1)`;
2. source-native linewidth is exactly `0.010` under the 0072 parser;
3. primitive path component is a two-point line segment with both endpoints inside the frozen left-panel box;
4. consecutive segments join at the already-frozen `1e-9` EPS Chebyshev tolerance into connected components;
5. components with fewer than 3 joined segments are dropped as label/fragment geometry exactly as in 0072c;
6. every retained component must be monotonic in EPS x, so it represents a single-valued upper-bound function over its own support. If a retained component is not x-monotonic, the gate is BLOCKED rather than split post hoc.

The expected connected-component topology is frozen from the corrected 0072d structural result:
- blue: **4 connected components** (one source experiment is printed as two disconnected trace components; no interpolation across that gap is allowed);
- red: 1;
- orange: 1;
- magenta: 2.
Total expected retained connected components: **8**.

The names of the four blue components remain intentionally unresolved and are irrelevant to 0085. No blue component may be merged, dropped, renamed, or bridged based on visual label proximity or curve shape.

## Frozen envelope construction
Work in `x = log10(m_V/eV)`, `y = log10(|g_BL|)`.

For each retained component:
- transform all source-native vertices using the frozen 0072b calibration and frozen 0072 coupling conversion;
- sort by `x` increasing;
- interpolate **linearly in log-log coordinates only between adjacent source-native vertices of that same connected component**;
- never extrapolate outside that component's x-support;
- never bridge disconnected components, including the two components belonging to the unresolved EW94 source trace.

Evaluation grid:
- union all transformed source-native vertex x values;
- add a deterministic uniform grid of 20,001 points over the union support;
- clip to the global NMIR lower-mass target `m_V >= 1e-6 eV`;
- do not invent an upper mass endpoint beyond the source support.

At each grid x with one or more supported components, define

`y_env(x) = min_i y_i(x)`.

This is named only:

**`POINTWISE_STRONGEST_PUBLISHED_WAGNER_95CL_UPPER_LIMIT`**.

It is **not** a statistically combined 95% CL confidence curve. It is the lower envelope of individually published 95% CL upper limits: at each supported mass it reports the strongest individual source curve. The excluded side is `y > y_env(x)` because at least one published individual upper bound excludes that point.

## Frozen diagnostics
PASS requires all of:
1. exact EPS SHA and 0072b calibration authority match;
2. primary source text explicitly verifies B-L semantics and `95% CL upper bounds` for Figure 6 left panel;
3. retained topology is exactly 4 blue + 1 red + 1 orange + 2 magenta components;
4. all 8 components are x-monotonic and have finite positive transformed `m_V`, `|alpha_tilde|`, and `|g_BL|`;
5. transform round-trip residual in EPS coordinates stays <= `1e-9` as in 0072c;
6. pointwise minimum is invariant to component **names/order**: recomputing after deterministic permutation of anonymous component IDs changes `y_env` by <= `1e-12` decade wherever support is identical;
7. a second independent grid with 40,001 uniform points plus all vertices reproduces the interpolated envelope at 10,001 shared check points within `1e-10` decade;
8. envelope support after the `1e-6 eV` lower clip is non-empty and contains no interpolation across unsupported gaps.

## Frozen classifications
- `PASS_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE`: every diagnostic passes. This closes the **curve-name-independent Wagner side/envelope authority** while leaving blue names unresolved.
- `BLOCKED_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE`: source caption authority, topology, monotonicity, or support membership is insufficient to construct the anonymous envelope without a new assumption.
- `SCIENTIFIC_FAIL_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE`: the frozen source geometry/calibration gives a reproducible contradiction such as invalid/nonfinite transformed bounds or failed deterministic envelope invariance after all prerequisites pass.
- Network/parser/hash/test failures before classification are infrastructure failures.

## Consequence
PASS authorizes the Wagner **identity-free upper-limit curve object** for later F8 envelope composition. It does not authorize a joint/global 95% CL statistical statement and does not by itself authorize union with cosmology, SN1987A, fifth-force, CEvNS or other B-L families. A separate prospective composition/materialization gate is required.

BLOCKED/FAIL retires this anonymous-envelope bypass and leaves only the four already named 0072c Wagner curves as usable primary constraints.

## Guards
No raster/OCR/manual digitization. No visual label-to-curve assignment. No rescue of EW/EW94/EW99 names. No interpolation across disconnected components. No extrapolation outside component support. No post-result curve dropping. No statistical combination claim. No global B-L envelope claim. No BSM response/enhancement scan.
