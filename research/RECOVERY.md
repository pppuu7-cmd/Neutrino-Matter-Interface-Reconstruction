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

## Iteration 0024 — passive leading-allowed target-space bound
Prospective commit `88bf3a6718122a354f6bada3ad2fb43d58371392`. With deliberately extreme `A<=300`, `Z_f<=119`, zero threshold/excitation, `E_nu<=20 MeV` and artificial neutrino energy flux `2000 W/m^2`:
- leading-allowed envelope **`9.419449302949355e-12 W/kg`**;
- deficit to 1 W/kg `1.0616e11`;
- separate x1e6 stress `9.419e-6 W/kg`.
Run `34038214660`, artifact `9990839187`. **STRONG_NEGATIVE_SCOPED**.

## Iteration 0025 — G8 resonance integrated-strength gate
Prospective commit `31bd2467140cdfcfeede18de115934904849eb3d`.

For isolated resonance:
`I_sigma <= 2*pi^2/k_r^2 * g * Gamma_in`.
Line narrowing raises peak but does not create integrated weak entrance strength. Run `34038642747`, artifact `9990968127`: peak gain `1e6` under 1e6 narrowing while integrated area stayed fixed. **G8_FORMAL_PASS**. Target-specific entrance strength + physical solar profile still OPEN.

## Iteration 0026 — finite-q leading multipole envelope
Prospective commit `c3a29bc01b2af4f68ca1a6cf55447c6200e28c81`.
- finite-q leading vector-charge/axial-spin envelope **`1.2056895107775174e-9 W/kg`**;
- deficit `8.294e8`;
- separate x1e6 omitted-current stress `1.2056895107775173e-3 W/kg`, still factor `829.4` below 1 W/kg.
Run `34038882486`, artifact `9991038179`. **FINITE_Q_LEADING_STRONG_NEGATIVE**. Omitted currents are not covered by theorem.

## Two-body-current sensitivity map — OPEN diagnostic
Commit `e40759020746eca3a8a73439773d9ae0717b81c2`. Conditional pair-current model `G_2body=[1+(A-1)r/2]^2` says at `A=300` one would need `r≈192.63` to lift the iteration-0026 envelope to 1 W/kg. Literature anchors are qualitatively far smaller, but this is not an all-nucleus bound and receives no readiness credit.

## Iteration 0027 — passive density-response f-sum
Prospective commit `0fbc3f1977630add7eb15896f7da2458742e8df7`.

For coordinate-local passive density response,
`m1(q)=integral dω ω S(q,ω)=q^2/2 sum_i g_i^2/m_i`.
Hence for `0<=K<=Kmax`, `D<=Kmax*m1`.

Hosted run `34039755966`, job `101504245884`, artifact `9991299921`, digest `064566b0bf75040f35c0308f0b8fe53103e995a175ce5c06bb6d694467cde6be`; 5 tests PASS. Raw results:
- max m1 error `0.0`;
- max unit-kernel error `1.79856e-16`;
- low collective mode: unweighted gain `1e6`, energy-weighted gain `1.0`;
- `N=1 -> 1e6` f-sum gain `~1e6`, not `1e12`.

**PASS_DENSITY_FSUM / STRONG-NEGATIVE scoped** against free superextensive energy-weighted density engineering. Density phonons/crystals/staggered layers may improve detectability/directionality but cannot manufacture new integrated energy-weighted strength under these assumptions.

## Iteration 0028 — local spin/axial first-moment gate
Prospective contract `research/spin_local_sum_prereg.md`, commit `c68cc0da22abc5a11ee248d341473733b7f1084d`.

For `H=sum_X h_X`, `O=sum_i g_i S_i^a`:
`m1 = 1/2 <[O^dagger,[H,O]]>` and
`|m1| <= 2 sum_X ||h_X|| ||O_X||^2`.
For pairwise spin-1/2 Heisenberg bonds:
`|m1| <= (3/2) sum_bonds |J_ij|`.
For bounded coordination `z`, `|J|<=Jmax`:
`|m1| <= (3/4) N z Jmax`, extensive in N.

Hosted authority: run `34040105285`, job `101505185065`, head `336d01532d9ed2fdcc5665e63a3fc5e4329e6b26`, artifact `9991400307`, digest `c0dc0698997fa43b54be8d93a247068a1d213785b7e3922f20a260047c4e7ece`; 5 tests PASS. Raw log inspected.

| diagnostic | result |
|---|---:|
| pair-specialization error | `0.0` |
| local `N=1 -> 1e6` first-moment gain | **`1e6`** |
| soft-mode unweighted gain | **`1e6`** |
| soft-mode energy-weighted gain | **`1.0`** |
| all-to-all unscaled gain, `N=1000 -> 1e6` | `1001000.0` |
| all-to-all Kac-scaled gain | `1000.0` |

Classification: **PASS_LOCAL_SPIN_SUM / STRONG-NEGATIVE scoped** against free superextensive energy-weighted gain in passive bounded-local spin/magnon systems. Crucially, the unscaled all-to-all control is superextensive, so genuinely long-range/nonlocal interactions remain a distinct surviving loophole rather than being assumed away.

Detailed records: `research/iterations/0027_density_fsum_gate.md`, `research/iterations/0028_local_spin_sum_gate.md`.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE — naive N² opacity disfavored; density/local-spin energy-weighted N² rescue constrained |
| G2 many-body deposited-energy channels | **PARTIAL NEGATIVE — passive local density and local-spin branches class-bounded; long-range/nonlocal/active/itinerant remain OPEN** |
| G3 maximum SM deposited solar-neutrino power | **PARTIAL PASS — validated targets + allowed/finite-q class bounds; subleading/two-body/resonant/nonlocal/focusing loopholes remain** |
| G4 engineered resonance/polarization/periodicity | PARTIAL — local passive density/spin energy gain constrained; nonlocal/active and target-specific resonance OPEN |
| G5 minimal BSM solution | LOCKED |
| G6 BSM constraints | LOCKED |
| G7 production/decay → inverse capture | PARTIAL PASS |
| G8 resonance integrated-strength/bandwidth | PARTIAL PASS — formal gate done, target-specific completion OPEN |
| G9 finite gravitational focusing gain | OPEN |
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
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered material; `0006` ft→capture; `0007–0012` B16/MSW; `0013–0019` Ga/Cl folds and power; `0020–0021` In115 screen + Se82 authority; `0022–0023` Li7 authority; `0024` passive allowed bound; `0025` resonance formal gate; `0026` finite-q leading envelope; `0027` density f-sum; `0028` local spin sum-rule gate.

## Current maturity
**NMIR_READINESS: 54%** (audit estimate).

52%→54% credit is only for the prospectively frozen, hosted/raw-inspected local spin-response class gate. It closes the ordinary bounded-local magnon route as a source of free superextensive energy-weighted gain but explicitly leaves long-range/nonlocal, active/itinerant, nuclear-current, target-specific resonance and gravitational focusing loopholes open.

## Exact next funnel gates
1. **G9 gravity:** reproduce the transparent-Sun `~23.5 AU` benchmark and then derive finite-source/Liouville magnification bounds before composing with capture.
2. **Long-range/nonlocal response:** characterize what interaction-range/energy-scaling is required to beat the local density/spin extensivity gates without simply importing external energy.
3. **Full nuclear-current loopholes:** bound convection/recoil, axial charge, weak magnetism, induced pseudoscalar and genuine two-body currents over `E_nu<=20 MeV`.
4. **G10 structured matter:** fixed-mass-column angle+solar-spectrum comparison for staggered/multi-isotope stacks; surviving claims must be directional, CC/isotope-selective or outside local response assumptions.
5. **G8 target-specific resonance:** only measured/evaluated entrance strength + physical source profile may enter W/kg ranking.