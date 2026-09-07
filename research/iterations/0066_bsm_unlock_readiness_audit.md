# NMIR iteration 0066 — formal BSM unlock readiness audit

Date: 2026-09-07
Classification: **FAIL_KEEP_BSM_LOCKED_OPEN_SM_ACTIONABLE**

## Prospective authority
- prereg: `research/prereg/0066_bsm_unlock_readiness_audit.md`
- prereg commit: `77ecef8795ccdcd7ec990b2f280fdf39012c5c15`
- pre-result evidence-set amendment: `research/amendments/0066_g8_concurrent_evidence_correction.md`
- amendment commit: `0534ea599560b050f576e9b706864f41ca797f3c`

The amendment did not alter the frozen unlock criterion. It corrected the evidence set after discovering that a prospectively frozen concurrent G8 result already existed before 0066 was frozen.

## Survivor audit
- **G2 — BLOCKED_NOT_ACTIONABLE.** 0063 found no public same-configuration sub-keV measured rejection × bulk-NR acceptance pair satisfying the frozen comparator. Do not cross-multiply different detectors/configurations.
- **G3 — OPEN residual, but no currently identified new actionable universal route.** Absolute short-range/contact-current coefficient remains physically open. 0059, 0062 and 0065 retire theory-hard-bound, naive finite-l unitarity and observable-only inclusive-map routes respectively. This is not counted as closed.
- **G8 — OPEN_ACTIONABLE.** The concurrent exact-state Cu63 audit (`b6553966b90cbe6a35662ba975507217ca6f04c9`) establishes an independently evaluated crossed B(GT) package for `63Cu(g.s.) + anti-nu_e + e_K -> 63Ni*(87.220 keV)` and reconstructs `E_R=162.496486 keV`. The remaining gate is now quantitative source overlap: materialize/recompute the Standard-Model thermal-solar `anti-nu_e` differential spectrum at 162.5 keV and fold the full reverse-strength envelope. This gate is executable with existing target-side authority and therefore outranks BSM.
- **G9 — STRONG_NEGATIVE_SCOPED.** 0061 closes the frozen 10-kpc Galactic CCSN transparent-Sun utility benchmark after finite-source/alignment/duty accounting.
- **G4/G10 broad guards — STRONG_NEGATIVE_SCOPED** in their frozen assumptions: integrated resonance strength, fixed-column geometry, local density/spin sum-rule/extensivity, passive mediator/free-energy accounting.

## Frozen criterion application
Criterion 2 states that BSM may unlock only if no remaining SM branch is both quantitatively unbounded and immediately actionable with presently available primary inputs.

G8 fails that criterion because the Cu63 exact-state target package is now available and its source-overlap/rate gate has not yet been executed.

Therefore the only allowed classification is

**`FAIL_KEEP_BSM_LOCKED_OPEN_SM_ACTIONABLE`**.

No BSM constraint-ledger branch is opened in this iteration.

## Reproducibility
Machine-readable ledger: `data/bsm_unlock_readiness_0066.json` (commit `7af07949d90c8aefe9889665920a0520e106ccd1`). This is an evidence/architecture audit; a green CI status is not used as scientific evidence.

## Exact next gate
Prospectively freeze G8 Cu63 high-energy-tail contract. First determine whether the primary Standard-Model thermal-solar electron-antineutrino calculation is numerically valid/recoverable at `E_nu = 162.496486 keV`. No plotted-spectrum extrapolation is permitted. If recoverable, freeze the differential spectrum and fold it with the full `B_reverse=2.85e-3...6.72e-2` envelope and atomic factors to obtain events/kg/s and neutrino-supplied W/kg. If not recoverable, classify `BLOCKED_HIGH_ENERGY_TAIL`.

## Readiness
0066 is an audit failure that correctly re-ranks an actionable SM survivor; it does not close a physics gate. `NMIR_READINESS` remains **88%**.
