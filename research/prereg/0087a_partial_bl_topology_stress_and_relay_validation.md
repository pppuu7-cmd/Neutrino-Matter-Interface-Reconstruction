# NMIR preregistration 0087a — partial B-L topology stress test and constraint-relay validation

Date frozen: 2026-09-08
Status: PROSPECTIVE VALIDATION OF AN 0087-GENERATED CANDIDATE/HYPOTHESIS
Parent: 0087 `PASS_PARTIAL_B_L_TOPOLOGY_CANDIDATE`.

## Why this gate exists
0087 prospectively discovered N1 disconnected permitted topology in all four preserved scenario branches, but every component touched the finite analysis-window boundary. 0087 also generated, post hoc, a separate hypothesis from its overlap matrix: SN1987A may be an articulation bridge connecting the ultra-light Wagner constraint to the higher-mass CMB/solar-CEvNS constraint network.

0087a is a **falsification-oriented validation gate**. It does not retroactively change the 0087 novelty criteria.

## Frozen inputs
Reproduce the same authoritative geometries and semantics as 0087, with no new family added:
- Solar CEvNS 0078c;
- CMB 0080d, Majorana and Dirac separate;
- SN1987A 0084b, BODY_NATIVE and CONCLUSION_SUMMARY separate;
- Wagner 0085-r1.

All source hashes/classifications accepted by 0087 must reproduce. NA64/BBN/Cerdeno/COHERENT/finite fifth-force remain omitted rather than approximated.

## Scenario branches
Validate all four independently:
1. CMB Majorana + SN BODY_NATIVE
2. CMB Majorana + SN CONCLUSION_SUMMARY
3. CMB Dirac + SN BODY_NATIVE
4. CMB Dirac + SN CONCLUSION_SUMMARY

## A. Inward-window stress test
The original 0087 x range remains fixed: `-6 <= log10(m/eV) <= 10`.
The lower y analysis edge remains `-25`.

Without any outward extrapolation, repeat the permitted-complement connectivity test at these prospectively frozen inward ceilings:
- `y_max = -2.0` (0087 reference)
- `y_max = -3.0`
- `y_max = -4.0`
- `y_max = -5.0`.

For every ceiling, each family is intersected with the smaller finite window before union. Empty geometry is permitted only if the source family truly has no support inside that inward window; it must be recorded and may not be extended.

`WINDOW_STABLE_N1=true` for a scenario only if at every one of the four ceilings the permitted complement contains >=2 connected polygon components of area >= `0.01 decade^2`.

Global partial-topology stress PASS requires `WINDOW_STABLE_N1=true` in **all four** scenario branches.

This validates only stability under inward truncation. It still does not turn a boundary-touching component into a globally bounded physical island.

## B. Leave-one-family-out stress test
At the original `y_max=-2` window, remove each included family exactly once and recompute:
- permitted connected-component count;
- qualifying component count >=0.01 decade^2;
- N1 truth value.

No LOFO outcome is required for PASS; it is a causal diagnostic used to identify whether one family is structurally necessary for the observed fragmentation. Results must be reported without reinterpretation.

## C. Prospectively frozen constraint-relay hypothesis test
Build an undirected overlap graph at each of the four y ceilings separately for every scenario.

Nodes are the four included source families:
- `WAGNER_0085`
- `SN1987A_<variant>_0084b`
- `CMB_<scenario>_0080d`
- `SOLAR_CEVNS_0078c`.

Add an edge only when the exact positive-area overlap inside that finite window is >= `0.01 decade^2`. Point/line contact does not count.

The generated `SN1987A ARTICULATION / CONSTRAINT-RELAY` hypothesis is prospectively validated for a scenario at a given y ceiling iff:
1. the full four-node overlap graph is connected;
2. Wagner has a positive-threshold edge to SN1987A;
3. after deleting the SN1987A node, Wagner has no graph path to either CMB or Solar CEvNS;
4. before deletion, Wagner has a graph path to both CMB and Solar CEvNS.

`RELAY_STABLE=true` requires these four conditions at all four y ceilings.
Global relay validation requires `RELAY_STABLE=true` in all four scenario branches.

## D. Exact geometry and integrity
- No topology repair / `buffer(0)`.
- No raster/OCR/manual digitization.
- No interpolation/extrapolation beyond already accepted geometry.
- Area closure for each stress window must satisfy relative error <= `1e-10`.
- All overlap areas and component areas must be finite and nonnegative.
- Majorana/Dirac and BODY_NATIVE/CONCLUSION_SUMMARY remain separate.

## Acceptance taxonomy
- `PASS_PARTIAL_B_L_TOPOLOGY_AND_RELAY_ROBUST`: window-stable N1 passes in all four scenarios AND relay validation passes in all four scenarios.
- `PASS_B_L_CONSTRAINT_RELAY_ONLY_TOPOLOGY_EDGE_SENSITIVE`: relay validation passes in all four scenarios, but window-stable N1 fails in >=1 scenario/ceiling.
- `PASS_PARTIAL_B_L_TOPOLOGY_STABLE_RELAY_NOT_VALIDATED`: window-stable N1 passes in all four scenarios, but relay validation fails.
- `PASS_0087A_NO_ROBUST_STRUCTURE`: both window-stability and relay validation fail without integrity failure.
- `BLOCKED_0087A_INPUT_AUTHORITY`: a required accepted input cannot be reproduced.
- `SCIENTIFIC_FAIL_0087A_GEOMETRY_INTEGRITY`: geometry/area closure contradicts frozen accepted inputs or invariants.
- Parser/network/test failures remain infrastructure-only.

## Interpretation guard
Even the strongest PASS establishes only a new **cross-family structural synthesis within the authoritative partial constraint set**. It is not literature-priority proof, a complete B-L allowed region, or evidence for a new particle. Missing-family stability remains mandatory next, especially NA64, BBN, Cerdeño and combined COHERENT.

BSM response/enhancement remains locked.
