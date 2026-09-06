# NMIR Discovery Funnel

## Purpose
NMIR is a model-agnostic discovery funnel for identifying, bounding or ruling out physically real neutrino↔matter/field interfaces and, where relevant, irreversible neutrino-supplied energy deposition. It is not a linear material search.

Common interface:

`Gamma = sum_ab integral dE d^3q dω Phi(E) K_ab(E,q,ω) S_ab(q,ω)`.

For energy harvesting,

`P_dep,nu = N_T integral dE Phi(E) mu(E,x) sigma_eff(E) E_dep,nu(E)`,

with frozen `E_dep,nu<=E_nu`. Daughter decay, nuclear mass release, mediator preparation, stored free energy and external pumping are never counted as neutrino-supplied power.

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

## Current funnel position — iteration 0041
- **Production↔absorption:** measured-ft route + validated two-state Li-7 PASS.
- **Validated passive targets:** Li-7, Se-82, Ga-71, Cl-37. Pure Li-7/GS98 leader `1.06589117e-21 W/kg`, still `~9.38e20` below 1 W/kg.
- **Leading allowed passive CC:** STRONG-NEGATIVE scoped envelope `9.419e-12 W/kg`.
- **Finite-q vector-charge/axial-spin:** STRONG-NEGATIVE envelope `1.2056895108e-9 W/kg`.
- **Omitted one-body nuclear currents:** `ONE_BODY_SUBLEADING_STRONG_NEGATIVE_SCOPED`; extreme full-one-body stress gives `1.0131561292e-8 W/kg`, still `9.87e7` below 1 W/kg.
- **Genuine two-body nuclear currents:** global theorem OPEN. Required extra amplitude to bridge to 1 W/kg is `r_bridge=28798.32`; known literature-scale corrections remain orders of magnitude short.
- **RIOEC resonance:** `RIOEC_B16_FLAVOR_NO_GO_PASS / RIOEC_AREA_PROFILE_PASS`. Ordinary pp-chain/CNO/B16 solar `nu_e` has zero RIOEC entrance factor; thermal solar pair-process `anti-nu_e` remains a distinct surviving source. Narrowing linewidth does not create integrated strength: rate tends to `B0*phi_anti-nu_e(E_R)`.
- **Real-resonance positive control:** Glashow resonance PASS as known SM resonance physics, but solar application fails kinematically at PeV energy.
- **Low-energy resonance design window:** F3 PASS only; target-specific RIOEC entrance strength × physical thermal-solar `anti-nu_e` spectrum remains OPEN. BSM remains LOCKED.
- **Coordinate-local density:** `PASS_DENSITY_FSUM`; no free superextensive energy-weighted density gain.
- **Bounded-local spin/magnon:** `PASS_LOCAL_SPIN_SUM`; O(N) at bounded coordination.
- **Passive long-range pair response:** `PASS_LONG_RANGE_BUDGET`; superextensive response tracks superextensive interaction budget.
- **Passive linear mediator/cavity:** `PASS_HARMONIC_MEDIATOR_BUDGET` and `PASS_MULTIMODE_LINEAR_BUDGET`; basis/mode count/softening do not create free energy gain when mediator energy is counted.
- **Passive convex homogeneous nonlinear mediator:** `PASS_NONLINEAR_HOMOGENEOUS_BUDGET`; extensivity requires the coupling scaling that removes free per-particle N-gain.
- **Passive metastable/non-convex avalanche:** iteration 0040 gives `PASS_METASTABLE_AVALANCHE_LEDGER / STRONG-NEGATIVE` for energy harvesting, but **PASS-SURVIVOR for detection/control**. Arbitrarily large signal gain can come from stored medium free energy, while neutrino-energy gain remains <=1 and cyclic reset must replenish the reservoir.
- **CEvNS source-opening kinematics:** iteration 0041 gives `CEVNS_SOURCE_OPENING_KINEMATICS_PASS / DETECTION_SURVIVOR / ENERGY_GAIN_NONE`. For Ar-40 and a 40-eV recoil threshold, exact inverse kinematics requires `E_nu>=0.862860938 MeV`; pp endpoint is closed, pep/B8 are open, and the 0.8618-MeV Be7 reference line has `Tmax=39.901698 eV`, only `0.098302 eV` below threshold. This forces a physical thermally broadened Be7 profile fold; no cross-section enhancement is inferred.
- **Gravitational focusing:** G9 PARTIAL PASS. Full Model-S projection gives `F_min=23.629351 AU`, 0.5504% from published 23.5 AU. This is distant-source-behind-Sun geometry, not solar self-lensing; usable finite magnification remains OPEN.
- **Staggered/multi-isotope geometry:** `G10_GEOMETRY_ONLY_STRONG_NEGATIVE / FIXED_COLUMN_MIXTURE_THEOREM_PASS`. Layer order/offset and passive isotope mixing cannot beat fixed microscopic `sigma/m`; only structures that change microscopic response remain under G2/G4/G8.
- **BSM:** LOCKED until target-specific low-energy resonance and genuine two-body/higher-body residuals are substantially bounded.

## Highest-value surviving branches
1. **G2 metastable CEvNS physical-spectrum fold:** use the already frozen thermally broadened Be7 profile and SM differential CEvNS response on Ar-40 to quantify the near-40-eV boundary, above-threshold cross section and events/kg/day. This tests a real detection survivor, not an energy-harvesting loophole.
2. **G8 target-specific thermal-solar antineutrino RIOEC resonance:** freeze a primary thermal-solar `anti-nu_e` spectrum plus one independently evaluated candidate and compute `B0*phi(E_R)`, events/kg/s and neutrino-only W/kg.
3. **Global two-body/higher-body nuclear-current residual:** seek a correlation-independent finite-range/saturation/sum-rule/operator bound.
4. **Residual active/driven or genuinely higher-body many-body sector:** complete source-resolved energy accounting before any gain claim.
5. **G9 astrophysical focusing:** distant-source flux × finite-source/alignment duty cycle, separate from solar capture.
6. **Minimal BSM only after unlock audit.**

## Research discipline
Class-level bounds dominate target scans. Negative results are discoveries because they shrink mechanism space; positive controls and detector survivors are retained only in their correct objective class. A gain must survive F0-F8 before F9 composition. BSM is opened only after remaining SM loopholes are quantitatively mature.

Current audit state: **`NMIR_READINESS: 71%`**.
