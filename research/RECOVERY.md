# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Funnel authority: `research/NMIR_FUNNEL.md`

## Mission and frozen accounting
NMIR is a discovery funnel over all plausible neutrino↔matter/field interfaces, not a linear material search. Distinguish state control, detection and focusing from true absorption and irreversible neutrino-sourced energy deposition.

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

Authority highlights:
- Ga71 full B16×spectrum×MSW PASS; run `34028394336`, artifact `9987793879`.
- Cl37 full fold PASS; run `34031200366`, artifact `9988653883`.
- Se82 point-Coulomb scientific FAIL `-32.6%`; finite-size repair `-0.453%`; full measured-response fold PASS, run `34033368287`, artifact `9989345911`.
- Li7 production↔absorption + two-state response matched-B8 residual `+1.454%`; full fold `34037570254`, artifact `9990650435`.
- In115 one-state model remains scientific FAIL as a complete response and is not authority.

## Class-level passive bounds
- `0024` leading-allowed envelope: `9.419449302949355e-12 W/kg`, STRONG_NEGATIVE_SCOPED; run `34038214660`, artifact `9990839187`.
- `0025` isolated-resonance area bound: `I_sigma <= 2*pi^2/k_r^2 * g * Gamma_in`; narrowing cannot create integrated entrance strength; run `34038642747`, artifact `9990968127`.
- `0026` finite-q vector-charge/axial-spin envelope: `1.2056895107775174e-9 W/kg`, STRONG_NEGATIVE; x1e6 omitted-current stress `1.2056895107775173e-3 W/kg`; run `34038882486`, artifact `9991038179`.
- Two-body/subleading-current sensitivity remains OPEN; conditional A=300 map needs `r≈192.63` per-pair norm ratio to bridge the finite-q envelope to 1 W/kg.
- `0027` coordinate-local density f-sum PASS/STRONG-NEGATIVE against free superextensive energy-weighted density gain; run `34039755966`, artifact `9991299921`.
- `0028` bounded-local spin first-moment PASS/STRONG-NEGATIVE against free superextensive local-magnon energy gain; run `34040105285`, artifact `9991400307`. Long-range/nonlocal response remains OPEN.

## G9 gravity — iterations 0029/0030
### 0029 rounded transparent-Sun + finite-source/Liouville control
Prospective contract `research/gravity_focusing_prereg.md`, commit `30f93fa94267fafdc1ca14d05b30f97b6af471ee`.

Patla & Nemiroff report transparent-Sun minimum focus `23.5 +/- 0.1 AU` and a rounded interior check near `b=0.024 R_sun`, projected mass `0.0137 M_sun`. NMIR rounded implementation gives `23.0291102335 AU`, residual `-2.004%`, inside frozen 3% tolerance.

Finite-source point-lens control: `mu_fs(rho)=sqrt(rho^2+4)/rho`, with Liouville/surface-brightness bookkeeping. Hosted baseline CI run `34040499051`, job `101506252362`: raw log `141 passed`.

### 0030 full independent Model-S projected lens
Prospective contract `research/gravity_modelS_prereg.md`, commit `a237aa336b52ba57bca57b5e289d4ca3505f4586`, frozen before implementation/result.

Independent Model-S density input is pinned at RAMSES commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`, blob `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`. For spherical density,

`M_2D(<b)=integral 4*pi*r^2*rho(r) f(b,r) dr`,

where `f=1` for `r<=b` and `f=1-sqrt(1-(b/r)^2)` otherwise; then

`F(b)=b^2 c^2/(4 G M_2D(<b))`.

Hosted authority: run `34041004727`, job `101507632178`, head `ea85975f083b24b6cdd47fd3209ff5dfe190c41a`, artifact `9991661778`, ZIP SHA256 `77b56826ee622042b57cfd658d2d4596d93b7f5c6f87aacf5e9b6a0592258d60`; dedicated tests `9 passed`, pinned Git blob matched exactly.

Raw results:
- synthetic uniform-sphere projection max rel. error `2.9062e-6`;
- integrated Model-S mass `1.9890968238e33 g`, relative error to frozen solar mass `4.86796e-5`;
- `M_2D(0.024R)/M_model = 0.01311330481`, only `4.282%` from rounded `0.0137`;
- `F(0.024R)=24.07378082 AU`, `2.442%` from 23.5 AU;
- full scan minimum **`F_min=23.62935116 AU`**, only **`0.5504%`** from 23.5 AU;
- sampled minimum at frozen lower scan edge `b/R=1e-4`, consistent with a finite central projected-surface-density limit.

Classification: **MODEL_S_ROBUSTNESS_PASS / G9 PARTIAL**. The ~23.5 AU scale is robust to an independent full solar density profile and is not an artifact of the rounded `0.024 R_sun` point.

Critical source-class guard: this lens geometry applies to a **distant source behind the Sun**. It cannot be multiplied into the Sun's own solar-neutrino flux. A receiver-integrated extended-source magnification is still required for astrophysical-source use.

Detailed records: `research/iterations/0029_gravity_focusing_finite_source_gate.md`, `research/iterations/0030_gravity_modelS_projected_lens.md`.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body deposited-energy channels | PARTIAL NEGATIVE — passive local density/spin class-bounded; long-range/nonlocal/active/itinerant OPEN |
| G3 maximum SM deposited solar-neutrino power | PARTIAL PASS — nuclear class bounds strong-negative; subleading/two-body/resonant/nonlocal loopholes remain; transparent-Sun self-lensing is inapplicable to solar source |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5 minimal BSM solution | LOCKED |
| G6 BSM constraints | LOCKED |
| G7 production/decay → inverse capture | PARTIAL PASS |
| G8 resonance integrated-strength/bandwidth | PARTIAL PASS — formal gate done, target-specific completion OPEN |
| G9 finite gravitational focusing gain | **PARTIAL PASS — 23.5 AU scale reproduced both by rounded check and independent full Model-S projection; distant-source finite magnification/usefulness OPEN** |
| G10 staggered/multi-isotope fixed-mass-column gain | PARTIAL NEGATIVE for density-only energy gain; directional/CC-isotope-selective controls OPEN |

## Critical scope guards
1. Event/detection gain != energy-deposition gain.
2. Directional coherence != integrated opacity.
3. Peak resonance != flux-integrated capture.
4. Gravitational gain must satisfy finite-source/Liouville/wave-optics limits and correct source geometry.
5. Projected atomic coverage != neutrino opacity.
6. Daughter/nuclear/external energy is not neutrino-supplied power.
7. A few-target maximum is not a global SM ceiling.
8. Negative approximations/infrastructure failures remain recorded; frozen gates are never relaxed.
9. Density f-sum is not a spin theorem; local-spin gate is not a long-range/nonlocal theorem.
10. No F9 multiplication of unvalidated gains.

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered material; `0006` ft→capture; `0007–0012` B16/MSW; `0013–0019` Ga/Cl folds and power; `0020–0021` In115 screen + Se82 authority; `0022–0023` Li7 authority; `0024` passive allowed bound; `0025` resonance formal gate; `0026` finite-q leading envelope; `0027` density f-sum; `0028` local spin sum rule; `0029` rounded transparent-Sun + finite-source/Liouville; `0030` full Model-S projected-lens robustness PASS.

## Current maturity
**NMIR_READINESS: 56%** (audit estimate).

55%→56% credit is limited to the prospectively frozen, hosted/raw-inspected independent full-profile G9 robustness result. No credit is assigned for an uncomputed usable magnification or for composing gravity with solar capture.

## Exact next funnel gates
1. **Long-range/nonlocal response:** derive the extensivity/energy-budget condition needed for a genuine all-to-all collective medium to beat the local density/spin sum-rule gates without importing external power. This is now the highest-value material survivor.
2. **G9 source-class completion:** quantify whether any distant astrophysical neutrino source, after finite-source/alignment duty-cycle limits, can compete with solar-neutrino energy flux; do not use transparent-Sun gain for solar neutrinos.
3. **Full nuclear-current loopholes:** bound convection/recoil, axial charge, weak magnetism, induced pseudoscalar and genuine two-body currents for `E_nu<=20 MeV`.
4. **G10 structured matter:** fixed-mass-column angle+solar-spectrum comparison for staggered/multi-isotope stacks.
5. **G8 target-specific resonance:** only measured/evaluated entrance strength + physical source profile may enter W/kg ranking.
