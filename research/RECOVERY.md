# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Funnel authority: `research/NMIR_FUNNEL.md`

## Mission and frozen accounting
Reconstruct the low-energy neutrino↔matter interface through a discovery funnel; distinguish state control/detection/focusing from true absorption and irreversible neutrino-sourced energy deposition; establish quantitative Standard-Model ceilings before opening BSM solution-building.

Central accounting:
\[
P_{dep}=N_T\int dE\,\mu(E,\mathbf x)\Phi(E)\sigma(E)E_{dep}(E).
\]
For G3, every successful reaction is credited at most the incident neutrino energy: `E_dep,nu <= E_nu`. Daughter-decay energy, nuclear-mass release, target preparation/external pumping energy and extra thermalization are never counted as neutrino-supplied power. Unvalidated gains are never multiplied.

## Frozen baseline authority
- Xe-132 ideal CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; Xe-like mean free path `~3.08e16 m`.
- Minimal Dirac magnetic-moment benchmark (`m_nu=0.05 eV`): `~1.6e-20 mu_B`; ideal 1-m spin-precession maximum `~3.35e17 T`.
- Tritium measured-ft capture: `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fluxes; pinned pp/hep/B8/CNO spectra; thermally broadened Be7 profiles; daytime adiabatic three-flavour MSW with `sin^2 theta12=0.307`, `sin^2 theta13=0.0220`, `Delta m^2_21=7.53e-5 eV^2`, normal ordering, Earth regeneration OFF.

## G3 individually validated target ledger
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

### Target authority summary
- **71Ga:** Bahcall PRC 56, 3391 (1997); full B16×spectrum×MSW fold PASS; power run `34028394336`, artifact `9987793879`.
- **37Cl:** Bahcall et al. PRC 54, 411 (1996), with source-average Be7 authority; power run `34031200366`, artifact `9988653883`.
- **82Se:** Frekers et al. PRC 94, 014614 (2016). Point-Coulomb pp approximation scientific FAIL `-32.6%` (`34032960415`); relativistic finite-size repair PASS `-0.453%` (`34033049596`); nine-component response validation PASS (`34033182939`); B16+MSW fold PASS (`34033368287`, artifact `9989345911`).
- **7Li:** evaluated Be7 EC ground-state seed + independently authorized 429-keV excited state. Matched-B8 validation PASS (`34037499594`, artifact `9990627394`; total residual `+1.454%`). B16+MSW fold `34037570254`, artifact `9990650435`.
- **115In:** provisional one-state response is scientific FAIL as a complete response: no-oscillation `~371.7 SNU` vs historical full-response scale `~750 SNU`; not G3 authority.

## Iteration 0024 — passive leading-allowed target-space bound
Prospective contract commit `88bf3a6718122a354f6bada3ad2fb43d58371392`.

Using `p E F_pc <= (1+2*pi*alpha*Z_f)E^2`, loose one-body caps `S_F<=A^2`, `S_GT<=3A^2`, and intentionally extreme `A<=300`, `Z_f<=119`, zero threshold/excitation, `E_nu<=20 MeV`, artificial neutrino energy flux `2000 W/m^2`:

- analytic leading-allowed envelope: **`9.419449302949355e-12 W/kg`**;
- deficit to 1 W/kg: `1.0616331888e11`;
- separately labelled x1e6 omitted-physics stress: `9.419449302949354e-6 W/kg`.

Hosted run `34038214660`, job `101500085408`, artifact `9990839187`. Classification: **STRONG_NEGATIVE_SCOPED** for leading allowed one-body Fermi/GT passive response.

## Iteration 0025 — G8 integrated resonance-strength / overlap
Prospective contract commit `31bd2467140cdfcfeede18de115934904849eb3d`.

For an isolated Breit-Wigner resonance,

`I_sigma = 2*pi^2/k_r^2 * g * Gamma_in*Gamma_out/Gamma <= 2*pi^2/k_r^2 * g * Gamma_in`.

Therefore line narrowing can raise `sigma_peak` without creating new integrated weak entrance strength. For non-negative source flux/profile: `R_per_target <= sup(phi) I_sigma`.

Hosted run `34038642747`, job `101501241557`, artifact `9990968127`: narrowing by `1e6` raised peak by `1e6` while fixed-branch integrated area remained invariant; **G8_FORMAL_PASS**. Target-specific `Gamma_in`, branching and real solar source profiles are still required before any resonant W/kg claim.

## Iteration 0026 — finite-q leading-current multipole envelope
Prospective contract commit `c3a29bc01b2af4f68ca1a6cf55447c6200e28c81`.

For leading vector-charge/axial-spin finite-q currents the phase `exp(i q·r_i)` does not enlarge the operator-norm caps. A preregistered safety factor 128 over iteration 0024 yields:

- **finite-q leading envelope `1.2056895107775174e-9 W/kg`**;
- deficit to 1 W/kg `8.2940092873e8`;
- separate x1e6 subleading-current stress `1.2056895107775173e-3 W/kg`, still factor `829.4` below 1 W/kg.

Hosted run `34038882486`, job `101501885143`, artifact `9991038179`. Classification: **FINITE_Q_LEADING_STRONG_NEGATIVE**. The x1e6 stress is robustness evidence, not a theorem for omitted currents.

## Two-body-current sensitivity map — open loophole diagnostic
`research/two_body_current_gap_map.md`, commit `e40759020746eca3a8a73439773d9ae0717b81c2`.

Conditional pair-current model gives `G_2body=[1+(A-1)r/2]^2`. With `A=300` and the iteration-0026 envelope, reaching 1 W/kg would require an individual pair-current norm ratio `r≈192.63` relative to the reference one-body current. Published few-body weak-current corrections are qualitatively far smaller, but this is **not an all-nucleus theorem** and receives no G3 closure credit. A current-algebra/chiral-EFT or inclusive one+two-body sum-rule bound remains open.

## Iteration 0027 — passive density-response f-sum gate
Prospective contract: `research/density_fsum_prereg.md`, commit `0fbc3f1977630add7eb15896f7da2458742e8df7`.

For coordinate-local passive nonrelativistic density response,

`rho_q = sum_i g_i exp(i q·r_i)`,

`m1(q)=integral_0^infinity dω ω S(q,ω)=q^2/2 * sum_i g_i^2/m_i`.

Thus for any non-negative bounded kernel `K<=Kmax`,

`D(q)=integral dω ω K S <= Kmax*m1(q)`.

Hosted authority: run `34039755966`, job `101504245884`, head `1b1b4c388648d5f0ee75b96bd0cb61c283ae9863`, artifact `9991299921`, ZIP SHA256 `064566b0bf75040f35c0308f0b8fe53103e995a175ce5c06bb6d694467cde6be`. Raw log inspected; **5 tests PASS**.

| diagnostic | result |
|---|---:|
| max `m1` relative error | `0.0` |
| max unit-kernel deposition error | `1.7985613162596616e-16` |
| max `D/(Kmax*m1)` | `0.9999999995` |
| unweighted gain from lowering one collective mode by 1e6 | **`1.0e6`** |
| corresponding energy-weighted gain | **`1.0`** |
| f-sum gain from `N=1` to `N=1e6` | `999999.9999999999` |

Classification: **PASS_DENSITY_FSUM / STRONG-NEGATIVE scoped against superextensive energy-weighted density engineering**. Passive phonon/crystal/staggered-density structure can redistribute/directionally concentrate response and improve detectability, but cannot manufacture extra integrated energy-weighted density strength from the same constituents under the stated Hamiltonian assumptions. Spin/axial, charged-current transmutation, nonlocal/active media, two-body currents, gravity and BSM are explicitly outside this gate.

Detailed record: `research/iterations/0027_density_fsum_gate.md`.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS — CEvNS, tritium-ft, Ga, Cl, Se82, validated two-state Li7 |
| G1 static macroscopic coherence | PARTIAL NEGATIVE — naive N² opacity disfavored; density energy-weighted N² rescue now additionally constrained by f-sum |
| G2 many-body deposited-energy channels | **PARTIAL PASS/NEGATIVE — passive coordinate-local density branch class-bounded; spin/axial/magnon branch OPEN** |
| G3 maximum SM deposited solar-neutrino power | **PARTIAL PASS — validated targets + leading allowed/finite-q class bounds; subleading/two-body/resonant/spin/focusing loopholes remain** |
| G4 engineered resonance/polarization/periodicity | OPEN — density-only spectral rearrangement cannot create new energy-weighted strength; spin/polarization remains open |
| G5 minimal BSM solution | LOCKED until remaining G3 loopholes close |
| G6 BSM constraints | LOCKED until G5 |
| G7 production/decay → inverse capture | PARTIAL PASS — measured-ft route + Li7 two-state validation |
| G8 resonance integrated-strength/bandwidth | PARTIAL PASS — formal area/overlap gate PASS; target-specific entrance strength + real source profile open |
| G9 finite gravitational focusing gain | OPEN |
| G10 staggered/multi-isotope fixed-mass-column gain | **PARTIAL NEGATIVE — density-response energy gain constrained by f-sum; directional/CC/multi-isotope fixed-column tests remain open** |

## Critical scope guards
1. Detector threshold != total cross section; event-count gain != deposited-energy gain.
2. Directional coherence != integrated opacity.
3. Peak resonance != flux-integrated capture.
4. Ordinary CC capture with continuum outgoing electron is not automatically an incident-energy resonance.
5. Gravitational magnification is finite and multiplicative.
6. Projected atomic coverage != neutrino opacity.
7. Exact time reversal/crossing must be classified correctly.
8. Never mix solar flux/spectrum/matter/oscillation/nuclear conventions silently.
9. Green workflow != scientific PASS until raw result and frozen gate are inspected.
10. Daughter decay/nuclear-mass/external pumping energy is not neutrino-supplied energy.
11. A few-target maximum is not a global SM ceiling.
12. Negative approximations and infrastructure failures remain recorded; gates are never loosened after results.
13. A crossed ground-state ft response is not automatically a complete multi-state response.
14. Iteration 0024 covers leading q->0 Fermi/GT; iteration 0026 extends only leading vector-charge/axial-spin finite-q multipoles.
15. Iteration 0027 covers coordinate-local passive density response only; it must not be used as a spin/axial theorem.
16. Unvalidated channel gains are never multiplied in F9.

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered metamaterial; `0006` ft→capture; `0007–0012` B16 flux/spectra/matter/MSW; `0013–0014` Ga; `0015–0017` Cl; `0018` Ga power; `0019` Cl power; `0020` In115 screen + Se82 pivot; `0021` Se82 authority; `0022` Li7 gs screen; `0023` Li7 two-state authority; `0024` passive leading-allowed bound; `0025` G8 formal resonance gate; `0026` finite-q leading multipole envelope; `0027` density-response f-sum gate.

## Current maturity
**NMIR_READINESS: 52%** (audit estimate).

Increase from 50% to 52% is credited only for the prospectively frozen, hosted/raw-inspected density-response class gate. No readiness credit is assigned to the conditional two-body sensitivity map. The density result narrows G2/G10 but does not close spin/axial, subleading/two-body nuclear currents, target-specific resonance, gravity or active/nonlocal media.

## Exact next funnel gates
1. **G2 spin/axial many-body gate:** derive and implement an energy-weighted spin-response sum-rule/toy with explicit Hamiltonian dependence; test whether magnon/collective spin modes can raise neutrino-supplied energy deposition rather than only unweighted event strength.
2. **Full nuclear-current loopholes:** seek an inclusive/current-algebra or chiral-EFT bound covering convection/recoil, axial charge, weak magnetism, induced pseudoscalar and genuine two-body currents over `E_nu<=20 MeV`.
3. **G9 gravity:** reproduce transparent-Sun `~23.5 AU` focusing and impose finite-source/Liouville gain before any composition with capture.
4. **G10 structured matter:** fixed-mass-column angle+solar-spectrum comparison for staggered/multi-isotope stacks; density-only energy gain is already constrained, so surviving claims must be directional, charged-current/isotope-selective or outside the density f-sum assumptions.
5. **G8 target-specific resonance:** only candidates with measured/evaluated entrance strength and physical solar line/continuum profile may be ranked.