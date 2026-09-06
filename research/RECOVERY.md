# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Mission

Reconstruct the low-energy neutrino↔matter interface, distinguish state control/detection from irreversible energy deposition, establish a quantitative Standard-Model ceiling, and only then open BSM model-building as a solution branch.

Frozen organizing principles:

1. response reconstruction;
2. production ↔ absorption / crossed weak channels;
3. finite gravitational focusing;
4. staggered-layer / multi-isotope response engineering.

## Central objective

For incident flux `Phi(E)`, absorber optical depth `tau(E)`, deposited fraction `eta_dep(E)` and finite gravitational magnification `mu(E,x)`,

\[
P_{dep}=N_T\int dE\,\mu(E,\mathbf x)\Phi(E)\sigma_{cap}(E)E_{dep}(E),
\]

or equivalently in slab form

\[
\frac{P_{dep}}{A}=\int dE\,\mu\Phi E\,\eta_{dep}(1-e^{-\tau}).
\]

Useful capture therefore depends on **finite flux gain × real interaction probability × deposited-energy fraction**.

## Current validated baselines

### CEvNS / magnetic

- Xe-132 ideal CEvNS at 1 MeV: `Q_W≈75.5311`, `sigma≈2.405e-41 cm^2`.
- Liquid-Xe-like mean free path: `~3.08e16 m`; optical-depth-one mass column `~9.07e18 g/cm^2`.
- Minimal Dirac magnetic moment for `m_nu=0.05 eV`: `~1.6e-20 mu_B`; ideal 1-m magnetic-precession maximum requires `~3.35e17 T`.
- Naive whole-crystal elastic `N^2` total-opacity promotion is not accepted; directional coherent peaks require integrated-strength/sum-rule checks.

### Measured beta decay → inverse capture

For allowed/superallowed long-wavelength transitions,

\[
\sigma_{NCB}v_\nu=2\pi^2\ln2\,\frac{p_eE_eF}{ft}.
\]

With the repository SI conversion, tritium gives `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of the published measured-ft benchmark `7.84e-45 cm^2`.

Authoritative scientific CI: run `34004890286`, job `101410168170`, `29 passed`.

### B16 solar flux freeze

`data/solar_flux_b16.csv` freezes B16-GS98 and B16-AGSS09met integrated source fluxes from Vinyoles et al. (2017). Examples, GS98: pp `5.98e10`, Be7 `4.93e9`, B8 `5.46e6 cm^-2 s^-1`; derived CNO sum `4.8829e8 cm^-2 s^-1`.

Iteration-0007 CI run `34007336474` completed SUCCESS on head `a4372f98965b3705f3b56363539805672772e3e6`.

### Spectral-shape identity and byte materialization — iterations 0008–0009

`data/solar_spectrum_manifest.csv` pins standard spectral shapes by upstream repository commit plus exact blob SHA. The pinned upstream implementation/provenance snapshot is `michelelucente/PEANUTS` commit `59e3a2ae102d58f42cc1146eaca2cae68be879ce`.

Bookkeeping line convention: pep `1.442 MeV`; Be7 `0.862 MeV` weight `0.897`, `0.384 MeV` weight `0.103`. Precision Be7 calculations use thermally broadened profile tables.

`src/nmir/solar_spectra.py` provides fail-closed immutable materialization: bytes are downloaded from the frozen upstream commit and canonical Git-blob SHA is checked before acceptance/write.

Hosted materialization authority:

- run `34012460541`, job `101430502114`, head `f207836f32496b7e78990a485f27568ee659ee15`;
- all 8 expected spectral/profile files reproduced frozen Git-blob SHA exactly;
- artifact ID `9982880231`;
- artifact ZIP SHA256 `c506de14cf1c0f0d02c706143449ae4a2fea887195f41de66763651e4f65cda6`.

Head regression CI on the same head: run `34012460563`, job `101430502143`, raw output `48 passed in 0.08s`.

**Spectral source identity: PASS. Exact spectral-byte materialization: PASS.**

### Frozen first oscillation convention — iteration 0008

`data/solar_oscillation_convention.csv` prospectively fixes the first Ga/Cl benchmark:

- `sin^2(theta12)=0.307`;
- `sin^2(theta13)=0.0220`;
- `Delta m^2_21=7.53e-5 eV^2`;
- normal ordering;
- standard three-flavour adiabatic MSW in the Sun;
- Earth regeneration OFF for the first benchmark.

The numerical component-averaged survival curve remains OPEN pending validated solar matter/production inputs and the numerical MSW kernel.

### B16 solar matter / production-distribution freeze candidate — iteration 0010

The same pinned PEANUTS snapshot contains the B16 radial tables used by its solar adiabatic calculation. Their headers cite Vinyoles et al. (2017), and `peanuts/solar.py` uses radius, electron density and reaction-specific production distributions for the production average.

`data/solar_matter_manifest.csv` now prospectively freezes both metallicity branches:

- B16 GS98: `Data/nudistr_b16_gs98.dat`, blob `f73c47cf6f2d77086634a5c180b50039e10805e7`;
- B16 AGSS09met: `Data/nudistr_b16_agss09.dat`, blob `d9bd29f3374c63e8ea898733a55fb7aa566a2c96`.

Frozen column contract for both: radius column 0 (`r/Rsun`), electron-density-log10 column 2 (`cm^-3/N_A`, numerically mol/cm^3 after exponentiation), production distributions columns 4–11 for pp, pep, hep, Be7, B8, N13, O15, F17.

`src/nmir/solar_matter.py` and `tests/test_solar_matter.py` add immutable identity/column/component/fail-closed guards. The new source-selection freeze is **PENDING head CI/materialization**; no numerical `P_ee` or Ga/Cl PASS is claimed from it yet.

## Other active branches

### Many-body/spin response

\[
\Gamma\propto\int d^3q\,d\omega\,L_{ab}S^{ab}.
\]

A 1-meV magnon produced by a 1-MeV neutrino deposits only `1e-9` of incident energy. Spin/magnon channels remain detection/response candidates, not bulk-energy winners unless a harder or repeated deposition mechanism appears.

### Gravitational focusing

\[
\alpha\simeq\frac{4GM}{bc^2},\qquad f\simeq\frac{b^2c^2}{4GM}.
\]

Solar-limb benchmark: `~547.741 AU`; transparent-Sun literature benchmark near `23.5 ± 0.1 AU` for distant-source neutrinos. Finite source/receiver size and Liouville conservation remain mandatory.

### Staggered-layer metamaterial

\[
F(\mathbf q)=\sum_j e^{i\mathbf q\cdot\mathbf r_j}.
\]

Shifted layers move constructive/destructive reciprocal-space peaks but projected atomic coverage is not weak opacity. At `E_nu=1 MeV`, `lambda≈1.23984e-12 m`; for `d=3 Å`, first-order Bragg angle is `~0.118396 deg`. Any useful claim must survive angle/energy integration at fixed mass column.

## Research gates

| Gate | Question | Status |
|---|---|---|
| G0 | Known weak/CEvNS/capture normalizations reproduced? | PARTIAL PASS — CEvNS + tritium ft benchmark |
| G1 | Static macroscopic coherence beyond ordinary nuclear coherence? | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 | Can many-body spin/density/current modes deposit useful energy? | OPEN |
| G3 | Maximum SM deposited solar-neutrino power? | OPEN — B16 flux + exact spectra + oscillation convention validated; B16 matter source freeze pending CI; numerical survival/capture kernels missing |
| G4 | Can resonance/polarization/periodicity increase useful deposition parametrically? | OPEN |
| G5 | Minimal BSM structure if SM ceiling insufficient? | LOCKED until G3 |
| G6 | Does BSM survive constraints? | LOCKED until G5 |
| G7 | Can known production/decay identify strong inverse capture? | PARTIAL PASS — explicit measured-ft route validated |
| G8 | Can resonance beat source bandwidth under integrated-strength bounds? | OPEN |
| G9 | Can finite gravitational lensing give useful gain? | OPEN |
| G10 | Can staggered/multi-isotope stacks beat same atoms at fixed mass column? | OPEN |

## Chronology

- `0001`: CEvNS/magnetic/coherence gates.
- `0002`: production↔absorption and spin-response triage.
- `0003`: inverse-transition seeds; Ga historical normalization and W/kg gap.
- `0004`: gravitational focusing branch.
- `0005`: staggered-layer metamaterial branch.
- `0006`: unit-explicit ft→capture normalization; tritium benchmark reproduced.
- `0007`: B16-GS98/AGSS09met integrated solar fluxes frozen.
- `0008`: commit/blob-pinned spectral manifest + first oscillation convention.
- `0009`: hosted exact materialization reproduces all eight frozen spectrum/profile blobs.
- `0010`: B16 GS98/AGSS09met electron-density + component production-distribution source identities frozen prospectively; validation pending.

## Critical scope guards

1. Detector threshold is not total cross section.
2. Directional coherent gain is not integrated opacity gain.
3. Peak resonance is not flux-integrated capture.
4. Gravitational magnification is finite and multiplicative, not a substitute for microscopic absorption.
5. Projected atomic coverage is not neutrino opacity.
6. Exact time reversal and a crossed process are not automatically identical external-particle reactions.
7. Do not mix solar flux, spectrum, matter profile, oscillation and nuclear cross-section conventions silently.
8. BSM remains locked as a solution branch until G3 is quantitatively bounded.
9. No ad-hoc effective solar production radius/density is permitted when component-resolved B16 distributions are available.

## Current repository components through iteration 0010

- flux: `data/solar_flux_b16.csv` + loader/tests;
- spectra: `data/solar_spectrum_manifest.csv`, `src/nmir/solar_spectra.py`, tests, materialization workflow;
- solar matter candidate: `data/solar_matter_manifest.csv`, `src/nmir/solar_matter.py`, tests;
- oscillation: `data/solar_oscillation_convention.csv`, `src/nmir/solar_oscillation.py`, tests;
- capture: `src/nmir/ft_capture.py`, `capture_metrics.py`;
- other branches: `gravity_focusing.py`, `staggered_lattice.py`, response/duality theory documents;
- chronological `research/iterations/0001...0010` notes.

## Current maturity

**NMIR_READINESS: 25%**.

Readiness remains 25% until the new B16 matter provenance/loader contract passes head CI and exact materialization/parse checks. The prior increase from 24% to 25% is credited only to the validated eight-spectrum hosted materialization gate.

## Exact next gate

1. Consume the latest head CI for `solar_matter` and classify PASS/FAIL.
2. Materialize both B16 matter tables with exact blob verification; parse radius/density/production columns and verify finite positive production integrals.
3. Implement day-side adiabatic three-flavour `P_ee(E,r)` and production averaging under frozen oscillation parameters.
4. Validate low-/high-energy survival limits; reproduce Ga-71, then Cl-37.
5. Convert validated capture rates to W/kg and start quantitative G3 ceiling.
6. Parallel non-biasing work only: resonance integrated-strength gate, sum-rule axial response, transparent-Sun benchmark, staggered fixed-mass-column comparison.
