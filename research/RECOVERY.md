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

With the repository SI conversion, tritium gives

\[
\sigma(v/c)\simeq7.785\times10^{-45}\,\mathrm{cm^2},
\]

within ~0.7% of the published measured-ft benchmark `7.84e-45 cm^2`.

Authoritative scientific CI for this normalization: run `34004890286`, job `101410168170`, `29 passed`.

### B16 solar flux freeze

`data/solar_flux_b16.csv` freezes B16-GS98 and B16-AGSS09met integrated source fluxes from Vinyoles et al. (2017). Examples, GS98: pp `5.98e10`, Be7 `4.93e9`, B8 `5.46e6 cm^-2 s^-1`; derived CNO sum `4.8829e8 cm^-2 s^-1`.

Iteration-0007 CI run `34007336474` completed SUCCESS on head `a4372f98965b3705f3b56363539805672772e3e6`.

### Spectral-shape identity and byte materialization — iterations 0008–0009

`data/solar_spectrum_manifest.csv` pins the standard spectral-shape inputs by **upstream repository commit plus exact blob SHA**, preventing silent spectral drift:

- pp/hep: Bahcall, Phys. Rev. C 56, 3391 (1997);
- B8 baseline: Ortiz et al., Phys. Rev. Lett. 85, 2909 (2000);
- N13/O15/F17: Bahcall & Ulrich, Rev. Mod. Phys. 60, 297 (1988);
- Be7 thermally broadened line profiles: Bahcall, Phys. Rev. D 49, 3923 (1994).

Pinned upstream implementation/provenance snapshot: `michelelucente/PEANUTS` commit `59e3a2ae102d58f42cc1146eaca2cae68be879ce`.

Bookkeeping line convention: pep `1.442 MeV`; Be7 `0.862 MeV` weight `0.897`, `0.384 MeV` weight `0.103`. Precision Be7 calculations must use the broadened profile tables rather than delta lines.

`src/nmir/solar_spectra.py` now provides fail-closed immutable materialization: bytes are downloaded from the frozen upstream commit, canonical Git-blob SHA is checked **before** acceptance/write, and all six continuum spectra plus two Be7 profiles can be materialized together.

Hosted materialization authority:

- workflow run `34012460541`, job `101430502114`;
- head `f207836f32496b7e78990a485f27568ee659ee15`;
- all 8 expected spectral/profile files reproduced their frozen Git-blob SHA exactly;
- artifact ID `9982880231`;
- artifact ZIP SHA256 `c506de14cf1c0f0d02c706143449ae4a2fea887195f41de66763651e4f65cda6`;
- artifact name `nmir-solar-spectra-f207836f32496b7e78990a485f27568ee659ee15`.

Head regression CI on the same head: run `34012460563`, job `101430502143`, raw output `48 passed in 0.08s`.

**Spectral source identity: PASS. Exact spectral-byte materialization: PASS.**

### Frozen first oscillation convention — iteration 0008

`data/solar_oscillation_convention.csv` prospectively fixes the first Ga/Cl benchmark before any rate calculation:

- `sin^2(theta12)=0.307`;
- `sin^2(theta13)=0.0220`;
- `Delta m^2_21=7.53e-5 eV^2`;
- normal ordering;
- standard three-flavour adiabatic MSW in the Sun;
- Earth regeneration OFF for the first benchmark, later robustness branch.

`src/nmir/solar_oscillation.py` and tests freeze these values/scope. **The numerical component-averaged survival curve is still OPEN** because production-radius/electron-density weighting is not yet frozen.

## Other active branches

### Many-body/spin response

Inclusive rate organization:

\[
\Gamma\propto\int d^3q\,d\omega\,L_{ab}S^{ab}.
\]

A 1-meV magnon produced by a 1-MeV neutrino deposits only `1e-9` of the incident energy. Spin/magnon channels remain detection/response candidates, not bulk-energy winners unless a harder or repeated deposition mechanism appears.

### Gravitational focusing

Weak-field benchmark:

\[
\alpha\simeq\frac{4GM}{bc^2},\qquad f\simeq\frac{b^2c^2}{4GM}.
\]

Solar-limb benchmark: `~547.741 AU`. Published transparent-Sun calculations give minimum focal distance near `23.5 ± 0.1 AU` for distant-source neutrinos crossing the solar interior. Finite source/receiver size and Liouville phase-space conservation are mandatory; the Sun is not a separate downstream lens for its own emitted solar neutrinos.

### Staggered-layer metamaterial

\[
F(\mathbf q)=\sum_j e^{i\mathbf q\cdot\mathbf r_j}.
\]

Shifted layers can move constructive/destructive reciprocal-space peaks but projected atomic coverage is not weak opacity. For nuclear radius `5 fm` and lattice spacing `3 Å`, naive geometric nuclear projected fraction is `8.73e-10` per layer; ~`1.15e9` perfectly complementary layers would only reach unity **geometric** nuclear projection. For `E_nu=1 MeV`, `lambda≈1.23984e-12 m`, giving first-order Bragg angle `~0.118396 deg` at `d=3 Å`. Any useful claim must survive angle/energy integration at fixed mass column.

## Research gates

| Gate | Question | Status |
|---|---|---|
| G0 | Known weak/CEvNS/capture normalizations reproduced? | PARTIAL PASS — CEvNS + tritium ft benchmark |
| G1 | Static macroscopic coherence beyond ordinary nuclear coherence? | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 | Can many-body spin/density/current modes deposit useful energy? | OPEN |
| G3 | Maximum SM deposited solar-neutrino power? | OPEN — B16 flux + exact spectral bytes + oscillation convention frozen; numerical survival/capture kernels missing |
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
- `0003`: inverse-transition seeds; historical Ga rate normalization gives `~8.99e-23 W/kg` for optimistic 1-MeV deposition and requires `~1.11e22` gain to reach 1 W/kg.
- `0004`: gravitational focusing branch.
- `0005`: staggered-layer metamaterial branch.
- `0006`: unit-explicit ft→capture normalization; tritium benchmark reproduced.
- `0007`: B16-GS98/AGSS09met integrated solar fluxes frozen.
- `0008`: commit/blob-pinned spectral manifest + first prospective oscillation convention frozen.
- `0009`: fail-closed hosted materialization reproduces all eight frozen spectral/profile blobs exactly; verified artifact produced.

## Critical scope guards

1. Detector threshold is not total cross section.
2. Directional coherent gain is not integrated opacity gain.
3. Peak resonance is not flux-integrated capture.
4. Gravitational magnification is multiplicative and finite, not a substitute for microscopic absorption.
5. Projected atomic coverage is not neutrino opacity.
6. Exact time reversal and a crossed process are not automatically identical external-particle reactions.
7. Do not mix solar flux, spectrum, oscillation and nuclear cross-section conventions silently.
8. BSM remains locked as a solution branch until G3 is quantitatively bounded.
9. Exact spectrum identity is now recoverable through frozen commit/blob provenance plus validated fail-closed materialization; Ga/Cl still require a separately frozen solar matter/production weighting.

## Current repository components added through iteration 0009

- flux: `data/solar_flux_b16.csv`, provenance + loader/tests;
- spectra: `data/solar_spectrum_manifest.csv`, `src/nmir/solar_spectra.py`, tests, `.github/workflows/spectra-materialize.yml`;
- oscillation: `data/solar_oscillation_convention.csv`, `src/nmir/solar_oscillation.py`, tests;
- capture: `src/nmir/ft_capture.py`, `capture_metrics.py`;
- other branches: `gravity_focusing.py`, `staggered_lattice.py`, response/duality theory documents;
- chronological `research/iterations/0001...0009` notes.

## Current maturity

**NMIR_READINESS: 25%**.

The increase from 24% to 25% is credited only for a real hosted materialization PASS: all eight exact spectrum/profile blob identities were reproduced, an immutable run/artifact provenance was recorded, and head regression CI passed. No credit is assigned yet for numerical solar `P_ee(E)`, Ga/Cl reproduction, or G3 closure.

## Exact next gate

1. Identify and freeze a provenance-controlled solar electron-density profile plus component production-radius distributions; do not substitute an ad-hoc effective production radius.
2. Implement day-side adiabatic three-flavour `P_ee(E,r)` and production averaging under the already frozen oscillation parameters.
3. Reproduce a published Ga-71 component/total rate; then Cl-37.
4. Convert reproduced capture rates to W/kg and start the quantitative G3 ceiling.
5. In parallel only when non-biasing: resonance integrated-strength gate, sum-rule axial toy response, transparent-Sun `~23.5 AU`, and staggered fixed-mass-column comparison.
