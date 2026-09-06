# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Recovery protocol: `research/RECOVERY_MANUAL.md`
Funnel authority: `research/NMIR_FUNNEL.md`
Latest immutable validated scientific record: `research/iterations/0045_cevns_real_nucleus_full_solar_exact_mass.md`
Active preregistered work: `research/cevns_target_phase_diagram_prereg.md` (implementation/test commits exist; no scientific PASS until dedicated hosted result is terminal and raw-inspected)

## Recovery rule
Chat history is not scientific authority. A new session must read, in order: `RECOVERY_MANUAL.md`, this file, `NMIR_FUNNEL.md`, newest iteration/prereg files, recent commits, then relevant queued/in-progress/newly-terminal GitHub Actions. If newer commits exist than this reconciliation, reconcile them before opening new science. Do not duplicate queued/in-progress work. A green workflow is not a scientific PASS without result/log/artifact inspection.

## Mission and frozen accounting
NMIR is a discovery funnel over neutrino↔matter/field interfaces, not a linear material search. Keep separate: state control/focusing; microscopic interaction/capture; detector visibility/amplification; irreversible neutrino-sourced deposited energy.

`P_dep,nu = N_T integral dE mu(E,x) Phi(E) sigma_eff(E) E_dep,nu(E)`, with `0 <= E_dep,nu <= E_nu`.

Daughter decay, nuclear mass release, target preparation, stored medium free energy, external pumping, mediator preparation and reset work are never counted as neutrino-supplied power. Unvalidated gains are never multiplied.

General response: `Gamma = sum_ab integral dE d^3q dω Phi(E) K_ab(E,q,ω) S_ab(q,ω)`. Energy-deposition scoring carries the `ω` weight and must obey positivity, kinematics, conservation, applicable sum rules, causality/stability and complete energy-budget accounting.

## Frozen baseline authority
- Xe-132 ideal low-q CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; Xe-like mean free path `~3.08e16 m`.
- Minimal Dirac magnetic moment (`m_nu=0.05 eV`): `~1.6e-20 mu_B`; ideal 1-m spin-precession maximum `~3.35e17 T`.
- Tritium measured-ft inverse capture: `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fluxes; pinned pp/hep/B8/CNO spectra; thermally broadened Be7 profile; daytime adiabatic 3-flavour MSW for charged-current electron-neutrino folds. CEvNS is active-flavour neutral current and has no `P_ee` factor.

## Validated G3 solar-capture ledger
Detailed authority: `research/sm_power_ledger.md`.

| target / branch | capture [SNU] | energy moment [SNU MeV] | pure-isotope neutrino-only ceiling [W/kg] |
|---|---:|---:|---:|
| **7Li / GS98** | **19.34881333** | **77.50707776** | **1.06589117e-21** |
| 7Li / AGSS09met | 16.84165298 | 65.03364861 | 8.94354349e-22 |
| 82Se / GS98 | 355.03190979 | 249.61364032 | 2.94006655e-22 |
| 71Ga / GS98 | 65.00993895 | 75.78103575 | 1.03091848e-22 |
| 37Cl / GS98 | ~3.02 | ~22.65 | ~5.91e-23 |

Current validated charged-current target leader is pure `7Li/GS98 = 1.06589117e-21 W/kg`, still `~9.38e20` below 1 W/kg. This is not a universal all-nucleus theorem.

## Broad class-level closures / no-free-lunch authority
Do not reopen without a genuinely new assumption; immutable notes retain full derivations and provenance.
- `0024` leading-allowed envelope `9.419449302949355e-12 W/kg`, `STRONG_NEGATIVE_SCOPED`; run `34038214660`, artifact `9990839187`.
- `0025` isolated-resonance area theorem: linewidth narrowing cannot create integrated entrance strength; run `34038642747`, artifact `9990968127`.
- `0026` finite-q vector/axial envelope `1.2056895107775174e-9 W/kg`; even x1e6 stress gives `1.2056895107775173e-3 W/kg`; run `34038882486`, artifact `9991038179`.
- `0027` coordinate-local density f-sum: no free superextensive energy-weighted density/phonon gain; run `34039755966`, artifact `9991299921`.
- `0028` bounded-local spin first moment: no free superextensive local-magnon energy gain; run `34040105285`, artifact `9991400307`.
- `0031` long-range pair budget enforces extensive response for extensive absolute interaction budget; run `34041247733`, artifact `9991728037`.
- `0032` harmonic mediator energy ledger removes free per-particle N gain; run `34041392001`, artifact `9991770130`.
- `0033` extreme complete one-body-current stress `1.0131561292246442e-8 W/kg`, still `9.87e7` below 1 W/kg; universal genuine two-/higher-body theorem remains OPEN. Run `34042934477`, job `101512822458`, artifact `9992226798`.
- `0034` fixed-column geometry theorem: layer order/offset cannot change `1-exp(-sum tau)` at fixed microscopic response; passive isotope mixing cannot beat best component in `sigma/m`; run `34043114890`, artifact `9992278460`.
- `0038` passive finite linear multimode mediator: no free gain after complete mediator-energy accounting; run `34047675712`, artifact `9993592020`.
- `0039` passive convex positive homogeneous nonlinear mediator: extensivity removes free per-particle N gain; run `34048018268`, artifact `9993688056`.
- `0040` metastable avalanche: detector/control `PASS-SURVIVOR`, harvesting `STRONG_NEGATIVE_SCOPED`; stored free energy supplies avalanche, neutrino-energy gain <=1. Run `34048287780`, job `101527189597`, artifact `9993764694`.

## G8 resonance branch
- `0035`: RIOEC is incident `anti-nu_e`; ordinary solar pp/CNO/B8 `nu_e` has zero entrance factor. Area/profile theorem passed; run `34043507541`, artifact `9992388766`.
- `0036`: Glashow resonance positive control is real SM resonance physics but at ~6.325 PeV, outside <=20 MeV solar window.
- `0037`: low-energy resonance kinematic design window PASS only. Target-specific evaluated entrance strength × primary thermal-solar `anti-nu_e` spectrum remains OPEN/BLOCKED; run `34044012213`, artifact `9992535787`.

## G9 gravity
- `0029`: rounded transparent-Sun focal benchmark ~23.03 AU plus finite-source/Liouville control.
- `0030`: Model-S projection `F_min=23.62935116 AU`, 0.5504% from published ~23.5 AU; run `34041004727`, artifact `9991661778`.
Classification: `MODEL_S_ROBUSTNESS_PASS / G9 PARTIAL`. This is distant-source-behind-Sun geometry, not solar-neutrino self-lensing. Physical source flux × finite-source/alignment/duty-cycle usefulness remains OPEN.

## G2 CEvNS detection chain
### 0041 — source-opening kinematics
For Ar-40 at 40 eV, `E_nu,min=0.8628609380456526 MeV`; pp closed, pep/B8 open, nominal Be7 line sits at the boundary. Run `34049714420`, job `101530992980`, artifact `9994165815`.

### 0042 — physical Be7 profile × Ar-40
Frozen Bahcall-1994 dominant Be7 profile. At 40 eV, 31.104% of profile lies above source-energy threshold but recoil-phase-space retained fraction is only `4.906342834e-6`; ideal dominant-Be7 rate `3.973604373e-8 events/(kg day)`. At 20 eV rate `2.022320664e-3`; at 10 eV `4.553823547e-3`. Classification `DETECTION PASS-SURVIVOR / RATE_STRONGLY_ENDPOINT_SUPPRESSED / ENERGY_GAIN_NONE`. Run `34050807911`, job `101533964874`, artifact `9994471349`.

### 0043 — continuous-A inverse optimum
At fixed kg and approximately fixed `Q_W/A`, low-q envelope gives `R(A) ∝ A(1-A/Amax)^2`, unique `A_star=Amax/3=2E_nu^2/(3m_u T_thr)`, equivalently `Tmax(A_star)≈3T_thr`. Prospective numerical validation: max relative `A_star` residual `5.0032e-8`; max relative `Tmax/(3Tthr)` residual `1.3915e-4`. This is a class-level design law, not a real-isotope recommendation. Run `34051179823`, job `101534970552`, artifact `9994578242`.

### 0044 — approximation FAIL retained
Prospective real-nucleus full-solar gate initially used `M=A m_u` and required Ar-40 no-Helm Be7 rates at 10/20/40 eV to reproduce 0042 within 1%. The 40-eV value was `2.7813779481704556e-8` versus exact-isotope authority `3.973604373087567e-8`, ratio ~0.700: ~30% endpoint shift. This is a scientific/approximation FAIL, not a criterion to relax. Dedicated run `34051573524`; baseline run `34051556950` had `1 failed, 267 passed`. Corrective action was prospectively frozen exact NIST isotope masses.

### 0045 — exact-mass real-nucleus full-solar optimization PASS
Immutable authority: `research/iterations/0045_cevns_real_nucleus_full_solar_exact_mass.md`.
Prospective contract: `research/cevns_real_nucleus_exact_mass_prereg.md`.
Frozen candidates: 23 physical nuclei with exact NIST isotope masses (`data/cevns_target_candidates_exact_mass.csv` + provenance), actual Z/N; full B16-GS98 pp, both Be7 branches/profiles, pep, N13/O15/F17, B8/hep; thresholds 1,3,5,10,20,40 eV; Helm form factor; detector efficiency/chemistry/backgrounds excluded.

An infrastructure failure from `E_nu=0` continuum endpoints plus a non-fail-closed shell pipeline was minimally repaired: zero energy contributes zero cross section, negative energies remain invalid, regression tests were added, workflow uses `set -o pipefail`. Frozen physics criteria were unchanged.

Authoritative corrected workflow head `58bbb246e47abc5541b216e4db18a6011e968c41`; hosted run `34052577623`, job `101538698697`; raw dedicated tests `23 passed`; artifact `9995006029`; ZIP SHA256 `5ec6157a102ba9dc4fc2d97fc710d975020641393a0f48c184f39235ea58c897`; benchmark status `PASS_REAL_NUCLEUS_SOLAR_EXACT_MASS_OPTIMIZATION`.

Threshold winners [ideal events/(kg day)]:
- 1 eV: Pb208 `5.633559994e-2` (runner W184 `5.163448674e-2`), Be7-ground dominant;
- 3 eV: Pb208 `3.025222341e-2` (W184 `2.890291478e-2`), Be7-ground;
- 5 eV: Xe132 `1.728556077e-2` (I127 `1.675116223e-2`), Be7-ground;
- 10 eV: Se82 `8.212077955e-3` (Ge74 `7.871654050e-3`), Be7-ground;
- 20 eV: Pb208 `4.227008240e-3` (W184 `3.820668921e-3`), B8 dominant;
- 40 eV: Pb208 `3.873772682e-3` (W184 `3.394947723e-3`), B8 dominant.

Ar40 at 40 eV gives Be7-ground `3.972432637e-8 events/(kg day)`, reproducing 0042 after the expected small Helm/exact-fold difference. Winner Helm/no-Helm ratios show only ~0.3–0.5% suppression at 1–10 eV and ~3% for Pb at 20–40 eV.

Scientific interpretation: the optimum is a source-dependent phase diagram, not a monotonic target-mass rule. The observed six-point topology is `Pb208 -> Pb208 -> Xe132 -> Se82 -> Pb208 -> Pb208`; the high-threshold heavy-target re-entry is driven by the source switch from Be7-dominated to B8-dominated recoils. This is target/threshold matching, not interaction enhancement and not a practical detector-material recommendation.

## Active preregistered work after 0045
`research/cevns_target_phase_diagram_prereg.md` was committed prospectively at `37e28276d7fa24039c1ac5114e899b1b8e697f1e`, before implementation. Frozen scan is 0.5–100 eV with adaptive bisection of every winner crossover to <=0.02 eV and independent topology/stability check; classifications are `PASS_PHASE_DIAGRAM`, `PARTIAL_PHASE_DIAGRAM`, or `FAIL_NONROBUST_WINNER_SEQUENCE`. Implementation commit `2dca53ed8c10db38980a2b0ea0deaf1d055a40e9`; test commit `b64df566e2e50c8eef2bf94b1d64942c844a4408`. Baseline CI may validate software only; no phase-diagram scientific PASS is authoritative until a dedicated result is terminal and its raw result/log/artifact is inspected. Do not launch a duplicate while related work is queued/in progress.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body/deposited-energy/detection channels | **PARTIAL PASS: passive free-energy-gain classes bounded; metastable avalanche detector survivor; physical-spectrum CEvNS and exact-mass full-solar real-nucleus inverse optimization PASS; threshold phase diagram ACTIVE; real detector transfer-function ledger OPEN** |
| G3 maximum SM deposited solar-neutrino power | **PARTIAL PASS — leading, finite-q and one-body-current sectors strong-negative; universal genuine two-/higher-body residual and target-specific thermal-antineutrino resonance OPEN** |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5 minimal BSM solution | LOCKED |
| G6 BSM constraints | LOCKED |
| G7 production/decay -> inverse capture | PARTIAL PASS |
| G8 resonance integrated-strength/bandwidth | **PARTIAL PASS — area/source/flavor/kinematic controls passed; target-specific evaluated RIOEC entrance strength × thermal-solar anti-nu_e fold OPEN/BLOCKED** |
| G9 finite gravitational focusing gain | **PARTIAL PASS — transparent-Sun scale robust; distant-source usefulness OPEN; solar self-lensing inapplicable** |
| G10 staggered/multi-isotope fixed-mass-column gain | **GEOMETRY-ONLY STRONG NEGATIVE / FIXED-COLUMN MIXTURE THEOREM PASS** |

## Critical scope guards
1. Event/detection gain != interaction gain != neutrino-energy gain.
2. Directional coherence != integrated opacity.
3. Peak resonance != flux-integrated capture.
4. Gravitational gain requires correct source geometry, finite source, Liouville and receiver integration.
5. Daughter/nuclear/external/mediator/stored-medium energy is not neutrino-supplied power.
6. A few-target maximum is not a global SM ceiling.
7. Frozen gates are never relaxed after seeing results.
8. Selected-nucleus two-body corrections are evidence-distance anchors, not universal maxima.
9. Geometry-only G10 does not cover structure-induced microscopic-response changes.
10. No F9 multiplication of unvalidated gains.
11. RIOEC is an electron-antineutrino entrance channel; ordinary B16 solar `nu_e` flux must never be inserted into its rate.
12. Kinematic resonance matching alone is not a microscopic-strength or rate PASS.
13. Metastable amplification requires explicit stored-free-energy/reset accounting.
14. Detector-threshold opening is not cross-section enhancement; near-boundary sources require physical spectral folding.
15. A nonzero endpoint-tail rate is not automatically a practically useful detector rate.
16. Continuous-A CEvNS optimization is only a local monoenergetic design envelope; full-solar physical-nucleus optimum is source- and threshold-dependent.
17. Exact isotope masses are mandatory near recoil endpoints where `M=A m_u` can materially move source opening.

## Chronology
`0001–0023`: baseline microphysics, solar/MSW authority, target validation; `0024` allowed bound; `0025` resonance area; `0026` finite-q envelope; `0027` density f-sum; `0028` local spin; `0029–0030` gravity; `0031` long-range pair budget; `0032` harmonic mediator; `0033` omitted one-body currents; `0034` fixed-column theorem; `0035–0037` RIOEC/Glashow/resonance window; `0038–0039` passive multimode/nonlinear mediator; `0040` metastable avalanche; `0041` CEvNS source opening; `0042` physical Be7 CEvNS; `0043` continuous-A inverse law; `0044` endpoint mass-approximation FAIL; `0045` exact-mass full-solar real-nucleus CEvNS PASS. A prospectively preregistered threshold phase-diagram gate is active after 0045.

## Current maturity
**NMIR_READINESS: 74%** (audit estimate).

73% -> 74% credit: +1% for the prospectively frozen, hosted, raw-inspected exact-mass full-solar real-nucleus CEvNS inverse-optimization PASS. Iteration 0044 earns no positive credit but is retained as a useful negative result demonstrating endpoint sensitivity. Documentation/reconciliation and baseline CI earn no scientific credit.

## Exact next funnel gates
1. **ACTIVE G2 target/threshold phase diagram:** do not duplicate. Inspect the dedicated terminal result when available; classify against the preregistered topology/refinement/stability criteria and create immutable iteration note only after raw result/log/artifact inspection.
2. **After phase-diagram PASS: G2 real metastable detector transfer-function ledger:** use primary/measured nucleation or trigger efficiency vs recoil, threshold distribution/stability, target chemistry/phase, dark counts/backgrounds, live fraction/dead time, reset/preparation cost and stored-free-energy accounting. Keep signal amplification separate from microscopic rate and neutrino-sourced energy.
3. **G8 target-specific thermal-solar antineutrino RIOEC:** require independently evaluated entrance strength × primary thermal `anti-nu_e` spectrum; remain BLOCKED rather than substituting blanket strengths.
4. **Global genuine two-/higher-body nuclear residual:** seek a finite-range/saturation/sum-rule/operator bound without promoting selected-nucleus calculations to a theorem.
5. **G9 distant-source utility:** physical astrophysical source flux × full finite-source/alignment/duty-cycle magnification; never apply transparent-Sun gain to solar neutrinos.
6. **BSM unlock audit:** only after principal passive-SM residuals are substantially bounded.
