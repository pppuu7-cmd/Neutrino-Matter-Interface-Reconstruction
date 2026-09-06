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
- Ga71: full B16×spectrum×MSW PASS; run `34028394336`, artifact `9987793879`.
- Cl37: full fold PASS; run `34031200366`, artifact `9988653883`.
- Se82: point-Coulomb scientific FAIL `-32.6%`; finite-size repair `-0.453%`; 9-component validation PASS; full fold run `34033368287`, artifact `9989345911`.
- Li7: production↔absorption from evaluated Be7 EC + independent 429-keV state; matched-B8 total residual `+1.454%`; full fold `34037570254`, artifact `9990650435`.
- In115 one-state model remains scientific FAIL as a complete response and is not authority.

## Class-level passive bounds already closed/scoped
- Iteration 0024 leading-allowed envelope: `9.419449302949355e-12 W/kg`, STRONG_NEGATIVE_SCOPED; run `34038214660`, artifact `9990839187`.
- Iteration 0025 isolated-resonance integrated area: `I_sigma <= 2*pi^2/k_r^2 * g * Gamma_in`; line narrowing cannot create integrated entrance strength; run `34038642747`, artifact `9990968127`. Target-specific resonance remains OPEN.
- Iteration 0026 finite-q vector-charge/axial-spin envelope: `1.2056895107775174e-9 W/kg`, STRONG_NEGATIVE; x1e6 omitted-current stress `1.2056895107775173e-3 W/kg`; run `34038882486`, artifact `9991038179`.
- Two-body/subleading-current sensitivity remains OPEN; diagnostic needs `r≈192.63` at A=300 to bridge the finite-q envelope to 1 W/kg.
- Iteration 0027 coordinate-local density f-sum PASS/STRONG-NEGATIVE against free superextensive energy-weighted density gain; run `34039755966`, artifact `9991299921`.
- Iteration 0028 bounded-local spin first-moment PASS/STRONG-NEGATIVE against free superextensive local-magnon energy gain; run `34040105285`, artifact `9991400307`. Long-range/nonlocal spin remains OPEN.

## Iteration 0029 — G9 transparent-Sun focal-scale + finite-source/Liouville subgate
Prospective contract `research/gravity_focusing_prereg.md`, commit `30f93fa94267fafdc1ca14d05b30f97b6af471ee`.

Patla & Nemiroff (ApJ 685, 1297; arXiv:0711.4811) report a transparent-Sun minimum focal distance `23.5 +/- 0.1 AU` and quote a rounded interior check using projected mass `0.0137 M_sun` at `0.024 R_sun`. NMIR implementation commit `1afc10d2c6272a55ef007506113b1aed5ac1a364` gives `23.0291102335 AU`, a `-2.004%` residual, within the prospectively frozen 3% tolerance for those rounded inputs.

Finite-source point-lens control:
`mu_fs(rho)=sqrt(rho^2+4)/rho`,
with numerical disk averaging and Liouville/surface-brightness bookkeeping tests at commit `5d339d180441458c0f8e137382e0ece6eba2de0e`.

Hosted authority: baseline CI run `34040499051`, job `101506252362`, head `5d339d180441458c0f8e137382e0ece6eba2de0e`; raw log inspected: `141 passed in 1.29s`, baseline physics executable SUCCESS.

Classification: **G9_FOCAL_SCALE_PASS / FINITE_SOURCE_LIOUVILLE_PASS**, but G9 overall remains PARTIAL because full extended-Sun finite-source receiver-integrated magnification is still OPEN. No focusing gain is composed with capture yet.

Detailed record: `research/iterations/0029_gravity_focusing_finite_source_gate.md`.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body deposited-energy channels | PARTIAL NEGATIVE — passive local density/spin class-bounded; long-range/nonlocal/active/itinerant OPEN |
| G3 maximum SM deposited solar-neutrino power | PARTIAL PASS — validated targets + allowed/finite-q class bounds; subleading/two-body/resonant/nonlocal/focusing loopholes remain |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5 minimal BSM solution | LOCKED |
| G6 BSM constraints | LOCKED |
| G7 production/decay → inverse capture | PARTIAL PASS |
| G8 resonance integrated-strength/bandwidth | PARTIAL PASS — formal gate done, target-specific completion OPEN |
| G9 finite gravitational focusing gain | **PARTIAL PASS — published 23.5 AU scale reproduced from rounded primary inputs; finite-source/Liouville regularization PASS; extended-lens gain OPEN** |
| G10 staggered/multi-isotope fixed-mass-column gain | PARTIAL NEGATIVE for density-only energy gain; directional/CC-isotope-selective controls OPEN |

## Critical scope guards
1. Event/detection gain != energy-deposition gain.
2. Directional coherence != integrated opacity.
3. Peak resonance != flux-integrated capture.
4. Gravitational gain must satisfy finite-source/Liouville/wave-optics limits.
5. Projected atomic coverage != neutrino opacity.
6. Daughter/nuclear/external energy is not neutrino-supplied power.
7. A few-target maximum is not a global SM ceiling.
8. Negative approximations/infrastructure failures remain recorded; frozen gates are never relaxed.
9. Density f-sum is not a spin theorem; local-spin gate is not a long-range/nonlocal theorem.
10. No F9 multiplication of unvalidated gains.

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered material; `0006` ft→capture; `0007–0012` B16/MSW; `0013–0019` Ga/Cl folds and power; `0020–0021` In115 screen + Se82 authority; `0022–0023` Li7 authority; `0024` passive allowed bound; `0025` resonance formal gate; `0026` finite-q leading envelope; `0027` density f-sum; `0028` local spin sum-rule gate; `0029` transparent-Sun focal-scale + finite-source/Liouville PASS subgate.

## Current maturity
**NMIR_READINESS: 55%**.

54%→55% credit is only for the prospectively frozen, hosted/raw-inspected G9 focal-scale reproduction plus finite-source/Liouville regularization. Full extended-Sun magnification remains open and receives no credit.

## Exact next funnel gates
1. **G9 gravity:** construct an extended transparent-Sun projected-mass lens from primary SSM data and compute finite-source receiver-integrated gain versus observer distance/source angular size before composition with capture.
2. **Long-range/nonlocal response:** characterize interaction-range/energy scaling needed to beat local density/spin extensivity without importing external energy.
3. **Full nuclear-current loopholes:** bound convection/recoil, axial charge, weak magnetism, induced pseudoscalar and genuine two-body currents for `E_nu<=20 MeV`.
4. **G10 structured matter:** fixed-mass-column angle+solar-spectrum comparison for staggered/multi-isotope stacks.
5. **G8 target-specific resonance:** only measured/evaluated entrance strength + physical source profile may enter W/kg ranking.
