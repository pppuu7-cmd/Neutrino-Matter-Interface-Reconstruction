# 0105a5b R1c preregistration — DeepCore B4RITM coordinate-semantics authority

Date frozen: 2026-09-10
Scope: NMIR v2 only. This preregistration does not modify any NMIR v1 result.

## Motivation and separation from R1b

R1b is immutable `BLOCKED_0105A5B_R1B_MACHINE_SCHEMA_OR_STRUCTURE_INCOMPLETE`, with the specific stopping condition `BLOCKED_0105A5B_R1B_MC_COORDINATES_OUTSIDE_OBSERVED_GRID`. R1c is a new authority-only gate whose sole purpose is to determine whether the frozen B4RITM authority itself specifies an exact deterministic mapping between the published observed 200-cell representation and the native MC reconstructed-coordinate representation.

The numerical/cardinality facts revealed by R1b may motivate this authority question, but they may not determine its answer. In particular, R1c is forbidden from declaring a bin-center/bin-edge interpretation merely because both sides contain 200 unique coordinates.

## Frozen authority scope

Allowed authority is limited to the already locked IceCube DeepCore B4RITM release `10.7910/DVN/B4RITM`, release 1.0, using the byte-authoritative Saved Original files and the official documentation/method material belonging to that release or the explicitly pinned IceCube publication authority already recorded in the 0105a5 lineage.

`10.7910/DVN/QKL28Z` remains a separate sterile-control authority and is forbidden as a substitute.

No secondary reconstruction, tutorial, community code, guessed convention, interpolation chosen after inspection, or residual-derived mapping is permitted.

## Frozen objects

Observed representation is the exact locked `data.csv` 200-cell `10 x 10 x 2` table.

MC representation is the union of the exact locked native MC files used by R1b, projected only onto the already frozen reconstructed analysis coordinates:

- `reco_coszen`
- `reco_energy`
- `pid`

Expected structural cardinalities carried forward as fixed controls before semantic inspection:

- observed unique cells: 200
- MC unique reconstructed-coordinate tuples: 200

These cardinalities are controls only and are insufficient for PASS.

## Frozen questions

R1c shall answer, using authority text/metadata and exact locked bytes only:

1. What semantic quantity does each observed `reco_coszen`, `reco_energy`, and `pid` value encode: center, lower edge, upper edge, interval label, category label, or another explicitly documented representation?
2. What semantic quantity do the corresponding MC reconstructed values encode?
3. Does the authority provide sufficient bin-boundary/category information to derive a unique deterministic mapping from every native MC tuple to exactly one observed cell?
4. Is that mapping total and bijective over the frozen 200-cell support, with no duplicate, missing, multiply assigned, or out-of-support cell?
5. Can the mapping be stated without inspecting observed-minus-null residuals, oscillated expectations, nuisance fit behavior, or any BSM quantity?

## Frozen PASS criterion

`PASS_0105A5B_R1C_COORDINATE_SEMANTICS_AUTHORITY_NONDISCOVERY` requires all of the following:

- exact source provenance is the frozen B4RITM/IceCube authority described above;
- the semantic interpretation of all three reconstructed axes is explicitly supported by authority rather than inferred from numerical coincidence;
- one deterministic mapping rule is frozen and executable before any 3nu expectation/likelihood calculation;
- all 200 unique native MC reconstructed-coordinate tuples map to exactly one of the 200 observed cells;
- every observed cell receives exactly one unique reconstructed-coordinate tuple at the coordinate-support level;
- no tuple requires clipping, nearest-neighbor guessing, tolerance selected after inspection, interpolation chosen from residual behavior, or unpinned convention;
- dedicated tests reproduce the mapping and structural invariants from the byte-locked release;
- hosted artifact/raw result reproduces the local implementation and passes the same frozen conditions.

A PASS is `NONDISCOVERY`: it only resolves coordinate semantics. It does not resolve the seven external nuisance dependencies and does not authorize observed residual execution.

## Frozen BLOCKED criterion

`BLOCKED_0105A5B_R1C_COORDINATE_SEMANTICS_AUTHORITY_INCOMPLETE` if the official frozen authority does not uniquely specify enough semantics/boundaries/categories to derive the mapping without an assumption or external substitute.

Missing documentation is BLOCKED, not permission to infer bin centers/edges from values.

## Frozen structural/scientific FAIL criterion

`SCIENTIFIC_FAIL_0105A5B_R1C_COORDINATE_MAPPING_NONBIJECTIVE` if the authority does specify the semantics, but the resulting exact mapping is non-total or non-bijective on the frozen 200-cell support (duplicate assignment, missing observed cell, unresolved overlap, or authoritative incompatibility between the released observed and MC coordinate supports).

This is a release-structure/reproduction-path FAIL, not a statement about BSM physics.

## Frozen infrastructure taxonomy

`INFRASTRUCTURE_FAIL_0105A5B_R1C` is reserved for failures occurring before the semantic/structural criterion can be evaluated, such as provider transport failure, GitHub runtime failure, missing runtime dependency, artifact upload failure, or inability to retrieve a previously byte-locked authority file. Infrastructure repair may change transport/runtime only and may not alter the source set, mapping rule, tolerances, or scientific criteria.

## Explicitly forbidden calculations

R1c must not compute or inspect:

- oscillated 3nu expectation;
- chi-square or likelihood value;
- nuisance fit/profiling;
- observed-minus-null residual;
- BSM residual;
- NSI, magnetic spin-flavor, light-mediator or alternative BSM fit;
- significance or Wilks threshold.

## Seven external dependencies remain orthogonal

R1c does not resolve `BarrWP`, `BarrWM`, `BarrYP`, `BarrYM`, `BarrZP`, `BarrZM`, or `DIS-CSMS`. Even a full R1c PASS only permits the next separately preregistered authority step for those dependencies before standard-3nu likelihood reproduction.

## Permission after R1c

- PASS: permits only the next prospectively frozen external-computational-authority subgate(s) required by R1b, while preserving the exact coordinate mapping established here.
- BLOCKED or FAIL: forbids DeepCore standalone 3nu/null reproduction until a new, independently justified authority route is prospectively frozen; no post-hoc mapping substitution is allowed.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%` throughout R1c.
