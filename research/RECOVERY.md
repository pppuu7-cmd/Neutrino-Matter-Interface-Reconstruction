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
- Xe-132 ideal CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; mean free path in liquid-Xe-like density `~3.08e16 m`; optical-depth-one mass column `~9.07e18 g/cm^2`.
- Minimal Dirac magnetic-moment benchmark for `m_nu=0.05 eV`: `~1.6e-20 mu_B`; ideal 1-m magnetic-precession maximum requires `~3.35e17 T`.
- Tritium measured-ft route gives `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45 cm^2`; CI `34004890286`, job `101410168170`.

### Solar inputs
- B16 GS98/AGSS09met integrated fluxes frozen in `data/solar_flux_b16.csv`.
- Exact pinned pp/hep/B8/CNO and thermally broadened Be7 spectra in `data/solar_spectrum_manifest.csv`.
- Spectrum materialization authority: run `34012460541`, job `101430502114`, artifact `9982880231`, ZIP SHA256 `c506de14cf1c0f0d02c706143449ae4a2fea887195f41de66763651e4f65cda6`.
- B16 matter blobs: GS98 `f73c47cf6f2d77086634a5c180b50039e10805e7`; AGSS09met `d9bd29f3374c63e8ea898733a55fb7aa566a2c96`; materialization run `34014923087`, artifact `9983598047`.
- Frozen oscillation convention: `sin^2(theta12)=0.307`, `sin^2(theta13)=0.0220`, `Delta m^2_21=7.53e-5 eV^2`, normal ordering, day-side adiabatic three-flavour MSW, Earth regeneration OFF.
- Exact B16 survival authority: run `34015021346`, artifact `9983624802`. Representative GS98 `Pee`: pp(0.300)=0.544186; Be7(0.862)=0.526972; pep(1.442)=0.516871; B8(5)=0.393449; B8(10)=0.327017.

### Ga-71 response and full solar fold
Primary response: J. N. Bahcall, Phys. Rev. C 56, 3391 (1997). `data/ga71_bahcall1997_response.csv` has 58 points over 0.240–30 MeV with best and ±3σ branches.

Source-average validation run `34017366528`, job `101443416887`, artifact `9984322724`: relative errors vs Bahcall pp 0.205%, pep 0.796%, Be7 0.022%, N13 0.085%, O15 0.161%, F17 0.581%.

First full Ga fold run `34020172203` failed before a scientific result because a valid continuum includes `E=0` while `Pee(0)` is undefined. Since `sigma_Ga(0)=0`, repair `a5b6d2a109fe39695f421ecc455026c9c0f92c94` skips Pee at exactly zero capture contribution and caches immutable weights/constants; no physics convention changed. Regression commit `382024af46534e4332d79d33896064480f7339a3`; CI `34020276133`, job `101451443326`: 74 passed.

Authoritative Ga fold: run `34020272911`, job `101451434118`, artifact `9985246195`, ZIP SHA256 `aafe91e60b19a91845988d4f87ec45dd769ed57ca0529d342bf5dd93435f750a`.

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

Full component-specific B16 × spectrum × production-averaged MSW × Ga response folding: PASS.

### Cl-37 response and sensitivity — iteration 0015
Primary numerical response: John Bahcall IAS data page, improved values identified as Bahcall et al., Phys. Rev. C 54, 411 (1996). `data/cl37_bahcall1996_response.csv` freezes 19 improved + older Bahcall-Ulrich points from 1 to 30 MeV in units `1e-46 cm^2`. Physical threshold is `0.814 MeV`.

Implementation: `src/nmir/cl37_response.py`, `src/nmir/cl37_solar_fold.py`, regression tests, hosted workflow. Response/fold baseline CI `34020442734`, job `101451908216`: SUCCESS.

First full Cl fold: run `34020427430`, job `101451868492`, artifact `9985296780`, ZIP SHA256 `900526f17c6a7f3990de0a3e46d4f5a8b42d27d74fd6b662005c6a9964312f2f`, SUCCESS.

Using an explicit threshold-linear convention in the unpublished/tabulation gap `0.814–1.0 MeV`:
- GS98: total `2.71951 SNU`, B8 `2.13959`, Be7 `0.31711`, pep `0.14336`.
- AGSS09met: total `2.28573 SNU`, B8 `1.76236`, Be7 `0.28939`, pep `0.14530`.

Because the primary table begins at 1 MeV, a second prospective `zero_to_1` mode was implemented solely to measure sensitivity, not as an alternate fitted model. Sensitivity authority: run `34020504315`, job `101452083142`, head `8781012e35e92c12aee9ea83e07992fc5adc8843`, artifact `9985321559`, ZIP SHA256 `347a2e3fbf53ecac44221ab8feb1aa91fb760ebe13e6919c7bb0796e02b771f2`, SUCCESS.

- GS98 total: `2.71951` threshold-linear vs `2.38893 SNU` zero-to-1; shift `0.33057 SNU` (~12.2%).
- AGSS09met: `2.28573` vs `1.98662 SNU`; shift `0.29911 SNU` (~13.1%).
- Almost all sensitivity is the 0.862-MeV Be7 line. B8 changes by only a few `1e-6 SNU` and is robust to the unresolved interval.

Final Homestake observation used in modern radiochemical analyses is `2.56 ± 0.23 SNU`; agreement with observation is context only and was not used to normalize NMIR.

Classification: published `>=1 MeV` Cl response PASS; B8-dominated high-energy full fold PASS; full Cl total PARTIAL PASS / LOW-ENERGY RESPONSE BLOCKED until a primary constraint at/near 0.862 MeV replaces the interpolation ambiguity.

## Other active branches
- Many-body/spin: response formalism active; a single 1-meV magnon from a 1-MeV neutrino deposits only `1e-9` of incident energy.
- Gravitational focusing: solar-limb weak-field benchmark `~547.741 AU`; transparent-Sun literature benchmark near `23.5 ± 0.1 AU`; finite-source/Liouville gate mandatory.
- Staggered metamaterial: at 1 MeV, `lambda≈1.23984e-12 m`; for `d=3 Å`, first Bragg angle `~0.118396 deg`; any gain must survive angle/energy integration at fixed mass column.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS — CEvNS + tritium ft + Ga response + Cl >=1-MeV response |
| G1 static macroscopic coherence | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 many-body deposited-energy channels | OPEN |
| G3 maximum SM deposited solar-neutrino power | OPEN — Ga fold PASS; Cl high-energy PASS but Be7 low-energy response unresolved; W/kg missing |
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
10. Missing response below a tabulated energy must remain an explicit uncertainty, never silently interpolated into authority.

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered metamaterial; `0006` ft→capture; `0007–0012` B16 flux/spectra/matter/MSW; `0013` Ga response; `0014` full Ga fold; `0015` Cl response + full fold + explicit low-energy sensitivity.

## Current maturity
**NMIR_READINESS: 32%**.

Increase `31% -> 32%` credits only the authoritative Cl response freeze, hosted robust high-energy fold and quantified threshold-gap sensitivity. Full Cl closure is withheld.

## Exact next gate
1. Resolve/bound `37Cl` response at the 0.862-MeV Be7 line from primary nuclear/capture literature; replace the threshold interpolation with authority or a defensible uncertainty interval.
2. Reproduce the standard-spectrum B8-on-Cl average (`~1.1e-42 cm^2`) using a matched B8 spectral convention.
3. Freeze final Cl component/total interval.
4. In parallel begin neutrino-only deposited-energy accounting for validated Ga capture, carefully excluding daughter-decay/nuclear-mass energy not supplied by the incident neutrino; convert to W/kg.
5. Continue independent G8/G9/G10 gates without result-dependent tuning.
