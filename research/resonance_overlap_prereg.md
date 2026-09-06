# NMIR G8 preregistration — integrated resonance strength and spectral overlap

Date: 2026-09-06
Gate: G8 resonance integrated-strength/bandwidth/solar-overlap guard.

## Why this gate exists
A huge **peak** cross section from an ultranarrow resonance is not evidence for a large solar-neutrino interaction rate. The rate is an energy convolution, so a peak must be accompanied by its integrated area and by an incident spectral profile on the same energy scale.

Ordinary charged-current capture `nu + A -> B* + e-` into a discrete nuclear state is not automatically a Breit-Wigner resonance in the incident neutrino energy: the outgoing electron carries continuously variable kinetic energy. The G8 formulas below apply only when the physical channel genuinely has isolated-resonance kinematics (for example a two-body/bound-state/recoilless inverse channel).

## Frozen isolated-resonance convention
Use

`sigma(E) = pi/k_r^2 * g * Gamma_in*Gamma_out / ((E-Er)^2 + (Gamma/2)^2)`

in the narrow-resonance approximation where `k` is fixed at `k_r` across the line. Here `Gamma` is the total width and `Gamma_out <= Gamma`.

The Lorentzian identity

`integral dE / ((E-Er)^2 + (Gamma/2)^2) = 2*pi/Gamma`

gives

`I_sigma = integral sigma(E)dE = 2*pi^2/k_r^2 * g * Gamma_in * Gamma_out/Gamma`

and therefore the width-independent entrance-strength bound

`I_sigma <= 2*pi^2/k_r^2 * g * Gamma_in`.

This inequality is the primary G8 authority. Narrowing `Gamma` may increase the peak, but cannot increase the integrated area beyond the weak entrance width.

## Spectral-overlap inequality
For a non-negative incident differential number flux `phi(E)`,

`R_per_target = integral phi(E) sigma(E)dE`

obeys

`R_per_target <= sup_E phi(E) * I_sigma`.

For a normalized source line profile `rho(E)`, the line-averaged cross section obeys

`<sigma> <= ||rho||_infinity * I_sigma`.

Thus a claim based on `sigma_peak` alone is scientifically invalid. The relevant enhancement is controlled by integrated entrance strength multiplied by the source/resonance spectral overlap.

## Solar-source scope
- Continuum pp/hep/B8/CNO profiles may use the already frozen NMIR spectral tables.
- Thermally broadened Be7 profiles may use the already frozen Bahcall line-shape tables.
- The current bookkeeping-only monoenergetic pep line is **not** valid G8 resonance authority. A physical solar pep line profile/broadening model must be frozen before any narrow-resonance pep claim.
- No delta-function source may be used to evade the overlap bound.

## Prospective computational validation
Before promotion:
1. Numerically integrate Breit-Wigner profiles over widths spanning at least 12 decades and reproduce the analytic area to <=1e-4 relative error when the numerical domain/resolution is adequate.
2. At fixed `Gamma_in` and branching ratio, demonstrate that changing total width moves peak height but leaves the analytic area invariant when `Gamma_out/Gamma` is held fixed.
3. Verify `integral rho*sigma <= max(rho)*I_sigma` for broad Gaussian/Lorentzian test source profiles and several line offsets.
4. Include fail-closed guards for `Gamma_out>Gamma`, non-positive widths/energy/wavenumber/statistical factor, and non-normalizable/negative source profiles.
5. Hosted raw output must be inspected before scientific classification.

## Prospective classification
- `G8_FORMAL_PASS` if all identities/inequalities and numerical tests pass.
- This alone does **not** produce a numerical W/kg ceiling because `Gamma_in` remains target-specific weak authority.
- A resonant target may enter the G3 power ledger only after its `Gamma_in` (or equivalent measured ft/decay strength), branching, recoil-free/environment factor if applicable, and actual solar spectral overlap are frozen.

## Literature anchors
- Standard single-level Breit-Wigner reaction formula; e.g. modern nuclear-astrophysics treatments.
- D. Suzuki et al., Phys. Lett. B 687 (2010) 144–148, DOI 10.1016/j.physletb.2010.03.024: resonant-neutrino peak cross sections can be enormous, but energy spread/line broadening attenuates the mean cross section roughly through linewidth-to-source-width overlap.
