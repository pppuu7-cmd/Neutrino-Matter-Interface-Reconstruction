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

For incident flux `Phi(E)`, finite gravitational gain `mu(E,x)`, capture cross section and deposited energy,

\[
P_{dep}=N_T\int dE\,\mu(E,\mathbf x)\Phi(E)\sigma_{cap}(E)E_{dep}(E).
\]

Useful capture requires **finite flux gain × real interaction probability × deposited-energy fraction**.

## Validated baselines

### CEvNS / magnetic

- Xe-132 ideal CEvNS at 1 MeV: `Q_W≈75.5311`, `sigma≈2.405e-41 cm^2`.
- Liquid-Xe-like mean free path: `~3.08e16 m`; optical-depth-one mass column `~9.07e18 g/cm^2`.
- Minimal Dirac magnetic moment at `m_nu=0.05 eV`: `~1.6e-20 mu_B`; ideal 1-m precession maximum requires `~3.35e17 T`.
- Naive whole-crystal elastic `N^2` total-opacity promotion is not accepted; directional peaks require integrated-strength/sum-rule checks.

### Measured beta decay → inverse capture

For allowed/superallowed long-wavelength transitions,

\[
\sigma_{NCB}v_\nu=2\pi^2\ln2\,\frac{p_eE_eF}{ft}.
\]

Tritium gives `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of the published measured-ft benchmark `7.84e-45 cm^2`. Authoritative CI: run `34004890286`, job `101410168170`, `29 passed`.

### B16 solar flux

`data/solar_flux_b16.csv` freezes B16-GS98 and B16-AGSS09met integrated source fluxes from Vinyoles et al. (2017). Iteration-0007 CI run `34007336474` completed SUCCESS on head `a4372f98965b3705f3b56363539805672772e3e6`.

### Solar spectral shapes

`data/solar_spectrum_manifest.csv` pins standard pp/hep/B8/CNO and thermally broadened Be7 spectral/profile files by upstream commit + exact Git-blob SHA from PEANUTS commit `59e3a2ae102d58f42cc1146eaca2cae68be879ce`.

Hosted materialization authority:

- run `34012460541`, job `101430502114`, head `f207836f32496b7e78990a485f27568ee659ee15`;
- all 8 expected files reproduced frozen Git-blob SHA exactly;
- artifact `9982880231`, ZIP SHA256 `c506de14cf1c0f0d02c706143449ae4a2fea887195f41de66763651e4f65cda6`;
- same-head CI run `34012460563`: `48 passed`.

**Spectral source identity: PASS. Exact spectral-byte materialization: PASS.**

### Frozen first oscillation convention

`data/solar_oscillation_convention.csv` fixes:

- `sin^2(theta12)=0.307`;
- `sin^2(theta13)=0.0220`;
- `Delta m^2_21=7.53e-5 eV^2`;
- normal ordering;
- standard three-flavour adiabatic MSW in the Sun;
- Earth regeneration OFF for the first benchmark.

### B16 matter + production distributions — validated iteration 0011

`data/solar_matter_manifest.csv` freezes both B16 radial tables from the same immutable PEANUTS snapshot:

- GS98: `Data/nudistr_b16_gs98.dat`, blob `f73c47cf6f2d77086634a5c180b50039e10805e7`;
- AGSS09met: `Data/nudistr_b16_agss09.dat`, blob `d9bd29f3374c63e8ea898733a55fb7aa566a2c96`.

Column contract: radius column 0 (`r/Rsun`), electron-density-log10 column 2 (`cm^-3/N_A`, numerically mol/cm^3 after exponentiation), production columns 4–11 for pp, pep, hep, Be7, B8, N13, O15, F17.

The candidate manifest/loader head `ec3082e9b08bce1f6ec46fb52fb970ee62c67b20` is validated by CI run `34012590342`, job `101430836362`; raw result `56 passed in 0.15s`.

Exact hosted materialization/parse authority:

- run `34014923087`, job `101436936728`;
- head `37267d5c75103d8ff07ba2104bc8330d10878128`;
- SUCCESS;
- artifact `9983598047`;
- artifact ZIP SHA256 `9b7baa133f74d616b62e158c27de71984ff025b209639a46c423f73acfc7c1e9`.

Both exact blobs were reproduced. Each table has 1000 rows over `r/Rsun=0.0005...0.5`, positive finite electron density, and all eight native production distributions integrate to unity within about `8e-5` by trapezoidal quadrature:

- GS98 integrals: `0.99992238 ... 0.99999162`;
- AGSS09met integrals: `1.00001814 ... 1.00006286`.

This independently validates the production-column interpretation. Explicit normalized quadrature weights are used for production averaging; the upstream tabulation is not silently rewritten.

**B16 matter source identity: PASS. Exact materialization/parse: PASS. Production-distribution normalization gate: PASS.**

### Adiabatic solar MSW kernel — pending current head CI

`src/nmir/solar_oscillation.py` now implements the prospectively fixed day-side adiabatic three-flavour approximation

\[
P_{ee}=c_{13}^4\frac{1+\cos2\theta_{12}\cos2\theta_{12}^m}{2}+s_{13}^4,
\]

with direct B16 electron-density input and `A_eff = 2 E sqrt(2) G_F n_e c13^2`. Tests were frozen before inspecting any real B16 survival curve: zero-density vacuum limit, high-density limit, physical low/high behavior, and native-grid production averaging.

Current MSW code/test head: `9a2cdc3e8ba6a35043ca50e4f7f632d89b65763f`. CI run `34014950750` was still active at the iteration-0011 checkpoint. **No numerical solar-survival, Ga or Cl PASS is claimed until that CI is consumed and real B16 component curves are benchmarked.**

## Other active branches

### Many-body/spin response

\[
\Gamma\propto\int d^3q\,d\omega\,L_{ab}S^{ab}.
\]

A 1-meV magnon produced by a 1-MeV neutrino deposits only `1e-9` of incident energy. Spin/magnon modes remain detection/response candidates unless a harder/repeated deposition mechanism appears.

### Gravitational focusing

Weak-field solar-limb benchmark `~547.741 AU`; transparent-Sun literature benchmark near `23.5 ± 0.1 AU` for distant-source neutrinos. Finite source/receiver size and Liouville conservation are mandatory.

### Staggered-layer metamaterial

Shifted layers move reciprocal-space peaks but projected atomic coverage is not weak opacity. At `E_nu=1 MeV`, `lambda≈1.23984e-12 m`; for `d=3 Å`, first-order Bragg angle `~0.118396 deg`. Any claim must survive angle/energy integration at fixed mass column.

## Research gates

| Gate | Question | Status |
|---|---|---|
| G0 | Known weak/CEvNS/capture normalizations reproduced? | PARTIAL PASS — CEvNS + tritium ft |
| G1 | Static macroscopic coherence beyond nuclear coherence? | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 | Can many-body spin/density/current modes deposit useful energy? | OPEN |
| G3 | Maximum SM deposited solar-neutrino power? | OPEN — flux/spectra/matter inputs validated; MSW kernel pending CI/benchmark; Ga/Cl missing |
| G4 | Can resonance/polarization/periodicity increase useful deposition parametrically? | OPEN |
| G5 | Minimal BSM structure if SM ceiling insufficient? | LOCKED until G3 |
| G6 | Does BSM survive constraints? | LOCKED until G5 |
| G7 | Can known production/decay identify strong inverse capture? | PARTIAL PASS — measured-ft route validated |
| G8 | Can resonance beat source bandwidth under integrated-strength bounds? | OPEN |
| G9 | Can finite gravitational lensing give useful gain? | OPEN |
| G10 | Can staggered/multi-isotope stacks beat same atoms at fixed mass column? | OPEN |

## Chronology

- `0001`: CEvNS/magnetic/coherence gates.
- `0002`: production↔absorption and spin triage.
- `0003`: inverse-transition seeds; Ga historical normalization/W/kg gap.
- `0004`: gravitational focusing.
- `0005`: staggered-layer metamaterial.
- `0006`: ft→capture; tritium reproduced.
- `0007`: B16 integrated flux freeze.
- `0008`: pinned spectral manifest + oscillation convention.
- `0009`: exact spectrum materialization.
- `0010`: B16 matter source freeze candidate.
- `0011`: B16 matter candidate CI consumed; exact hosted matter materialization/parse + production integrals PASS; prospective adiabatic MSW kernel added, current-head CI pending.

## Critical scope guards

1. Detector threshold is not total cross section.
2. Directional coherent gain is not integrated opacity gain.
3. Peak resonance is not flux-integrated capture.
4. Gravitational magnification is finite and multiplicative.
5. Projected atomic coverage is not neutrino opacity.
6. Exact time reversal and a crossed process are not automatically identical reactions.
7. Do not silently mix solar flux/spectrum/matter/oscillation/nuclear conventions.
8. BSM remains locked as a solution branch until G3 is quantitatively bounded.
9. No ad-hoc solar production radius/density when component-resolved B16 distributions are available.

## Current maturity

**NMIR_READINESS: 26%**.

Increase 25% -> 26% is credited only to the newly validated exact B16 matter materialization + production-normalization gate. The new MSW implementation earns no readiness credit until its CI and physical benchmarks pass.

## Exact next gate

1. Consume CI `34014950750` and classify the prospective MSW tests.
2. Run the validated kernel on exact B16 GS98/AGSS09met and publish component-resolved `P_ee(E)` checkpoints.
3. Cross-check low/high survival plateaus against standard/primary references without retuning.
4. Freeze Ga-71 response and reproduce published total/component SNU; then Cl-37.
5. Convert validated capture rates to W/kg and advance quantitative G3.
6. Parallel non-biasing work: resonance integrated-strength gate, sum-rule axial response, transparent-Sun benchmark, staggered fixed-mass-column comparison.
