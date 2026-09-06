# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Mission and frozen accounting
Reconstruct the low-energy neutrino↔matter interface; distinguish detection/state control from irreversible neutrino-sourced energy deposition; establish a quantitative Standard-Model ceiling before opening BSM solution-building.

Central accounting:
\[
P_{dep}=N_T\int dE\,\mu(E,\mathbf x)\Phi(E)\sigma(E)E_{dep}(E).
\]
For G3, every successful reaction is credited at most the incident neutrino energy: `E_dep,nu <= E_nu`. Daughter-decay energy, nuclear-mass release, target preparation/external energy and incomplete/extra thermalization are never counted as neutrino-supplied power.

## Frozen baseline authority
- Xe-132 ideal CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; Xe-like mean free path `~3.08e16 m`.
- Minimal Dirac magnetic-moment benchmark (`m_nu=0.05 eV`): `~1.6e-20 mu_B`; ideal 1-m spin-precession maximum `~3.35e17 T`.
- Tritium measured-ft capture: `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fluxes; pinned pp/hep/B8/CNO spectra; thermally broadened Be7 profiles; daytime adiabatic three-flavour MSW with `sin^2 theta12=0.307`, `sin^2 theta13=0.0220`, `Delta m^2_21=7.53e-5 eV^2`, normal ordering, Earth regeneration OFF.

## G3 validated target ledger
Detailed authority: `research/sm_power_ledger.md`.

| target / B16 branch | capture [SNU] | energy moment [SNU MeV] | mean captured Eν [MeV] | pure-isotope ceiling [W/kg] |
|---|---:|---:|---:|---:|
| **7Li / GS98** | **19.34881333** | **77.50707776** | **4.00577939** | **1.06589117e-21** |
| 7Li / AGSS09met | 16.84165298 | 65.03364861 | 3.86147658 | 8.94354349e-22 |
| 82Se / GS98 | 355.03190979 | 249.61364032 | 0.70307382 | 2.94006655e-22 |
| 82Se / AGSS09met | 345.60519781 | 226.65979252 | 0.65583444 | 2.66970537e-22 |
| 71Ga / GS98 | 65.00993895 | 75.78103575 | 1.16568385 | 1.03091848e-22 |
| 71Ga / AGSS09met | 62.31786849 | 66.37456240 | 1.06509680 | 9.02953653e-23 |
| 37Cl / GS98 | ~3.02 | ~22.65 | ~7.50 | ~5.91e-23 |
| 37Cl / AGSS09met | ~2.56 | ~18.77 | ~7.33 | ~4.90e-23 |

Current individually validated leader is pure `7Li/GS98 = 1.06589117e-21 W/kg`; natural Li gives `9.95777156e-22 W/kg`. The leader remains `~9.38e20` below `1 W/kg`.

### Target authorities
- **71Ga:** Bahcall, Phys. Rev. C 56, 3391 (1997); full B16×spectrum×MSW fold PASS; power run `34028394336`, artifact `9987793879`.
- **37Cl:** Bahcall et al., Phys. Rev. C 54, 411 (1996), with source-average Be7 authority; power run `34031200366`, artifact `9988653883`; sub-1-MeV residual changes power only ~0.05%.
- **82Se:** Frekers et al., Phys. Rev. C 94, 014614 (2016). Point-Coulomb pp approximation scientific FAIL (`-32.6%`, run `34032960415`); relativistic finite-size repair PASS (`-0.453%`, run `34033049596`); nine-component response validation PASS (`34033182939`); repaired B16+MSW fold PASS (`34033368287`, artifact `9989345911`).
- **7Li:** evaluated Be7 EC ground-state seed + independently authorized 429-keV excited state. Matched-B8 validation PASS (`34037499594`, artifact `9990627394`; total residual `+1.454%`). Validated B16+MSW fold `34037570254`, artifact `9990650435`. GS98 pure Li7 `1.06589117e-21 W/kg`; B8 dominates energy moment despite modest event count.

## Passive leading-allowed target-space upper bound — iteration 0024
Prospective contract: `research/passive_allowed_bound_prereg.md`, commit `88bf3a6718122a354f6bada3ad2fb43d58371392`.

For attractive point-Coulomb `F_pc=x/(1-exp(-x))`, `x=2*pi*alpha*Z_f*E/p`, `exp(x)>=1+x` yields

`p E F_pc <= (1+2*pi*alpha*Z_f) E^2`.

Correlation-independent one-body operator-norm caps:

`S_F<=A^2`, `S_GT<=3A^2`, hence `S_allowed<=A^2(1+3 g_A^2)`.

The maximization intentionally grants `A<=300`, daughter `Z_f<=119`, zero threshold/excitation, `E_nu<=20 MeV`, artificial neutrino energy flux `2000 W/m^2`, +2% target-count safety, plus a separately labeled `x1e6` omitted-physics stress diagnostic.

Hosted authority: run `34038214660`, job `101500085408`, artifact `9990839187`, ZIP SHA256 `f9e544b9aa5372f8e286e8214f2eba422f35cc8e02468501babc99cfcbbc8642`; six tests PASS; same-head baseline CI `34038214654` SUCCESS.

| quantity | result |
|---|---:|
| analytic leading-allowed envelope | **`9.419449302949355e-12 W/kg`** |
| deficit to 1 W/kg | `1.0616331888e11` |
| x1e6 stressed diagnostic | **`9.419449302949354e-6 W/kg`** |
| stressed deficit to 1 W/kg | `1.0616331888e5` |
| classification | **STRONG_NEGATIVE_SCOPED** |

Scope: leading allowed one-body Fermi/GT passive nuclear response in the stated target/solar-energy domain. The x1e6 diagnostic is not a proof for other operators.

## G8 integrated resonance-strength / spectral-overlap formal gate — iteration 0025
Prospective contract: `research/resonance_overlap_prereg.md`, commit `31bd2467140cdfcfeede18de115934904849eb3d`.

Ordinary continuum `nu+A -> B*+e-` capture is not automatically a narrow incident-energy resonance because the outgoing electron carries variable kinetic energy. For genuine isolated resonances, the frozen Breit-Wigner convention gives

`I_sigma = integral sigma(E)dE = 2*pi^2/k_r^2 * g * Gamma_in * Gamma_out/Gamma`

and therefore

`I_sigma <= 2*pi^2/k_r^2 * g * Gamma_in`.

For non-negative source flux/profile:

`R_per_target <= sup(phi) * I_sigma`, `sigma_avg <= ||rho||_infinity * I_sigma`.

Hosted authority: run `34038642747`, job `101501241557`, artifact `9990968127`, ZIP SHA256 `db13ac11dbd5cba7aaa76465987265c710dd64ff10cea28617edd9c298d239c5`; same-head baseline CI `34038642903` SUCCESS.

| diagnostic | result |
|---|---:|
| widths tested | `1e-3 ... 1e-15` |
| max numeric area relative error | `6.3661977016e-5` |
| fixed-branch area invariance error | `0.0` |
| peak gain after 1e6 narrowing | `1e6` |
| max source-overlap / supremum bound | `0.8797668563` |
| status | **G8_FORMAL_PASS** |

Peak-only resonance ranking is forbidden. A resonant target requires measured/evaluated weak `Gamma_in` (or equivalent ft/decay strength), branching, environmental/recoil-free factor if applicable, and a physical solar source profile. Current bookkeeping-only delta-like pep convention is not G8 resonance authority.

## Finite-q leading-current multipole envelope — iteration 0026
Prospective contract: `research/finite_q_multipole_prereg.md`, commit `c3a29bc01b2af4f68ca1a6cf55447c6200e28c81`.

The standard CC multipole decomposition contains Coulomb `M_J`, longitudinal `L_J`, transverse-electric `T_J^el`, and transverse-magnetic `T_J^mag` sectors. Bounding angular coefficients/interferences gives a conservative raw ratio `24*pi≈75.398` relative to the allowed normalization; a larger frozen factor `128` was preregistered before execution.

For leading finite-q currents

`J_V^0(q) ~ sum_i tau_i^+ exp(i q·r_i)`, `J_A(q) ~ g_A sum_i tau_i^+ sigma_i exp(i q·r_i)`,

the unit-modulus phase leaves the operator-norm caps unchanged. Therefore

`P_finite_q_leading <= 128 * P_allowed_0024`.

Convection/recoil current, axial charge, weak magnetism, induced pseudoscalar and nuclear-relativistic corrections are **not** claimed as rigorously included. A separately preregistered `x1e6` cross-section multiplier probes them only as a non-theorem stress diagnostic.

Hosted authority: run `34038882486`, job `101501885143`, artifact `9991038179`, artifact ZIP SHA256 `d281d3057ce5976545fda62888395a95cf6acfc183e2b64999dfb0c8b849f89f`; four dedicated tests PASS; same-head baseline CI `34038882497` SUCCESS. Raw JSON inspected before classification.

| quantity | result |
|---|---:|
| inherited allowed envelope | `9.419449302949355e-12 W/kg` |
| raw angular factor `24*pi` | `75.39822368615503` |
| frozen safety factor | `128` |
| **finite-q leading envelope** | **`1.2056895107775174e-9 W/kg`** |
| deficit to 1 W/kg | **`8.2940092873e8`** |
| separate subleading-current stress | `1e6` |
| x1e6 stressed diagnostic | **`1.2056895107775173e-3 W/kg`** |
| stressed deficit to 1 W/kg | **`829.4009287`** |
| leading classification | **FINITE_Q_LEADING_STRONG_NEGATIVE** |
| stress classification | **MILLIONFOLD_SUBLEADING_STRESS_NEGATIVE** |

Scientific interpretation: finite-q redistribution among leading vector-charge/axial-spin Coulomb/longitudinal/transverse multipoles cannot rescue passive solar-neutrino power. Even a separate millionfold stress on omitted subleading one-body-current cross section remains only ~1.2 mW/kg. That last statement is robustness evidence, not a proof for the omitted operators.

Detailed record: `research/iterations/0026_finite_q_leading_multipole_envelope.md`.

## 115In screening status
Provisional one-state model (`threshold≈0.114 MeV`, `B(GT)=0.17`) run `34032630382`, artifact `9989115502`. No-osc GS98 `~371.7 SNU` versus historical full-response `~750 SNU`: scientific FAIL as complete response. Precision In115 remains open only with a fuller primary response.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS — CEvNS, tritium-ft, Ga, Cl, Se82, validated two-state Li7 |
| G1 static macroscopic coherence | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 many-body deposited-energy channels | OPEN |
| G3 maximum SM deposited solar-neutrino power | **PARTIAL PASS — four validated targets; leading allowed + leading finite-q multipole classes STRONG NEGATIVE; subleading full-current/resonant/collective/focusing loopholes remain** |
| G4 engineered resonance/polarization/periodicity | OPEN |
| G5 minimal BSM solution | LOCKED until remaining G3 loopholes close |
| G6 BSM constraints | LOCKED until G5 |
| G7 production/decay → inverse capture | PARTIAL PASS — measured-ft route + Li7 two-state validation |
| G8 resonance integrated-strength/bandwidth | **PARTIAL PASS — formal area/overlap gate PASS; target-specific Gamma_in + real solar-profile W/kg bound open** |
| G9 finite gravitational focusing gain | OPEN |
| G10 staggered/multi-isotope fixed-mass-column gain | OPEN |

## Critical scope guards
1. Detector threshold != total cross section.
2. Directional coherence != integrated opacity.
3. Peak resonance != flux-integrated capture.
4. Ordinary discrete-state CC capture with continuum outgoing electron is not automatically an incident-energy resonance.
5. Gravitational magnification is finite and multiplicative.
6. Projected atomic coverage != neutrino opacity.
7. Exact time reversal and crossed weak processes must be classified correctly.
8. Never mix solar flux/spectrum/matter/oscillation/nuclear conventions silently.
9. Green workflow != scientific PASS until raw result and frozen gate are inspected.
10. Daughter decay or target nuclear-mass energy must never be counted as neutrino-supplied energy.
11. A few-target maximum is not a global SM ceiling.
12. Negative approximations and infrastructure failures remain separately recorded; gates are never loosened after results.
13. A crossed ground-state ft response is not automatically a complete multi-state target response.
14. Iteration 0024 is scoped to leading long-wavelength Fermi/GT; iteration 0026 extends only leading vector-charge + axial-spin finite-q multipoles.
15. The x1e6 subleading-current diagnostic in iteration 0026 is explicitly not a theorem.
16. G8 formal PASS does not replace target-specific entrance-width and solar-profile authority.

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered metamaterial; `0006` ft→capture; `0007–0012` B16 flux/spectra/matter/MSW; `0013–0014` Ga; `0015–0017` Cl; `0018` Ga power; `0019` Cl power; `0020` In115 screen + Se82 pivot; `0021` Se82 authority; `0022` Li7 gs screen; `0023` Li7 two-state authority; `0024` passive leading-allowed target-space bound; `0025` G8 integrated resonance-overlap formal pass; `0026` finite-q leading-current multipole envelope.

## Current maturity
**NMIR_READINESS: 50%** (audit estimate).

Increase from 48% to 50% is credited for a prospectively frozen, hosted/raw-inspected finite-q class-level bound that closes the leading vector-charge/axial-spin multipole loophole beyond the allowed q->0 limit. No rigorous credit is assigned for omitted subleading one-body current operators, target-specific resonances, collective response or focusing.

## Exact next gates
1. **Full one-body current norm:** independently bound convection/recoil, axial-charge, weak-magnetism and induced-pseudoscalar operators over `E_nu<=20 MeV`; either obtain a rigorous aggregate factor over iteration 0026 or retain them as an explicit open loophole.
2. **G8 quantitative completion:** select genuine resonant inverse channels with measured weak decay/ft authority; derive `Gamma_in`; convolve with frozen Be7/continuum profiles. Freeze a physical pep line profile before any pep resonance test.
3. **G2 many-body:** implement the sum-rule-preserving spin/magnon response toy and compare energy-weighted response with the single-particle nuclear envelope.
4. **G9/G10:** reproduce transparent-Sun finite-source/Liouville focusing and fixed-mass-column staggered/multi-isotope controls.
