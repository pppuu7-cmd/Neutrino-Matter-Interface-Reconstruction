# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Mission
Reconstruct the low-energy neutrino↔matter interface, distinguish detection/state control from irreversible neutrino-sourced energy deposition, establish a quantitative Standard-Model ceiling, and only then open BSM model-building as a solution branch.

Frozen organizing principles: response reconstruction; production↔absorption/crossed weak channels; finite gravitational focusing; staggered-layer/multi-isotope response engineering.

Central objective:
\[
P_{dep}=N_T\int dE\,\mu(E,\mathbf x)\Phi(E)\sigma_{cap}(E)E_{dep}(E).
\]

## Validated baseline authority

### Weak / inverse-capture anchors
- Xe-132 ideal CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; liquid-Xe-like mean free path `~3.08e16 m`; optical-depth-one mass column `~9.07e18 g/cm^2`.
- Minimal Dirac magnetic moment for `m_nu=0.05 eV`: `~1.6e-20 mu_B`; ideal 1-m magnetic-precession maximum requires `~3.35e17 T`.
- Tritium measured-ft route: `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45 cm^2`; CI `34004890286`, job `101410168170`.

### Solar inputs
- B16 GS98/AGSS09met integrated fluxes frozen in `data/solar_flux_b16.csv`.
- Exact pinned pp/hep/B8/CNO and thermally broadened Be7 spectra in `data/solar_spectrum_manifest.csv`; materialization authority run `34012460541`, artifact `9982880231`, SHA256 `c506de14cf1c0f0d02c706143449ae4a2fea887195f41de66763651e4f65cda6`.
- B16 matter blobs: GS98 `f73c47cf6f2d77086634a5c180b50039e10805e7`; AGSS09met `d9bd29f3374c63e8ea898733a55fb7aa566a2c96`; materialization run `34014923087`, artifact `9983598047`.
- Frozen oscillation convention: `sin^2(theta12)=0.307`, `sin^2(theta13)=0.0220`, `Delta m^2_21=7.53e-5 eV^2`, normal ordering, day-side adiabatic three-flavour MSW, Earth regeneration OFF.
- Exact B16 survival authority: run `34015021346`, artifact `9983624802`. Representative GS98 `Pee`: pp(0.300)=0.544186; Be7(0.862)=0.526972; pep(1.442)=0.516871; B8(5)=0.393449; B8(10)=0.327017.

### Ga-71 response and full solar fold
Primary response: J. N. Bahcall, Phys. Rev. C 56, 3391 (1997). `data/ga71_bahcall1997_response.csv`: 58 points, 0.240–30 MeV, best and ±3σ branches.

Source-average validation run `34017366528`, artifact `9984322724`: relative errors vs Bahcall pp 0.205%, pep 0.796%, Be7 0.022%, N13 0.085%, O15 0.161%, F17 0.581%.

Authoritative full Ga fold: run `34020272911`, artifact `9985246195`, SHA256 `aafe91e60b19a91845988d4f87ec45dd769ed57ca0529d342bf5dd93435f750a`.

| component SNU | GS98 | AGSS09met |
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

Classification: full component-specific B16 × spectrum × production-averaged MSW × Ga response folding PASS.

### Cl-37 pointwise response
Primary numerical response: John Bahcall IAS data page, improved values identified as Bahcall et al., Phys. Rev. C 54, 411 (1996). `data/cl37_bahcall1996_response.csv`: 19 points from 1 to 30 MeV, physical threshold `0.814 MeV`.

Iteration 0015 established that a naive threshold-linear extrapolation in `0.814–1.0 MeV` was not authoritative: it gave Be7 only `0.31711 SNU` for GS98 and caused ~12–13% total-rate ambiguity relative to a zero-to-1 sensitivity mode. High-energy/B8 response remained robust.

### Cl-37 source-average authority — iteration 0016
Primary authority: Bahcall & Ulrich, Rev. Mod. Phys. 60, 297 (1988), source-averaged Cl-37 cross sections. Frozen in `data/cl37_bahcall_ulrich1988_source_average.csv`:
- pp `0`
- pep `16e-46 cm^2`
- hep `3.9e-42 cm^2`
- Be7 `2.4e-46 cm^2`
- B8 `1.06e-42 cm^2`
- N13 `1.7e-46 cm^2`
- O15 `6.8e-46 cm^2`
- F17 `6.9e-46 cm^2`.

Because the 0.384-MeV Be7 line is below the 0.814-MeV Cl threshold, the published Be7 source-average cross section is effectively the capture-active 0.862-MeV branch strength folded with its solar line profile/branching. `src/nmir/cl37_source_average.py` therefore provides the authoritative Be7 component route; the old pointwise sub-1-MeV interpolation remains only for residual continuum sensitivity/history.

Hosted authority-backed Cl fold: run `34022999659`, head `4e29bef5f15ac39c5d97fc51274d0ff40235f893`, artifact `9986121953`, SHA256 `ce64ed62d0fc50632d48815c0c0e42a8afdb14d00bee47ae292666cba3edfe7c`, SUCCESS.

| Cl component/total SNU | GS98 | AGSS09met |
|---|---:|---:|
| Be7 authority | 0.6235128 | 0.5690128 |
| B8 | 2.1395856 | 1.7623578 |
| pep | 0.1433597 | 0.1453031 |
| total, threshold-linear residual | **3.0259103** | **2.5653535** |
| total, zero-to-1 residual | **3.0124470** | **2.5556371** |

Key result: once Be7 uses primary source-average authority, residual total sensitivity to the unresolved `0.814–1.0 MeV` continuum interval collapses from ~12–13% to ~0.4%. The old `~0.317 SNU` Be7 value is classified as a scientific FAIL of the threshold-linear interpolation model, not of Cl capture physics.

CI for authority utilities/tests: `34023005898` on head `fb1c78fc5a1a205992962c017de02a09e87a0ae5`, SUCCESS.

Independent B8 source-average reproduction is now implemented in `src/nmir/cl37_benchmark.py` + `scripts/cl37_source_average_benchmark.py`; hosted workflow head `b423cd694069ae70c98d88d8d66cae560a59190a` is the next result to consume. Do not promote B8 matched-average PASS until its raw artifact is inspected.

Final Homestake observation `2.56 ± 0.23 SNU` is context only and was never used to normalize NMIR.

## Other active branches
- Many-body/spin: response formalism active; a single 1-meV magnon from a 1-MeV neutrino deposits only `1e-9` of incident energy.
- Gravitational focusing: solar-limb weak-field benchmark `~547.741 AU`; transparent-Sun literature benchmark near `23.5 ± 0.1 AU`; finite-source/Liouville gate mandatory.
- Staggered metamaterial: at 1 MeV, `lambda≈1.23984e-12 m`; for `d=3 Å`, first Bragg angle `~0.118396 deg`; any gain must survive angle/energy integration at fixed mass column.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS — CEvNS + tritium ft + Ga response + Cl pointwise/source-average anchors |
| G1 static macroscopic coherence | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 many-body deposited-energy channels | OPEN |
| G3 maximum SM deposited solar-neutrino power | OPEN — Ga fold PASS; Cl Be7 blocker resolved at component level and total residual uncertainty ~0.4%; B8 source-average matched check + W/kg still missing |
| G4 engineered resonance/polarization/periodicity | OPEN |
| G5 minimal BSM solution | LOCKED until G3 |
| G6 BSM constraints | LOCKED until G5 |
| G7 production/decay → inverse capture | PARTIAL PASS — measured-ft route validated |
| G8 resonance integrated-strength/bandwidth | OPEN |
| G9 finite gravitational focusing gain | OPEN |
| G10 staggered/multi-isotope fixed-mass-column gain | OPEN |

## Critical scope guards
1. Detector threshold ≠ total cross section.
2. Directional coherence ≠ integrated opacity.
3. Peak resonance ≠ flux-integrated capture.
4. Gravitational magnification is finite and multiplicative.
5. Projected atomic coverage ≠ neutrino opacity.
6. Exact time reversal and crossed weak processes must be classified correctly.
7. Never mix solar flux/spectrum/matter/oscillation/nuclear conventions silently.
8. BSM solution branch remains locked until G3 is quantified.
9. Green workflow ≠ scientific PASS until raw result and frozen gate are inspected.
10. Missing pointwise response must not be silently interpolated into authority when a source-average or uncertainty formulation is the correct observable.

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered metamaterial; `0006` ft→capture; `0007–0012` B16 flux/spectra/matter/MSW; `0013` Ga response; `0014` full Ga fold; `0015` Cl pointwise fold/sensitivity; `0016` Cl source-average Be7 authority.

## Current maturity
**NMIR_READINESS: 33%**.

Increase `32% -> 33%` credits the published Cl source-average freeze, removal of the Be7 interpolation blocker at component level, hosted corrected fold, and reduction of residual sub-1-MeV total uncertainty to ~0.4%. B8 matched source-average check and W/kg remain open.

## Exact next gate
1. Consume hosted B8-on-Cl standard-spectrum average and compare with frozen `1.06e-42 cm^2` authority without retuning.
2. Freeze final Cl component/total uncertainty interval.
3. Implement neutrino-only deposited-energy accounting for validated Ga/Cl capture, explicitly excluding daughter-decay/nuclear-mass energy not supplied by the incident neutrino; convert to W/kg and bound G3.
4. Continue independent G8 resonance integrated-strength, G9 transparent-Sun finite-source focusing, and G10 fixed-mass-column staggered-stack gates without result-dependent tuning.
