# NMIR preregistration 0071 — gauge-complete U(1)_{B-L} primary constraints ledger

Date frozen: 2026-09-07
Status: PROSPECTIVE
Parent: iteration 0070 `BLOCKED_BSM_CONSTRAINT_NORMALIZATION`.

## Scope
Audit one well-defined, anomaly-free benchmark only: a light vector mediator `V_mu` gauging `U(1)_{B-L}` with mass `m_V` and one gauge coupling `g_BL`:

`L_int = g_BL V_mu J_{B-L}^mu`.

Use standard B-L charges: leptons `-1`, quarks `+1/3`, hence approximately `+1` per nucleon before nuclear form factors. Right-handed-neutrino/anomaly-cancellation content must be stated whenever a cited bound depends on it.

This gate freezes external constraints only. It does not calculate or optimize an NMIR response.

## Required primary constraint families
For the same `(m_V,g_BL)` convention, freeze primary and dated authority for all applicable families:
1. low-energy laboratory neutrino scattering / CEvNS / neutrino-electron scattering;
2. collider/fixed-target visible/invisible searches, with decay assumptions explicit;
3. stellar/SN production, cooling and trapping where applicable;
4. cosmological BBN/CMB/free-streaming, with thermal-history assumptions explicit;
5. fifth-force/equivalence-principle/long-range-force limits at sufficiently small `m_V`.

A family may be marked `NOT_APPLICABLE_IN_FROZEN_MASS_RANGE` only with explicit physical justification. Do not import a universal-vector or product-coupling contour as B-L unless the primary source gives an exact mapping.

## Machine-readable requirements
Each retained constraint record must contain:
- primary citation/DOI/arXiv or experimental publication;
- date/version;
- mass range;
- coupling convention and confidence level where given;
- visible/invisible/trapping/thermal-history assumptions;
- whether it excludes above, below, or a band in `g_BL`;
- digitized numerical contour only when recoverable without reading values by eye from an uncalibrated plot.

## Acceptance criteria
`PASS_B_MINUS_L_CONSTRAINT_LEDGER_FROZEN` only if the ledger establishes a reproducible externally allowed region or a reproducible statement that no region survives over a prospectively specified mass interval, with all applicable constraint families represented in the same B-L convention.

`BLOCKED_B_MINUS_L_PRIMARY_CONTOUR_MATERIALIZATION` if relevant primary constraints exist but their numerical contours cannot be materialized sufficiently to define the allowed region.

`SCIENTIFIC_FAIL_B_MINUS_L_NO_SURVIVING_REGION` only if the frozen primary ledger reproducibly excludes the entire audited mass interval under the same benchmark assumptions.

## Frozen initial mass interval
Audit `1e-6 eV <= m_V <= 10 GeV` as the broad discovery interval. The ledger may use subranges appropriate to each experiment; no uncovered mass gap may be silently called excluded.

## Next action
On PASS with surviving space: freeze a separate prospective NMIR B-L response bound using only surviving points and no unresolved SM gain multiplication.

On BLOCKED: keep BSM at constraints-ledger-only and record exactly which primary contour/data product is missing.

On scientific no-survivor FAIL: retire this B-L benchmark in the audited interval and choose the next gauge-complete benchmark rather than weakening constraints.

## Readiness
Constraint collection alone earns no readiness credit. A reproducible bound on the surviving B-L response may earn credit later.
