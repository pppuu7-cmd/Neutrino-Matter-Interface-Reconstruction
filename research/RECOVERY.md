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
For G3, every capture is credited at most the incident neutrino energy: `E_dep,nu <= E_nu`. Daughter-decay energy, nuclear-mass release, target preparation energy and incomplete/extra thermalization are never counted as neutrino-supplied power.

## Frozen baseline authority
- Xe-132 ideal CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; Xe-like mean free path `~3.08e16 m`.
- Minimal Dirac magnetic moment benchmark (`m_nu=0.05 eV`): `~1.6e-20 mu_B`; ideal 1-m spin-precession maximum `~3.35e17 T`.
- Tritium measured-ft capture: `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fluxes; pinned pp/hep/B8/CNO spectra; thermally broadened Be7 profiles; daytime adiabatic three-flavour MSW with `sin^2 theta12=0.307`, `sin^2 theta13=0.0220`, `Delta m^2_21=7.53e-5 eV^2`, normal ordering, Earth regeneration OFF.

## G3 validated target ledger
Authoritative table: `research/sm_power_ledger.md`.

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

Current validated passive-target leader is pure `7Li/GS98 = 1.06589117e-21 W/kg`, about `3.63x` the previous pure-82Se leader. Natural Li gives `9.95777156e-22 W/kg`. The leader is still `~9.38e20` below `1 W/kg`. This is a four-target benchmark, **not** a global all-nuclei SM theorem.

### 71Ga authority
Bahcall, Phys. Rev. C 56, 3391 (1997). Full B16×spectrum×MSW fold PASS. Power authority run `34028394336`, artifact `9987793879`.

### 37Cl authority
Bahcall et al., Phys. Rev. C 54, 411 (1996), with source-average Be7 authority. Power run `34031200366`, artifact `9988653883`; sub-1-MeV residual changes power by only ~0.05%.

### 82Se authority — iterations 0020/0021
Frekers et al., Phys. Rev. C 94, 014614 (2016), measured `82Se(3He,t)82Br` GT response.
- Point-Coulomb pp check: scientific FAIL, `-32.6%`, run `34032960415`.
- Relativistic finite-size repair, unchanged 15% gate: PASS, residual `-0.453%`, run `34033049596`.
- Full measured/binned response: nine source-average controls PASS, run `34033182939`.
- First full fold `34033250446`: infrastructure FAIL only (`Pee(0)` at zero-weight endpoint); regression added.
- Repaired B16+MSW fold PASS: `34033368287`, job `101486927672`, artifact `9989345911`; baseline CI after promotion `34033479337` SUCCESS.
- GS98 pure power `2.94006655e-22 W/kg`; natural selenium `2.66241785e-23 W/kg`.

## 7Li validated authority — iterations 0022/0023
### Ground-state seed
Evaluated `7Be(gs,3/2-) -> 7Li(gs,3/2-)` EC: `Q_EC=861.815 keV`, branch `89.56%`, `log ft=3.324`. Ground-only hosted screen `34034095803`, artifact `9989580600`, produced `7.49107965e-22 W/kg` pure Li7 but remained non-authoritative pending a complete response.

### Two-state completion and external validation
Iteration 0023 adds the independently authorized first `7Be` excited state (`429 keV`, threshold `~1.291 MeV`) using allowed strengths `B(F)_gs=1`, `B(GT)_gs=1.19`, `B(GT)_ex=1.06`, `g_A/g_V=1.2723`. Ground normalization remains fixed by the evaluated log-ft; the excited contribution uses only the measured strength ratio and shifted phase space. No published neutrino cross section is used to tune the model.

Prospective matched-B8 controls were frozen before hosted execution:
- published ground `2.470e-42 cm^2`;
- excited `1.289e-42 cm^2`;
- total `3.759e-42 cm^2`;
- component tolerance `12%`, total tolerance `10%`.

Initial run `34037418081`, job `101497916296`: **INFRASTRUCTURE FAIL only** — `pytest` absent, scientific calculation never ran. Minimal repair commit `5b9728b8f9d2159e291f2e35e4460d43846a1463` changed dependency setup only.

Repaired validation `34037499594`, job `101498137412`: scientific PASS after raw-log inspection:
- ground `2.50624405e-42`, residual `+1.467%`;
- excited `1.30740265e-42`, residual `+1.428%`;
- total `3.81364669e-42`, residual `+1.454%`.
Artifact `9990627394`, SHA256 `a3ecbf1d489c215576b9e7b99c3ae7017509070c77104aa4a7265576246e9eb6`.

Full B16+MSW fold was launched only after validation PASS. Run `34037570254`, job `101498329856`, head `c826fc69429589744996132d03aa462eb148fa4c`, artifact `9990650435`, SHA256 `320331ff1d3c068d78a27ff09d61a0e07965ff6ef7f2884d940fc7f214fb41cd`.

GS98+MSW:
- `19.3488133336 SNU`;
- `77.5070777600 SNU MeV`;
- pure Li7 `1.06589117436e-21 W/kg`;
- natural Li `9.95777155992e-22 W/kg`.
B8 contributes `7.24140 SNU` but `62.60901 SNU MeV`, so the new W/kg leader is driven by low target mass plus the high-energy tail, not by the largest event rate.

AGSS09met+MSW: `16.8416529756 SNU`, `65.0336486081 SNU MeV`, pure Li7 `8.94354349192e-22 W/kg`.

**Classification: Li7 target gate PASS; promoted to validated G3 ledger.** Near-threshold atomic/screening refinements remain a precision issue, but they cannot erase the matched B8 external validation and do not dominate the energy moment.

## 115In screening status
Provisional one-state model (`threshold≈0.114 MeV`, `B(GT)=0.17`) run `34032630382`, artifact `9989115502`. No-osc GS98 `~371.7 SNU` versus historical full-response `~750 SNU`: **scientific FAIL as a complete response**. Its GS98+MSW pure screen `~8.32e-23 W/kg` is below Ga; precision In115 remains open only with a fuller primary response.

## Other active branches
- G2 many-body/spin: magnons may aid detection/state control but are poor energy carriers; sum-rule-preserving response toy still open.
- G8 resonance: no peak cross section may enter G3 ranking until integrated strength, linewidth and solar-spectrum-overlap gates are implemented.
- G9 gravity: solar-limb weak-field focus `~547.741 AU`; transparent-Sun literature target `~23.5±0.1 AU`; finite-source/Liouville gain open.
- G10 staggered/metamaterial: Bragg kinematics possible; fixed-mass-column angle/energy-integrated gain unproven.
- G5/G6 BSM remain locked until G3 is broader and a passive-SM ceiling/no-go is defensible.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS — CEvNS, tritium-ft, Ga, Cl, measured-GT Se82, externally validated two-state Li7 |
| G1 static macroscopic coherence | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 many-body deposited-energy channels | OPEN |
| G3 maximum SM deposited solar-neutrino power | **PARTIAL PASS — four validated targets; Li7 validated leader; global target-space ceiling open** |
| G4 engineered resonance/polarization/periodicity | OPEN |
| G5 minimal BSM solution | LOCKED until G3 |
| G6 BSM constraints | LOCKED until G5 |
| G7 production/decay → inverse capture | PARTIAL PASS — measured-ft route validated; Li7 crossed response now externally validated through two states |
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
8. Green workflow ≠ scientific PASS until raw result and frozen gate are inspected.
9. Daughter decay or target nuclear-mass energy must never be counted as neutrino-supplied energy.
10. A few-target maximum is not a global SM ceiling.
11. Negative approximations and infrastructure failures remain separately recorded; acceptance gates are never loosened after results.
12. A directly crossed ground-state ft response is not automatically a complete multi-state target response.

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered metamaterial; `0006` ft→capture; `0007–0012` B16 flux/spectra/matter/MSW; `0013–0014` Ga response/fold; `0015–0017` Cl response/convention audit; `0018` Ga power; `0019` Cl power; `0020` In115 provisional screen + Se82 pivot; `0021` Se82 validation/full fold; `0022` Li7 gs screen; `0023` Li7 two-state external validation + full power authority.

## Current maturity
**NMIR_READINESS: 44%**.

Increase from 42% is credited only because the Li7 candidate has now crossed the prospectively required external response-validation gate and a raw-inspected full B16+MSW fold, adding a fourth validated target and a new reproducible G3 leader. G3 remains globally open.

## Exact next gates
1. **Target-space passive-SM upper bound:** combine allowed-transition sum rules/strength limits, target nuclei per kg, solar spectral energy flux and weak phase space to bound how far any passive nuclear target can exceed validated Li7. Keep resonant peaks excluded unless G8 is passed.
2. Continue modern low-A / strong-allowed measured-response target screening under the same B16+MSW convention; rank pure and natural material separately.
3. Implement G8 integrated resonance-strength/linewidth/spectral-overlap bound before admitting resonant targets into energy rankings.
4. In parallel close the sum-rule-preserving spin-response toy, transparent-Sun finite-source/Liouville focusing benchmark, and fixed-mass-column staggered/multi-isotope control.
