# 0105a5b R1c amendment 01 — authority-derived bin-index mapping

Date frozen: 2026-09-10
Scope: NMIR v2 only. NMIR v1 remains frozen and unchanged.
Parent preregistration: `research/prereg/0105a5b_r1c_deepcore_coordinate_semantics_preregistration.md`.

## Why this amendment is allowed

The hosted R1c authority-evidence bundle was collected without computing any oscillated expectation, likelihood, nuisance fit, observed-minus-null residual, BSM residual, or significance. It recovered literal B4RITM v1.0 documentation stating that reconstructed variables are provided in the analysis binning, that events fall into the midpoint of their bin, and that the MC reconstructed variables follow the same convention as `data.csv`.

R1b had compared literal coordinate labels and found that the MC tuple support is not a literal subset of the observed tuple support. The evidence bundle shows why literal label equality is not the authority-defined semantic relation: labels are representations of analysis bins. This amendment freezes the authority-derived mapping before any standalone 3nu expectation or likelihood calculation and does not change the parent R1c PASS/BLOCKED/FAIL criteria.

## Frozen authority

Only the byte-locked B4RITM release `10.7910/DVN/B4RITM`, version 1.0, is used. `10.7910/DVN/QKL28Z` remains forbidden as a substitute.

The exact B4RITM README supplies the analysis-bin boundaries:

- `reco_energy` edges in GeV: `[6.31, 8.45862141, 11.33887101, 15.19987592, 20.37559363, 27.3136977, 36.61429921, 49.08185342, 65.79474104, 88.19854278, 158.49]`;
- `reco_coszen` edges: `[-1.0, -0.89, -0.78, -0.67, -0.56, -0.45, -0.34, -0.23, -0.12, -0.01, 0.1]`;
- `pid` edges: `[0.55, 0.75, 1.0]`.

The README explicitly states that reconstructed variables are in the analysis binning and events fall into the midpoint of their bin; it further states that MC reconstructed variables follow the same convention as `data.csv`.

## Frozen deterministic mapping

For each of the three reconstructed coordinates separately, assign the released coordinate label `x` to the unique bin index `j` satisfying the strict interior rule

`edge[j] < x < edge[j+1]`.

No tolerance, nearest-neighbour rule, clipping, rounding repair, interpolation, or residual-dependent choice is permitted. A coordinate on or outside a boundary is an immediate structural FAIL for this mapping route.

The 3D cell key is exactly

`(pid_bin_index, reco_coszen_bin_index, reco_energy_bin_index)`.

Apply the identical boundary-index rule independently to:

1. every one of the 200 observed rows in the locked `data.csv`; and
2. each unique native-MC reconstructed-coordinate tuple in the union of the four locked neutrino MC files.

## Frozen checks

PASS under the unchanged parent criterion requires all of the following in hosted execution:

1. exact locked B4RITM v1.0 source provenance;
2. exactly 200 observed rows and 200 unique observed cell keys;
3. exactly 200 unique native-MC coordinate tuples and 200 unique MC cell keys;
4. every coordinate on both sides maps to exactly one strict-interior bin index on every axis;
5. the set of 200 observed cell keys equals the set of 200 MC cell keys exactly;
6. each side spans exactly `2 x 10 x 10 = 200` cell keys;
7. no tolerance or numerical-distance criterion appears in the implementation;
8. dedicated tests verify the bin-index rule, the PID representation case (`0.88` observed versus `0.875` MC) maps to the same upper PID bin without rounding, and an edge-valued coordinate fails closed;
9. raw hosted result and artifact hashes are inspected before classification.

If official bytes fail any total/bijection condition despite these authority-derived semantics, classify `SCIENTIFIC_FAIL_0105A5B_R1C_COORDINATE_MAPPING_NONBIJECTIVE` exactly as in the parent preregistration. Provider/runtime/artifact failure before evaluation is `INFRASTRUCTURE_FAIL_0105A5B_R1C`.

## Explicit prohibition

This amendment does not authorize an oscillated 3nu expectation, likelihood, nuisance profiling, residual, NSI, magnetic spin-flavor, light-mediator fit, or any BSM/significance calculation. The six Barr/MCEq directions plus DIS-CSMS remain orthogonal unresolved external-computational authorities even if R1c passes.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`.
