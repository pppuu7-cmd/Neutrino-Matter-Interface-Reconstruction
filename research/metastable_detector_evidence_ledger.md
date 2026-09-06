# Metastable detector evidence ledger

Last updated: 2026-09-06
Purpose: primary-source inputs for the future real detector-transfer-function gate after the ideal CEvNS target/threshold phase diagram is validated.

This file is evidence preparation only. It is **not** a detector-performance PASS and contributes no NMIR readiness credit by itself.

## Scope guard

The ideal CEvNS calculation predicts nuclear-recoil interaction distributions. A metastable detector adds a response/acceptance function. The future accepted rate must be written explicitly as

`R_acc/kg = sum_s integral dE_nu Phi_s(E_nu) integral dT (d sigma_s/dT) epsilon_nuc(T, state) * live_fraction`,

with threshold/state uncertainty, backgrounds, dead time and reset/preparation energy reported separately.

A bubble/avalanche can amplify *signal* by releasing stored target free energy. That released energy must never be counted as neutrino-supplied energy.

## E1 — SBC-LAr10 calibration target and operating ledger

Primary publication:

- SBC Collaboration, E. Alfonso-Pita et al., **“Calibration plan for the SBC 10-kg liquid argon detector with 100 eV target threshold”**, Journal of Instrumentation **21** (2026) P03020.
- DOI: `10.1088/1748-0221/21/03/P03020`.
- arXiv: `2511.19817`.
- Received 2025-11-25; published 2026-03-11.

Frozen interpretation and numerical inputs for the future detector gate:

- The device is a 10-kg liquid-argon scintillating bubble chamber program with a **100 eV target nuclear-recoil threshold**.
- The published nuclear-recoil calibration plan explicitly covers thermodynamic thresholds of about **80–400 eV**.
- The same source states that a conservative spontaneous-nucleation thermodynamic threshold can reach roughly **40 eV**, but the threshold required for **electronic-recoil blindness is not yet known** and must be determined experimentally. Therefore 40 eV is not an accepted-detector threshold authority.
- The calibration plan emphasizes that the Seitz thermodynamic threshold does not by itself determine the full nuclear-recoil nucleation efficiency. The transfer function must be calibrated from source data.
- Reset/recompression after a bubble takes roughly **30 s**, limiting the chamber to order one bubble event per minute / order `10^3` per day in the calibration configuration. This is a live-time/dead-time constraint, not a neutrino-rate enhancement.
- At the Fermilab MINOS calibration location, simulations quoted in the calibration plan expect a fast-neutron background of order **2 bubble nucleations per hour**. That site background is configuration-specific and must not be imported into a future underground/solar detector without a geometry/site model.
- Calibration techniques include photoneutron scattering, nuclear Thomson scattering and thermal-neutron capture to constrain sub-keV recoil response.

`100 eV` is therefore a target/calibration scale, not evidence for a measured step-function acceptance down to 100 eV and certainly not evidence for 1–20 eV operation.

Primary links/provenance:

- arXiv abstract: `https://arxiv.org/abs/2511.19817`
- Fermilab preprint: `https://lss.fnal.gov/archive/2025/pub/fermilab-pub-25-0863-etd.pdf`
- journal DOI above.

## E2 — measured scintillating xenon bubble-chamber response

Primary publication:

- SBC Collaboration, E. Alfonso-Pita et al., **“Low-threshold response of a scintillating xenon bubble chamber to nuclear and electronic recoils”**, Physical Review D **111** (2025) 032002.
- DOI: `10.1103/PhysRevD.111.032002`.
- arXiv: `2410.07241`.
- Published 2025-02-07.

Frozen measured facts relevant to NMIR:

- XeBC operated at thermodynamic (Seitz) thresholds down to **0.50 keV**, hardware limited.
- It demonstrated sensitivity to approximately **1 keV nuclear recoils** while remaining highly insensitive to gamma-induced bubble nucleation.
- The paper gives a data-driven calibration of the chamber's nuclear-recoil nucleation response as a function of recoil energy and thermodynamic state.
- At the 0.50-keV thermodynamic threshold, the reported upper limit on gamma-induced Auger-cascade bubble nucleation probability is `<1.1e-6`.
- The authors explicitly note that the Seitz threshold is only an order-one indication of the actual nuclear-recoil detection threshold; observed/simulated NR thresholds can exceed it, so target-specific nucleation-efficiency calibration is mandatory.
- Their event cycle includes recompression/reset; the historical XeBC setup used a 60-s compression period between events. This is a detector live-time/dead-time consideration, not neutrino physics.

Primary links/provenance:

- APS: `https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.032002`
- arXiv: `https://arxiv.org/abs/2410.07241`

## E3 — latest public SBC-LAr10 status found before the detector gate

Primary/public experiment status sources:

- Fermilab DPF 2026 contribution, Gray Putnam, **“Status and Prospects of the Scintillating Bubble Chamber Liquid Argon 10 kg (SBC-LAr10) Detector”**, 2026-07-20.
- Fermilab 2025 collaboration poster `FERMILAB-POSTER-25-0079-PPD`.

Frozen status interpretation:

- By the July 2026 DPF status report, SBC-LAr10 at the Fermilab MINOS underground facility **had taken data** to demonstrate operation and characterize detector performance; the contribution advertised first operational results including coincident observation channels for bubble-nucleating events.
- The public status text does **not**, by itself, provide a validated nuclear-recoil efficiency curve down to 100 eV. Therefore NMIR must not assume a realized 100-eV step efficiency until a primary calibration curve/result is available.
- The 2025 Fermilab status timeline described calibration work from Fall 2025 through Summer 2026 and the 100-eV target threshold. Use later primary calibration publications/results when available rather than treating schedule language as performance evidence.

Primary links/provenance:

- DPF 2026 contribution list/timetable: `https://indico.fnal.gov/event/72820/`
- Fermilab poster: `https://lss.fnal.gov/archive/2025/poster/fermilab-poster-25-0079-ppd.pdf`

## E4 — measured 10-eV nuclear-recoil calorimeter positive control

Primary publication:

- CRESST Collaboration, G. Angloher et al., **“Results on sub-GeV dark matter from a 10 eV threshold CRESST-III silicon detector”**, Physical Review D **107** (2023) 122003.
- DOI: `10.1103/PhysRevD.107.122003`.
- arXiv: `2212.12513`.

Frozen measured facts relevant to NMIR:

- target: `0.35 g` silicon cryogenic calorimeter;
- reported baseline nuclear-recoil energy resolution: **`1.36 ± 0.05 eV_nr`**;
- reported energy threshold: **`10.0 ± 0.2 eV_nr`**;
- this is a measured macroscopic detector threshold in the central energy region highlighted by iterations 0043–0045;
- the experiment also observes a low-energy excess near threshold, illustrating that a low threshold alone does not guarantee a background-free CEvNS measurement.

Primary links/provenance:

- APS: `https://journals.aps.org/prd/abstract/10.1103/PhysRevD.107.122003`
- arXiv: `https://arxiv.org/abs/2212.12513`

NMIR interpretation:

The existence of a 10-eV measured calorimetric threshold means the `1–20 eV` CEvNS inverse-design region must **not** be labelled fundamentally detector-inaccessible. However, this positive control has only `0.35 g` active mass and is not a metastable bubble detector. The relevant residuals are therefore mass scaling, low-energy backgrounds, target choice and transfer-function stability — not merely threshold existence.

## E5 — high-mass/high-threshold solar-CEvNS positive control: XENONnT

Primary publication:

- XENON Collaboration, E. Aprile et al., **“First Indication of Solar 8B Neutrinos via Coherent Elastic Neutrino-Nucleus Scattering with XENONnT”**, Physical Review Letters **133** (2024) 191002.
- DOI: `10.1103/PhysRevLett.133.191002`.

Frozen measured facts relevant to NMIR:

- sensitive liquid-xenon target mass: **5.9 t**;
- blind-analysis exposure: **3.51 t yr**;
- analysis threshold: **0.5 keV nuclear recoil**;
- observed events above threshold: **37**;
- expected background: **`26.4_{-1.3}^{+1.4}`** events;
- background-only rejection: **2.73 sigma**;
- the measured flux-weighted CEvNS cross section on Xe is consistent with the Standard Model.

Primary links/provenance:

- APS: `https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.133.191002`
- PubMed: `https://pubmed.ncbi.nlm.nih.gov/39576901/`

NMIR interpretation:

XENONnT is an experimental positive control at the opposite corner from the CRESST 10-eV calorimeter: it demonstrates real **solar nuclear-recoil CEvNS** in a multi-ton detector, but with a 0.5-keV threshold that selects the high-energy B8 regime. It validates the basic high-mass/high-threshold end of the NMIR source-regime picture while providing no direct access to the low-energy pp/Be7/CNO recoil phases emphasized by the ideal 1–20-eV optimization.

The three detector anchors therefore span a useful mass-threshold trade space:

1. **XENONnT:** multi-tonne and directly observed solar CEvNS, but 0.5-keV threshold / B8-dominated;
2. **SBC noble-liquid metastability:** kg-scale program with strong rejection/readout amplification ambitions and O(100 eV) target/calibration thresholds, but sub-100-eV calibrated efficiency still open;
3. **CRESST silicon calorimetry:** measured 10-eV threshold, but sub-gram unit mass and low-energy-background/excess challenges.

## Immediate NMIR implication

Iteration 0045 found ideal full-solar CEvNS target transitions mainly in the `1–20 eV` region, with 40 eV retained as an endpoint/control scale. The current detector evidence no longer supports a simple statement that this region is technologically unreachable. Instead it shows a **mass-threshold-background trade space**.

Thus the future transfer-function gate must compare at least:

`epsilon_nuc(T)` + target mass scaling + background/false-trigger rate + threshold stability + live fraction/dead time.

For the metastable branch it must additionally preserve the stored-free-energy/reset ledger.

The next practical question is:

**Which detector-response architecture can preserve enough of the ideal NMIR solar-CEvNS rate at realistic mass and background, and what quantitative technology improvement is required where it cannot?**

This is a technology-gap / detector-acceptance problem, not a fundamental interaction no-go. No detector implementation is allowed to claim neutrino-energy gain from its internal amplification.
