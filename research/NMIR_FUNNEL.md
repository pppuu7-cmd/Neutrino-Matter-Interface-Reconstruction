# NMIR Discovery Funnel

## Purpose
NMIR is not a linear search for one favored material or mechanism. It is a model-agnostic discovery funnel for identifying, bounding, or ruling out physically real ways to couple neutrinos to engineered matter/fields and, where relevant, to transfer neutrino-supplied energy irreversibly into matter.

The funnel is analogous in philosophy to DSIR/RQIR but has a different target:
- DSIR: theories -> common influence residual -> observable reconstruction.
- RQIR: candidate gravity/quantum interfaces -> consistency/comparator gates -> surviving model space.
- NMIR: all neutrino-coupling mechanisms -> common interaction/response interface -> hard physical bounds -> surviving capture/deposition strategies.

## Common interface
Every candidate mechanism must ultimately be expressible as a contribution to a neutrino interaction kernel or medium response,

`Gamma = sum_ab integral dE d^3q dω Phi(E) K_ab(E,q,ω) S_ab(q,ω)`.

Focusing/magnification remains explicit and multiplicative. For energy harvesting,

`P_dep,nu = N_T integral dE Phi(E) mu(E,x) sigma_eff(E) E_dep,nu(E)`,

with frozen guard `E_dep,nu <= E_nu`. Daughter decay, nuclear mass release, target preparation or externally supplied pumping energy are never counted as neutrino-supplied power.

## Funnel stages
### F0 — Define the physical objective
State control; detection/event enhancement; directional concentration; irreversible energy deposition; or true absorption/capture. A gain in one category is not promoted to another.

### F1 — Enumerate the interaction channel
SM charged current; SM neutral current; electromagnetic form factors; matter potential/forward scattering; many-body density/spin response; resonant inverse transition; gravitational focusing; engineered structure factor/metamaterial geometry; or BSM operator/mediator. Unknown/hybrid channels must map into the same interface.

### F2 — Production <-> absorption duality
For channels that produce neutrinos, construct the crossed/inverse process where allowed. Prefer measured decay strengths, ft values, B(GT), widths and branching data. A crossed ground-state anchor is not automatically a complete response.

### F3 — Kinematics and spectral overlap
Require threshold, momentum transfer, final-state phase space, source spectrum and physical line/continuum width to overlap.

### F4 — Microscopic strength
Compute or bound the elementary interaction strength with matched conventions and prefer primary response/decay data. Unvalidated approximations remain SCREENING only.

### F5 — Collective / coherent / resonant enhancement
Test claimed gains against structure-factor integration, response sum rules, linewidth-integrated strength, coherence volume, recoil/dephasing, finite source size and phase-space restrictions. Peak/directional gain or low detector threshold is not total opacity or energy deposition.

### F6 — Fundamental no-free-lunch gates
Apply unitarity/optical theorem; causality/Kramers-Kronig where applicable; response sum rules; detailed balance; conservation laws; Liouville/surface-brightness conservation for gravity; finite-source/wave-optics regularization; and fixed-mass-column controls for structured matter.

### F7 — Common quantitative score
Rank survivors by event rate/kg or area, optical depth, deposited-neutrino-energy W/kg, flux-integrated gain, pure/natural normalization and required enhancement to practical benchmarks.

### F8 — External reality constraints
Apply laboratory, solar, astrophysical, cosmological, material-stability and engineering constraints appropriate to the mechanism.

### F9 — Cross-channel composition
Only gains that individually survive F0-F8 may be multiplied:

`G_total = G_focus * G_resonance * G_material * G_geometry`.

No product of unvalidated gains is accepted.

### F10 — Discovery outcome
- **PASS-SURVIVOR:** quantitatively real gain survives applicable gates.
- **STRONG-NEGATIVE:** a broad class is bounded far below relevance.
- **SCIENTIFIC-FAIL:** a claimed mechanism fails a frozen physical gate.
- **BLOCKED:** missing primary data or genuinely external prerequisite.

## Current funnel position — iteration 0027
- **Production <-> absorption:** measured-ft route + externally validated two-state Li-7 response PASS.
- **Individually validated passive targets:** Li-7, Se-82, Ga-71 and Cl-37. Pure Li-7/GS98 is current target leader at `1.06589117e-21 W/kg`, still `~9.38e20` below 1 W/kg.
- **Leading allowed passive charged-current response:** STRONG-NEGATIVE scoped envelope `9.419e-12 W/kg` under deliberately extreme assumptions.
- **Leading finite-q one-body vector-charge/axial-spin multipoles:** STRONG-NEGATIVE envelope `1.206e-9 W/kg`; even a separate x1e6 omitted-current stress is only `1.206e-3 W/kg` and is not a theorem.
- **Two-body weak currents:** OPEN. Conditional sensitivity map says an A=300 pair-current model would need per-pair norm ratio `r~193` to bridge the remaining 1 W/kg gap; literature anchors are far smaller but no all-nucleus theorem is yet claimed.
- **Resonance:** formal integrated-area/source-overlap gate PASS. Narrowing increases peak without generating new integrated entrance strength. Target-specific `Gamma_in` + real solar line/profile W/kg remains OPEN.
- **Static naive macroscopic N^2 opacity:** strongly disfavored/negative.
- **Passive coordinate-local density response (phonons/crystals/staggered density layers):** `PASS_DENSITY_FSUM`, giving a scoped STRONG-NEGATIVE against superextensive energy-weighted density engineering. Lowering a collective mode energy by `1e6` gave unweighted-strength gain `1e6` but energy-weighted gain exactly `1.0`; f-sum scales as N, not N^2.
- **Spin/axial/magnon response:** OPEN and now the highest-value many-body survivor because the density f-sum theorem does not automatically apply to spin-dependent Hamiltonians.
- **Gravitational focusing:** OPEN; solar-limb weak-field reference exists, transparent-Sun finite-source/Liouville authority still required.
- **Staggered/multi-isotope material:** PARTIAL NEGATIVE for density-only energy gain; directional and charged-current/isotope-selective fixed-mass-column variants remain OPEN.
- **Active/non-equilibrium or nonlocal media:** OPEN but all external pumping energy must be tracked separately.
- **BSM solution branch:** LOCKED until the major passive-SM loopholes are substantially closed.

## Research discipline
The next iteration must advance the highest-value open funnel gate, not the most convenient calculation. Class-level bounds dominate target-by-target scans. Negative results are retained as discoveries because they shrink the surviving mechanism space. A candidate gain must survive its own F0-F8 gates before any composition in F9.

The scientific goal is:
1. map the complete plausible interaction space;
2. reduce it with hard theory and data;
3. identify any surviving channel whose integrated, physically usable coupling is parametrically larger than ordinary weak matter response;
4. if none survives in the SM, determine exactly which new operator/medium property is required and only then open the minimal BSM branch.

Current audit state: `NMIR_READINESS: 52%`.