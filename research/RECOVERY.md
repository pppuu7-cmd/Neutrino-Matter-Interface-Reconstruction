# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Funnel authority: `research/NMIR_FUNNEL.md`

## Mission and frozen accounting
NMIR is a discovery funnel over plausible neutrino↔matter/field interfaces, not a linear material search. Distinguish state control, detection and focusing from true absorption and irreversible neutrino-sourced energy deposition.

`P_dep = N_T integral dE mu(E,x) Phi(E) sigma(E) E_dep(E)`.

For G3, `E_dep,nu <= E_nu`. Daughter decay, nuclear mass release, target preparation, external pumping and extra thermalization are never counted as neutrino-supplied power. Unvalidated gains are never multiplied.

## Frozen baseline authority
- Xe-132 ideal CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; Xe-like mean free path `~3.08e16 m`.
- Minimal Dirac magnetic moment (`m_nu=0.05 eV`): `~1.6e-20 mu_B`; ideal 1-m precession maximum `~3.35e17 T`.
- Tritium measured-ft capture: `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fluxes; pinned pp/hep/B8/CNO spectra; thermally broadened Be7; daytime adiabatic 3-flavour MSW, Earth regeneration OFF.

## Individually validated G3 targets
Detailed authority: `research/sm_power_ledger.md`.

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

Current target leader is pure `7Li/GS98 = 1.06589117e-21 W/kg`, still `~9.38e20` below 1 W/kg.

## Class-level passive bounds and gates
- `0024` leading-allowed envelope: `9.419449302949355e-12 W/kg`, STRONG_NEGATIVE_SCOPED; run `34038214660`, artifact `9990839187`.
- `0025` isolated-resonance area bound: line narrowing cannot create integrated entrance strength; run `34038642747`, artifact `9990968127`.
- `0026` finite-q vector-charge/axial-spin envelope: `1.2056895107775174e-9 W/kg`, STRONG_NEGATIVE; x1e6 omitted-current stress `1.2056895107775173e-3 W/kg`; run `34038882486`, artifact `9991038179`.
- `0027` coordinate-local density f-sum PASS/STRONG-NEGATIVE against free superextensive energy-weighted density gain; run `34039755966`, artifact `9991299921`.
- `0028` bounded-local spin first-moment PASS/STRONG-NEGATIVE against free superextensive local-magnon energy gain; run `34040105285`, artifact `9991400307`.

## G9 gravity — iterations 0029/0030
`0029`: prospectively frozen rounded transparent-Sun check + finite uniform-source/Liouville control. Patla-Nemiroff rounded inputs give `23.0291102335 AU`, residual `-2.004%` from published `23.5 AU`; baseline CI run `34040499051`, job `101506252362`, raw `141 passed`.

`0030`: independent full Model-S projected-density lens. Hosted run `34041004727`, job `101507632178`, artifact `9991661778`, 9 tests PASS. Raw results:
- integrated Model-S mass `1.9890968238e33 g`, relative error `4.86796e-5`;
- `M_2D(0.024R)/M=0.01311330481`;
- `F(0.024R)=24.07378082 AU`;
- full scan minimum `23.62935116 AU`, only `0.5504%` from published 23.5 AU.

Classification: **MODEL_S_ROBUSTNESS_PASS / G9 PARTIAL**. This is a distant-source-behind-Sun geometry, not solar-neutrino self-lensing. Usable distant-source finite magnification remains OPEN.

## Iteration 0031 — long-range/nonlocal pair budget
For `H=sum h_ij`, additive `O=sum o_i`, `||o_i||<=o0`,

`|m1| <= 8 o0^2 W_N`, `W_N=sum ||h_ij||`.

Thus `W_N=O(N)` enforces an extensive first-moment bound. Hosted run `34041247733`, artifact `9991728037`, 7 tests PASS. For `N:1000->1e6`: unscaled pair budget and response/particle both gain `1001`; `kappa=0.5` both `31.6544`; Kac `kappa=1` both `1.001`.

Classification: **PASS_LONG_RANGE_BUDGET / STRONG-NEGATIVE scoped**.

## Iteration 0032 — common harmonic mediator included explicitly
For `H=(kappa/2)x^2-g_N x O`, completion of the square gives

`E_field=|E_induced|=g_N^2 O^2/(2kappa)`.

Hosted run `34041392001`, artifact `9991770130`, 7 tests PASS. With `g_N=g0/N^gamma`, energy/particle gains for `N:1000->1e6` are: gamma 0 -> 1000; 0.25 -> 31.6228; 0.5 -> 1.0; 0.75 -> 0.03162. Dicke `gamma=1/2` gives `J_eff~1/N`.

Classification: **PASS_HARMONIC_MEDIATOR_BUDGET / STRONG-NEGATIVE scoped**.

## Iteration 0033 — subleading nuclear-current loophole
Prospective contract `research/nuclear_current_loophole_prereg.md`, commit `da68f1d8f89aa11045f587aeec0332da62fdea2c`.

Part A uses an intentionally generous complete omitted one-body current stress: axial charge, convection/recoil, weak magnetism and induced pseudoscalar, with `p/M<=1`, `q_max=40.51099895 MeV`, triangle component counting and an extra factor-2 amplitude safety.

Frozen finite-q leading power: `1.2056895107775174e-9 W/kg`.
Raw omitted/leading one-body component ratio: `0.9494073224324683`; safe amplitude ratio `r_1b=1.8988146448649366`.

`P_1b = 1.0131561292246442e-8 W/kg`, still `9.8701470697e7` below 1 W/kg.

Classification: **ONE_BODY_SUBLEADING_STRONG_NEGATIVE_SCOPED**.

Required extra amplitude to bridge to 1 W/kg:

`r_bridge=28798.321671367867`.

Literature-calibrated amplitude-distance diagnostics:
- 0.03 typical two-body axial anchor -> bridge gap `959944.0557`;
- 0.30 suppressed-GT exceptional anchor -> `95994.40557`;
- 0.61 axial-charge excess anchor -> `47210.36340`.

Even deliberate aggregate amplitude `r=1000` gives only `1.2081020955e-3 W/kg`. Generic NLO `C(Q/Lambda)` at deliberately large `Q/Lambda=0.5` would require `C=57596.64334`.

Hosted run `34042934477`, job `101512822458`, artifact `9992226798`; raw `9 passed in 0.03s`.

Classification: **TWO_BODY_DATA_DISTANCE_STRONG_NEGATIVE**, while **GLOBAL_TWO_BODY_THEOREM remains OPEN**. Known calculations are extremely distant from the bridge, but selected-nucleus corrections are not promoted into a correlation-independent bound for arbitrary nuclei.

## Iteration 0034 — staggered-layer / fixed-column theorem
Prospective contract `research/structured_column_prereg.md`, commit `868d71658cbbc41a6582136f9d88ae40c108fbe2`.

For independent passive layers,

`A(E)=1-exp(-sum_j tau_j)`.

Therefore layer order and transverse offsets are exactly irrelevant when microscopic cross sections are fixed.

At fixed mass column,

`tau/Sigma_mass=sum_i w_i (sigma_i/m_i) <= max_i sigma_i/m_i`,

so no passive isotope mixture/layering can beat the best pure component once microscopic responses are fixed.

For a fixed slab face area tilted by `c=cos(theta)`, total capture factor

`C(c)=c[1-exp(-tau/c)] <= C(1)`.

Hosted run `34043114890`, job `101513298058`, artifact `9992278460`; raw `6 passed in 0.04s`.

Atomic projected-coverage stress, using the already enormous A=300/Z=119/E=20 finite-q + full-one-body stressed microscopic cross section:
- `sigma_stress=2.4740960790061117e-32 cm^2`;
- 2 Å square cell gives `tau_layer=6.185240197515279e-17`;
- `1.61675208733481e16` ideal dense layers for `tau~1`;
- idealized thickness `3.2335041747e6 m` (~3234 km);
- effective weak interaction radius `8.87428442927202e-19 m`.

Classification: **G10_GEOMETRY_ONLY_STRONG_NEGATIVE / FIXED_COLUMN_MIXTURE_THEOREM_PASS**.

This closes geometry-only staggered layers, layer ordering, passive isotope mixing and simple slab-angle path-length tricks. It does not close structures that change `sigma(E,q)` itself through resonance, coherence, polarization, active driving or BSM.

## Iteration 0035 — RIOEC source-class + resonance-area gate
Prospective contract: `research/rioec_source_class_prereg.md`, commit `5decc89a2e19092ee362742ef42bc532f5321add`.

Akhmedov, Lasserre & Maturi (arXiv:2608.25001, 2026) define resonant induced orbital electron capture as

`anti-nu_e + [e^- + (Z,A)] -> (Z-1,A)*`.

F1/F3 source-flavor result: the ordinary pp-chain/CNO/B16 solar source frozen by NMIR is `nu_e`; standard active oscillations do not convert neutrinos into antineutrinos. Therefore its RIOEC entrance factor is exactly zero. Thermal solar pair-process antineutrinos are a distinct source class and remain eligible.

F5/F6 area/profile result: with `sigma(E)=B0 L(E)` and unit-area Lorentzian `L`, narrowing linewidth raises the peak but not the integrated strength. Hosted benchmark:
- area/B0 at gamma `1e-3`: `0.9999968169011043`;
- area/B0 at gamma `1e-9`: `0.9999968169011043`;
- smooth Gaussian source overlap / `[B0 phi(E_R)]`: `0.9996011826863775` for `gamma/source_sigma=1e-3`, `0.9999941797890092` for `1e-5`.

Hosted run `34043507541`, job `101514361978`, artifact `9992388766`; raw `5 passed in 0.13s`; artifact ZIP SHA256 `881167ee93b2d6963d8aa39e0dcd5a72e497bed0d31d7367fa048b69e2063941`.

Classification: **RIOEC_B16_FLAVOR_NO_GO_PASS / RIOEC_AREA_PROFILE_PASS / G8_TARGET_SPECIFIC_OPEN**.

Scientific consequence: a narrow RIOEC peak cannot use or multiply the ordinary ~B16 thermonuclear solar-neutrino flux. The surviving solar application must use the much lower-energy thermal `anti-nu_e` source class with its own primary spectral density, and a real evaluated target entrance strength. Candidate-specific W/kg is not yet claimed.

Detailed records: `research/iterations/0029_gravity_focusing_finite_source_gate.md` through `0035_rioec_source_class_and_area_gate.md`.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body deposited-energy channels | **PARTIAL NEGATIVE — local density, local spin, extensive long-range pair and passive single-harmonic-mediator routes class-bounded; multi-mode/gapless/nonlinear/active/higher-body remain OPEN** |
| G3 maximum SM deposited solar-neutrino power | **PARTIAL PASS — leading, finite-q and omitted one-body-current sectors strong-negative; known two-body corrections extremely distant; universal two-body/higher-body theorem and target-specific thermal-antineutrino resonance remain OPEN** |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5 minimal BSM solution | LOCKED |
| G6 BSM constraints | LOCKED |
| G7 production/decay → inverse capture | PARTIAL PASS |
| G8 resonance integrated-strength/bandwidth | **PARTIAL PASS — formal area theorem plus RIOEC source/flavor gate done; ordinary B16 source is forbidden for RIOEC; target-specific evaluated entrance-strength × thermal-solar anti-nu_e fold OPEN** |
| G9 finite gravitational focusing gain | PARTIAL PASS — 23.5 AU scale robust; distant-source usefulness OPEN; solar self-lensing inapplicable |
| G10 staggered/multi-isotope fixed-mass-column gain | **GEOMETRY-ONLY STRONG NEGATIVE / FIXED-COLUMN MIXTURE THEOREM PASS; microscopic-response-changing structured matter remains under G2/G4/G8** |

## Critical scope guards
1. Event/detection gain != energy-deposition gain.
2. Directional coherence != integrated opacity.
3. Peak resonance != flux-integrated capture.
4. Gravitational gain requires correct source geometry, finite source, Liouville and receiver integration.
5. Daughter/nuclear/external/mediator preparation energy is not neutrino-supplied power.
6. A few-target maximum is not a global SM ceiling.
7. Frozen gates are never relaxed after results.
8. Selected-nucleus two-body corrections are evidence-distance anchors, not universal maxima.
9. Geometry-only G10 does not cover any structure-induced microscopic response change.
10. No F9 multiplication of unvalidated gains.
11. RIOEC is an electron-antineutrino entrance channel; ordinary B16 solar `nu_e` flux must never be inserted into its rate.

## Chronology
`0001–0023`: baseline microphysics, solar/MSW authority and target validation; `0024` allowed bound; `0025` resonance area; `0026` finite-q leading envelope; `0027` density f-sum; `0028` local spin sum; `0029` rounded gravity + finite-source/Liouville; `0030` full Model-S gravity; `0031` long-range pair budget; `0032` passive harmonic mediator; `0033` omitted one-body nuclear currents + two-body data distance; `0034` staggered-layer/fixed-column theorem; `0035` RIOEC source/flavor + integrated-area/profile gate.

## Current maturity
**NMIR_READINESS: 64%** (audit estimate).

63%→64% credit: +1% for a hosted/preregistered class-level source/flavor closure that removes the dominant ordinary B16 solar flux from the RIOEC resonance branch while independently reproducing the integrated-area/smooth-profile limit. No credit yet for target-specific resonance W/kg.

## Exact next funnel gates
1. **G8 target-specific thermal-solar antineutrino RIOEC resonance:** choose one evaluated candidate from the 2026 RIOEC list, freeze Q value, daughter excitation, captured-shell binding/width and weak entrance strength; convolve with primary Haxton-Lin-class thermal-solar `anti-nu_e` spectral density; compute events/kg/s and neutrino-only W/kg.
2. **Global two-body/higher-body residual:** seek a finite-range/saturation/sum-rule/operator bound without promoting selected-nucleus calculations into a theorem.
3. **Residual many-body survivor:** multi-mode/gapless/nonlinear mediator, with complete medium/field energy accounting; active pumping separately tracked.
4. **G9 source-class completion:** distant astrophysical neutrino source flux × finite-source/alignment duty cycle; no transparent-Sun gain for solar neutrinos.
5. **BSM unlock audit:** only after G8 and the genuine two-body residual are substantially bounded.
