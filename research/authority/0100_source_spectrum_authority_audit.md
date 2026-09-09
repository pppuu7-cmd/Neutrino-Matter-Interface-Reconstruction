# 0100 source-spectrum authority audit

Date: 2026-09-09
Status: RESEARCH NOTE — DOES NOT AMEND FROZEN 0100/0100a CONTRACTS

## Question

Can benchmark 0100 obtain a machine-readable, immutable pre-supernova neutrino spectrum that is physically coherent with the already preregistered Farmer `25_79_0p005_ml` source-profile environment?

The answer at this audit stage is **not yet**. The candidates below must not be mixed post hoc merely to force a terminal PASS.

## Candidate A — Patton et al. beta-process spectra (Zenodo 2626645)

Authority:
- DOI: `10.5281/zenodo.2626645`
- record: `https://zenodo.org/records/2626645`
- publication: Patton, Lunardini, Farmer, Timmes, *Neutrinos from Beta Processes in a Presupernova: Probing the Isotopic Evolution of a Massive Star*.

Machine-readable spectra are public, but the released whole-star differential-luminosity products are for **15 and 30 solar-mass progenitors**, not the exact frozen 25-solar-mass Farmer model token `25_79_0p005_ml`.

Decision: **REJECT as the terminal spectrum paired to 0100a**. It may be used only in a separately preregistered cross-model robustness branch. Mixing it directly with the frozen 25-solar-mass profile would introduce an avoidable source-coherence mismatch.

## Candidate B — Dzhioev et al. TQRPA spectra on `25_79_0p005_ml`

Authority:
- DOI: `10.1093/mnras/stad3730`
- arXiv: `2312.07988`
- publication: Dzhioev, Yudin, Dunina-Barkovskaya, Vdovin, *Neutrinos from pre-supernova in the framework of TQRPA method*.

Strength: the paper explicitly uses the same Farmer `25_79_0p005_ml` pre-supernova model at onset of core collapse and computes neutrino/antineutrino luminosities and spectra.

Blocking issue: the paper's Data Availability statement says generated data are reported in the paper and additional data can be made available on reasonable request. No immutable public machine-readable spectrum asset with a frozen file hash has been identified in this audit.

Decision: **AUTHORITY-COMPATIBLE BUT CURRENTLY UNPINNABLE** under the NMIR reproducibility rule. Plot reconstruction is forbidden.

## Candidate C — Kato/Nagakura et al. 2026 comprehensive data release

Neutrino-data authority:
- v1.1 DOI stated by the release: `10.5281/zenodo.20618971`
- v1 release record: `https://zenodo.org/records/18886215`

Stellar-model authority:
- DOI: `10.5281/zenodo.20822085`
- includes a 25-solar-mass MESA model plus the associated pre-supernova calculation assets.

Strength: public machine-readable all-flavor luminosities/spectra exist, and a matching 25-solar-mass stellar-model archive is publicly released. This is therefore a strong candidate for a fully coherent source-profile + source-spectrum control.

Blocking issue for 0100a: it is **not the frozen Farmer/MESA-7624 `25_79_0p005_ml` model**. The 2026 stellar models use a newer MESA release and their own evolutionary assumptions.

Decision: **DO NOT substitute into 0100a**. If used, create a prospectively frozen separate coherent-control branch (provisional 0100c) before any terminal calculation and pin both the spectrum file and matching stellar-profile file by immutable hashes/member paths.

## Consequence for the funnel

1. Complete 0100a and freeze its exact selected-member and normalized-profile hashes in 0100b.
2. Do not call detector-level 0100 predictions terminal while the spectrum authority remains unpinned.
3. A source-propagation-only result may report its axis independently, but overall benchmark status must preserve any remaining spectrum/transport BLOCK rather than silently reinterpret the original preregistration.
4. The strongest current path to a fully coherent public terminal control is a **new prospectively preregistered Kato/Nagakura 25-solar-mass branch**, not a post-hoc hybrid of Farmer structure and another progenitor's spectrum.

No numerical model outcome was inspected or used to select among these authorities. This note is an authority/provenance audit only.
