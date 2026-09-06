# NMIR Discovery Funnel

## Purpose
NMIR is a model-agnostic discovery funnel for identifying, bounding or ruling out physically real neutrino↔matter/field interfaces and, where relevant, irreversible neutrino-supplied energy deposition. It is not a linear search for one favored material.

Common interface:

`Gamma = sum_ab integral dE d^3q dω Phi(E) K_ab(E,q,ω) S_ab(q,ω)`.

For energy harvesting,

`P_dep,nu = N_T integral dE Phi(E) mu(E,x) sigma_eff(E) E_dep,nu(E)`,

with frozen `E_dep,nu<=E_nu`. Daughter decay, nuclear mass release, mediator preparation and external pumping are never counted as neutrino-supplied power.

## Funnel stages
- **F0 objective:** state control, detection, focusing, irreversible deposition or true capture; never promote one into another.
- **F1 channel:** SM CC/NC, electromagnetic form factors, matter potential, many-body density/spin, resonant inverse transition, gravity, engineered geometry or later BSM.
- **F2 production↔absorption:** use measured ft/B(GT)/width/branching authority where possible.
- **F3 kinematics/spectral overlap:** threshold, q, phase space and physical source profile must overlap.
- **F4 microscopic strength:** matched conventions; unvalidated approximations remain screening.
- **F5 collective/resonant gain:** enforce integrated structure factors, coherence volume, linewidth and dephasing.
- **F6 no-free-lunch:** unitarity, sum rules, detailed balance, conservation, Liouville, finite source, fixed mass column and complete medium/field energy accounting.
- **F7 common score:** event rate, optical depth, neutrino-only W/kg, flux-integrated gain and enhancement required to practical benchmarks.
- **F8 external constraints:** laboratory, solar, astrophysical, cosmological, stability and engineering.
- **F9 composition:** only individually validated gains may multiply.
- **F10 outcome:** PASS-SURVIVOR, STRONG-NEGATIVE, SCIENTIFIC-FAIL or BLOCKED.

## Current funnel position — iteration 0037
- **Production↔absorption:** measured-ft route + validated two-state Li-7 PASS.
- **Validated passive targets:** Li-7, Se-82, Ga-71, Cl-37. Pure Li-7/GS98 leader `1.06589117e-21 W/kg`, still `~9.38e20` below 1 W/kg.
- **Leading allowed passive CC:** STRONG-NEGATIVE scoped envelope `9.419e-12 W/kg`.
- **Leading finite-q vector-charge/axial-spin:** STRONG-NEGATIVE envelope `1.2056895108e-9 W/kg`.
- **Omitted one-body nuclear currents:** `ONE_BODY_SUBLEADING_STRONG_NEGATIVE_SCOPED`. With deliberately extreme `p/M<=1`, `q<=40.511 MeV`, triangle component count and extra factor-2 amplitude safety, full recoil/convection + axial charge + weak magnetism + electron-channel induced pseudoscalar gives only `1.0131561292e-8 W/kg`, still `9.87e7` below 1 W/kg.
- **Genuine two-body nuclear currents:** global theorem OPEN, but known-current data are extraordinarily distant from the bridge. Required extra amplitude `r_bridge=28798.32`; literature-scale 0.03, 0.30 and 0.61 corrections are short by ~`9.60e5`, `9.60e4` and `4.72e4` in amplitude respectively. Even artificial `r=1000` gives only `1.208e-3 W/kg`.
- **RIOEC resonance:** iteration 0035 gives `RIOEC_B16_FLAVOR_NO_GO_PASS / RIOEC_AREA_PROFILE_PASS`. RIOEC requires incident `anti-nu_e`, so ordinary B16 pp-chain/CNO solar `nu_e` contributes exactly zero. Thermal solar pair-process antineutrinos are a distinct surviving source. For a continuous source, linewidth narrowing raises the peak but does not create integrated strength; the narrow-resonance rate tends to `B0*phi_anti-nu_e(E_R)`.
- **G8 real-resonance positive control:** iteration 0036 gives `G8_REAL_RESONANCE_POSITIVE_CONTROL_PASS`. The observed Glashow mechanism yields `E_R≈6.325 PeV`, demonstrating that known resonance physics can make a neutrino interaction cross-section scale enormously larger than ordinary MeV weak interactions. It fails the solar application on kinematics. No Glashow gain is composed with solar capture.
- **G8 low-energy resonance design window:** iteration 0037 gives `G8_LOW_ENERGY_RESONANCE_WINDOW_PASS`. For stationary-electron s-channel kinematics, the frozen 0–20 MeV solar window maps to `0.51099895 < M_* <= 4.5498437255 MeV`; thermal 10 eV–5 keV maps to only ~`0.010–4.976 keV` mass excess above the electron. This is F3 kinematics only: no Standard-Model state is asserted and BSM remains LOCKED. For RIOEC, `E_R=-Q_epsilon+E_x+E_b`; 10 eV, 1 keV and 5 keV resonances correspond to generic ~`1e-5`, `1e-3` and `5e-3` cancellation of MeV-scale terms. Candidate-specific entrance strength × physical thermal-solar `anti-nu_e` spectral density remains OPEN.
- **Validated narrow solar-line control:** in Li7, the thermally broadened Be7 line supplies `21.04%` of events but only `4.535%` of the neutrino-energy moment; event/energy fraction ratio `4.6407`. Thus line matching can improve event selectivity without becoming an energy-harvesting gain.
- **Mössbauer-antineutrino concept:** theory-positive idealized H3-He3 resonant capture around 18.6 keV with peak scale ~`5e-32 cm^2`, but material realization remains unvalidated because recoil-free fraction/broadening/lattice effects are not closed.
- **Static naive macroscopic N² opacity:** strongly disfavored.
- **Coordinate-local density response:** `PASS_DENSITY_FSUM`; soft-mode event strength can grow while energy-weighted first moment remains fixed; O(N), not free N².
- **Bounded-local spin/magnon:** `PASS_LOCAL_SPIN_SUM`; O(N) at bounded coordination.
- **Passive long-range pair response:** `PASS_LONG_RANGE_BUDGET`; superextensive response tracks a superextensive absolute interaction budget; Kac/extensive scaling removes per-particle gain.
- **Passive common harmonic mediator/cavity:** `PASS_HARMONIC_MEDIATOR_BUDGET`; including mediator energy makes the same scaling explicit; Dicke `g_N~1/sqrt(N)` gives `J_eff~1/N`.
- **Residual many-body survivor:** multi-mode/gapless/nonlinear mediators, active/driven media and genuine higher-body interactions remain OPEN, with complete energy accounting required.
- **Gravitational focusing:** G9 PARTIAL PASS. Full Model-S projection gives `F_min=23.629351 AU`, 0.5504% from published 23.5 AU. This is distant-source-behind-Sun geometry, not solar self-lensing; usable finite magnification remains OPEN.
- **Staggered/multi-isotope geometry:** `G10_GEOMETRY_ONLY_STRONG_NEGATIVE / FIXED_COLUMN_MIXTURE_THEOREM_PASS`. For fixed microscopic cross sections, `A=1-exp(-sum tau_j)` makes layer order/offset irrelevant, fixed-mass mixtures cannot beat best `sigma/m`, and slab tilt cannot increase total captured power. Under a deliberately enormous stressed weak cross section, a 2 Å ideal layer has `tau=6.19e-17` and would need `1.62e16` layers (~3234 km) for tau~1. Only structures that change microscopic `sigma(E,q)` remain open under G2/G4/G8.
- **BSM:** LOCKED until target-specific low-energy resonance and genuine two-body/higher-body residuals are substantially bounded. The Glashow control and low-energy design window may define kinematic requirements only; they do not unlock a new operator.

## Highest-value surviving branches
1. **G8 target-specific thermal-solar antineutrino RIOEC resonance:** freeze a primary thermal-solar `anti-nu_e` spectrum and one evaluated candidate from Akhmedov-Lasserre-Maturi 2026 with `Q_epsilon`, daughter excitation, captured-shell binding/width and entrance strength; compute `B0*phi_anti-nu_e(E_R)`, events/kg/s and neutrino-only W/kg. The RIOEC paper emphasizes that for continuous spectra the resonance enables access to very low energies rather than a generic rate enhancement.
2. **Global two-body/higher-body nuclear-current residual:** seek a correlation-independent finite-range/saturation/sum-rule bound.
3. **Residual exotic many-body sector:** multi-mode/gapless/nonlinear mediator or higher-body response with all field/medium energy included.
4. **Astrophysical gravitational focusing:** distant-source flux and alignment duty cycle, separate from solar capture.
5. **Minimal BSM only after unlock audit.**

## Research discipline
Class-level bounds dominate target scans. Negative results are discoveries because they shrink mechanism space; positive controls are equally important because they show which physical ingredient can genuinely alter the interaction scale. A gain must survive its own F0-F8 gates before F9 composition. BSM is opened only after remaining SM loopholes are quantitatively mature.

Current audit state: **`NMIR_READINESS: 66%`**.
