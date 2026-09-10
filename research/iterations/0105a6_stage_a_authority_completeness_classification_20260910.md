# 0105a6 Stage-A — COHERENT SM/null authority completeness classification

Date: 2026-09-10
Gate: `NMIR-V2-0105A6`
Stage-A execution classification: `PASS_0105A6_STAGE_A_AUTHORITY_INVENTORY_NONDISCOVERY`
Post-inventory completeness classification: `BLOCKED_0105A6_LIKELIHOOD_AUTHORITY_INCOMPLETE_RELEASE_SIDE`

## Scope

This record classifies the raw Stage-A inventory against the eight fields frozen prospectively in `research/prereg/0105a6_coherent_sm_null_semantics_authority_inventory.md`.

It does **not** reclassify the successful Stage-A execution as failed. Stage A passed: all seven frozen authority files were retrieved from the exact byte-locked releases, their SHA256 values matched, text extraction succeeded, and a reproducible evidence inventory was emitted. The separate question addressed here is whether those release-side files alone form a complete literal contract for a later standalone reproduction of the collaboration SM/null likelihood.

Hosted evidence:

- execution head: `3ab8325209725fa71afc9e142b12fd12e9f94905`;
- run/job: `34467435940/102839197445`;
- dedicated guards: `3 passed`;
- Stage-A result JSON SHA256: `7500530eec94880863c7d1e64258fa197cd437ad9a9261e0a55adfd6685cb2fd`;
- artifact: `10148102603`, `nmir-v2-0105a6-coherent-sm-null-semantics-stage-a`;
- artifact ZIP SHA256: `5b81dcc83d79334a7fb0c6ea490ef8427956f7cca44802538513efdd665f232c`;
- Stage-A status: `PASS_0105A6_STAGE_A_AUTHORITY_INVENTORY_NONDISCOVERY`;
- `sm_null_reproduction_allowed = false`;
- `observed_bsm_residual_permission_percent = 0`.

## Eight-field classification

### CsI[Na], Zenodo record 1228631

1. **Observable definition and binning — AVAILABLE / substantial release-side authority.** The collaboration companion describes the two-dimensional arrival-time/photoelectron representation and the released data structure; it gives the finest bin widths as 0.5 microsecond in arrival time and 2 PE. The README identifies signal/background regions and component files.
2. **SM CEvNS signal construction — PARTIAL.** The release supplies flux/exposure/detector parameters and the response ingredients needed to construct a CEvNS prediction, but the exact collaboration signal-generation implementation is not supplied as an executable frozen object in the release.
3. **Detector response — AVAILABLE / substantial.** The YAML and companion specify the analysis quenching-factor convention, light yield and explicit acceptance-efficiency function/parameters and instructions for applying it.
4. **Background components — AVAILABLE / substantial.** Steady-state and prompt-neutron authority is present, including released data/PDF material and prompt-neutron normalization semantics.
5. **Nuisance parameters and couplings — PARTIAL.** Numerical uncertainties are present for several ingredients, but the release-side material does not by itself provide a complete literal machine contract for every constraint/coupling/correlation used by the published profile-likelihood result.
6. **Normalization/exposure/flux — AVAILABLE / substantial.** Beam exposure, source-detector information, neutrino-production quantity and component normalization semantics are supplied.
7. **Exact likelihood/statistic — INCOMPLETE RELEASE-SIDE.** The companion permits comparison by a likelihood or chi-square but does not freeze a unique literal objective function and complete nuisance implementation. Inferring a Poisson/Gaussian form from common practice is prohibited by the preregistration.
8. **Published numerical benchmark — REFERENCED COLLABORATION AUTHORITY, NOT YET BYTE-PINNED IN THIS GATE.** The original collaboration publication is explicitly referenced and contains the published SM prediction/profile-likelihood behavior, but it was outside the frozen Stage-A byte set and therefore may not be promoted retroactively to Stage-A authority.

### CENNS-10 liquid argon, Zenodo record 3903810, Analysis A

1. **Observable definition and binning — AVAILABLE.** The release provides common 3D energy/F90/time-to-trigger arrays and literal binning information.
2. **SM CEvNS signal construction/template semantics — AVAILABLE / substantial.** `cevnspdf.txt` is identified as the Analysis-A CEvNS signal PDF and is normalized to the initial central-value SM prediction.
3. **Detector response — AVAILABLE / substantial.** Release-side authority contains quenching-factor, efficiency, energy-resolution and timing-response ingredients and instructions.
4. **Background components — AVAILABLE.** Prompt BRN, delayed BRN and steady-state background components and their released PDFs/normalizations are identified.
5. **Nuisance parameters and couplings — PARTIAL.** Central values and multiple Gaussian-constraint widths/systematic ingredients are provided, but the release does not freeze a complete literal executable treatment of all fit-shape systematics and their coupling to the likelihood.
6. **Normalization/exposure/flux — AVAILABLE.** Beam exposure, detector mass, neutrinos per proton, CV and best-fit component normalizations and uncertainties are present.
7. **Exact likelihood/statistic — INCOMPLETE RELEASE-SIDE.** The companion says to use the binned data with an appropriate likelihood procedure; it does not itself give a unique complete formula/implementation. The collaboration paper is known to describe an extended maximum-likelihood fit and a profiled `-2 Delta ln L`, but it was not part of Stage A and cannot be used retroactively to satisfy this field.
8. **Published numerical benchmark — AVAILABLE / substantial release-side benchmark, with publication-level benchmark still to be pinned.** The release gives CV and best-fit normalizations sufficient for deterministic projection/integral checks; the collaboration publication gives the null-significance/profile benchmark but remains outside Stage-A byte authority.

## Blocking reason

The common blocking field is **field 7**, with field 5 also incomplete at the level required for a defensible reproduction of the published constrained likelihood.

Therefore the release-side byte lock is scientifically useful but does not yet authorize a numerical standalone SM/null reproduction. A hand-built likelihood, generic Wilks threshold, post-hoc nuisance convention, or phenomenology implementation would violate the frozen gate.

This is an **authority BLOCKED**, not evidence against the Standard Model, CEvNS, COHERENT, or any BSM model.

## External collaboration evidence identified for the next prospective gate

The release documents explicitly point to the collaboration publications corresponding to the analyses. Public primary-source inspection identifies the following candidate authority targets for a new, prospectively frozen acquisition gate:

- CsI[Na]: COHERENT Collaboration, `Observation of Coherent Elastic Neutrino-Nucleus Scattering`, arXiv `1708.01294`, DOI `10.1126/science.aao0990`. Its collaboration supplementary material describes a 2D binned maximum-likelihood estimator, the CEvNS/prompt-neutron/steady-state components and constraints, and the published profile-likelihood benchmark.
- CENNS-10 Ar: COHERENT Collaboration, `First Measurement of Coherent Elastic Neutrino-Nucleus Scattering on Argon`, arXiv `2003.10630` final arXiv version v7, DOI `10.1103/PhysRevLett.126.012002`. Its appendix describes the extended maximum-likelihood analysis and the profiled `-2 Delta ln L` null statistic.

These publications are **candidate external collaboration authority only** at this point. Their bytes/source package and exact admissible evidence fields must be frozen prospectively before they can close 0105a6.

## Current permission

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

No residual, BSM parameter, model family, significance combination or discovery statistic may be inspected or fitted.

## Exact next step

Create a prospective 0105a6 Stage-B authority-acquisition gate restricted to explicitly referenced COHERENT collaboration primary sources. It must byte-pin exact publication/supplement/source artifacts first, then ask only whether they close the missing likelihood/nuisance contract. If a complete literal contract still cannot be recovered, 0105a6 remains BLOCKED rather than filling gaps from common statistical practice.
