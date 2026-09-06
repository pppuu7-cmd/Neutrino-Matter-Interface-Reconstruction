# Metastable detector evidence ledger

Last updated: 2026-09-06
Purpose: primary-source inputs for the future real detector-transfer-function gate after the ideal CEvNS target/threshold phase diagram is validated.

This file is evidence preparation only. It is **not** a detector-performance PASS and contributes no NMIR readiness credit by itself.

## Scope guard

The ideal CEvNS calculation predicts nuclear-recoil interaction distributions. A metastable detector adds a response/acceptance function. The future accepted rate must be written explicitly as

`R_acc/kg = sum_s integral dE_nu Phi_s(E_nu) integral dT (d sigma_s/dT) epsilon_nuc(T, state) * live_fraction`,

with threshold/state uncertainty, backgrounds, dead time and reset/preparation energy reported separately.

A bubble/avalanche can amplify *signal* by releasing stored target free energy. That released energy must never be counted as neutrino-supplied energy.

## E1 — SBC-LAr10 calibration target

Primary publication:

- SBC Collaboration, E. Alfonso-Pita et al., **“Calibration plan for the SBC 10-kg liquid argon detector with 100 eV target threshold”**, Journal of Instrumentation **21** (2026) P03020.
- DOI: `10.1088/1748-0221/21/03/P03020`.
- arXiv: `2511.19817`.
- Received 2025-11-25; published 2026-03-11.

Frozen interpretation:

- The device is a 10-kg liquid-argon scintillating bubble chamber program with a **100 eV target nuclear-recoil threshold**.
- The paper is a calibration plan for sub-keV response using photoneutron scattering, nuclear Thomson scattering and thermal-neutron capture.
- `100 eV` is a target/calibration threshold, not evidence that a fully measured step-function nucleation efficiency exists down to 100 eV, and certainly not evidence for 1–20 eV performance.

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
- The paper gives a data-driven calibration of nuclear-recoil nucleation response as a function of recoil energy and thermodynamic state.
- At the 0.50-keV thermodynamic threshold, the reported upper limit on gamma-induced Auger-cascade bubble nucleation probability is `<1.1e-6`.
- The authors explicitly note that the Seitz threshold is only an order-one indication of the actual nuclear-recoil detection threshold; observed/simulated NR thresholds can exceed it, so target-specific nucleation-efficiency calibration is mandatory.
- Their event cycle includes recompression/reset; the historical XeBC setup used a 60-s compression period between events. This is a detector live-time/dead-time consideration, not neutrino physics.

Primary links/provenance:

- APS: `https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.032002`
- arXiv: `https://arxiv.org/abs/2410.07241`

## Immediate NMIR implication

Iteration 0045 found ideal full-solar CEvNS target transitions in the `1–20 eV` region, with 40 eV retained as an endpoint/control scale. Existing/near-term scintillating bubble-chamber evidence is instead centered on approximately `100 eV` target LAr operation and `0.5–1 keV` measured Xe response.

Therefore the next practical question is not “can metastability amplify a recoil?” — iteration 0040 already answers that signal amplification can occur using stored free energy. The next question is:

**What nucleation-efficiency turn-on and stability would be required for the NMIR ideal 1–20 eV CEvNS phase diagram to survive after a real detector transfer function is applied, and how far is that required response from current primary-source bubble-chamber evidence?**

This is provisionally a technology-gap / detector-acceptance gate. Do not interpret the gap as a fundamental no-go: it may be engineering-limited, material-limited, or signal-formation-limited and must be quantified before classification.
