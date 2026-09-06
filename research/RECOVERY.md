# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Mission
Reconstruct the low-energy neutrino↔matter interface, distinguish state control/detection from irreversible energy deposition, establish a quantitative Standard-Model ceiling, and only then open BSM model-building as a solution branch.

Frozen organizing principles: response reconstruction; production↔absorption/crossed weak channels; finite gravitational focusing; staggered-layer/multi-isotope response engineering.

Central objective:

\[
P_{dep}=N_T\int dE\,\mu(E,\mathbf x)\Phi(E)\sigma_{cap}(E)E_{dep}(E).
\]

Useful capture requires finite flux gain × real interaction probability × deposited-energy fraction.

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
Tritium gives `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of the published `7.84e-45 cm^2` benchmark. Authoritative CI: run `34004890286`, job `101410168170`.

### B16 solar flux / spectra / matter
- `data/solar_flux_b16.csv`: B16-GS98 and B16-AGSS09met integrated fluxes; CI `34007336474` SUCCESS.
- `data/solar_spectrum_manifest.csv`: pinned pp/hep/B8/CNO and thermally broadened Be7 spectra by exact upstream commit + Git-blob SHA.
- Exact spectrum materialization: run `34012460541`, job `101430502114`, artifact `9982880231`, ZIP SHA256 `c506de14cf1c0f0d02c706143449ae4a2fea887195f41de66763651e4f65cda6`; same-head CI `34012460563`.
- B16 matter exact blobs: GS98 `f73c47cf6f2d77086634a5c180b50039e10805e7`; AGSS09met `d9bd29f3374c63e8ea898733a55fb7aa566a2c96`.
- Matter loader CI `34012590342`; exact materialization/parse run `34014923087`, artifact `9983598047`, SHA256 `9b7baa133f74d616b62e158c27de71984ff025b209639a46c423f73acfc7c1e9`.
- Both B16 tables: 1000 rows over `r/Rsun=0.0005...0.5`; all eight production distributions normalize to unity within ~`8e-5` on native-grid trapezoidal quadrature.

Solar flux identity: PASS. Spectral identity/materialization: PASS. Matter identity/materialization/production normalization: PASS.

### Frozen oscillation convention + exact B16 survival
`data/solar_oscillation_convention.csv`: `sin^2(theta12)=0.307`, `sin^2(theta13)=0.0220`, `Delta m^2_21=7.53e-5 eV^2`, normal ordering, day-side adiabatic three-flavour MSW, Earth regeneration OFF.

\[
P_{ee}=c_{13}^4\frac{1+\cos2\theta_{12}\cos2\theta_{12}^m}{2}+s_{13}^4.
\]

Prospective numerical-limit CI `34014950750`; exact B16 survival run `34015021346`, artifact `9983624802`, SHA256 `09cd10d0530723646dce465f3b965796624cc03ce1070a81556f374ebb7b5d50`.
Representative GS98 values: `Pee(pp,0.300)=0.544186`, `Pee(Be7,0.862)=0.526972`, `Pee(pep,1.442)=0.516871`, `Pee(B8,5)=0.393449`, `Pee(B8,10)=0.327017`. GS98/AGSS09 survival differences are only `~1e-4...1e-3` absolute at these checkpoints.

Prospective MSW kernel: PASS within frozen approximation. Exact component survival benchmark: PASS.

### Ga-71 response identity — iteration 0013
Primary response source: J. N. Bahcall, Phys. Rev. C 56, 3391 (1997).
- `data/ga71_bahcall1997_response.csv`: 58 energies, `0.240...30 MeV`, best and ±3σ branches.
- Hosted source-average benchmark run `34017366528`, job `101443416887`, artifact `9984322724`, ZIP SHA256 `fc162d6807a3f087aaf8086c6558d16e1c1358f497fc751b48cb6d97d66a0f4f`.
- Source-average relative errors versus Bahcall: pp 0.205%, pep 0.796%, Be7 0.022%, N13 0.085%, O15 0.161%, F17 0.581%.
- Row-count CI defect was infrastructure-only and repaired without physics changes; validated subsequent baseline CI.

Ga-71 energy-response identity: PASS. Standard-spectrum source-average reconstruction: PASS.

### Full oscillated Ga-71 solar folding — iteration 0014
New reusable engine: `src/nmir/ga71_solar_fold.py`; hosted script/workflow and zero-endpoint regression tests included.

First run `34020172203`, job `101451164446`, head `9236a23c4e7a619408804f6380a7466c91ab2053` FAILED before a scientific result because a valid continuum table includes `E=0` while `Pee(0)` is undefined. Since `sigma_Ga(0)=0`, this endpoint contributes exactly zero. Classification: infrastructure/numerical-boundary FAIL, not scientific FAIL.

Repair commit `a5b6d2a109fe39695f421ecc455026c9c0f92c94`: skip Pee evaluation at exactly zero capture contribution and cache immutable production weights/oscillation constants. No flux, spectrum, MSW convention, nuclear response or branching weight changed. Regression commit `382024af46534e4332d79d33896064480f7339a3`; baseline CI run `34020276133`, job `101451443326`: **74 passed**.

Authoritative scientific fold: run `34020272911`, job `101451434118`, head `a5b6d2a109fe39695f421ecc455026c9c0f92c94`, artifact `9985246195`, ZIP SHA256 `aafe91e60b19a91845988d4f87ec45dd769ed57ca0529d342bf5dd93435f750a`, SUCCESS.

Oscillated Ga-71 rates in SNU:

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

Metallicity dependence of the total is `~2.69 SNU`, dominated by source-flux differences (especially Be7/B8/CNO), consistent with the already-small GS98/AGSS09 differences in Pee itself.

A 2026 PTEP radiochemical Ga/Cl analysis by Ishidoshiro & Tachibana, published 18 March 2026, was frozen before output inspection as an independent post-result cross-check source because it explicitly uses both B16-GS98 and B16-AGSS09met. It was not used to tune NMIR.

Full component-specific B16 × spectrum × production-averaged MSW × Ga response folding: **PASS**. External modern component/total numerical comparison remains to be extracted explicitly, so this is a strong partial G3 pass rather than final Ga closure.

## Other active branches

### Many-body/spin response
\[
\Gamma\propto\int d^3q\,d\omega\,L_{ab}S^{ab}.
\]
A 1-meV magnon produced by a 1-MeV neutrino deposits only `1e-9` of incident energy. Detection interest does not imply useful energy capture.

### Gravitational focusing
Weak-field solar-limb benchmark `~547.741 AU`; transparent-Sun literature benchmark near `23.5 ± 0.1 AU` for distant-source neutrinos. Finite source/receiver size and Liouville conservation are mandatory.

### Staggered-layer metamaterial
At `E_nu=1 MeV`, `lambda≈1.23984e-12 m`; for `d=3 Å`, first-order Bragg angle `~0.118396 deg`. Any claimed gain must survive angle/energy integration at fixed mass column.

## Research gates
| Gate | Question | Status |
|---|---|---|
| G0 | Known weak/CEvNS/capture normalizations reproduced? | PARTIAL PASS — CEvNS + tritium ft + Ga response/source averages |
| G1 | Static macroscopic coherence beyond nuclear coherence? | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 | Can many-body spin/density/current modes deposit useful energy? | OPEN |
| G3 | Maximum SM deposited solar-neutrino power? | OPEN — full oscillated Ga fold PASS; Cl + W/kg + final ceiling missing |
| G4 | Can resonance/polarization/periodicity increase useful deposition parametrically? | OPEN |
| G5 | Minimal BSM structure if SM ceiling insufficient? | LOCKED until G3 |
| G6 | Does BSM survive constraints? | LOCKED until G5 |
| G7 | Can known production/decay identify strong inverse capture? | PARTIAL PASS — measured-ft route validated |
| G8 | Can resonance beat source bandwidth under integrated-strength bounds? | OPEN |
| G9 | Can finite gravitational lensing give useful gain? | OPEN |
| G10 | Can staggered/multi-isotope stacks beat same atoms at fixed mass column? | OPEN |

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravitational focusing; `0005` staggered metamaterial; `0006` ft→capture/tritium; `0007` B16 flux; `0008` spectra/oscillation freeze; `0009` spectrum materialization; `0010` B16 matter source; `0011` matter materialization/MSW kernel; `0012` MSW survival PASS; `0013` Ga response/source-average PASS; `0014` full oscillated Ga folding PASS after zero-endpoint infrastructure repair.

## Critical scope guards
1. Detector threshold is not total cross section.
2. Directional coherent gain is not integrated opacity gain.
3. Peak resonance is not flux-integrated capture.
4. Gravitational magnification is finite and multiplicative.
5. Projected atomic coverage is not neutrino opacity.
6. Exact time reversal and a crossed process are not automatically identical reactions.
7. Do not silently mix solar flux/spectrum/matter/oscillation/nuclear conventions.
8. BSM remains locked as a solution branch until G3 is quantitatively bounded.
9. No ad-hoc solar production radius/density when component-resolved B16 distributions exist.
10. Representative Pee checkpoints do not replace continuum folding.
11. A green workflow is not scientific PASS until raw results and frozen gates are inspected.

## Current maturity
**NMIR_READINESS: 31%**.

Increase `29% -> 31%` is credited only to the reusable, hosted, component-resolved full Ga-71 oscillated folding gate and its regression-protected boundary repair. No credit is assigned for the initial infrastructure failure itself.

## Exact next gate
1. Freeze/reproduce an authoritative energy-dependent `37Cl(nu_e,e-)37Ar` response with provenance and threshold `~0.814 MeV`.
2. Validate source-averaged Cl response before using solar output.
3. Fold B16 flux × pinned spectra × production-averaged Pee × Cl response for GS98 and AGSS09met.
4. Convert validated Ga+Cl capture/deposition to W/kg and advance the quantitative Standard-Model G3 ceiling.
5. In parallel, without tuning active results: resonance integrated-strength gate, sum-rule axial response, transparent-Sun `~23.5 AU`, staggered fixed-mass-column comparison.
