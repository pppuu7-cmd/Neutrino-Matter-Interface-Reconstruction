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
For the G3 neutrino-only ceiling, every successful capture is credited at most the incident neutrino energy: `E_dep,nu <= E_nu`. Daughter-decay/nuclear-mass energy is not counted as neutrino-supplied power.

## Frozen baseline authority
- Xe-132 ideal CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; Xe-like mean free path `~3.08e16 m`.
- Minimal Dirac magnetic moment benchmark for `m_nu=0.05 eV`: `~1.6e-20 mu_B`; ideal 1-m spin-precession maximum `~3.35e17 T`.
- Tritium measured-ft capture route: `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fluxes; pinned pp/hep/B8/CNO spectra; thermally broadened Be7 profiles; daytime adiabatic 3-flavour MSW with `sin^2 theta12=0.307`, `sin^2 theta13=0.0220`, `Delta m^2_21=7.53e-5 eV^2`, normal ordering, Earth regeneration OFF.

## G3 validated target ledger
Authoritative table: `research/sm_power_ledger.md`.

| target / B16 branch | capture rate [SNU] | energy moment [SNU MeV] | mean captured Eν [MeV] | pure-isotope ceiling [W/kg] |
|---|---:|---:|---:|---:|
| **82Se / GS98** | **355.03190979** | **249.61364032** | **0.70307382** | **2.94006655e-22** |
| 82Se / AGSS09met | 345.60519781 | 226.65979252 | 0.65583444 | 2.66970537e-22 |
| 71Ga / GS98 | 65.00993895 | 75.78103575 | 1.16568385 | 1.03091848e-22 |
| 71Ga / AGSS09met | 62.31786849 | 66.37456240 | 1.06509680 | 9.02953653e-23 |
| 37Cl / GS98 | ~3.02 | ~22.65 | ~7.50 | ~5.91e-23 |
| 37Cl / AGSS09met | ~2.56 | ~18.77 | ~7.33 | ~4.90e-23 |

Current **validated** leader remains pure `82Se/GS98`, `2.94006655e-22 W/kg`, about `2.85×` the pure-71Ga leader. Natural selenium gives only `2.66241785e-23 W/kg` because natural `82Se` abundance is about `0.0873`.

Even the upper propagated 82Se response envelope (`~3.204e-22 W/kg`) is still `~3.1e21` times below `1 W/kg`. This is a three-target benchmark, **not** a global Standard-Model theorem/ceiling.

### 71Ga authority
Primary response: Bahcall, Phys. Rev. C 56, 3391 (1997). Full B16×spectrum×MSW fold PASS; power authority run `34028394336`, artifact `9987793879`.

### 37Cl authority
Primary response: Bahcall et al., Phys. Rev. C 54, 411 (1996), with source-average Be7 authority. Power run `34031200366`, artifact `9988653883`. Sub-1-MeV residual changes power by only ~0.05%.

### 82Se authority — iterations 0020/0021
Primary nuclear response: Frekers et al., Phys. Rev. C 94, 014614 (2016), `82Se(3He,t)82Br` high-resolution GT measurement. Frozen data: `data/se82_frekers2016_gt_response.csv`; dominant 75-keV `1+` state has `B(GT)=0.338(31)` and threshold `~171.6 keV`.

Validation sequence, with criteria frozen prospectively:
1. **Point-Coulomb approximation scientific FAIL:** pp source-average `5.1362e-45 cm^2` vs published `7.62e-45`, residual `-32.6%`; run `34032960415`, artifact `9989215767`.
2. **Relativistic finite-size Fermi repair PASS:** same nuclear input, unchanged 15% gate; pp `7.5855e-45`, residual `-0.453%`; run `34033049596`, artifact `9989244871`.
3. **Full measured/binned GT response PASS:** nine published source-average controls all within prospectively frozen limits. Absolute residuals: pp 0.45%, pep 0.73%, Be7-862 0.68%, Be7-384 2.38%, N13 0.44%, O15 0.61%, F17 0.30%, B8 5.00%, hep 7.12%. Run `34033182939`, artifact `9989287872`.
4. First full B16+MSW fold `34033250446` was **infrastructure FAIL only**: code evaluated `Pee(0)` at a zero-weight spectral endpoint. Minimal fail-closed repair added a regression test.
5. Repaired fold PASS: run `34033368287`, job `101486927672`, artifact `9989345911`. Raw JSON inspected before promotion. Baseline CI after promotion: `34033479337` SUCCESS.

GS98+MSW 82Se component highlights: pp `246.766 SNU`, Be7 `84.385 SNU`, B8 `9.060 SNU`; pp dominates events, while B8 contributes `84.262 SNU MeV` to the energy moment.

## 7Li screening status — iteration 0022
Evaluated direct crossed anchor: ENSDF `7Be(gs,3/2-) -> 7Li(gs,3/2-)` EC with `Q_EC=861.815 keV`, branch `89.56%`, `log ft=3.324`. This directly anchors `7Li(gs)+nu_e -> 7Be(gs)+e-`. The separate `7Be -> 7Li*(477.612 keV)` decay matrix element is **not** naively reassigned to capture from a ground-state lithium target into a different external nuclear state.

Hosted ground-state-only B16+MSW screen: run `34034095803`, job `101488884067`, head `d667d2362ce74630b6bd15e29c141c63b398cb01`; artifact `9989580600`, ZIP SHA256 `3b66dfe40cd3403ed97b87bedc4e7f76002170de715c5e264390d0184cdc5bc8`. Raw job log inspected.

GS98+MSW ground-state-only result:
- total `15.9502837162 SNU`;
- energy moment `54.4719486265 SNU MeV`;
- pure `7Li` screen `7.49107964965e-22 W/kg`;
- natural Li screen `6.99831856035e-22 W/kg`.

AGSS09met+MSW ground-state-only: `13.9439186187 SNU`, `45.9024859132 SNU MeV`, pure `6.31259183421e-22 W/kg`.

This screen is **not promoted to the validated G3 ledger**. It would exceed validated 82Se by `~2.55×` for pure isotope if the full response/threshold convention survives external validation, making lithium high priority. The no-oscillation GS98 ground-only total `35.4339 SNU` is about 10% below the historical full-response scale `~39.4 SNU`, but conventions are unmatched; this comparison is context only, not a PASS/FAIL gate.

Baseline CI on the Li screen head: run `34034095805` SUCCESS.

## 115In screening status
A provisional one-state 115In model (`threshold≈0.114 MeV`, `B(GT)=0.17`) was folded on the same B16+MSW authority. Hosted run `34032630382`, artifact `9989115502`.

No-oscillation GS98 gave `~371.7 SNU`, about half the historical full-response scale `~750 SNU`, so the one-state model **fails as a complete 115In response** and is not G3 authority. Its GS98+MSW pure-isotope screening ceiling `~8.32e-23 W/kg` was below Ga. Precision 115In remains open only if a fuller primary response is obtained.

## Other active branches
- G2 many-body/spin: low-energy magnons remain detector-interesting but poor energy carriers; sum-rule-preserving response toy open.
- G8 resonance: peak cross section cannot enter rankings until integrated-strength, linewidth, and solar-spectrum-overlap gates are implemented.
- G9 gravity: solar-limb weak-field `~547.741 AU`; transparent-Sun literature target `~23.5±0.1 AU`; finite-source/Liouville gain remains open.
- G10 staggered/metamaterial: Bragg kinematics are possible, but fixed-mass-column angle/energy-integrated gain remains unproven.
- G5/G6 BSM solution/constraints remain locked until G3 is quantitatively broader and an SM ceiling/no-go is defensible.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS — CEvNS, tritium-ft, Ga, Cl, measured-GT Se82, direct crossed Li7-gs screen |
| G1 static macroscopic coherence | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 many-body deposited-energy channels | OPEN |
| G3 maximum SM deposited solar-neutrino power | **PARTIAL PASS — three validated targets; 82Se validated leader; Li7 promising screen only; global cross-target ceiling open** |
| G4 engineered resonance/polarization/periodicity | OPEN |
| G5 minimal BSM solution | LOCKED until G3 |
| G6 BSM constraints | LOCKED until G5 |
| G7 production/decay → inverse capture | PARTIAL PASS — measured-ft route validated; direct 7Be-EC→7Li inverse gs crossing implemented |
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
9. Daughter decay or target nuclear-mass energy must never be counted as energy supplied by the neutrino.
10. A few-target maximum is not a global SM ceiling.
11. Negative approximations and infrastructure failures remain separately recorded; acceptance gates are not loosened after results.
12. A directly crossed ground-state ft response is not automatically a complete multi-state target response.

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered metamaterial; `0006` ft→capture; `0007–0012` B16 flux/spectra/matter/MSW; `0013–0014` Ga response/fold; `0015–0017` Cl response/convention audit; `0018` Ga power; `0019` Cl power; `0020` In115 provisional screen and Se82 pivot; `0021` Se82 response validation and full power fold; `0022` Li7 direct crossed ground-state screen.

## Current maturity
**NMIR_READINESS: 42%** (audit estimate).

No increase for iteration 0022: the direct Li7 ground-state screen is reproducible and scientifically informative, but the prospectively required external/full-response validation has not yet passed. G3 remains globally open.

## Exact next gates
1. **Li7 full-response authority:** freeze complete `7Li(nu_e,e-)7Be` nuclear response, including independently authorized excited-state strength and near-threshold atomic convention; reproduce at least one published source-average cross section or matched historical total/component set prospectively; then rerun B16+MSW and decide whether Li7 replaces 82Se as validated leader.
2. Continue modern measured-GT cross-target screening after Li7, ranking pure and natural target power under the same B16+MSW convention.
3. Attempt a target-space upper-bound formulation: combine allowed-transition sum rules, number of target nuclei/kg, solar spectral energy flux, and weak coupling to bound how far passive SM nuclear targets can exceed the current validated leader.
4. Implement G8 integrated resonance-strength/linewidth overlap before considering any resonant target as an energy solution.
5. In parallel: sum-rule-preserving spin response; finite-source transparent-Sun gravitational gain; staggered/multi-isotope fixed-mass-column control.
