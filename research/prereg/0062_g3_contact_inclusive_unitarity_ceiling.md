# NMIR preregistration 0062 — G3 coefficient-independent inclusive unitarity ceiling

Date frozen: 2026-09-07
Status at freeze: PROSPECTIVE / NO RESULT INSPECTED
Parent authority: iteration 0059 leaves the absolute short-range/contact-current coefficient residual OPEN; iteration 0060 closes the separate actual-SM growing-coordination loophole in its audited scope; iteration 0061 closes the 10-kpc Galactic CCSN utility benchmark and makes G3 the highest-value OPEN class gate.

## Scientific question
Can the remaining short-range/contact-current residual be bounded without assuming EFT naturalness, a fitted `c_D` range, selected-nucleus two-body corrections, or any regulator/scheme-dependent coefficient prior, by using only S-matrix partial-wave unitarity plus finite target size and the already frozen solar-neutrino source set?

This is deliberately an **inclusive physical ceiling**, not a theorem about the contact coefficient itself.

## F0 objective
Primary score: maximum neutrino-supplied deposited power `W/kg` for a passive target under a coefficient-independent inclusive cross-section ceiling.

Secondary diagnostics: source-resolved ceiling, target-mass-number dependence, and distance to the `1 W/kg` benchmark.

No detector amplification, daughter decay energy, stored medium free energy, resonance gain, gravitational gain, geometry stacking or BSM factor may be multiplied.

## F1/F3 scope
- incoming particles: the already frozen Standard-Model solar neutrino source set used by the repository full-solar folds;
- target class: one nuclear species at fixed 1 kg target mass, with `1 <= A <= 250` treated as a continuous class envelope plus representative physical-nucleus controls when practical;
- short-range/contact residual only: finite interaction range is bounded by the nuclear target radius; genuinely long-range electromagnetic/mediator kernels are outside this gate and were separately audited in 0060;
- incident neutrinos are ultrarelativistic.

## Frozen geometry and kinematics
Use

`k = E_nu / (hbar c)`

and a deliberately conservative nuclear interaction radius

`R(A) = r0 A^(1/3)`, with `r0 = 1.4 fm`.

The enlarged `1.4 fm` coefficient is chosen prospectively to make the unitarity ceiling looser, not tighter. It must not be reduced after the result.

Define

`l_max(E,A) = ceil(k R(A))`

with a mandatory sensitivity control using `floor(kR)` plus the s-wave floor `l_max>=0`. The scientific ceiling must use the larger/conservative result.

## Partial-wave unitarity ceiling
For each included partial wave, use the deliberately conservative total-cross-section ceiling

`sigma_l <= 4 pi (2l+1) / k^2`.

Therefore

`sigma_unit(E,A) = 4 pi / k^2 * sum_{l=0}^{l_max} (2l+1)
                 = 4 pi (l_max+1)^2 / k^2`.

This is intentionally at least as loose as a pure reaction/absorption ceiling. The benchmark must also report the stricter black-disk/reaction normalization as a diagnostic when practical, but **scientific classification uses the larger total-cross-section ceiling** so that a negative conclusion cannot be manufactured by a normalization choice.

If a primary scattering-theory authority establishes a still larger correct inclusive coefficient for the stated convention before implementation, the code must adopt that larger value and document the change before any result-dependent benchmark is inspected. No smaller post-result coefficient is allowed.

## Fixed target-mass normalization
For 1 kg of a pure isotope/class point,

`N_T(A) = 1000 g / (A u)`.

No coherent `A^2` multiplier is added on top of the unitarity ceiling; doing so would double-count interaction strength already bounded by S-matrix unitarity.

## Deposited-energy ceiling
Use the maximally conservative neutrino-supplied bound

`E_dep,nu(E) = E_nu`.

Thus the class ceiling is

`P_unit(A) = N_T(A) integral dE Phi_solar(E) sigma_unit(E,A) E_nu`.

This intentionally overestimates passive deposited power because elastic neutrino scattering generally deposits only recoil energy and many channels leave outgoing-neutrino energy. The overestimate is frozen prospectively.

## Solar-source inputs and provenance
Use only locally frozen/pinned solar spectra already authoritative in NMIR for pp, both Be7 components/profiles, pep, N13, O15, F17, B8 and hep. Before the scientific run, the benchmark must enumerate every consumed file/blob/commit or call an existing repository loader whose inputs are themselves pinned in recovery authority.

Do not introduce chat-carried flux numbers.

## Numerical domain and low-energy guard
The integral must cover the full frozen source support. Because the `1/k^2` unitarity ceiling is intentionally loose at low energy, numerical quadrature must demonstrate convergence and separately report the pp low-energy contribution.

No ad-hoc low-energy cutoff may be inserted after seeing the result. If an existing frozen solar spectrum has a nonzero lower tabulation boundary, use that physical table boundary and document it; if the interpolation extrapolates to zero, the benchmark must use the repository's frozen interpolation convention.

## Prospective classifications
1. `PASS_CONTACT_RESIDUAL_BOUND_BELOW_1WKG`
   - the **larger conservative** inclusive unitarity ceiling, maximized over the frozen target class/domain and all frozen solar sources, is `< 1 W/kg`;
   - numerical convergence/provenance checks pass.
   This would close the remaining absolute contact-current residual at the 1-W/kg objective without claiming a coefficient theorem.

2. `PASS_UNITARITY_BOUND_VALID_BUT_TOO_WEAK / RESIDUAL_OPEN`
   - derivation/provenance/numerics pass but the conservative ceiling is `>=1 W/kg` for any allowed class point.
   This is an expected scientifically valid outcome. The threshold must **not** be weakened or the radius/partial-wave convention tightened post hoc.

3. `FAIL_UNITARITY_MODEL`
   - implementation violates a frozen formula, independent scattering-theory normalization check, units, positivity, or convergence criterion.

4. `BLOCKED_SOURCE_PROVENANCE`
   - the full frozen solar source set cannot be recovered locally/reproducibly without inventing numerical inputs.

Infrastructure failure is not scientific FAIL. Diagnose first causal infrastructure error, minimally fix, add regression coverage, rerun with unchanged physical criteria.

## Mandatory controls
- dimensional/unit tests for `k`, `sigma_unit`, target count and W/kg conversion;
- exact algebra check `sum_{l=0}^L (2l+1)=(L+1)^2`;
- cross-check against the s-wave `4 pi/k^2` limit for `kR<1`;
- `r0` sensitivity at least `1.2, 1.4, 1.6 fm`, with scientific result retaining the largest resulting ceiling;
- convergence under energy-grid refinement;
- source-resolved contributions;
- A-grid refinement and representative real-nucleus controls;
- no F9 multiplication.

## PASS/FAIL next action
- If `<1 W/kg`: reconcile G3 contact residual as objective-level class closure, then perform formal passive-SM residual/unlock audit before any BSM promotion.
- If `>=1 W/kg`: record that coefficient-independent unitarity is too weak; keep the contact residual OPEN and move to the next independent highest-value gate (currently G2 measured underground achievement anchor) rather than inventing a tighter coefficient prior.
- If source provenance blocks: repair provenance only; do not replace frozen source spectra with approximate chat values.
