# Iteration 0015 — Cl-37 response freeze and solar-fold launch

Date: 2026-09-06

## Goal
Advance G3 from the validated full Ga-71 solar folding to the second classic radiochemical target, `37Cl(nu_e,e-)37Ar`, using an authoritative energy-dependent response rather than a fitted effective cross section.

## Primary numerical response
John Bahcall's IAS neutrino-data page explicitly provides chlorine absorption cross sections as a function of neutrino energy in MeV, in units of `1e-46 cm^2`. The improved second column is identified as Bahcall et al., Phys. Rev. C 54, 411 (1996); the third column is the older Bahcall-Ulrich/book response. The downloadable table has 19 energies from 1 to 30 MeV.

Repository freeze:
- `data/cl37_bahcall1996_response.csv`: exact 19-point improved + older columns transcribed from the primary numerical table.
- `src/nmir/cl37_response.py`: threshold `0.814 MeV`, piecewise-linear interpolation, threshold-to-1-MeV zero anchor, fail-closed above 30 MeV, branch-explicit improved/old response.
- `tests/test_cl37_response.py`: exact point/threshold/fail-closed regression tests.

Important scope guard: the published numerical table starts at 1 MeV. The interval from the physical threshold 0.814 MeV to 1 MeV is therefore represented by a transparent zero-threshold linear anchor and must be treated as an interpolation convention, not direct tabulated authority. This matters especially for the 0.862-MeV Be7 contribution and must remain visible in the uncertainty/sensitivity analysis.

## Full solar fold launched
Added:
- `src/nmir/cl37_solar_fold.py`
- `scripts/cl37_oscillated_solar_benchmark.py`
- `.github/workflows/cl37-solar-fold.yml`

The fold uses the same already-frozen B16 GS98/AGSS09met fluxes, pinned spectra, exact production/electron-density distributions and day-side adiabatic MSW convention used by the validated Ga calculation. No radiochemical total-rate normalization is inserted.

Workflow run `34020427430`, job `101451868492`, head `ab8c31251a746a0b02185ea5c7fcbc8dd11d7b55` is currently queued. No duplicate run was launched.

## Classification
- Cl energy-response provenance/table identity: FROZEN, pending CI confirmation.
- Sub-1-MeV Cl interpolation: explicit model convention / uncertainty item, not primary-data closure.
- Full oscillated Cl solar result: PENDING active hosted run.
- Readiness credit: none yet for the queued scientific fold.

NMIR_READINESS: 31%

## Exact next action
Consume run `34020427430` and relevant baseline CI. Inspect raw component/total SNU. If successful, compare B8/source-average scale against Bahcall-1996 chlorine references without retuning and quantify sensitivity of the Be7 contribution to the 0.814–1.0 MeV interpolation convention. Only then promote Cl closure/readiness. Next, convert validated Ga+Cl capture to deposited-power W/kg and continue G3.
