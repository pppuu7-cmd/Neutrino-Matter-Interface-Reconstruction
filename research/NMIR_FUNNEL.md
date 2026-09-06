# NMIR Discovery Funnel

## Purpose
NMIR is not a linear search for one favored material or mechanism. It is a model-agnostic discovery funnel for identifying, bounding, or ruling out physically real ways to couple neutrinos to engineered matter/fields and, where relevant, to transfer neutrino-supplied energy irreversibly into matter.

The funnel is analogous in philosophy to DSIR/RQIR but has a different target:
- DSIR: theories -> common influence residual -> observable reconstruction.
- RQIR: candidate gravity/quantum interfaces -> consistency/comparator gates -> surviving model space.
- NMIR: all neutrino-coupling mechanisms -> common interaction/response interface -> hard physical bounds -> surviving capture/deposition strategies.

## Common interface
Every candidate mechanism must ultimately be expressible as

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
Compute or bound elementary strength with matched conventions and primary response/decay data. Unvalidated approximations remain SCREENING only.

### F5 — Collective / coherent / resonant enhancement
Test claimed gains against structure-factor integration, response sum rules, linewidth-integrated strength, coherence volume, recoil/dephasing, finite source size and phase-space restrictions. Peak/directional gain or low detector threshold is not total opacity or energy deposition.

### F6 — Fundamental no-free-lunch gates
Apply unitarity/optical theorem; causality/Kramers-Kronig where applicable; response sum rules; detailed balance; conservation laws; Liouville/surface-brightness conservation for gravity; finite-source/wave-optics regularization; and fixed-mass-column controls for structured matter.

### F7 — Common quantitative score
Rank survivors by event rate/kg or area, optical depth, deposited-neutrino-energy W/kg, flux-integrated gain, pure/natural normalization and enhancement required to practical benchmarks.

### F8 — External reality constraints
Apply laboratory, solar, astrophysical, cosmological, material-stability and engineering constraints.

### F9 — Cross-channel composition
Only gains that individually survive F0-F8 may be multiplied:

`G_total = G_focus * G_resonance * G_material * G_geometry`.

No product of unvalidated gains is accepted.

### F10 — Discovery outcome
- **PASS-SURVIVOR:** quantitatively real gain survives applicable gates.
- **STRONG-NEGATIVE:** a broad class is bounded far below relevance.
- **SCIENTIFIC-FAIL:** a claimed mechanism fails a frozen physical gate.
- **BLOCKED:** missing primary data or external prerequisite.

## Current funnel position — iteration 0030
- **Production <-> absorption:** measured-ft route + externally validated two-state Li-7 PASS.
- **Validated passive targets:** Li-7, Se-82, Ga-71, Cl-37. Pure Li-7/GS98 leader `1.06589117e-21 W/kg`, still `~9.38e20` below 1 W/kg.
- **Leading allowed passive CC:** STRONG-NEGATIVE scoped envelope `9.419e-12 W/kg` under deliberately extreme assumptions.
- **Leading finite-q vector-charge/axial-spin multipoles:** STRONG-NEGATIVE envelope `1.206e-9 W/kg`; separate x1e6 omitted-current stress gives `1.206e-3 W/kg` but is not a theorem.
- **Two-body/subleading nuclear currents:** OPEN. Conditional map needs per-pair norm ratio `r~193` at A=300 to bridge the gap; no all-nucleus theorem yet.
- **Resonance:** formal integrated-area/source-overlap gate PASS. Target-specific entrance strength + physical solar profile remains OPEN.
- **Static naive macroscopic N^2 opacity:** strongly disfavored/negative.
- **Passive coordinate-local density response:** `PASS_DENSITY_FSUM`; softening by `1e6` increases unweighted strength `1e6` but energy-weighted strength `1.0`; first moment scales N.
- **Passive bounded-local spin/magnon response:** `PASS_LOCAL_SPIN_SUM`; first-moment envelope is O(N) for bounded coordination. Softening by `1e6` again gives energy-weighted gain `1.0`.
- **Long-range/nonlocal response:** OPEN. Unscaled all-to-all control is superextensive while Kac/extensivity scaling returns O(N); this is now the highest-value material survivor.
- **Gravitational focusing:** **PARTIAL PASS G9**. Rounded primary check and finite-source/Liouville subgate PASS. Independent full Model-S projection on hosted run `34041004727` gives `F_min=23.629351 AU`, only `0.5504%` from the published `23.5 AU`, with Model-S integrated-mass error `4.87e-5` and `M_2D(0.024R)/M=0.0131133`. Thus the short transparent-Sun focal scale is robust and not a one-point artifact. However the geometry is for a **distant source behind the Sun**, not the Sun's own neutrinos; usable receiver-integrated magnification remains OPEN and may not be composed with the solar-capture ledger.
- **Staggered/multi-isotope material:** PARTIAL NEGATIVE for density-only energy gain; directional and charged-current/isotope-selective fixed-column variants remain OPEN.
- **Active/non-equilibrium media:** OPEN, but all external pumping energy must be separately accounted.
- **BSM solution branch:** LOCKED until major passive-SM loopholes are substantially closed.

## Research discipline
The next iteration must advance the highest-value open funnel gate, not the most convenient calculation. Class-level bounds dominate target scans. Negative results are discoveries because they shrink mechanism space. A gain must survive its own F0-F8 gates before composition in F9.

The scientific goal is:
1. map plausible interaction space;
2. reduce it with hard theory/data;
3. identify any surviving channel with parametrically larger integrated usable coupling;
4. if none survives in the SM, determine exactly which new operator/medium property is required before opening minimal BSM.

Current audit state: `NMIR_READINESS: 56%`.
