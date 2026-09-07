# NMIR 0072d pre-result amendment — overlap-logic correction

Date: 2026-09-07
Status: PRE-RESULT. No 0072d identity calculation/result had been executed when this correction was frozen.

## Why correction is required
The already-available structural diagnostic `data/wagner_blue_chains_0072d.json` predates the 0072d scientific calculation and shows that more than one three-chain subset has a common x-overlap. Therefore the preregistration's step requiring a **unique** three-chain overlapping subset is logically overconstrained and would manufacture a failure unrelated to source identity. This is corrected before any 0072d result is computed.

No numerical coordinates, chain points, labels or result produced after the preregistration are used to tune this amendment. The source fact remains unchanged: primary Figure 6 has one EW99 trace family, one EW trace family, and two disconnected EW94 trace components.

## Replacement frozen identity algorithm
Replace steps 2–5 of the parent preregistration with this graph/order rule:

1. For every pair of blue chains having a non-empty common EPS-x interval, sample 101 equally spaced x values across the pair's overlap and linearly interpolate only within each connected chain.
2. A pairwise order is accepted only if one chain is above the other at **all** 101 samples by at least `1e-6` EPS-y. Any crossing/tie within that margin is identity FAIL.
3. Construct the directed order graph `A > B` when A is consistently above B on their common interval.
4. Assign `EW99` only if there is exactly one chain that is consistently above each of the other three on every available pairwise overlap.
5. Assign `EW` only if there is exactly one different chain that is consistently below each of the other three on every available pairwise overlap.
6. The remaining two chains are admissible as `EW94` components only if:
   - they do **not** overlap each other in x (apart from an exact endpoint within `1e-9` EPS-x); and
   - each lies below EW99 and above EW throughout every respective overlap.
7. Label the remaining component with smaller mean/median x as `EW94_short` and the other as `EW94_long`.
8. Preserve the two EW94 components as disconnected. Never interpolate or connect their gap.

All other source guards, fixed points, axes, tolerances, classifications and consequences in the parent 0072d preregistration remain unchanged.
