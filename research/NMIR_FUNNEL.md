# NMIR Discovery Funnel

## Purpose
NMIR is a model-agnostic discovery funnel for identifying, bounding or ruling out physically real neutrino↔matter/field interfaces and, where relevant, irreversible neutrino-supplied energy deposition. It is not a linear material search.

Common interface:

`Gamma = sum_ab integral dE d^3q dω Phi(E) K_ab(E,q,ω) S_ab(q,ω)`.

For energy harvesting:

`P_dep,nu = N_T integral dE Phi(E) mu(E,x) sigma_eff(E) E_dep,nu(E)`, with frozen `E_dep,nu<=E_nu`. Daughter decay, nuclear mass release, mediator preparation, stored free energy, external pumping and reset work are never counted as neutrino-supplied power.

## Funnel stages
- **F0 objective:** state control, detection, focusing, irreversible deposition or true capture; never promote one into another.
- **F1 channel:** SM CC/NC, electromagnetic form factors, matter potential, many-body density/spin, resonant inverse transition, gravity, engineered geometry or later BSM.
- **F2 production↔absorption:** use measured ft/B(GT)/width/branching authority where possible.
- **F3 kinematics/spectral overlap:** threshold, q, phase space and physical source profile must overlap.
- **F4 microscopic strength:** matched conventions; unvalidated approximations remain screening.
- **F5 collective/resonant gain:** enforce integrated structure factors, coherence volume, linewidth and dephasing.
- **F6 no-free-lunch:** unitarity, sum rules, detailed balance, conservation, Liouville, finite source, fixed mass column and complete medium/field/free-energy accounting.
- **F7 common score:** event rate, optical depth, neutrino-only W/kg, flux-integrated gain and enhancement required to practical benchmarks.
- **F8 external constraints:** laboratory, solar, astrophysical, cosmological, stability and engineering.
- **F9 composition:** only individually validated gains may multiply.
- **F10 outcome:** PASS-SURVIVOR, STRONG-NEGATIVE, SCIENTIFIC-FAIL or BLOCKED.

## Current funnel position — through validated iteration 0045
- **Production↔absorption:** measured-ft route + validated two-state Li-7 PASS.
- **Validated passive CC targets:** Li-7, Se-82, Ga-71, Cl-37. Pure Li-7/GS98 leader `1.06589117e-21 W/kg`, still `~9.38e20` below 1 W/kg.
- **Leading allowed passive CC:** STRONG-NEGATIVE scoped envelope `9.419e-12 W/kg`.
- **Finite-q vector-charge/axial-spin:** STRONG-NEGATIVE envelope `1.2056895108e-9 W/kg`.
- **Omitted one-body nuclear currents:** `ONE_BODY_SUBLEADING_STRONG_NEGATIVE_SCOPED`; extreme full-one-body stress `1.0131561292e-8 W/kg`, still `9.87e7` below 1 W/kg.
- **Genuine two-/higher-body nuclear currents:** global theorem OPEN. Selected-nucleus corrections are evidence-distance anchors, not universal maxima.
- **RIOEC resonance:** ordinary pp/CNO/B8 solar `nu_e` has zero RIOEC entrance factor; thermal-solar pair-process `anti-nu_e` remains eligible. Line narrowing does not create integrated strength. Target-specific evaluated entrance strength × primary thermal `anti-nu_e` spectrum remains OPEN/BLOCKED.
- **Glashow positive control:** real SM resonance physics but ~6.325 PeV, outside solar <=20 MeV window.
- **Coordinate-local density / bounded-local spin / long-range pair / passive linear multimode / convex homogeneous nonlinear mediator:** broad no-free-energy-gain guards PASS in their frozen scopes.
- **Passive metastable avalanche:** detector/control `PASS-SURVIVOR`; energy harvesting `STRONG_NEGATIVE_SCOPED`. Macroscopic signal can be powered by stored target free energy, but neutrino-energy gain stays <=1 and reset must replenish the reservoir.
- **G10 staggered/fixed-column geometry:** `GEOMETRY_ONLY_STRONG_NEGATIVE / FIXED_COLUMN_MIXTURE_THEOREM_PASS` at fixed microscopic response.
- **G9 gravity:** PARTIAL PASS. Model-S gives `F_min=23.629351 AU`, close to published ~23.5 AU transparent-Sun scale. This is distant-source-behind-Sun geometry, not solar self-lensing; physical source flux × finite-source/alignment/duty-cycle utility remains OPEN.

## G2 CEvNS detection survivor — current authority
- **0041 source opening:** Ar40 at 40 eV requires `E_nu>=0.862860938 MeV`; pp closed, pep/B8 open, Be7 line sits at endpoint boundary.
- **0042 physical Be7 fold:** at 40 eV, 31.104% of the thermally broadened dominant Be7 profile lies above the source-energy threshold, but only `4.906342834e-6` of ideal CEvNS cross section survives recoil phase space; rate `3.973604373e-8 events/(kg day)`. At 20 eV `2.022320664e-3`; at 10 eV `4.553823547e-3`.
- **0043 class inverse law:** at fixed kg and approximately fixed `Q_W/A`, `R(A) ∝ A(1-A/Amax)^2`; `A_star=Amax/3=2E_nu^2/(3m_u T_thr)`, so `Tmax(A_star)≈3T_thr`. This is a local monoenergetic continuous-A design law.
- **0044 approximation FAIL:** using `M=A m_u` near the Ar40/Be7 40-eV endpoint shifted the benchmark by ~30% and failed the prospectively frozen 1% criterion. The FAIL is retained; criteria were not weakened.
- **0045 exact-mass full-solar real-nucleus PASS:** corrected gate freezes exact NIST isotope masses for 23 physical nuclei, actual Z/N, full B16-GS98 pp + both Be7 branches/profiles + pep + N13/O15/F17 + B8/hep, Helm form factor and thresholds `[1,3,5,10,20,40] eV`. Hosted run `34052577623`, job `101538698697`, raw `23 passed`, artifact `9995006029`, SHA256 `5ec6157a102ba9dc4fc2d97fc710d975020641393a0f48c184f39235ea58c897`.

Validated 0045 winner sequence:

| recoil threshold | winner | ideal total rate [events/(kg day)] | dominant source |
|---:|---|---:|---|
| 1 eV | Pb208 | `5.633559994e-2` | Be7-ground |
| 3 eV | Pb208 | `3.025222341e-2` | Be7-ground |
| 5 eV | Xe132 | `1.728556077e-2` | Be7-ground |
| 10 eV | Se82 | `8.212077955e-3` | Be7-ground |
| 20 eV | Pb208 | `4.227008240e-3` | B8 |
| 40 eV | Pb208 | `3.873772682e-3` | B8 |

Interpretation: the full-solar optimum is a source-dependent target/threshold phase diagram. The continuous-A rule remains a useful local guide but cannot choose a global full-solar winner. Heavy-target re-entry at 20–40 eV is driven by transition to B8-dominated recoil phase space, not new microphysics or interaction enhancement. No detector/material recommendation follows until the detector transfer function is applied.

## Active highest-value gate
**G2 target/threshold phase diagram is ACTIVE and must not be duplicated.** Prospective contract `research/cevns_target_phase_diagram_prereg.md` was frozen in commit `37e28276d7fa24039c1ac5114e899b1b8e697f1e` before implementation. It reuses exactly the 0045 physical inputs and target set, scans 0.5–100 eV, refines every winner crossover by bisection to <=0.02 eV, independently checks transition topology/stability, and requires source-dominance classification. Frozen outcomes: `PASS_PHASE_DIAGRAM`, `PARTIAL_PHASE_DIAGRAM`, `FAIL_NONROBUST_WINNER_SEQUENCE`.

Implementation commit: `2dca53ed8c10db38980a2b0ea0deaf1d055a40e9`; test commit: `b64df566e2e50c8eef2bf94b1d64942c844a4408`. Baseline CI success is software evidence only. Do not call a scientific PASS until the dedicated hosted result is terminal and its raw result/log/artifact are inspected.

## Highest-value surviving branches after the active gate
1. **G2 real metastable detector transfer function:** apply primary/measured `epsilon_nuc(T)` or trigger efficiency, threshold distribution/stability, chemistry/phase, backgrounds/dark counts, live fraction/dead time, reset/preparation energy and stored-free-energy accounting to the validated microscopic CEvNS phase map. Keep detection signal amplification separate from interaction rate and neutrino-energy gain.
2. **G8 target-specific thermal-solar antineutrino RIOEC:** freeze primary thermal-solar `anti-nu_e` spectral density and one independently evaluated entrance strength/width; compute flux-integrated rate and neutrino-only W/kg. Remain BLOCKED rather than using blanket strengths.
3. **Global genuine two-/higher-body nuclear-current residual:** seek a finite-range/saturation/sum-rule/operator bound, preferably class-level rather than another target scan.
4. **G9 distant-source utility:** physical astrophysical neutrino source flux × full finite-source/alignment/duty-cycle magnification; never use transparent-Sun gain for solar neutrinos.
5. **BSM unlock audit only after principal passive-SM residuals are substantially bounded.**

## Research discipline / guards
Class-level bounds dominate convenient target scans. Negative results shrink mechanism space and remain scientific results. A gain must survive F0-F8 before F9 composition. Event/detection gain != interaction gain != neutrino-energy gain; peak resonance != flux-integrated capture; directional coherence != integrated opacity; target threshold opening != cross-section enhancement. Near endpoints use physical spectra and exact masses. A nonzero endpoint tail is not automatically practical. BSM remains LOCKED.

Current audit state: **`NMIR_READINESS: 74%`**. The +1 point from 73% is solely for the prospectively frozen, hosted and raw-inspected 0045 exact-mass full-solar physical-nucleus inverse-optimization PASS. 0044 is retained as a useful FAIL; documentation and baseline CI add no readiness credit.
