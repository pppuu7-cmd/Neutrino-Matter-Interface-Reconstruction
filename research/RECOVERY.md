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

\[
P_{dep}=N_T\int dE\,\mu(E,\mathbf x)\Phi(E)\sigma_{cap}(E)E_{dep}(E).
\]

Useful capture requires **finite flux gain × real interaction probability × deposited-energy fraction**.

## Validated baselines

### CEvNS / magnetic

- Xe-132 ideal CEvNS at 1 MeV: `Q_W≈75.5311`, `sigma≈2.405e-41 cm^2`.
- Liquid-Xe-like mean free path `~3.08e16 m`; optical-depth-one mass column `~9.07e18 g/cm^2`.
- Minimal Dirac magnetic moment at `m_nu=0.05 eV`: `~1.6e-20 mu_B`; ideal 1-m precession maximum requires `~3.35e17 T`.
- Whole-crystal elastic directional coherence is not accepted as total-opacity `N^2` enhancement without integrated-strength/sum-rule closure.

### Measured beta decay → inverse capture

For allowed/superallowed long-wavelength transitions,

\[
\sigma_{NCB}v_\nu=2\pi^2\ln2\,\frac{p_eE_eF}{ft}.
\]

Tritium gives `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of the published measured-ft benchmark `7.84e-45 cm^2`. Authoritative CI: run `34004890286`, job `101410168170`, `29 passed`.

### B16 solar flux / spectra / matter

- `data/solar_flux_b16.csv` freezes B16-GS98 and B16-AGSS09met integrated source fluxes; CI run `34007336474` SUCCESS on head `a4372f98965b3705f3b56363539805672772e3e6`.
- `data/solar_spectrum_manifest.csv` pins pp/hep/B8/CNO and thermally broadened Be7 spectral/profile files by exact upstream commit + Git-blob SHA.
- Exact spectrum materialization: run `34012460541`, job `101430502114`, artifact `9982880231`, ZIP SHA256 `c506de14cf1c0f0d02c706143449ae4a2fea887195f41de66763651e4f65cda6`; same-head CI `34012460563`: `48 passed`.
- B16 matter inputs: GS98 blob `f73c47cf6f2d77086634a5c180b50039e10805e7`; AGSS09met blob `d9bd29f3374c63e8ea898733a55fb7aa566a2c96`.
- Matter manifest/loader CI: run `34012590342`, job `101430836362`, `56 passed`.
- Hosted exact matter materialization/parse: run `34014923087`, job `101436936728`, artifact `9983598047`, ZIP SHA256 `9b7baa133f74d616b62e158c27de71984ff025b209639a46c423f73acfc7c1e9`.
- Both B16 tables have 1000 rows over `r/Rsun=0.0005...0.5`; all eight component production distributions normalize to unity within ~`8e-5` by native-grid trapezoidal quadrature.

**Solar integrated flux identity: PASS. Spectral source/materialization identity: PASS. B16 matter identity/materialization/production normalization: PASS.**

### Frozen first oscillation convention + exact B16 survival

`data/solar_oscillation_convention.csv` fixes `sin^2(theta12)=0.307`, `sin^2(theta13)=0.0220`, `Delta m^2_21=7.53e-5 eV^2`, normal ordering, standard three-flavour day-side adiabatic MSW, Earth regeneration OFF.

`src/nmir/solar_oscillation.py` implements

\[
P_{ee}=c_{13}^4\frac{1+\cos2\theta_{12}\cos2\theta_{12}^m}{2}+s_{13}^4.
\]

Prospective numerical-limit CI: run `34014950750`, job `101437007287`, head `9a2cdc3e8ba6a35043ca50e4f7f632d89b65763f`, `64 passed`.

Exact B16 survival authority: run `34015021346`, job `101437186911`, artifact `9983624802`, ZIP SHA256 `09cd10d0530723646dce465f3b965796624cc03ce1070a81556f374ebb7b5d50`.

Representative GS98 checkpoints: `Pee(pp,0.300)=0.544186`, `Pee(Be7,0.862)=0.526972`, `Pee(pep,1.442)=0.516871`, `Pee(B8,5)=0.393449`, `Pee(B8,10)=0.327017`. GS98/AGSS09 survival differences are only `~1e-4...1e-3` absolute at these checkpoints.

**Prospective MSW kernel: PASS within frozen approximation. Exact component survival benchmark: PASS.**

### Ga-71 energy response + source-average validation — iteration 0013

Primary response source: J. N. Bahcall, Phys. Rev. C 56, 3391 (1997), specific-energy Tables II-IV / associated numerical data and Table VI standard-spectrum averages.

Repository components:

- `data/ga71_bahcall1997_response.csv` — 58 frozen response energies from `0.240` to `30 MeV`, best and ±3σ cross sections;
- `src/nmir/ga71_response.py` — fail-closed interpolation, threshold handling, spectrum parser/folding and SNU line conversion;
- `scripts/ga71_unoscillated_benchmark.py` — prospective source-average identity gate;
- `.github/workflows/ga71-benchmark.yml` — hosted validation.

Prospective tolerances were frozen before output inspection: pp 1.5%, pep 4%, Be7 0.5%, N13/O15/F17 2.5%. B8/hep were excluded from this identity gate because NMIR's pinned B8/hep spectral conventions are not identical to Bahcall's 1997 standard spectra.

Authoritative scientific benchmark:

- run `34017366528`;
- job `101443416887`;
- head `a3fb3dcceafeecb4cdda59bf6459437c33d7050f`;
- artifact `9984322724`;
- artifact ZIP SHA256 `fc162d6807a3f087aaf8086c6558d16e1c1358f497fc751b48cb6d97d66a0f4f`;
- conclusion: SUCCESS.

Source-average cross sections, units `1e-46 cm^2`:

| source | NMIR | Bahcall | relative error |
|---|---:|---:|---:|
| pp | 11.74399 | 11.72 | 0.2047% |
| pep | 205.624 | 204.0 | 0.7961% |
| Be7 | 71.71590 | 71.7 | 0.0222% |
| N13 | 60.45132 | 60.4 | 0.0850% |
| O15 | 113.88247 | 113.7 | 0.1605% |
| F17 | 114.56221 | 113.9 | 0.5814% |

**Ga-71 energy-response identity: PASS. Ga-71 standard-spectrum source-average reconstruction: PASS.**

The same-head baseline CI run `34017366468` failed only because a regression test mistakenly expected 59 table rows instead of the actual frozen 58. Scientific benchmark step was already PASS. The cardinality test was corrected in commit `cd429081a35d04aa5b44c2e69a0c694320064ccd`; no physics data, interpolation, tolerances or gate logic changed. Classification: **infrastructure/test FAIL repaired, not scientific FAIL**.

## Other active branches

### Many-body/spin response

\[
\Gamma\propto\int d^3q\,d\omega\,L_{ab}S^{ab}.
\]

A 1-meV magnon produced by a 1-MeV neutrino deposits only `1e-9` of incident energy. Spin/magnon modes remain detection/response candidates unless harder/repeated deposition is demonstrated.

### Gravitational focusing

Weak-field solar-limb benchmark `~547.741 AU`; transparent-Sun literature benchmark near `23.5 ± 0.1 AU` for distant-source neutrinos. Finite source/receiver size and Liouville conservation are mandatory.

### Staggered-layer metamaterial

At `E_nu=1 MeV`, `lambda≈1.23984e-12 m`; for `d=3 Å`, first-order Bragg angle `~0.118396 deg`. Any claimed gain must survive angle/energy integration at fixed mass column.

## Research gates

| Gate | Question | Status |
|---|---|---|
| G0 | Known weak/CEvNS/capture normalizations reproduced? | PARTIAL PASS — CEvNS + tritium ft + Ga source averages |
| G1 | Static macroscopic coherence beyond nuclear coherence? | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 | Can many-body spin/density/current modes deposit useful energy? | OPEN |
| G3 | Maximum SM deposited solar-neutrino power? | OPEN — flux/spectra/matter/MSW/Ga response validated; oscillated Ga total + Cl + W/kg missing |
| G4 | Can resonance/polarization/periodicity increase useful deposition parametrically? | OPEN |
| G5 | Minimal BSM structure if SM ceiling insufficient? | LOCKED until G3 |
| G6 | Does BSM survive constraints? | LOCKED until G5 |
| G7 | Can known production/decay identify strong inverse capture? | PARTIAL PASS — measured-ft route validated |
| G8 | Can resonance beat source bandwidth under integrated-strength bounds? | OPEN |
| G9 | Can finite gravitational lensing give useful gain? | OPEN |
| G10 | Can staggered/multi-isotope stacks beat same atoms at fixed mass column? | OPEN |

## Chronology

- `0001` CEvNS/magnetic/coherence gates.
- `0002` production↔absorption and spin triage.
- `0003` inverse-transition seeds; Ga historical normalization/W/kg gap.
- `0004` gravitational focusing.
- `0005` staggered-layer metamaterial.
- `0006` ft→capture; tritium reproduced.
- `0007` B16 integrated flux freeze.
- `0008` pinned spectral manifest + oscillation convention.
- `0009` exact spectrum materialization.
- `0010` B16 matter source freeze.
- `0011` exact B16 matter materialization/parse + prospective MSW kernel.
- `0012` prospective MSW CI + exact B16 component survival PASS.
- `0013` Bahcall Ga-71 response freeze + prospective source-average reconstruction PASS; non-scientific row-count CI defect repaired.

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
10. Representative `P_ee(E)` checkpoints do not replace continuum spectral folding.
11. The Ga response gate validates nuclear/spectral interpolation identity, not yet the oscillated solar Ga rate.

## Current maturity

**NMIR_READINESS: 29%**.

Increase `27% -> 29%` is credited only to the newly validated, reusable Ga-71 energy response and prospective source-average reconstruction gate. The repaired row-count CI defect earns no readiness credit.

## Exact next gate

1. Build full component-specific `Pee(E)` arrays from the validated B16 production distributions.
2. Fold `B16 flux × pinned spectral shape × Pee(E) × Ga71 sigma(E)` for GS98 and AGSS09met, including Be7/pep line treatment.
3. Record component and total oscillated Ga SNU prospectively and compare against an authoritative modern/reference calculation without retuning.
4. Freeze/reproduce Cl-37 response and repeat the folding.
5. Convert validated capture/deposition to W/kg and advance quantitative G3.
6. Parallel non-biasing work: resonance integrated-strength gate, sum-rule axial response, transparent-Sun benchmark, staggered fixed-mass-column comparison.
