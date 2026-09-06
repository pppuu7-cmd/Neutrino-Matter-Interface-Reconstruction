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
- Two-body/subleading-current sensitivity remains OPEN; conditional A=300 map needs `r≈192.63` per-pair norm ratio to bridge the finite-q envelope to 1 W/kg.
- `0027` coordinate-local density f-sum PASS/STRONG-NEGATIVE against free superextensive energy-weighted density gain; run `34039755966`, artifact `9991299921`.
- `0028` bounded-local spin first-moment PASS/STRONG-NEGATIVE against free superextensive local-magnon energy gain; run `34040105285`, artifact `9991400307`.

## G9 gravity — iterations 0029/0030
`0029`: prospectively frozen rounded transparent-Sun check + finite uniform-source/Liouville control. Patla-Nemiroff rounded inputs give `23.0291102335 AU`, residual `-2.004%` from published `23.5 AU`; baseline CI run `34040499051`, job `101506252362`, raw `141 passed`.

`0030`: independent full Model-S projected-density lens, preregistered at commit `a237aa336b52ba57bca57b5e289d4ca3505f4586`. Hosted run `34041004727`, job `101507632178`, artifact `9991661778`, 9 tests PASS, pinned external blob verified. Raw results:
- integrated Model-S mass `1.9890968238e33 g`, relative error `4.86796e-5`;
- `M_2D(0.024R)/M=0.01311330481`, 4.282% from rounded 0.0137;
- `F(0.024R)=24.07378082 AU`;
- full scan minimum **`23.62935116 AU`**, only **0.5504%** from published 23.5 AU.

Classification: **MODEL_S_ROBUSTNESS_PASS / G9 PARTIAL**. The short transparent-Sun focal scale is robust, but this is a distant-source-behind-Sun geometry and cannot be multiplied into the Sun's own solar-neutrino flux. Usable extended-source/receiver gain remains OPEN.

## Iteration 0031 — long-range/nonlocal pair budget
Prospective contract `research/long_range_budget_prereg.md`, commit `fb6e777b9306a5d1cbaef409cf72b19d597bdf52`.

For `H=sum h_ij`, additive `O=sum o_i`, `||o_i||<=o0`,

`|m1| <= 8 o0^2 W_N`, `W_N=sum ||h_ij||`.

Thus an extensive absolute interaction budget `W_N=O(N)` enforces an extensive first-moment bound. For all-to-all `||h_ij||=J0/N^kappa`, both interaction budget per particle and response bound per particle scale `N^(1-kappa)`.

Hosted run `34041247733`, job `101508285576`, artifact `9991728037`, 7 tests PASS. For `N:1000->1e6`:
- `kappa=0`: budget gain=response-bound gain=`1001.0`;
- `kappa=0.5`: both `31.6543993783`;
- `kappa=1`: both `1.001`;
- max response-vs-budget mismatch `2.218e-16`.

Classification: **PASS_LONG_RANGE_BUDGET / STRONG-NEGATIVE scoped** against free passive superextensive response at fixed extensive absolute pair-interaction budget.

## Iteration 0032 — common harmonic mediator included explicitly
Prospective contract `research/harmonic_mediator_prereg.md`, commit `059b66d1e12f58bf520eef59a6b54d7d3030f682`.

For passive stable mediator

`H=(kappa/2)x^2-g_N x O`, `|O|<=oN`,

completion of the square gives equal field-displacement and induced-interaction energy scales

`E_field=|E_induced|=g_N^2 O^2/(2kappa)`.

With `g_N=g0/N^gamma`, energy per particle scales `N^(1-2gamma)`. The extensive Dicke scaling `gamma=1/2` therefore gives O(1) energy per particle and induced pair scale `J_eff~1/N`.

Hosted run `34041392001`, job `101508681617`, artifact `9991770130`, 7 tests PASS. Raw gains for `N:1000->1e6`:
- `gamma=0`: field and induced energy/particle gain `1000`;
- `gamma=0.25`: both `31.62277660`;
- `gamma=0.5`: both `1.0` (roundoff `2.2e-16`);
- `gamma=0.75`: both `0.03162277660`;
- at `gamma=1/2`, effective pair ratio `J_eff(N2)/J_eff(N1)=0.001`, exactly the Kac `1/N` scaling.

Classification: **PASS_HARMONIC_MEDIATOR_BUDGET / STRONG-NEGATIVE scoped** against a free superextensive collective gain from a passive stable single harmonic cavity/common mode when mediator energy is included.

Detailed records: `research/iterations/0029_gravity_focusing_finite_source_gate.md`, `0030_gravity_modelS_projected_lens.md`, `0031_long_range_interaction_budget_gate.md`, `0032_passive_harmonic_mediator_budget_gate.md`.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body deposited-energy channels | **PARTIAL NEGATIVE — local density, local spin, extensive long-range pair and passive single-harmonic-mediator routes class-bounded; multi-mode/gapless/nonlinear/active/higher-body remain OPEN** |
| G3 maximum SM deposited solar-neutrino power | PARTIAL PASS — nuclear class bounds strong-negative; subleading/two-body/resonant and exotic many-body loopholes remain |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5 minimal BSM solution | LOCKED |
| G6 BSM constraints | LOCKED |
| G7 production/decay → inverse capture | PARTIAL PASS |
| G8 resonance integrated-strength/bandwidth | PARTIAL PASS — formal gate done, target-specific completion OPEN |
| G9 finite gravitational focusing gain | PARTIAL PASS — 23.5 AU scale robust; distant-source usefulness OPEN; solar self-lensing inapplicable |
| G10 staggered/multi-isotope fixed-mass-column gain | PARTIAL NEGATIVE for density-only energy gain; directional/CC-isotope-selective controls OPEN |

## Critical scope guards
1. Event/detection gain != energy-deposition gain.
2. Directional coherence != integrated opacity.
3. Peak resonance != flux-integrated capture.
4. Gravitational gain requires correct source geometry, finite source, Liouville and receiver integration.
5. Daughter/nuclear/external/mediator preparation energy is not neutrino-supplied power.
6. A few-target maximum is not a global SM ceiling.
7. Frozen gates are never relaxed after results.
8. Density/local-spin/long-range-pair/harmonic-mediator results are scoped theorems, not claims about arbitrary quantum fields.
9. No F9 multiplication of unvalidated gains.

## Chronology
`0001–0023`: baseline microphysics, solar/MSW authority and target validation; `0024` allowed bound; `0025` resonance area; `0026` finite-q leading envelope; `0027` density f-sum; `0028` local spin sum; `0029` rounded gravity + finite-source/Liouville; `0030` full Model-S gravity robustness; `0031` long-range pair budget; `0032` passive harmonic mediator budget.

## Current maturity
**NMIR_READINESS: 59%** (audit estimate).

56%→59% credit: +2% for the prospectively frozen hosted long-range interaction-budget class closure and +1% for the mediator-inclusive single-mode closure. This is not publication readiness and does not unlock BSM yet.

## Exact next funnel gates
1. **Full nuclear-current loopholes:** independently bound convection/recoil, axial charge, weak magnetism, induced pseudoscalar and genuine two-body currents for `E_nu<=20 MeV`. This is now the highest-value SM power gap.
2. **G8 target-specific resonance:** measured/evaluated entrance strength + physical source profile only; convert the formal area gate into a real W/kg ceiling.
3. **Residual many-body survivor:** multi-mode/gapless/nonlinear mediator and higher-body interactions, with complete medium/field energy accounting; active pumping tracked separately.
4. **G10 structured matter:** fixed-mass-column directional/CC-isotope-selective comparison.
5. **G9 source-class completion:** astrophysical source flux × finite-source/alignment duty cycle; no transparent-Sun gain for solar neutrinos.
