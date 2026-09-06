# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Recovery protocol: `research/RECOVERY_MANUAL.md`
Funnel authority: `research/NMIR_FUNNEL.md`
Latest immutable scientific record: `research/iterations/0042_cevns_be7_physical_profile_gate.md`

## Recovery rule
Chat history is not scientific authority. A new session must read, in order: `RECOVERY_MANUAL.md`, this file, `NMIR_FUNNEL.md`, newest iteration/prereg files, recent commits, then raw terminal GitHub Actions results. If newer commits exist than this reconciliation, reconcile them before new science. Do not duplicate queued/in-progress work.

## Mission and frozen accounting
NMIR is a discovery funnel over plausible neutrino↔matter/field interfaces, not a linear material search. Distinguish:
1. state control/redirection/focusing;
2. interaction/capture probability;
3. detector visibility/event amplification;
4. irreversible neutrino-sourced deposited energy.

Frozen power accounting:

`P_dep = N_T integral dE mu(E,x) Phi(E) sigma(E) E_dep,nu(E)`

with `0 <= E_dep,nu <= E_nu`. Daughter decay, nuclear mass release, target preparation, stored medium free energy, external pumping, cavity/mediator preparation and extra thermalization are never counted as neutrino-supplied power. Unvalidated gains are never multiplied.

General many-body response:

`Gamma = sum_ab integral d^3q dω K_ab(E_nu,q,ω) S_ab(q,ω)`.

Energy-deposition scoring includes the corresponding `ω` weight and must obey positivity, kinematics, conservation laws, applicable sum rules, causality/stability and energy-budget constraints.

## Frozen baseline authority
- Xe-132 ideal low-q CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; Xe-like mean free path `~3.08e16 m`.
- Minimal Dirac magnetic moment (`m_nu=0.05 eV`): `~1.6e-20 mu_B`; ideal 1-m spin-precession maximum `~3.35e17 T`.
- Tritium measured-ft inverse capture: `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fluxes; pinned pp/hep/B8/CNO spectra; thermally broadened Be7 profile; daytime adiabatic 3-flavour MSW for charged-current electron-neutrino folds, Earth regeneration OFF.

## Individually validated G3 solar-capture targets
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

Current validated target leader is pure `7Li/GS98 = 1.06589117e-21 W/kg`, still `~9.38e20` below 1 W/kg.

## Broad class-level closures / no-free-lunch gates
Do not reopen these without a genuinely new assumption; exact derivations are in immutable iteration notes.

- `0024` leading-allowed nuclear envelope: `9.419449302949355e-12 W/kg`, `STRONG_NEGATIVE_SCOPED`; run `34038214660`, artifact `9990839187`.
- `0025` isolated-resonance area theorem: line narrowing cannot create integrated entrance strength; run `34038642747`, artifact `9990968127`.
- `0026` finite-q vector-charge/axial-spin envelope: `1.2056895107775174e-9 W/kg`; even x1e6 omitted-current stress gives `1.2056895107775173e-3 W/kg`; run `34038882486`, artifact `9991038179`.
- `0027` coordinate-local density f-sum: no free superextensive energy-weighted density/phonon gain; run `34039755966`, artifact `9991299921`.
- `0028` bounded-local spin first moment: no free superextensive local-magnon energy gain; run `34040105285`, artifact `9991400307`.
- `0031` long-range pair budget: `|m1| <= 8 o0^2 W_N`; an extensive absolute interaction budget enforces extensive response; run `34041247733`, artifact `9991728037`.
- `0032` common harmonic mediator: `E_field=|E_induced|=g_N^2 O^2/(2 kappa)`; extensive/Dicke scaling removes per-particle N gain; run `34041392001`, artifact `9991770130`.
- `0033` omitted one-body nuclear currents: deliberately extreme complete one-body stress gives `1.0131561292246442e-8 W/kg`, still `9.87e7` below 1 W/kg. Required extra amplitude to reach 1 W/kg: `r_bridge=28798.3217`. Known selected-nucleus two-body corrections are vastly smaller, but a universal two-/higher-body theorem remains OPEN. Run `34042934477`, job `101512822458`, artifact `9992226798`.
- `0034` geometry-only staggered/fixed-column theorem: layer order/offset does not change `1-exp(-sum tau)` at fixed microscopic response; isotope mixtures cannot beat the best component in `sigma/m` at fixed mass column; run `34043114890`, job `101513298058`, artifact `9992278460`.
- `0038` passive finite linear multimode mediator: `E_field=|E_induced|=1/2 O^T G^T K^-1 G O`; adding modes or approaching a positive soft mode does not create free energy gain. A coupled exact zero mode lacks stable passive equilibrium. Run `34047675712`, job `101525546661`, artifact `9993592020`.
- `0039` passive convex positive homogeneous nonlinear mediator: Euler homogeneity gives `b·x*=pV(x*)`, `|E_induced|=(p-1)V(x*)`; extensive scaling removes free per-particle N gain. Run `34048018268`, job `101526462429`, artifact `9993688056`.

## G8 resonance branch
- `0035`: RIOEC is incident `anti-nu_e`; ordinary B16 pp/CNO solar `nu_e` has zero entrance factor. Thermal solar pair-process antineutrinos are a distinct eligible source. Lorentzian area/profile checks verify that narrowing alone does not create integrated strength. Run `34043507541`, artifact `9992388766`.
- `0036`: Glashow resonance is a real SM positive control for strong resonant enhancement but sits at ~6.325 PeV, far outside the <=20 MeV solar window.
- `0037`: low-energy resonance kinematic design window passed. RIOEC matching `E_R=-Q_epsilon+E_x+E_b` is only a kinematic condition. Target-specific evaluated entrance strength × physical thermal-solar `anti-nu_e` spectrum remains OPEN/BLOCKED rather than using blanket matrix elements. Run `34044012213`, artifact `9992535787`.

## G9 gravity
- `0029`: rounded transparent-Sun focal benchmark ~23.03 AU plus finite-source/Liouville control.
- `0030`: full Model-S projected-density calculation gives `F_min=23.62935116 AU`, only `0.5504%` from the published ~23.5 AU scale; run `34041004727`, artifact `9991661778`.
Classification: `MODEL_S_ROBUSTNESS_PASS / G9 PARTIAL`. This is a distant-source-behind-Sun geometry, not solar-neutrino self-lensing. Usable distant-source magnification after finite source/alignment/duty-cycle accounting remains OPEN.

## Iteration 0040 — metastable / avalanche interface
Prospective contract: `research/metastable_avalanche_prereg.md`.
Hosted run `34048287780`, job `101527189597`, artifact `9993764694`, artifact SHA256 `c9221192087c1d38171fc849e2ff5bb44e3f5f76859c6fa12fb89e9ed8e4f619`; raw `7 passed`.

A 1-eV neutrino trigger plus a 1-MeV stored reservoir can create signal gain `1,000,001`, while source-resolved neutrino-energy gain stays exactly `1.0`. In 5000 randomized positive ledgers the maximum relative conservation residual was `2.220192245414529e-16`.

Classification: **energy harvesting `STRONG_NEGATIVE_SCOPED`; detector/control `PASS-SURVIVOR`.** The neutrino may trigger a macroscopic phase transition, but released stored free energy belongs to the target and cyclic reset must replenish it.

## Iteration 0041 — Ar-40 CEvNS threshold/source opening
Prospective contract: `research/cevns_source_opening_prereg.md`.
Hosted run `34049714420`, job `101530992980`, artifact `9994165815`.

Exact CEvNS recoil kinematics:
`T_max=2E_nu^2/(M+2E_nu)`,
`E_min(T)=0.5[T+sqrt(T^2+2MT)]`.

For Ar-40 at `40 eV`, `E_nu,min=0.8628609380456526 MeV`. pp endpoint is closed (`Tmax~9.48 eV`), nominal Be7 861.8-keV line is only ~0.10 eV below recoil threshold, pep/B8 are open. This demanded a physical Be7 line-profile fold.

## Iteration 0042 — physical Be7 profile × Ar-40 CEvNS
Immutable authority: `research/iterations/0042_cevns_be7_physical_profile_gate.md`.
Prospective contract: `research/cevns_be7_profile_prereg.md`.
Frozen local source profile: `data/be7_bahcall1994_ground_profile.csv`, sourced from Bahcall 1994 via pinned PEANUTS commit/blob provenance.
Workflow head `a0d50d8d8bcfb8fffa0c5c95362d4527d25a3d15`; hosted run `34050807911`; job `101533964874`; artifact `9994471349`; artifact SHA256 `510b200aa3d6b723c025b61280edd547f6716c3e6b0cb1b17fc53db254be9cdb`; raw dedicated tests `7 passed`.

Profile normalization: `1.0`.
Zero-threshold dominant-line profile-averaged ideal CEvNS cross section: `1.4066113108028225e-42 cm^2`.

At **40 eV**:
- `E_nu,min = 0.8628609380456526 MeV`;
- line-profile fraction above `E_min = 0.3110401476`;
- above-threshold profile-averaged cross section `6.901317324978097e-48 cm^2`;
- retained CEvNS fraction only `4.906342834e-6`;
- ideal B16-GS98 dominant-Be7 rate `3.973604373e-8 events/(kg day)` ≈ `1.45e-5 events/(kg year)`.

Threshold sensitivity:
- 20 eV retains `0.2497027274` of the CEvNS cross section and gives `2.022320664e-3 events/(kg day)` ≈ `0.738 events/(kg year)`;
- 10 eV retains `0.5622758944` and gives `4.553823547e-3 events/(kg day)` ≈ `1.662 events/(kg year)`;
- zero-threshold dominant-line ideal ceiling is `8.098912994e-3 events/(kg day)` ≈ `2.956 events/(kg year)`.

Scientific classification: **`DETECTION PASS-SURVIVOR`, but 40-eV Be7 is `RATE_STRONGLY_ENDPOINT_SUPPRESSED`; interaction enhancement NONE; neutrino-energy gain NONE.** Thermal broadening makes the channel nonzero but does not make a 40-eV detector practically efficient for the dominant Be7 line because recoil phase space collapses at endpoint.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body/deposited-energy/detection channels | **PARTIAL: major passive local/long-range/linear/convex-homogeneous free-energy-gain classes bounded; metastable avalanche is a detector survivor; Be7 physical-profile rate closed for Ar threshold map; cross-target solar optimization + real detector efficiency/dark-count model OPEN** |
| G3 maximum SM deposited solar-neutrino power | **PARTIAL PASS — leading, finite-q and one-body-current sectors strong-negative; universal genuine two-/higher-body residual and target-specific thermal-antineutrino resonance remain OPEN** |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5 minimal BSM solution | LOCKED |
| G6 BSM constraints | LOCKED |
| G7 production/decay → inverse capture | PARTIAL PASS |
| G8 resonance integrated-strength/bandwidth | **PARTIAL PASS — area/source/flavor/kinematic controls passed; target-specific evaluated RIOEC entrance strength × thermal-solar anti-nu_e fold OPEN/BLOCKED** |
| G9 finite gravitational focusing gain | PARTIAL PASS — ~23.5 AU transparent-Sun scale robust; distant-source usefulness OPEN; solar self-lensing inapplicable |
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
9. Geometry-only G10 does not cover structure-induced microscopic response changes.
10. No F9 multiplication of unvalidated gains.
11. RIOEC is an electron-antineutrino entrance channel; ordinary B16 solar `nu_e` flux must never be inserted into its rate.
12. Kinematic resonance matching alone is not a microscopic-strength or rate PASS.
13. Metastable amplification requires an explicit stored-free-energy/reset ledger.
14. Detector-threshold opening is not cross-section enhancement; near-boundary sources require physical spectral folding.
15. A nonzero endpoint-tail rate is not automatically a practically useful detector rate.

## Chronology
`0001–0023`: baseline microphysics, solar/MSW authority and target validation; `0024` allowed bound; `0025` resonance area; `0026` finite-q envelope; `0027` density f-sum; `0028` local spin sum; `0029–0030` gravity; `0031` long-range pair budget; `0032` harmonic mediator; `0033` omitted one-body currents + two-body distance; `0034` fixed-column theorem; `0035` RIOEC source/flavor + area; `0036` Glashow positive control; `0037` low-energy resonance window; `0038` passive linear multimode; `0039` passive convex homogeneous nonlinear; `0040` metastable avalanche; `0041` CEvNS source opening; `0042` physical Be7-profile CEvNS rate.

## Current maturity
**NMIR_READINESS: 72%** (audit estimate).

71%→72% credit: +1% for a prospectively frozen, hosted and raw-inspected F7 physical source-profile rate closure that converts the Ar-40/40-eV near-threshold statement into a quantitative result. The recovery manual itself earns no scientific-readiness credit; it improves reproducibility only.

## Exact next funnel gates
1. **G2 inverse metastable-target optimization:** at fixed target mass and threshold grid, fold the full frozen pp + Be7 + pep + CNO + B8/hep solar spectra through ideal CEvNS for candidate nuclei. Optimize events/kg/day above threshold over nuclear mass/weak charge rather than assuming Ar. Explicitly test the 1–20 eV region and report which source component dominates. Use nuclear form factors where they become material.
2. **G2 real detector ledger:** for any experimentally motivated metastable target, fold nucleation/recoil efficiency, threshold distribution/stability, dark counts/backgrounds, reset/dead time and stored-energy cost. Keep signal amplification separate from microscopic interaction rate.
3. **G8 target-specific thermal-solar antineutrino RIOEC:** require independently evaluated entrance strength × primary thermal `anti-nu_e` spectrum; remain BLOCKED rather than substituting blanket strengths.
4. **Global two-/higher-body nuclear residual:** seek a finite-range/saturation/sum-rule/operator bound without promoting selected-nucleus calculations to a theorem.
5. **G9 distant-source utility:** physical astrophysical source flux × full finite-source/alignment/duty-cycle magnification; do not use transparent-Sun gain for solar neutrinos.
6. **BSM unlock audit:** only after G8 and the genuine two-/higher-body residual are substantially bounded.
