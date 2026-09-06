# NMIR Discovery Funnel

## Purpose
NMIR is not a linear search for one favored material or mechanism. It is a model-agnostic discovery funnel for identifying, bounding, or ruling out physically real ways to couple neutrinos to engineered matter/fields and, where relevant, to transfer neutrino-supplied energy irreversibly into matter.

The funnel is analogous in philosophy to DSIR/RQIR but has a different target:

- DSIR: theories -> common influence residual -> observable reconstruction.
- RQIR: candidate gravity/quantum interfaces -> consistency/comparator gates -> surviving model space.
- NMIR: all neutrino-coupling mechanisms -> common interaction/response interface -> hard physical bounds -> surviving capture/deposition strategies.

## Common interface
Every candidate mechanism must ultimately be expressible as a contribution to a neutrino interaction kernel or medium response,

Gamma = sum_ab integral dE d^3q dω Phi(E) K_ab(E,q,ω) S_ab(q,ω),

with any focusing/magnification factor kept explicit and multiplicative. For energy harvesting the scored quantity is

P_dep,nu = N_T integral dE Phi(E) mu(E,x) sigma_eff(E) E_dep,nu(E),

with the frozen guard E_dep,nu <= E_nu. Daughter decay energy, nuclear mass release, target preparation energy, or externally supplied pumping energy are never counted as neutrino-supplied power.

## Funnel stages

### F0 — Define the physical objective
A candidate must state which of these it targets:
1. state control / flavor-spin conversion;
2. detection/event-rate enhancement;
3. directional concentration/focusing;
4. irreversible energy deposition;
5. true absorption/capture.
A gain in one category is not silently promoted to another.

### F1 — Enumerate the interaction channel
Classify the channel before optimizing it:
- SM charged current;
- SM neutral current;
- electromagnetic neutrino form factors;
- matter potential / forward scattering;
- many-body density/spin response;
- resonant inverse transition;
- gravitational focusing;
- engineered structure factor / metamaterial geometry;
- BSM operator/mediator (locked as a solution branch until the SM funnel is quantitatively mature).
Unknown or hybrid channels may be added, but must be mapped into the same interface.

### F2 — Production <-> absorption duality
For any channel that produces neutrinos, explicitly construct the crossed/inverse process where allowed. Use measured decay strengths, ft values, B(GT), widths, branching fractions, or other primary response data whenever possible. Do not assume a ground-state crossed anchor is a complete multi-state response.

### F3 — Kinematics and spectral overlap
Require threshold, momentum transfer, final-state phase space, source spectrum, and line/continuum width to overlap. A formally large matrix element with no source overlap is rejected.

### F4 — Microscopic strength
Compute or bound the elementary interaction strength with matched conventions. Prefer direct experimental response/decay data. A candidate that relies on an unvalidated approximation remains SCREENING only.

### F5 — Collective / coherent / resonant enhancement
Test claimed gains against structure-factor integration, response sum rules, linewidth-integrated strength, coherence volume, recoil/dephasing, finite source size, and phase-space restrictions. Peak gain, directional gain, or low detector threshold is not total opacity.

### F6 — Fundamental no-free-lunch gates
Apply the relevant hard constraints:
- unitarity / optical theorem;
- causality / Kramers-Kronig where applicable;
- response sum rules;
- detailed balance;
- conservation of energy and momentum;
- Liouville / surface-brightness conservation for gravitational focusing;
- finite-source and wave-optics regularization;
- fixed mass-column comparisons for layered/metamaterial claims.

### F7 — Common quantitative score
All surviving candidates are ranked under common metrics:
- event rate per kg and/or per area;
- optical depth tau(E);
- deposited-neutrino-energy W/kg;
- flux-integrated gain over an explicitly frozen source spectrum;
- pure-isotope and natural-material normalization separately;
- required enhancement factor to reach practical benchmarks.

For energy claims the primary score is neutrino-only deposited power, never target-internal released energy.

### F8 — External reality constraints
Check laboratory, solar, astrophysical, cosmological, material-stability, and engineering constraints appropriate to the mechanism. A candidate is not promoted if its required parameter region is already excluded or physically unrealizable.

### F9 — Cross-channel composition
Only after individual gains survive F0-F8 may they be multiplied or combined, e.g.

G_total = G_focus * G_resonance * G_material * G_geometry.

No product of unvalidated gains is accepted.

### F10 — Discovery outcome
A branch exits the funnel in exactly one of four states:
- PASS-SURVIVOR: quantitatively real gain survives all applicable gates;
- STRONG-NEGATIVE: a broad class is bounded far below relevance;
- SCIENTIFIC-FAIL: the claimed mechanism fails a frozen physical gate;
- BLOCKED: missing primary data or genuinely external prerequisite.

## Current funnel position
As of the current repository state:
- leading allowed passive charged-current nuclear response: broad STRONG-NEGATIVE scoped bound;
- resonance: formal integrated-strength/overlap gate PASS, target-specific entrance-width numerics still open;
- production<->absorption: measured-ft route and Li-7 two-state response PASS;
- static naive macroscopic N^2 opacity: strongly disfavored/negative;
- many-body spin/magnon deposited-energy channel: open;
- finite gravitational focusing: open;
- staggered/multi-isotope fixed-mass-column gain: open;
- first-forbidden/higher multipole passive nuclear loophole: open;
- BSM solution branch: locked until passive-SM loopholes are substantially closed.

## Research discipline
The next iteration must advance the highest-value open funnel gate, not merely the most convenient calculation. Repeating nearby isotopes/materials is low priority once a broader class bound is available. Negative results are retained as discoveries because they shrink the surviving mechanism space.

The scientific goal is therefore not 'find something eventually'. It is:

1. map the complete plausible interaction space;
2. reduce it with hard theory and data;
3. identify any surviving channel whose integrated, physically usable coupling is parametrically larger than ordinary weak matter response;
4. if none survives in the SM, determine exactly what new operator/medium property would be required and only then open the minimal BSM branch.
