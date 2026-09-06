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

## Current funnel position — iteration 0032
- **Production↔absorption:** measured-ft route + validated two-state Li-7 PASS.
- **Validated passive targets:** Li-7, Se-82, Ga-71, Cl-37. Pure Li-7/GS98 leader `1.06589117e-21 W/kg`, still `~9.38e20` below 1 W/kg.
- **Leading allowed passive CC:** STRONG-NEGATIVE scoped envelope `9.419e-12 W/kg`.
- **Leading finite-q vector-charge/axial-spin:** STRONG-NEGATIVE envelope `1.206e-9 W/kg`; separate x1e6 omitted-current stress `1.206e-3 W/kg` is robustness only, not a theorem.
- **Two-body/subleading nuclear currents:** OPEN; conditional A=300 map needs per-pair norm ratio `r~193` to bridge the finite-q gap.
- **Resonance:** integrated-area/source-overlap formal gate PASS; target-specific entrance strength + physical source profile OPEN.
- **Static naive macroscopic N² opacity:** strongly disfavored.
- **Coordinate-local density response:** `PASS_DENSITY_FSUM`; soft-mode event strength can grow while energy-weighted first moment remains fixed; O(N), not free N².
- **Bounded-local spin/magnon:** `PASS_LOCAL_SPIN_SUM`; O(N) at bounded coordination.
- **Passive long-range pair response:** `PASS_LONG_RANGE_BUDGET`. For additive bounded neutrino operator, `|m1|<=8 o0² sum||h_ij||`; any superextensive response bound tracks a superextensive absolute interaction budget. Kac/extensive scaling removes the per-particle gain.
- **Passive common harmonic mediator/cavity:** `PASS_HARMONIC_MEDIATOR_BUDGET`. Including mediator displacement energy gives `E_field=|E_induced|~g_N²N²`; extensive Dicke scaling `g_N~1/sqrt(N)` gives `J_eff~1/N` and no parametric per-particle gain.
- **Residual many-body survivor:** multi-mode/gapless/nonlinear mediators, active/driven media and genuine higher-body interactions remain OPEN, with complete energy accounting required.
- **Gravitational focusing:** G9 PARTIAL PASS. Independent full Model-S projection gives `F_min=23.629351 AU`, only 0.5504% from published 23.5 AU. This is a distant-source-behind-Sun geometry, not solar-neutrino self-lensing; usable finite magnification remains OPEN.
- **Staggered/multi-isotope:** PARTIAL NEGATIVE for density-only energy gain; directional/CC-isotope-selective fixed-column variants OPEN.
- **BSM:** LOCKED until major SM loopholes are substantially closed.

## Highest-value surviving branches
1. **Full nuclear-current sector:** recoil/convection, axial charge, weak magnetism, induced pseudoscalar and genuine two-body currents.
2. **Target-specific genuine resonances:** measured entrance strength convolved with real solar line/continuum profiles.
3. **Residual exotic many-body sector:** multi-mode/gapless/nonlinear mediator or higher-body response with all field/medium energy included.
4. **Directional/isotope-selective structured matter.**
5. **Astrophysical gravitational focusing**, source-flux and duty-cycle ranked separately from solar capture.

## Research discipline
Class-level bounds dominate target scans. Negative results are discoveries because they shrink mechanism space. A gain must survive its own F0-F8 gates before F9 composition. BSM is opened only after remaining SM loopholes are quantitatively mature.

Current audit state: **`NMIR_READINESS: 59%`**.
