# NMIR preregistration 0072 — reproducible U(1)_{B-L} contour materialization

Date frozen: 2026-09-07
Status: PROSPECTIVE
Parent: iteration 0071 `BLOCKED_B_MINUS_L_PRIMARY_CONTOUR_MATERIALIZATION`.

## Scientific question
Can the primary B-L constraints already identified in 0071 be converted into a reproducible numerical exclusion/allowed-region ledger in the single `(m_V,g_BL)` convention without manual plot reading or hidden recasting assumptions?

## Frozen scope
Model and interval remain unchanged from 0071:

`L_int = g_BL V_mu J_{B-L}^mu`,

with standard B-L charges and

`1e-6 eV <= m_V <= 10 GeV`.

This gate materializes external constraints only. It does not calculate any NMIR response.

## Allowed materialization routes, in priority order
For each retained primary constraint use exactly one auditable route:
1. author/publisher-provided numerical table, ancillary file or public code producing the contour;
2. calibrated vector-path extraction from publication PDF/XML/SVG where axes/transforms are exactly recoverable;
3. independent likelihood/rate reproduction from the primary paper and released experimental data under the same B-L convention.

Manual point reading from raster/un-calibrated figures is forbidden. A review or secondary plot cannot replace missing primary numerical authority.

## Priority families
Materialize first the constraints capable of controlling the frozen interval:
- fifth-force/long-range-force low-mass region;
- BBN/CMB and stellar/SN eV–MeV region;
- CEvNS and neutrino-electron/direct-detection keV–GeV region.
Collider bounds outside 10 GeV are retained as context but do not need to define the frozen interval.

## Numerical representation
Every successfully materialized contour must be stored as machine-readable monotonic segments or polygons with:
- source identifier and date/version;
- exact units and axis transforms;
- coupling convention and CL where given;
- exclusion sense (`above`, `below`, `band`, polygon);
- applicable assumptions;
- source file/hash or code commit when available;
- extraction/reproduction method and validation check.

A combined allowed-region calculation may occur only after each included contour passes its own validation.

## Acceptance criteria
`PASS_B_MINUS_L_CONTOURS_MATERIALIZED` only if enough primary contours are reproducibly materialized to determine whether a nonempty allowed region exists across the full frozen interval, with no uncovered mass gap silently classified.

`BLOCKED_PRIMARY_NUMERICAL_DATA_UNAVAILABLE` if one or more controlling primary contours cannot be materialized by any allowed route and therefore prevent a global allowed-region statement.

`SCIENTIFIC_FAIL_REPRODUCTION_MISMATCH` if an independent reproduction or vector extraction fails a source-stated benchmark beyond its declared numerical tolerance.

## Infrastructure versus scientific failure
Download/parser/API/vector-extraction software failures are infrastructure failures and do not alter physics classification. A missing author data product or irrecoverable raster-only contour after all allowed routes is a scientific-authority blocker, not evidence that the parameter region is allowed.

## Frozen next actions
On PASS: freeze the global B-L allowed region and prospectively preregister a separate NMIR B-L response **bound** using only surviving points.

On BLOCKED: keep BSM constraints-only and record the exact source/contour preventing closure; choose the next primary materialization/reproduction route rather than interpolating by eye.

On reproduction mismatch: preserve the failure and do not use that contour until the discrepancy is resolved under a new prospective amendment.

## Readiness
No readiness credit for contour extraction alone. Credit is possible only after an external parameter envelope is reproducibly closed or a later physical response is bounded.
