# NMIR prereg 0087b — missing-family mass-support threat ranking

Date: 2026-09-08

## Motivation
Iteration 0087a established a scenario-stable disconnected permitted topology for the authoritative partial B-L family set and identified SN1987A as the unique leave-one-family-out pivot. Missing numerical families can invalidate a global claim. Before spending effort on blocked y-coordinate geometry, rank those families by source-authorized mediator-mass support alone.

This gate is a **threat-ranking / falsification gate**, not a global allowed-region composition and not a BSM-response unlock.

## Transparency about pre-prereg input recovery
Before this preregistration, repository/source-authority recovery had already established:
- the robust 0087a candidate and its parent 0087 component ranges;
- NA64 0086c has three accepted printed x anchors at 10^-2, 10^-1, 10^0 GeV, with the exact source-native plot frame sharing the outer x coordinates; therefore the exact unbroken-B-L NA64 figure mass support is 10^-2..10^0 GeV (1e7..1e9 eV). No y calibration is used;
- the 0071 primary ledger explicitly records the Esseili–Kribs cosmology BBN/CMB source-family mass range as 1..1e8 eV;
- Fayet 0079/0079a authorizes only the strict long-range/asymptotic m_V->0 result and no finite-mass support interval;
- Cerdeño 0082c and COHERENT 0074c have no already-promoted complete numerical mass-support interval suitable for this threat test.

Accordingly the novel prospective step is the **uniform classification of missing families against the recomputed robust 0087a component mass interval**, not discovery of the already recovered source endpoints above.

## Frozen target
Recompute the 0087a geometry using the exact same accepted parent loaders and the inward ceiling `log10(g_BL)=-5`, separately for all four CMB × SN endpoint scenarios. In each scenario:
1. form the permitted complement in the frozen x window `-6 <= log10(m/eV) <= 10` and y window `-25 <= log10(g_BL) <= -5`;
2. retain polygon components with area >=0.01 decade^2;
3. require exactly two qualifying components as reproduced by 0087a;
4. define the **robust low-mass candidate component** as the qualifying component with the smaller area;
5. record its exact x bounds. The conservative target mass interval is the union-envelope `[min x_min, max x_max]` across the four preserved scenarios.

No component may be selected by visual appearance or desired location.

## Frozen missing-family authority table
Classify only the following outstanding threats:

1. `NA64_UNBROKEN_BL_0086c`
   - mass support: `[1e7, 1e9] eV`;
   - authority: exact source-native `bminusl_unbroken.pdf` x-axis printed anchors and plot-frame alignment from 0086c diagnostic; y remains blocked and unused.

2. `BBN_ESSEILI_KRIBS_0081a`
   - conservative source-family mass support: `[1, 1e8] eV`;
   - authority: `data/b_minus_l_primary_constraints_0071.json` explicit `mass_range_eV` for cosmology BBN/CMB;
   - BBN y geometry remains blocked and unused.

3. `CERDENO_SN_TRANSPORT_0082c`
   - mass support: `UNRESOLVED` for this gate because 0082c did not promote an x calibration after parser/sign/axis ambiguity;
   - do not reuse provisional 0082b x anchors as a physical interval.

4. `COHERENT_COMBINED_0074c`
   - mass support: `UNRESOLVED` for this gate because the current authoritative COHERENT record does not freeze a complete B-L mediator-mass contour support interval and the combined likelihood is blocked;
   - no figure reading or benchmark interpolation.

5. `FIFTH_FORCE_FINITE_MASS_0079`
   - mass support: `UNRESOLVED_FINITE_MASS`; only the strict `m_V -> 0` asymptote is authoritative;
   - no Yukawa turn-off extrapolation.

## Threat classification rule
For a family with a closed source-authorized interval `[a,b]` and target `[t0,t1]`:
- `PROVABLY_MASS_DISJOINT` iff `b < t0` or `a > t1` (strict separation);
- `MASS_OVERLAP_THREAT` otherwise, including endpoint contact;
- `UNRESOLVED_MASS_SUPPORT_THREAT` if no finite source-authorized interval is available.

The audit must report the logarithmic separation in decades for disjoint intervals and overlap width/fraction for overlapping intervals.

## Acceptance / classification
- `PASS_MISSING_FAMILY_MASS_SUPPORT_THREAT_RANKING` if the 0087a two-component geometry is exactly reproduced in all four scenarios, the target interval is finite/positive, and every listed missing family receives one of the frozen threat labels without inventing y geometry.
- `SCIENTIFIC_FAIL_0087B_PARENT_REPRODUCTION` if the two-component 0087a topology or area/integrity checks fail.
- `BLOCKED_0087B_INPUT_AUTHORITY` for missing/corrupt parent authority bytes or incompatible ledger semantics.

No stronger classification is possible in 0087b. In particular, clearing NA64 by mass does not imply global completeness if BBN overlaps or other families remain unresolved.

## Guards
No y-coordinate inference for blocked families. No raster/OCR/manual digitization. No Cerdeño provisional x promotion. No COHERENT benchmark interpolation. No finite-mass fifth-force extrapolation. No cross-scenario union of excluded regions. No global B-L allowed-region claim. No BSM response/enhancement scan.
