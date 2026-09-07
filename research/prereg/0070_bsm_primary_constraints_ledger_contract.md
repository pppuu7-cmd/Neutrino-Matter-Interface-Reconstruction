# NMIR preregistration 0070 — primary BSM constraints-ledger gate

Date frozen: 2026-09-07
Status: PROSPECTIVE
Parent authority: iteration 0069 `PASS_UNLOCK_BSM_CONSTRAINT_LEDGER_ONLY`.

## Scope
This gate does **not** search for a large NMIR enhancement. It freezes external constraints first so that any later BSM response calculation is restricted to already-allowed parameter space.

## Frozen operator basis to audit first
Start with the minimal neutrino-matter light-mediator classes that can modify low-energy scattering without changing the NMIR bookkeeping rules:
1. vector mediator coupled to neutrinos and ordinary matter currents;
2. scalar mediator coupled to neutrinos and nucleons/electrons;
3. axial/spin-dependent mediator only as a separately normalized class.

For each class, define before collecting limits:
- mediator mass convention;
- neutrino coupling and matter coupling convention;
- whether quoted limits constrain a product or individual couplings;
- operator normalization and target species;
- whether the mediator is universal, leptophilic, baryonic, or otherwise restricted.

Do not combine limits written in incompatible coupling conventions until an explicit conversion is frozen.

## Required primary constraint families
Freeze primary, dated, recoverable sources for all applicable classes:
- laboratory neutrino scattering / CEvNS / neutrino-electron scattering;
- collider or fixed-target constraints where applicable;
- stellar cooling / supernova energy-loss or trapping constraints where applicable;
- cosmological BBN/CMB/free-streaming constraints where applicable;
- fifth-force/equivalence-principle constraints if the mediator couples to ordinary matter strongly enough for them to apply.

## Acceptance criteria
`PASS_BSM_CONSTRAINT_LEDGER_FROZEN` only if:
- coupling conventions are explicit and machine-readable;
- each retained exclusion/limit has primary provenance and date/version;
- applicability assumptions are recorded;
- contradictory/non-overlapping conventions are not silently merged;
- no NMIR enhancement result is inspected or optimized before the ledger is frozen.

`BLOCKED_BSM_CONSTRAINT_NORMALIZATION` if a class cannot be mapped to a common convention without model assumptions not frozen prospectively.

## Next action on PASS
Freeze a separate prospective NMIR-response gate using only parameter points surviving the external ledger. No gain factor from G2/G3/G8/G9 may be multiplied into the BSM result unless independently validated and compatible.

## Readiness
Documentation/constraint collection alone earns no automatic readiness credit. A later reproducible exclusion of parameter space or a bounded BSM response gate may earn scientific credit.
