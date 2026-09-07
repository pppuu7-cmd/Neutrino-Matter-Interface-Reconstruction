# NMIR preregistration 0067 — Cu63 thermal-solar anti-nu_e high-energy-tail and rate gate

Date frozen: 2026-09-07
Status: PROSPECTIVE
Parent authority: iteration 0066 FAIL_KEEP_BSM_LOCKED_OPEN_SM_ACTIONABLE and concurrent G8 Cu63 exact-state result `b6553966b90cbe6a35662ba975507217ca6f04c9`.

## Scientific question
Does the physically calculated Standard-Model thermal-solar electron-antineutrino spectrum have a recoverable, non-invented differential flux at the exact Cu63 RIOEC resonance `E_R=162.496486 keV`, and if so what rate/power envelope follows from the independently evaluated exact crossed B(GT) range?

## Frozen target package
Channel: `63Cu(g.s.,3/2-) + anti-nu_e + e_K -> 63Ni*(87.220 keV,5/2-)`.
Use only the target inputs frozen by the prior exact-state authority package:
- `Q_epsilon = -66.945 keV` at the frozen precision;
- `E_x = 87.220 keV`;
- Ni K-vacancy comparator `E_b = 8.331486 keV`;
- `E_R = 162.496486 keV`;
- atomic-vacancy natural width about `1.39 eV`, retaining documented source-column uncertainty;
- reverse-strength envelope `B_reverse = 2.85e-3 ... 6.72e-2` (mandatory ~23.58x model spread).
Do not substitute the generic `|M|^2=0.1` ranking value.

## Source provenance requirement
Before any rate calculation, recover or independently recompute from primary Standard-Model thermal-solar-neutrino authority the **electron-antineutrino differential flux** at 162.496486 keV. The source model must explicitly cover that energy or supply equations/tables sufficient for controlled evaluation there.

Forbidden:
- reading/extrapolating a plotted spectrum by eye;
- replacing `anti-nu_e` with ordinary solar `nu_e` pp/CNO/B8 flux;
- assuming a Maxwell/Boltzmann tail without showing that the relevant thermal production channels and solar radial integral justify it;
- optimizing away the full B(GT) envelope.

## Calculations if source provenance passes
1. Freeze source spectrum/table/equations locally under `data/` with primary citation, version and hash when permitted.
2. Evaluate `dPhi_anti-nu_e/dE` at/over the physical resonance profile.
3. Use the RIOEC integrated-strength formalism, preserving the distinction between peak cross section and integrated entrance strength.
4. Fold the source profile with the resonance and the entire frozen reverse-B(GT) envelope.
5. Report events/(kg s), events/(kg day), and neutrino-supplied deposited-power ceiling in W/kg with `0 <= E_dep,nu <= E_nu`.
6. Daughter/atomic relaxation energy beyond neutrino-supplied energy must be separately ledgered and not credited as harvested neutrino power.

## Prospective classifications
- `PASS_G8_CU63_RATE_QUANTIFIED_STRONG_NEGATIVE` if the primary source is valid at 162.5 keV and the complete fold is reproducibly tiny relative to relevant NMIR benchmarks.
- `PASS_G8_CU63_RATE_SURVIVOR` only if a non-negligible rate survives with all source/strength/width constraints; this is not a technology claim.
- `BLOCKED_HIGH_ENERGY_TAIL` if primary authority does not support a controlled numerical electron-antineutrino spectrum at 162.5 keV.
- `SCIENTIFIC_FAIL_MODEL` if the implemented source/rate model fails an independent calibration or dimensional/normalization check.
- `INFRASTRUCTURE_FAIL` only for execution/tooling failure; never change physics criteria to obtain PASS.

## Next action
If strong-negative, re-run the formal BSM unlock audit against the newly closed G8 sub-branch while leaving the G3 contact residual explicit. If blocked, G8 remains evidence-blocked and the unlock audit may be reconsidered only under its original blocker-limited criterion. If survivor, continue G8 before BSM.
