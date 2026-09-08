# NMIR preregistration 0087 — authoritative partial B-L topology discovery

Date frozen: 2026-09-08
Status: PROSPECTIVE
Purpose: discovery-oriented synthesis, not completeness bookkeeping.

## Scientific question
When only already accepted, same-current, numerically materializable B-L constraint families are composed without manual/raster inference, does their union generate a reproducible parameter-space structure that is not encoded in any single input family: a disconnected permitted component, a bounded/narrow permitted pocket or corridor, or a persistent switch in the family controlling the admissible upper boundary?

A positive result is a **partial-topology candidate** only. It is not a claim of complete allowed B-L space or new physics until missing-family stability/completeness is separately passed.

## Frozen analysis coordinates and window
Use
- `x = log10(m_V / eV)`
- `y = log10(g_BL)`.

Frozen topology analysis window:
- `-6 <= x <= 10` corresponding to `1e-6 eV <= m_V <= 10 GeV`;
- `-25 <= y <= -2`.

The lower y edge is an analysis-window boundary, not a physical exclusion or lower coupling limit.

## Included authoritative numerical families
Only the following may enter 0087:

1. **Solar CEvNS 0078c** — the accepted 90% C.L. polygon from `data/deromeri_bl_excluded_region_0078c.json`. Its native x coordinate is `log10(m_V/GeV)` and must be converted exactly by `x_eV = x_GeV + 9`; y is already `log10(g_BL)`.
2. **CMB 0080d** — the accepted hard `Delta N_eff >= 0.4` conservative excluded geometry, reconstructed from the exact source assets with the already accepted 0080d parser/calibration. Majorana and Dirac are separate alternatives.
3. **SN1987A 0084b** — exact analytical excluded bands from the accepted source-native relations. `BODY_NATIVE` and `CONCLUSION_SUMMARY` upper-mass variants remain separate. T and L are two source-authorized polarization exclusion bands and may be unioned only within the same chosen mass-endpoint variant because both are simultaneous source constraints for that variant.
4. **Wagner 0085 r1** — `POINTWISE_STRONGEST_PUBLISHED_WAGNER_95CL_UPPER_LIMIT`, with only its accepted support and with `y > y_env(x)` excluded. It is not described as a statistically combined 95% C.L. curve.

## Explicitly excluded from numerical composition
The following may be reported as missing-family stability risks but may not contribute invented geometry:
- NA64 0086c: `BLOCKED_NA64_B_L_VECTOR_AXIS_CALIBRATION`;
- BBN 0081a: numerical polygon blocked;
- Cerdeño 0082c: axis calibration blocked;
- combined COHERENT 0074c global B-L contour: blocked;
- Hong/Cas A prose-only approximate endpoint where no exact finite geometry is authorized;
- Fayet 0079a fifth-force finite-mass continuation: forbidden. Its asymptotic bound may be mentioned separately but cannot be extended across finite mass in the topology union.

No blocked family may be converted into an approximate polygon, upper curve, or fill.

## Scenario-conditioned compositions
Compute exactly four independent scenario combinations:
1. `CMB_MAJORANA__SN_BODY_NATIVE`
2. `CMB_MAJORANA__SN_CONCLUSION_SUMMARY`
3. `CMB_DIRAC__SN_BODY_NATIVE`
4. `CMB_DIRAC__SN_CONCLUSION_SUMMARY`

Solar CEvNS and Wagner are common to all four.

Majorana/Dirac must never be unioned or intersected with each other. BODY_NATIVE and CONCLUSION_SUMMARY must never be unioned or intersected with each other.

## Geometry rules
- All accepted polygon inputs must be valid before composition; no `buffer(0)` or topology repair.
- Clip each input only to the frozen analysis window.
- Preserve disconnected components.
- Excluded union for a scenario is the exact geometric union of only its included source-authorized excluded sets.
- Permitted complement is `analysis_window - excluded_union`.
- Window-edge contacts must be recorded; a component touching the analysis-window boundary is not called a physically bounded island.
- No smoothing, extrapolation, rasterization, OCR, manual clicking, or bridging.

### Wagner upper-limit polygonization
Use the accepted 0085 piecewise-linear envelope vertices/support. Close the excluded set only upward to `y=-2` within the envelope's own x support. This closure encodes the already accepted 0085 semantics `y > envelope excluded` and is not extrapolation in x.

### SN analytical bands
Build exact polygons directly from the 0084b accepted `polygon_log10_m_eV_log10_g` vertices. Union T and L within each chosen mass-endpoint variant only.

### CMB geometry
Re-run exact 0080d source-hash/vector/calibration code and use its refined `tol=0.01 pt` geometry. The 0080d PASS and source hashes must reproduce before its WKT may enter 0087.

## Frozen topology observables
For every scenario report:
- excluded-union area in `decade^2`;
- permitted-complement area in the finite analysis window;
- number and area of permitted connected components;
- for each permitted component, whether it touches left/right/top/bottom analysis-window boundaries;
- pairwise overlap areas between included independent families;
- source-family labels touching each non-window segment of any bounded permitted component boundary.

## Frozen novelty criteria
A scenario receives `PARTIAL_TOPOLOGY_CANDIDATE=true` if at least one of the following is satisfied:

### N1 — disconnected permitted topology
The permitted complement has at least two connected polygonal components with area `>= 0.01 decade^2` each.

### N2 — bounded multi-family pocket/corridor
A permitted component of area `>= 0.01 decade^2` touches no analysis-window boundary and at least two independent source families contribute nonzero-length segments to its boundary.

### N3 — persistent controlling-family switch
For the **upper admissible frontier only where such a frontier is defined by upper-limit-type included families**, the controlling independent family changes at least once, and the controlling family on each side persists over at least `0.1 decade` in x. The switch location must reproduce within `0.01 decade` under an independently doubled deterministic sampling density.

SN excluded bands and finite filled polygons are not silently reinterpreted as global upper-limit curves for N3.

## Acceptance taxonomy
- `PASS_PARTIAL_B_L_TOPOLOGY_CANDIDATE`: all included authoritative inputs reproduce and at least one N1/N2/N3 criterion is satisfied in at least one scenario.
- `PASS_PARTIAL_B_L_NO_NONTRIVIAL_TOPOLOGY`: all included inputs reproduce but N1/N2/N3 are false in every scenario.
- `BLOCKED_PARTIAL_B_L_TOPOLOGY_INPUT_AUTHORITY`: an included previously accepted numerical object cannot be reproduced exactly enough to enter the composition.
- `SCIENTIFIC_FAIL_PARTIAL_B_L_TOPOLOGY_INTEGRITY`: reproduced accepted inputs contradict their frozen geometry/semantics or composition invariants.
- Infrastructure/network/parser/test failures remain non-scientific and may be rerun without changing this preregistration.

## Robustness / convergence
- Polygon areas/topology use exact Shapely operations on accepted vector/polyline/analytical geometry.
- N3 deterministic samples: base `2001 samples/decade`, refined `4001 samples/decade`; switch locations must agree to `<=0.01 decade` and persistence must pass at both densities.
- Areas must be finite/nonnegative; `excluded_area + permitted_area` must reproduce the analysis-window area within relative `1e-10`.

## Interpretation guard
A PASS candidate means: **the already-authoritative subset of independent B-L constraints generates a nontrivial synthetic topology**. It does not mean the feature survives NA64, BBN, Cerdeño, COHERENT, other missing families, or a future completeness audit. It does not unlock BSM response/enhancement.

If a candidate passes, the mandatory next gate is a missing-family stability/completeness test. Only after that may a separate preregistration test whether a surviving corridor overlaps an independently defined neutrino-matter response optimum.
