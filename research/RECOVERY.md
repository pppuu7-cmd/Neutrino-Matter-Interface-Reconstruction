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

### 71Ga authority
Bahcall, Phys. Rev. C 56, 3391 (1997). Full B16×spectrum×MSW fold PASS. Power run `34028394336`, artifact `9987793879`.

### 37Cl authority
Bahcall et al., Phys. Rev. C 54, 411 (1996), with source-average Be7 authority. Power run `34031200366`, artifact `9988653883`; unresolved sub-1-MeV response changes power only ~0.05%.

### 82Se authority — iterations 0020/0021
Frekers et al., Phys. Rev. C 94, 014614 (2016), measured `82Se(3He,t)82Br` GT response.
- Point-Coulomb pp check: scientific FAIL, `-32.6%`, run `34032960415`.
- Relativistic finite-size repair, unchanged prospective gate: PASS, residual `-0.453%`, run `34033049596`.
- Full measured/binned response: nine source-average controls PASS, run `34033182939`.
- First full fold `34033250446`: infrastructure FAIL only (`Pee(0)` at zero-weight endpoint); regression added without changing physics.
- Repaired B16+MSW fold PASS: `34033368287`, job `101486927672`, artifact `9989345911`; same-head baseline CI passed.
- GS98 pure power `2.94006655e-22 W/kg`; natural selenium `2.66241785e-23 W/kg`.

### 7Li authority — iterations 0022/0023
Evaluated `7Be(gs,3/2-) -> 7Li(gs,3/2-)` EC seed: `Q_EC=861.815 keV`, branch `89.56%`, `log ft=3.324`. Ground-only run `34034095803`, artifact `9989580600`, remained non-authoritative pending multi-state completion.

Two-state completion used the independently authorized first `7Be` excited state (`429 keV`, capture threshold `~1.291 MeV`) with `B(F)_gs=1`, `B(GT)_gs=1.19`, `B(GT)_ex=1.06`, `g_A/g_V=1.2723`. Ground normalization remained fixed by log-ft; no neutrino cross section was used to tune the response.

Prospective matched-B8 gates: ground `2.470e-42`, excited `1.289e-42`, total `3.759e-42 cm^2`; component tolerance 12%, total tolerance 10%.

Initial run `34037418081`, job `101497916296`: infrastructure FAIL only (`pytest` missing; science never ran). Dependency-only repair changed no physics/gate.

Repaired validation `34037499594`, job `101498137412`: scientific PASS:
- ground `2.50624405e-42`, residual `+1.467%`;
- excited `1.30740265e-42`, residual `+1.428%`;
- total `3.81364669e-42`, residual `+1.454%`.
Artifact `9990627394`.

Validated B16+MSW fold `34037570254`, job `101498329856`, artifact `9990650435`. GS98: `19.34881333 SNU`, `77.50707776 SNU MeV`, pure Li7 `1.06589117e-21 W/kg`. B8 gives only `7.24140 SNU` but `62.60901 SNU MeV`, so low target mass plus high-energy solar tail drives W/kg.

## Passive leading-allowed target-space upper bound — iteration 0024
Prospective contract: `research/passive_allowed_bound_prereg.md`, commit `88bf3a6718122a354f6bada3ad2fb43d58371392`.

For attractive point-Coulomb `F_pc=x/(1-exp(-x))`, `x=2*pi*alpha*Z_f*E/p`, `exp(x)>=1+x` yields

`p E F_pc <= (1+2*pi*alpha*Z_f) E^2`.

The nuclear response is capped by deliberately loose correlation-independent one-body operator norms:

`S_F<=A^2`, `S_GT<=3A^2`, so `S_allowed<=A^2(1+3 g_A^2)`.

Maximization grants `A<=300`, daughter `Z_f<=119`, zero threshold/excitation, `E_nu<=20 MeV`, artificial neutrino energy flux `2000 W/m^2`, and +2% target-count safety. A separate preregistered `x1e6` omitted-physics stress multiplier is diagnostic only, not theorem/uncertainty.

Hosted run `34038214660`, job `101500085408`, artifact `9990839187`, ZIP SHA256 `f9e544b9aa5372f8e286e8214f2eba422f35cc8e02468501babc99cfcbbc8642`; six dedicated tests PASS; same-head baseline CI `34038214654` SUCCESS.

| quantity | result |
|---|---:|
| analytic leading-allowed envelope | **`9.419449302949355e-12 W/kg`** |
| deficit to 1 W/kg | `1.0616331888e11` |
| x1e6 stressed diagnostic | **`9.419449302949354e-6 W/kg`** |
| stressed deficit to 1 W/kg | `1.0616331888e5` |
| classification | **STRONG_NEGATIVE_SCOPED** |

The analytic envelope is `~8.84e9` above validated Li7, so it is a genuine broad over-envelope. Scientific scope: leading allowed one-body charged-current passive nuclear response under the stated solar-energy/A/Z domain. Forbidden multipoles are not silently covered by the x1e6 diagnostic.

## G8 integrated resonance-strength / spectral-overlap formal gate — iteration 0025
Prospective contract: `research/resonance_overlap_prereg.md`, commit `31bd2467140cdfcfeede18de115934904849eb3d`.

Ordinary continuum capture `nu+A -> B*+e-` is not automatically a narrow incident-energy resonance because the outgoing electron carries variable kinetic energy. G8 applies to genuine isolated-resonance kinematics such as two-body/bound-state/recoilless inverse channels.

Frozen Breit-Wigner convention:

`sigma(E)=pi/k_r^2 * g * Gamma_in*Gamma_out / ((E-Er)^2+(Gamma/2)^2)`.

Its integrated area is

`I_sigma = 2*pi^2/k_r^2 * g * Gamma_in * Gamma_out/Gamma`

and because `Gamma_out<=Gamma`,

`I_sigma <= 2*pi^2/k_r^2 * g * Gamma_in`.

Therefore making a line narrower can increase `sigma_peak`, but cannot generate new integrated weak entrance strength. For incident differential flux `phi(E)`,

`R_per_target <= sup(phi) * I_sigma`,

and for normalized line profile `rho(E)`,

`<sigma> <= ||rho||_infinity * I_sigma`.

No delta-function source is accepted for G8. The current bookkeeping-only monoenergetic pep convention is not resonant authority until a physical solar pep line profile is frozen.

Implementation: formal code `5c8e75e38168a156d983e9e1113c49bf52db6435`; tests `48b791fa1a486578353e70c15218761081d1f5a1`; benchmark `dcb28c55abb7fd3537b2c39a66ae04e2d59b1e75`; hosted head `8c778ccecc9df3f579fef178b068762c5476fc10`.

Hosted authority: run `34038642747`, job `101501241557`, artifact `9990968127`, ZIP SHA256 `db13ac11dbd5cba7aaa76465987265c710dd64ff10cea28617edd9c298d239c5`; same-head baseline CI `34038642903` SUCCESS. Raw JSON inspected before classification.

| G8 formal diagnostic | result |
|---|---:|
| widths tested | `1e-3 ... 1e-15` |
| max numeric area relative error | `6.3661977016e-5` |
| fixed-branch area invariance error | `0.0` |
| peak gain after 1e6 narrowing | `1e6` |
| area / entrance-width bound | `0.5` |
| max Gaussian/Lorentzian overlap / supremum bound | `0.8797668563` |
| status | **G8_FORMAL_PASS** |

Scientific meaning: peak-only resonance claims are now formally rejected. A resonant candidate can enter G3 only after target-specific weak `Gamma_in` (or equivalent measured decay/ft strength), branching, environmental/recoil-free factor if applicable, and physical solar source profile are frozen and convolved.

This formal PASS is not itself a resonant W/kg ceiling.

## 115In screening status
Provisional one-state model (`threshold≈0.114 MeV`, `B(GT)=0.17`) run `34032630382`, artifact `9989115502`. No-osc GS98 `~371.7 SNU` versus historical full-response `~750 SNU`: scientific FAIL as complete response. Precision In115 remains open only with a fuller primary response.

## Other active branches
- First-forbidden/higher multipole charged-current response: priority remaining nuclear loophole.
- G2 many-body/spin: magnons may aid detection/state control but are poor energy carriers; sum-rule-preserving response toy open.
- G8 target-specific resonance numerics: formal gate PASS; entrance-width + real solar-profile ceiling still open.
- G9 gravity: solar-limb weak-field focus `~547.741 AU`; transparent-Sun literature target `~23.5±0.1 AU`; finite-source/Liouville gain open.
- G10 staggered/metamaterial: Bragg kinematics possible; fixed-mass-column angle/energy-integrated gain unproven.
- G5/G6 BSM remain locked until remaining passive-SM loopholes are bounded.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS — CEvNS, tritium-ft, Ga, Cl, measured-GT Se82, validated two-state Li7 |
| G1 static macroscopic coherence | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 many-body deposited-energy channels | OPEN |
| G3 maximum SM deposited solar-neutrino power | **PARTIAL PASS — four validated targets + STRONG NEGATIVE scoped leading-allowed class bound; forbidden/global loopholes open** |
| G4 engineered resonance/polarization/periodicity | OPEN |
| G5 minimal BSM solution | LOCKED until G3 passive-SM loopholes close |
| G6 BSM constraints | LOCKED until G5 |
| G7 production/decay → inverse capture | PARTIAL PASS — measured-ft route + Li7 two-state external validation |
| G8 resonance integrated-strength/bandwidth | **PARTIAL PASS — formal Breit-Wigner area/overlap gate PASS; target-specific Gamma_in + solar-profile W/kg bound open** |
| G9 finite gravitational focusing gain | OPEN |
| G10 staggered/multi-isotope fixed-mass-column gain | OPEN |

## Critical scope guards
1. Detector threshold ≠ total cross section.
2. Directional coherence ≠ integrated opacity.
3. Peak resonance ≠ flux-integrated capture.
4. Ordinary discrete-state CC capture with a continuum outgoing electron is not automatically a narrow incident-energy resonance.
5. Gravitational magnification is finite and multiplicative.
6. Projected atomic coverage ≠ neutrino opacity.
7. Exact time reversal and crossed weak processes must be classified correctly.
8. Never mix solar flux/spectrum/matter/oscillation/nuclear conventions silently.
9. Green workflow ≠ scientific PASS until raw result and frozen gate are inspected.
10. Daughter decay or target nuclear-mass energy must never be counted as neutrino-supplied energy.
11. A few-target maximum is not a global SM ceiling.
12. Negative approximations and infrastructure failures remain separately recorded; gates are never loosened after results.
13. A crossed ground-state ft response is not automatically a complete multi-state target response.
14. Iteration 0024 is scoped to leading one-body Fermi/GT response; forbidden multipoles are separate.
15. G8 formal PASS forbids peak-only ranking but does not replace target-specific entrance-width and solar-profile authority.

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered metamaterial; `0006` ft→capture; `0007–0012` B16 flux/spectra/matter/MSW; `0013–0014` Ga; `0015–0017` Cl; `0018` Ga power; `0019` Cl power; `0020` In115 screen + Se82 pivot; `0021` Se82 authority; `0022` Li7 gs screen; `0023` Li7 two-state authority; `0024` passive leading-allowed target-space bound; `0025` G8 integrated resonance-overlap formal pass.

## Current maturity
**NMIR_READINESS: 48%** (audit estimate).

Increase from 47% to 48% is credited only for a prospectively frozen, hosted/raw-inspected G8 formal gate that eliminates peak-only resonance claims and turns resonance candidates into measurable entrance-width × source-overlap problems. No numerical resonant W/kg ceiling is credited yet.

## Exact next gates
1. **Forbidden/finite-q one-body envelope:** use the full charged-current multipole decomposition to bound Coulomb, longitudinal, transverse-electric and transverse-magnetic responses over `E_nu<=20 MeV`; separate leading finite-q charge/spin operators from recoil/weak-magnetism/axial-charge corrections.
2. **G8 quantitative completion:** choose genuine resonant inverse channels with measured weak decay/ft authority, derive `Gamma_in`, and convolve with frozen Be7/continuum solar profiles. Freeze a physical pep line profile before any pep resonance test.
3. Deprioritize ordinary allowed isotope scanning unless it tests an independent assumption.
4. In parallel close sum-rule-preserving spin response, transparent-Sun finite-source/Liouville focusing, and fixed-mass-column staggered/multi-isotope controls.
