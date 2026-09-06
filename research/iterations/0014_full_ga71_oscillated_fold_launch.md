# Iteration 0014 — full oscillated Ga-71 solar folding

Date: 2026-09-06

## Goal
Compute the first component-resolved oscillated B16 solar-neutrino capture rate on 71Ga using only already-frozen inputs: B16 GS98/AGSS09met source fluxes, exact pinned spectra, exact B16 production/electron-density tables, frozen day-side adiabatic three-flavour MSW convention, and the validated Bahcall-1997 Ga-71 energy response.

## New implementation
- `src/nmir/ga71_solar_fold.py`: component folding engine.
- `scripts/ga71_oscillated_solar_benchmark.py`: hosted benchmark/report.
- `.github/workflows/ga71-solar-fold.yml`: artifact-producing hosted run.

Continuum components use

`R_i = Phi_i * int[f_i(E) Pee_i(E) sigma_Ga(E) dE] / int[f_i(E)dE`.

pep is treated as the frozen 1.442-MeV line. Be7 uses the two exact pinned thermally broadened line profiles with frozen 0.897/0.103 branching weights. No result-dependent tuning or external rate normalization is used.

## Live authority
Workflow run `34020172203`, job `101451164446`, head `9236a23c4e7a619408804f6380a7466c91ab2053` was launched and is in progress. No duplicate run was started.

## Code-audit observation while run is active
The current scientifically correct implementation is computationally conservative rather than optimized: `production_averaged_day_pee` recomputes native-grid production weights and default oscillation parameters repeatedly for each energy. If the hosted job becomes a performance failure/timeout, the prospective repair is to cache immutable production weights and numerical oscillation parameters without changing any physics arithmetic, spectra, response, or acceptance gates. Do not apply a result-dependent physics modification.

## External cross-check frozen before output inspection
A 2026 PTEP radiochemical analysis (Ishidoshiro & Tachibana, published 18 March 2026) explicitly uses B16-GS98 and B16-AGSS09met solar-model realizations for Ga/Cl predictions. It is retained only as an independent post-result comparison source; it must not be used to retune NMIR inputs.

## Classification
- Scientific result: PENDING active hosted fold.
- Infrastructure/performance: no terminal failure yet; possible repeated-weight performance bottleneck identified prospectively.
- Readiness credit: none until the hosted result is terminal and validated.

NMIR_READINESS: 29%

## Exact next action
Consume run `34020172203`. If SUCCESS, inspect raw component/total SNU artifact and compare prospectively to independent radiochemical expectations. If performance/timeout FAIL, cache immutable weights/oscillation constants, add equivalence regression tests, rerun once, and preserve all physical conventions unchanged. Then freeze/reproduce Cl-37 response.
