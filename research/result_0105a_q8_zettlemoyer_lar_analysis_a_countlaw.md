# 0105a-q8 result — Zettlemoyer CENNS-10 LAr Analysis-A elementary count-law authority

Date adjudicated: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Frozen preregistration commit: `0c771e13accfa52de93c760af8ed7174d39795e4`
Mode: NONDISCOVERY external-authority audit

## Authoritative classification

`PASS_0105A_Q8_F1_ZETTLEMOYER_LAR_ELEMENTARY_COUNTLAW_LOCATED_NONDISCOVERY`

q8 satisfies the prospectively frozen four-element F1 semantic contract. This closes the F1 authority field only. It does not inspect or authorize an observed BSM residual, systematic Monte Carlo, a Tier-A exact collaboration likelihood claim, or a new BSM model.

## Source identity / provenance

Target source frozen before body inspection:

- Jacob C. Zettlemoyer, *First Detection of Coherent Elastic Neutrino-Nucleus Scattering on an Argon Target*, PhD dissertation, Indiana University, Department of Physics, May 2020.
- DOI `10.5967/3wza-6w73`; Indiana University persistent item `https://hdl.handle.net/2022/25448`.
- The official COHERENT/ORNL thesis index independently lists this dissertation as the 2020 Indiana University PhD thesis for the first argon detection.

The dissertation body was inspected only after preregistration. Indiana ScholarWorks' PDF endpoint is a ~33 MB PDF whose body is indexed and returns page-specific scientific text. The web screenshot backend did not recognize the endpoint as `application/pdf`, so screenshot requests failed at the transport/content-type layer; no OCR or visual inference was used. The classification below relies on indexed verbatim mathematical/text extraction from the exact frozen bitstream plus comparison against the official collaboration release.

## Frozen element 1 — elementary/generative likelihood: PASS

Chapter 7 explicitly states that the final first-detection result uses a 3D binned maximum-likelihood analysis of the full-shielded on-beam data in energy, F90 and time. Section 7.4 gives the extended likelihood in Eq. (7.1):

`ln L(theta) = -nu(theta) + sum_i ln(nu(theta) f(x_i; theta))`.

This is the standard extended-likelihood count-generative form: the `-nu` term plus event-density product/log-sum is mathematically equivalent to a Poisson total-count factor times the event-shape likelihood. This meets the preregistered allowance for an explicit Poisson **or mathematically equivalent elementary count/generative likelihood**; exact `n_on/n_off/alpha` notation was prospectively not required.

Scope is unambiguous: Chapter 7 is titled the first detection with CENNS-10 and states that this likelihood fit provides the final result/first detection. The full-shielded dataset is 6.12 GWhr (13.8e22 POT), July 2017–December 2018.

## Frozen element 2 — off-beam sample is count-bearing auxiliary information: PASS

The dissertation explicitly defines the on/off counting construction rather than treating off-beam data as a merely qualitative shape template:

- `Nbeam` is the on-beam sample containing signal plus steady-state beam-unrelated background.
- `Nss` is the measured steady-state background sample **derived from off-beam triggered data with sample size `Noff`**.
- Eq. (6.1): `Nsig = Nbeam - Nss`.
- Eq. (6.2): `Nss = f Noff`.
- Eq. (6.3) propagates count statistics as `sigma_sig^2 = Nbeam + f^2 Noff`, subsequently rewritten using the scaled SS expectation.

For the final likelihood, the measured off-beam data form the steady-state energy:F90 PDF, and Table 7.8 gives the steady-state normalization as `Nss = 3154 +/- 25` in the dissertation, with the table text explicitly stating that quoted errors are widths of Gaussian normalization constraints in the fit.

Thus the auxiliary off-beam sample carries both measured shape and measured count/normalization information into the fit. This is stronger than the frozen minimum requirement of an auxiliary measurement or count-bearing constraint.

## Frozen element 3 — normalization / oversampling mapping: PASS

The dissertation supplies the exact scaling semantics:

- `Nss = f Noff` where `f` is the ratio implied by the analysis and off-beam time windows.
- In the cut-formation discussion, the off-beam SS estimate uses a 25 us window compared with a 3.5 us signal-region window and explicitly gives `f = 7/50`.
- In the final 3D likelihood, Section 7.4 defines the fit time range as `-0.1 < t_trig < 4.9 us`, i.e. 5 us total.
- The steady-state PDF section states that the larger 25 us DAQ window is used and scaled to the likelihood-fit time-window length for higher statistics.

Therefore the final likelihood uses the same explicit window-scaling rule with a 25 us auxiliary window mapped to a 5 us fit window, i.e. fivefold off-beam oversampling (`f = 1/5` for the time-window mapping).

The official COHERENT LAr release independently corroborates this exact semantics: it states that the steady-state background is measured off-beam data and was originally oversampled from a **5x larger** `t_trig` window than the data; that factor is accounted for in the provided PDF and normalization, and the subtraction statistical error must account for the oversampling.

## Frozen element 4 — same CENNS-10 first-detection / Analysis-A construction: PASS

The source is not a generic LAr or earlier engineering-run analysis. Chapter 7 explicitly applies the binned likelihood to the full-shielded production dataset and says the likelihood fit yields the final first-detection result. The official collaboration LAr release states that the released 3D data/PDFs correspond to Analysis A of the first-detection paper. The source title, dataset exposure, fit dimensions, expected component rates and fit architecture all identify the same first-detection production analysis.

## q7 numerical-precedence compatibility

The dissertation's Table 7.8 contains the pre-correction `Nss = 3154 +/- 25`. q7 already prospectively adjudicated the version history independently:

- arXiv:2003.10630v3 contains `3154 +/- 25`;
- v4 is explicitly labeled by the collaboration as `fix typo in table 1` and changes the value to `3152 +/- 25`;
- `3152 +/- 25` persists in the final paper and official data release.

Therefore q8 does **not** promote the obsolete numerical value. For all reproduction work, q7 precedence controls the normalization central value: `3152 +/- 25`. q8 promotes only the elementary count-law / auxiliary-scaling semantics. The typo is a previously resolved numerical-precedence issue, not a contradiction in the q8 statistical construction.

## Why this is a PASS rather than partial/BLOCKED

The preregistration required all four of: count-generative likelihood; count-bearing off-beam role; explicit scaling/oversampling mapping; and same-analysis scope. The dissertation provides each separately and consistently. In particular, the evidence goes beyond the BLOCKED examples frozen in advance (a Gaussian `Nss` constraint alone, qualitative off-beam language, a template alone, or oversampling prose alone): it supplies the extended likelihood equation, the `Nbeam/Noff/Nss` count algebra, propagated counting variance, explicit scale-factor definition and same-analysis linkage.

## Authorization consequence

F1 is now resolved under q8, while F7 remains resolved under q7. The next COHERENT action may be a **new prospectively frozen null-reproduction gate** consuming q7+q8 semantics and the official LAr release. This result alone does not authorize:

- observed BSM-residual inspection;
- systematic-Monte-Carlo execution;
- Tier-A exact-collaboration-likelihood language beyond the fields actually closed;
- construction/promotion of a new BSM model.

DeepCore standard-3nu reproduction remains independently blocked at its recorded authority boundary.

## External evidence anchors

Exact frozen thesis bitstream:
`https://scholarworks.iu.edu/dspace/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/download`

Official thesis provenance:
`https://coherent.ornl.gov/theses/`

Official LAr release authority:
COHERENT, arXiv:2006.12659v2 / Zenodo DOI `10.5281/zenodo.3903810`.
