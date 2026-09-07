# NMIR iteration 0063 — measured underground topology rejection × bulk-acceptance anchor audit

Date: 2026-09-07
Classification: **BLOCKED_PUBLIC_ACHIEVEMENT_ANCHOR**

## Funnel target
G2 / F7–F8. Determine whether a public primary underground detector result supplies a directly comparable measured low-energy background/topology rejection factor paired with a measured CEvNS-like bulk nuclear-recoil acceptance, strong enough to compare against the 0058 requirement envelope.

## Prospective contract
Frozen before the result-dependent literature classification:
- `research/prereg/0063_g2_measured_underground_topology_anchor.md`
- prereg commit `b52a9f810c677ea29a22f1001e05f044b6e4ecdf`.

The comparator was frozen unchanged from 0058:
- full signal acceptance: `R_req ≈ 1.44e7–1.78e7`;
- 50% fixed-exposure acceptance: `9.41e7–1.11e8`;
- 30% fixed-exposure acceptance: `4.58e8–5.25e8`.

No requirement was relaxed and no unmatched-detector multiplication was allowed.

## Frozen primary-evidence ledger
Machine-readable audit ledger:
- `data/g2_public_underground_anchor_authority_0063.json`
- ledger commit `519617dac8dc934e100d17983c8c15bc3e40a19f`.

Primary-source classes audited include:
1. CRESST-III released underground low-threshold data (`arXiv:1905.07335`): 30.1-eV nuclear-recoil threshold and selected/acceptance-region event data, but no measured detector-wide low-energy topology/background rejection factor paired with same-cut bulk-NR acceptance.
2. CRESST low-energy-excess study (`arXiv:2207.09375`): useful background-origin constraints, but no comparable rejection × NR-acceptance achievement pair.
3. CRESST 112-eV neutron-capture recoil calibration (`arXiv:2303.15315`): genuine low-energy nuclear-recoil calibration evidence, but not a detector-wide leakage/rejection measurement paired with the same NR acceptance.
4. SuperCDMS HVeV underground anticoincidence analysis (Phys. Rev. D 111, 012006): genuine underground low-energy topology/anticoincidence mechanism, but the analysis is electron-scattering/charge-quanta based and its sensitivity improvement is not a measured CEvNS-like bulk-NR rejection × acceptance factor.
5. Historical CDMS Soudan result (`arXiv:astro-ph/0507190`): real underground measured background discrimination with calibrated efficiencies, but only above 10 keV, far outside the 10–100 eV/sub-keV NMIR regime and therefore rejected by the preregistered comparable-window criterion.

## Scientific interpretation
The audit found **real pieces of the desired technology chain** — underground operation, low thresholds, low-energy NR calibration, topology/anticoincidence mechanisms, and high-energy measured discrimination — but did not find them combined in a public same-configuration sub-keV result satisfying all frozen inclusion criteria.

Therefore NMIR must not construct an achievement number by multiplying:
- rejection measured in one detector,
- NR acceptance from another,
- above-ground topology demonstrations,
- projected future suppression,
- raw trigger-rate reductions,
- or cross-section-sensitivity improvements.

No directly comparable `R_meas` can be honestly quoted against the `1.44e7–1.78e7` 0058 full-acceptance requirement from the audited public authority set.

## F10 classification
**`BLOCKED_PUBLIC_ACHIEVEMENT_ANCHOR`**.

This is not evidence that the required detector performance is impossible. It means the public primary evidence audited here does not yet provide the measured paired low-energy rejection × bulk-NR acceptance quantity needed to promote G2 beyond its current requirements-map status.

## Next funnel action
Per the prospective contract, after a genuine public-achievement block, move to the next independent OPEN survivor rather than inventing a technology factor.

The next candidate is G8 target-specific thermal-solar `anti-nu_e` RIOEC source/entrance-strength provenance: first ask whether a primary thermal-solar electron-antineutrino spectral density and an independently evaluated target entrance strength/width can be frozen. If either is unavailable, record the blocker rather than using ordinary solar `nu_e` flux or guessed resonance strength.

`NMIR_READINESS` receives no increase for 0063 because no new physical mechanism/performance gate was closed; the result is a reproducible evidence blocker that prevents overclaim.
