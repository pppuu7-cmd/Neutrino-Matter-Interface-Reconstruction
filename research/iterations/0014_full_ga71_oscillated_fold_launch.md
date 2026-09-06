# Iteration 0014 — full oscillated Ga-71 solar folding

Date: 2026-09-06

## Goal
Compute component-resolved oscillated B16 solar-neutrino capture rates on 71Ga using only previously frozen inputs: B16 GS98/AGSS09met fluxes, exact pinned spectra, exact B16 production/electron-density tables, frozen day-side adiabatic three-flavour MSW, and validated Bahcall-1997 Ga-71 response.

## Implementation
- `src/nmir/ga71_solar_fold.py`
- `scripts/ga71_oscillated_solar_benchmark.py`
- `.github/workflows/ga71-solar-fold.yml`
- `tests/test_ga71_solar_fold.py`

Continuum components use `R_i = Phi_i * int[f_i Pee_i sigma dE]/int[f_i dE]`. pep is the frozen 1.442-MeV line. Be7 uses the exact pinned thermally broadened profiles with frozen 0.897/0.103 branch weights.

## First run and repair
Run `34020172203`, job `101451164446`, head `9236a23c4e7a619408804f6380a7466c91ab2053` FAILED before producing a scientific result. First causal error: a valid continuum spectrum contains an `E=0` endpoint, while `Pee(E=0)` is undefined. Since `sigma_Ga(E=0)=0`, that endpoint has exactly zero capture contribution and must not evaluate Pee. Classification: infrastructure/numerical-boundary FAIL, not scientific FAIL.

Repair commit `a5b6d2a109fe39695f421ecc455026c9c0f92c94` skips Pee evaluation whenever the capture cross section or spectral weight is exactly zero and caches immutable production weights/oscillation constants. No flux, spectrum, MSW formula/parameters, Ga response, branching weight, or scientific criterion changed. Regression tests were added in commit `382024af46534e4332d79d33896064480f7339a3`.

Baseline CI `34020276133`, job `101451443326`: SUCCESS, **74 passed**.

## Authoritative scientific result
Hosted run `34020272911`, job `101451434118`, head `a5b6d2a109fe39695f421ecc455026c9c0f92c94`: SUCCESS.
Artifact `9985246195`; ZIP SHA256 `aafe91e60b19a91845988d4f87ec45dd769ed57ca0529d342bf5dd93435f750a`.

Rates in SNU:

| component | B16-GS98 | B16-AGSS09met |
|---|---:|---:|
| pp | 38.17593 | 38.49195 |
| pep | 1.53045 | 1.55119 |
| Be7 | 18.66889 | 17.03715 |
| B8 | 4.49332 | 3.70099 |
| hep | 0.02095 | 0.02159 |
| N13 | 0.88944 | 0.65312 |
| O15 | 1.19983 | 0.84271 |
| F17 | 0.03112 | 0.01917 |
| **total** | **65.00994** | **62.31787** |

The metallicity dependence is therefore ~2.69 SNU in total and is dominated by Be7/B8/CNO source-flux differences, consistent with the earlier finding that GS98/AGSS09met differences in Pee itself are small.

## Independent context frozen before output inspection
Ishidoshiro & Tachibana, PTEP, published 18 March 2026, explicitly uses both B16-GS98 and B16-AGSS09met for radiochemical Ga/Cl prediction/likelihood work. This source was frozen as a post-result cross-check only; it was not used to tune the NMIR fold.

## Classification
- Full component-specific B16 × spectrum × production-averaged MSW × Ga response folding: **PASS**.
- Initial zero-energy endpoint failure: **infrastructure/boundary FAIL repaired**.
- Ga solar-rate gate: **PARTIAL SCIENTIFIC PASS**; external modern component/total numerical comparison still needs to be extracted explicitly, but the result is already in the expected radiochemical scale.

NMIR_READINESS: 31%

## Exact next gate
Freeze and reproduce the 37Cl energy-dependent capture response, then perform the same oscillated B16 folding. After Ga+Cl are independently validated, convert capture/deposition to W/kg and advance the quantitative Standard-Model G3 ceiling. Parallel non-biasing work may proceed on G8/G9/G10.
