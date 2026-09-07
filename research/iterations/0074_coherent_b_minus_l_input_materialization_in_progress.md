# Iteration 0074 — COHERENT CsI+Ar B-L primary likelihood materialization (in progress)

Date: 2026-09-07
Status: **PARTIAL_PASS_COHERENT_INPUTS / benchmark open**
Frozen prereg: `research/prereg/0074_coherent_b_minus_l_likelihood_materialization.md`, commit `1e9ffedebf56a5c07e14676a3aed03bfebd4ae23`.

## Primary B-L likelihood authority materialized
Cadeddu et al., JHEP 01 (2021) 116 / arXiv:2008.05022 explicitly provides the B-L CEvNS convention and the CsI/Ar fit structure. The published B-L convention uses lepton charge `Q'_ell=1` and quark charge `Q'_f=-Q'_ell/3`; the CEvNS amplitude contains the SM weak charge minus the B-L propagator term proportional to `g_Z'^2 [Z F_Z+N F_N]/(q^2+M_Z'^2)`. This exact algebraic convention is frozen; no universal-vector contour is relabelled as B-L.

The primary paper specifies the source/exposure normalizations used in the event-rate calculation: Ar `r=(9±0.9)e-2`, `N_POT=13.7e22`, baseline `27.5 m`, target mass `24 kg`; CsI `r=0.08`, `N_POT=17.6e22`, baseline `19.3 m`, active mass `14.6 kg`.

Radiatively corrected weak couplings used by the analysis are `gV^p(nu_e)=0.0401`, `gV^p(nu_mu)=0.0318`, `gV^n=-0.5094`; Helm form factors are used. Published proton rms radii are Cs `4.804 fm`, I `4.749 fm`, Ar `3.448 fm`; adopted neutron radii are Cs `5.01 fm`, I `4.94 fm`, Ar `3.55 fm`.

## CsI fit structure
Cadeddu et al. use bins `i=4..15` (12 bins) because the fit is restricted to the Chicago-3 quenching-factor range. The least-squares nuisance widths are signal normalization `sigma_alpha=0.112`, background normalization `sigma_beta=0.25`, and quenching normalization `sigma_eta=0.051`.

The official COHERENT data page confirms the first-observation CsI public release and links its Zenodo/direct archive. Exact package bytes and hashes still need to be materialized before the gate can close.

## Ar fit structure and public numerical package
Cadeddu et al. use COHERENT liquid-Ar `Analysis A`, reconstructed range `0–120 keVee` in 12 bins of 10 keVee. Frozen nuisance widths from the primary analysis are CEvNS `13.4%`, prompt beam-related neutrons `32%`, late beam-related neutrons `100%`, plus uncorrelated beam-related-neutron energy-shape uncertainty `sqrt(0.058^2/12)=1.7%` per energy bin.

The official COHERENT public-data page links Zenodo DOI `10.5281/zenodo.3903810`, version 1.0, explicitly corresponding to Analysis A of the first liquid-Ar CEvNS measurement. The record exposes primary numerical files covering observed data, CEvNS/background PDFs, Analysis-A efficiency, parameters, and systematic-error inputs, including `datanobkgsub.txt`, `energydata1d.txt`, `f90data1d.txt`, `cevnspdf.txt`, `bkgpdf.txt`, BRN PDF files, `CENNS10AnlAEfficiency.txt`, `LArParametersAnlA.yaml`, and `systerrors1denergy.txt`.

This removes the question of whether the Ar side is publicly materializable. It does **not** yet establish a scientific likelihood reproduction: bytes/SHA256 pins and the preregistered SM/background benchmark are still open.

## Scientific guards
No B-L parameter scan has been performed. No contour points were read from a plot. No missing covariance/background term was replaced by an Asimov/diagonal approximation. No different-generation COHERENT release was mixed into the fit.

## Current classification
**PARTIAL_PASS_COHERENT_INPUTS**.

A final 0074 PASS requires: (1) hash-pinned exact Ar and CsI numerical packages matching the Cadeddu analysis; (2) a primary numerical SM/background benchmark target and prospectively frozen tolerance; (3) benchmark reproduction under that frozen criterion. Only after that may a separate B-L contour computation be preregistered.

Machine-readable progress ledger: `data/coherent_b_minus_l_input_audit_0074.json`, commit `a292c71510f2587f840f4e1ae4edc22154f06a4a`.

`NMIR_READINESS` remains 89%.
