# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Funnel authority: `research/NMIR_FUNNEL.md`

## Mission and frozen accounting
NMIR is a discovery funnel over plausible neutrino↔matter/field interfaces, not a linear material search. Distinguish state control, detection and focusing from true absorption and irreversible neutrino-sourced energy deposition.

`P_dep = N_T integral dE mu(E,x) Phi(E) sigma(E) E_dep(E)`.

For G3, `E_dep,nu <= E_nu`. Daughter decay, nuclear mass release, target preparation, stored medium free energy, external pumping and extra thermalization are never counted as neutrino-supplied power. Unvalidated gains are never multiplied.

## Frozen baseline authority
- Xe-132 ideal CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; Xe-like mean free path `~3.08e16 m`.
- Minimal Dirac magnetic moment (`m_nu=0.05 eV`): `~1.6e-20 mu_B`; ideal 1-m precession maximum `~3.35e17 T`.
- Tritium measured-ft capture: `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fluxes; pinned pp/hep/B8/CNO spectra; thermally broadened Be7; daytime adiabatic 3-flavour MSW, Earth regeneration OFF.

## Individually validated G3 targets
Detailed authority remains `research/sm_power_ledger.md`.

| target / B16 branch | capture [SNU] | energy moment [SNU MeV] | pure-isotope neutrino-only ceiling [W/kg] |
|---|---:|---:|---:|
| **7Li / GS98** | **19.34881333** | **77.50707776** | **1.06589117e-21** |
| 7Li / AGSS09met | 16.84165298 | 65.03364861 | 8.94354349e-22 |
| 82Se / GS98 | 355.03190979 | 249.61364032 | 2.94006655e-22 |
| 82Se / AGSS09met | 345.60519781 | 226.65979252 | 2.66970537e-22 |
| 71Ga / GS98 | 65.00993895 | 75.78103575 | 1.03091848e-22 |
| 71Ga / AGSS09met | 62.31786849 | 66.37456240 | 9.02953653e-23 |
| 37Cl / GS98 | ~3.02 | ~22.65 | ~5.91e-23 |
| 37Cl / AGSS09met | ~2.56 | ~18.77 | ~4.90e-23 |

Current validated target leader is pure `7Li/GS98 = 1.06589117e-21 W/kg`, still `~9.38e20` below 1 W/kg.

## Class-level passive bounds and no-free-lunch gates
- `0024` leading-allowed envelope: `9.419449302949355e-12 W/kg`, `STRONG_NEGATIVE_SCOPED`; run `34038214660`, artifact `9990839187`.
- `0025` isolated-resonance area theorem: narrowing cannot create integrated entrance strength; run `34038642747`, artifact `9990968127`.
- `0026` finite-q vector-charge/axial-spin envelope: `1.2056895107775174e-9 W/kg`, strong-negative; x1e6 omitted-current stress `1.2056895107775173e-3 W/kg`; run `34038882486`, artifact `9991038179`.
- `0027` coordinate-local density f-sum: `PASS_DENSITY_FSUM`; no free superextensive energy-weighted density gain; run `34039755966`, artifact `9991299921`.
- `0028` bounded-local spin first moment: `PASS_LOCAL_SPIN_SUM`; no free superextensive local-magnon energy gain; run `34040105285`, artifact `9991400307`.
- `0031` long-range pair budget: `|m1| <= 8 o0^2 W_N`; an extensive absolute interaction budget enforces extensive response. Run `34041247733`, artifact `9991728037`.
- `0032` common harmonic mediator: `E_field=|E_induced|=g_N^2 O^2/(2 kappa)`; Dicke/extensive scaling removes per-particle N gain. Run `34041392001`, artifact `9991770130`.
- `0033` omitted one-body nuclear currents: deliberately extreme complete one-body stress gives `1.0131561292246442e-8 W/kg`, still `9.87e7` below 1 W/kg. Required extra two-body amplitude bridge `r_bridge=28798.3217`; known literature-scale corrections are orders of magnitude short. Hosted run `34042934477`, job `101512822458`, artifact `9992226798`. Classification: `ONE_BODY_SUBLEADING_STRONG_NEGATIVE_SCOPED / TWO_BODY_DATA_DISTANCE_STRONG_NEGATIVE`; universal two-/higher-body theorem OPEN.
- `0034` fixed-column geometry theorem: `A=1-exp(-sum tau_j)` makes layer order irrelevant; at fixed mass column `sum w_i sigma_i/m_i <= max sigma_i/m_i`; simple tilt cannot increase total capture. Hosted run `34043114890`, job `101513298058`, artifact `9992278460`. Classification: `G10_GEOMETRY_ONLY_STRONG_NEGATIVE / FIXED_COLUMN_MIXTURE_THEOREM_PASS`.
- `0038` passive finite linear multimode mediator: for positive-definite `K`, `E_field=|E_induced|=1/2 O^T G^T K^-1 G O`, basis/mode-count independent; a coupled exact zero mode has no stable passive equilibrium. Hosted run `34047675712`, job `101525546661`, artifact `9993592020`; raw `7 passed`.
- `0039` passive convex homogeneous nonlinear mediator: Euler homogeneity gives `b·x*=pV(x*)`, `|E_induced|=(p-1)V(x*)`; extensive scaling removes free per-particle N gain. Hosted run `34048018268`, job `101526462429`, artifact `9993688056`; raw `14 passed`.

## G8 resonance branch
`0035` RIOEC source/flavor + area gate: RIOEC is an incident `anti-nu_e` channel. Ordinary B16 pp-chain/CNO solar `nu_e` contributes exactly zero entrance factor; thermal solar pair-process antineutrinos remain a distinct source class. Unit-area Lorentzian tests verify `rate -> B0*phi_anti-nu_e(E_R)` for a smooth source. Hosted run `34043507541`, job `101514361978`, artifact `9992388766`. Classification: `RIOEC_B16_FLAVOR_NO_GO_PASS / RIOEC_AREA_PROFILE_PASS / G8_TARGET_SPECIFIC_OPEN`.

`0036` real-resonance positive control: observed Glashow mechanism demonstrates that genuine SM resonance physics can enlarge the interaction scale enormously, but its ~6.325-PeV kinematics fail the <=20-MeV solar application. No Glashow gain is composed with solar capture.

`0037` low-energy design window: stationary-electron s-channel mapping `M*=sqrt(m_e^2+2m_eE_nu)` implies 0–20 MeV requires `0.51099895<M*<=4.5498437255 MeV`; thermal 10 eV–5 keV lies only ~0.010–4.976 keV above the electron mass. RIOEC condition `E_R=-Q_epsilon+E_x+E_b` gives a kinematic cancellation requirement only. Hosted run `34044012213`, job `101515715322`, artifact `9992535787`; raw `7 passed`. Classification: `G8_LOW_ENERGY_RESONANCE_WINDOW_PASS`; target-specific entrance strength × physical thermal `anti-nu_e` spectrum remains OPEN and BSM remains LOCKED.

## G9 gravity
`0029`: rounded transparent-Sun focal-scale + finite-source/Liouville control; Patla-Nemiroff rounded inputs give `23.0291102335 AU`, residual `-2.004%` from 23.5 AU; CI `34040499051`, job `101506252362`.

`0030`: full Model-S projected-density lens. Hosted run `34041004727`, job `101507632178`, artifact `9991661778`; full scan minimum `23.62935116 AU`, `0.5504%` from published 23.5 AU. Classification: `MODEL_S_ROBUSTNESS_PASS / G9 PARTIAL`. This is distant-source-behind-Sun geometry, not solar-neutrino self-lensing; usable distant-source finite magnification remains OPEN.

## Iteration 0040 — passive metastable / avalanche trigger gate
Prospective contract `research/metastable_avalanche_prereg.md`, prereg commit `96e101b811838cc12e6bbcf788a6524c637c4fa7`.
Scientific workflow head `249aaeee4a1f841a4c97519b1b7e4ea4db234f1d`; hosted run `34048287780`, job `101527189597`, artifact `9993764694`, artifact ZIP SHA256 `c9221192087c1d38171fc849e2ff5bb44e3f5f76859c6fa12fb89e9ed8e4f619`.

Source-resolved first-law ledger for stored free energy `DeltaF_store>=0`:
`E_out,total = epsilon_nu + epsilon_assist + DeltaF_store`, but `E_out,nu=epsilon_nu<=E_nu`. Signal gain can be arbitrarily large by releasing stored medium energy; neutrino-energy gain remains <=1. Cyclic reset must replenish the released reservoir. Deterministic one-shot trigger without fluctuations/assist additionally requires `epsilon_nu>=DeltaF_barrier`.

Frozen 1-eV trigger / 1-MeV reservoir control produced signal gain `1,000,001` while neutrino-energy gain stayed exactly `1.0`; 5000 randomized positive ledgers had max relative residual `2.220192245414529e-16`. Classification: **`PASS_METASTABLE_AVALANCHE_LEDGER / STRONG_NEGATIVE` for energy harvesting, but `PASS-SURVIVOR` for detection/control.**

## Iteration 0041 — CEvNS source-opening threshold gate
Prospective contract `research/cevns_source_opening_prereg.md`, prereg commit `4d42397aced8817714472e5d52e79b69f0361d7e`.
Scientific head `f733d9979878a10bd46d1b0f7aab96f6c33652c9`; hosted run `34049714420`, job `101530992980`, artifact `9994165815`, artifact ZIP SHA256 `bbeb8ecd3d8c8b003ec7f2218ec962437e3e2f38fc5e6eba00364958cdbb92c2`. Raw job log inspected: `4 passed in 0.01s`.

Exact CEvNS kinematics:
`T_max(E,M)=2E^2/(M+2E)` and inverse `E_min(T,M)=0.5[T+sqrt(T^2+2MT)]`.

For Ar-40 (`39.9623831237 u`) at a `40 eV` recoil threshold:
- required `E_nu >= 0.8628609380456526 MeV`;
- pp endpoint 0.420 MeV -> `Tmax=9.477358036 eV` -> CLOSED;
- Be7 reference line 0.8618 MeV -> `Tmax=39.901698063 eV` -> formally CLOSED by only `0.098301937 eV`;
- pep 1.44 MeV -> `111.401205887 eV` -> OPEN;
- B8 endpoint 16.36 MeV -> `14367.577044465 eV` -> OPEN.

Classification: **`CEVNS_SOURCE_OPENING_KINEMATICS_PASS / DETECTION_SURVIVOR / ENERGY_GAIN_NONE`.** The Be7 boundary is too close for a central-line step approximation; the already frozen thermally shifted/broadened Be7 profile must be folded with the SM differential CEvNS response and the detector threshold/efficiency. Lowering threshold changes observability, not the weak cross section or neutrino-supplied energy.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body/deposited-energy/detection channels | **PARTIAL: local density/spin, extensive long-range pair, passive single-/multi-mode linear and convex homogeneous nonlinear energy-gain classes bounded; metastable avalanche energy gain strong-negative but detector survivor; CEvNS threshold/profile detection branch OPEN at F4/F7** |
| G3 maximum SM deposited solar-neutrino power | **PARTIAL PASS — leading, finite-q and one-body-current sectors strong-negative; universal two-/higher-body theorem and target-specific thermal-antineutrino resonance remain OPEN** |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5 minimal BSM solution | LOCKED |
| G6 BSM constraints | LOCKED |
| G7 production/decay → inverse capture | PARTIAL PASS |
| G8 resonance integrated-strength/bandwidth | **PARTIAL PASS — area/source/flavor/kinematic controls passed; target-specific evaluated entrance-strength × thermal-solar anti-nu_e fold OPEN/BLOCKED on real strength data** |
| G9 finite gravitational focusing gain | PARTIAL PASS — 23.5 AU scale robust; distant-source usefulness OPEN; solar self-lensing inapplicable |
| G10 staggered/multi-isotope fixed-mass-column gain | **GEOMETRY-ONLY STRONG NEGATIVE / FIXED-COLUMN MIXTURE THEOREM PASS** |

## Critical scope guards
1. Event/detection gain != energy-deposition gain.
2. Directional coherence != integrated opacity.
3. Peak resonance != flux-integrated capture.
4. Gravitational gain requires correct source geometry, finite source, Liouville and receiver integration.
5. Daughter/nuclear/external/mediator/stored-medium energy is not neutrino-supplied power.
6. A few-target maximum is not a global SM ceiling.
7. Frozen gates are never relaxed after results.
8. Selected-nucleus two-body corrections are evidence-distance anchors, not universal maxima.
9. Geometry-only G10 does not cover structure-induced microscopic response change.
10. No F9 multiplication of unvalidated gains.
11. RIOEC is an electron-antineutrino entrance channel; ordinary B16 solar `nu_e` flux must never be inserted into its rate.
12. Kinematic resonance matching alone is not a microscopic-strength or rate PASS.
13. Metastable signal amplification must carry an explicit stored-free-energy/reset ledger.
14. Detector-threshold opening is not cross-section enhancement; near-boundary solar lines require their physical source profile.

## Chronology
`0001–0023`: baseline microphysics, solar/MSW authority and target validation; `0024` allowed bound; `0025` resonance area; `0026` finite-q leading envelope; `0027` density f-sum; `0028` local spin sum; `0029–0030` gravity; `0031` long-range pair budget; `0032` harmonic mediator; `0033` omitted one-body currents + two-body distance; `0034` fixed-column theorem; `0035` RIOEC source/flavor + area; `0036` Glashow positive control; `0037` low-energy resonance window; `0038` passive linear multimode; `0039` passive convex homogeneous nonlinear; `0040` metastable avalanche ledger; `0041` CEvNS source-opening threshold.

## Current maturity
**NMIR_READINESS: 71%** (stable audit estimate).

Credit since 69%: +1% for the prospectively frozen/raw-inspected metastable avalanche first-law closure, which closes a broad apparent energy-amplification loophole while retaining detection as a survivor; +1% for the exact class-level CEvNS source-opening gate that converts the survivor into a quantitative threshold map. No credit yet for the Be7 physical-profile rate, target-specific RIOEC W/kg, universal two-/higher-body theorem, distant-source focusing utility, or BSM.

## Exact next funnel gates
1. **G2 metastable CEvNS Be7 physical-profile fold:** use the already frozen thermally broadened Be7 source profile + SM differential CEvNS on Ar-40 + 40-eV recoil threshold. Report above-threshold cross section, line-profile fraction capable of `T>=40 eV`, events/kg/day and threshold sensitivity. This is detection scoring only.
2. **G8 target-specific thermal-solar antineutrino RIOEC:** independently evaluated entrance strength × primary thermal `anti-nu_e` spectrum; otherwise remain BLOCKED rather than substitute blanket matrix elements.
3. **Global two-body/higher-body residual:** seek a finite-range/saturation/sum-rule/operator bound without turning selected-nucleus calculations into a theorem.
4. **G9 source-class completion:** distant astrophysical source flux × finite-source/alignment duty cycle; no transparent-Sun gain for solar neutrinos.
5. **BSM unlock audit:** only after G8 and genuine two-/higher-body residual are substantially bounded.
