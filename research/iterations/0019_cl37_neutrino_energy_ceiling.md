# Iteration 0019 — Cl-37 neutrino-only deposited-energy ceiling

Date: 2026-09-06

## Gate
Compute the Cl-37 analogue of the validated Ga-71 neutrino-supplied deposited-energy ceiling, preserving the authoritative Be7 source-average treatment and propagating the existing `0.814–1.0 MeV` continuum-response ambiguity instead of hiding it.

Prospective accounting rule remained unchanged from iteration 0018:

`E_dep,nu <= E_nu` per successful capture.

Daughter-decay energy, nuclear-mass release, externally supplied preparation energy, and other target-internal reservoirs are excluded. This is an upper bound on energy supplied by the incident neutrino, not an assumption that all incident energy becomes useful local heat.

## Implementation

Added:
- `src/nmir/cl37_power_ceiling.py`
- `tests/test_cl37_power_ceiling.py`
- `scripts/cl37_power_ceiling_benchmark.py`
- `.github/workflows/cl37-power-ceiling.yml`

The continuum fold uses the already frozen B16 fluxes, spectra, production-averaged MSW survival probability, and Bahcall-1996 Cl response. The Be7 contribution remains the Bahcall-Ulrich source-average authority; because only the 0.862-MeV Be7 line lies above the 0.814-MeV Cl threshold, its neutrino-energy moment is the authoritative capture rate multiplied by 0.862 MeV. Two pre-existing low-energy continuum conventions (`threshold_linear` and `zero_to_1`) are propagated as an explicit envelope.

## Hosted scientific result

Scientific workflow: run `34031200366`, job `101480904061`, head `f8c825802d02909bfcba49c31f6363e17887b4a8`.

Artifact: `9988653883`; uploaded ZIP SHA256 `d4ca449c691597c954fa9638f3b8fdaa15faf307f6dfc93b090a340651851837`.

### GS98

| quantity | threshold-linear | zero-to-1 |
|---|---:|---:|
| total rate [SNU] | 3.0259102626 | 3.0124469721 |
| energy moment [SNU MeV] | 22.6611607598 | 22.6485660026 |
| mean captured Eν [MeV] | 7.4890392619 | 7.5183285259 |
| pure-37Cl neutrino-energy ceiling [W/kg] | **5.9148281752e-23** | **5.9115407962e-23** |

The power-envelope fractional span is only `5.55786e-4` = **0.0556%**.

B8 dominates the GS98 neutrino-energy moment: `21.61176396 SNU MeV` out of `22.66116076`, with capture-weighted B8 neutrino energy `10.10091 MeV`. Be7 contributes only `0.53746805 SNU MeV` despite its important role in the low-energy response audit.

### AGSS09met

| quantity | threshold-linear | zero-to-1 |
|---|---:|---:|
| total rate [SNU] | 2.5653534895 | 2.5556370910 |
| energy moment [SNU MeV] | 18.7725068752 | 18.7634177894 |
| mean captured Eν [MeV] | 7.3177076579 | 7.3419727142 |
| pure-37Cl neutrino-energy ceiling [W/kg] | **4.8998440001e-23** | **4.8974716424e-23** |

The power-envelope fractional span is `4.84170e-4` = **0.0484%**.

## Validation

The same head baseline CI run `34031200372`, job `101480904147`, completed SUCCESS with **91 passed in 0.26 s**, followed by the baseline physics executable PASS. The scientific classification was made only after inspecting the raw benchmark JSON in the job log, not from workflow color alone.

No physical criterion, response normalization, spectrum, oscillation parameter, or residual convention was changed after seeing the result.

## Scientific interpretation

PASS: Cl-37 now has a reproducible neutrino-only W/kg upper bound under the same energy-accounting rule as Ga-71. The residual sub-1-MeV Cl response ambiguity that still moves the total SNU rate by about 0.4% moves the energy ceiling by only about 0.05%, because the energy moment is overwhelmingly B8-dominated.

The larger validated Cl value, `5.9148e-23 W/kg`, is about 1.74 times smaller than the validated pure-71Ga/GS98 ceiling `1.0309e-22 W/kg`. Thus higher capture-weighted neutrino energy does not compensate for the much lower Cl event rate.

`research/sm_power_ledger.md` now freezes the first Ga/Cl Standard-Model power ledger. This is explicitly a two-target benchmark, not yet a global cross-target SM ceiling.

## Next gate

Build a quantitative target-screening ledger for additional physically relevant Standard-Model inverse transitions, ranking event rate and neutrino-only W/kg with matched primary nuclear-response or measured-ft authority. The gate must include threshold/spectrum overlap and integrated resonance strength/linewidth where applicable; peak resonance values alone are forbidden. In parallel, G8/G9/G10 remain independent open gates.

## Readiness

`NMIR_READINESS: 38%`.

Increase from 36% to 38% is awarded only for the newly closed, hosted, reproducible Cl-37 W/kg gate plus the explicit two-target ledger. No credit is awarded for a global G3 closure, which remains open pending broader target screening.
