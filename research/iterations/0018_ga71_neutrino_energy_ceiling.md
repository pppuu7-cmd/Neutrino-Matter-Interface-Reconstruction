# Iteration 0018 — Ga-71 neutrino-only deposited-energy ceiling

Date: 2026-09-06

## Frozen scientific question
For the already validated oscillated solar-neutrino capture fold on 71Ga, what is the strict upper bound on power attributable to energy carried by the incident neutrinos themselves, excluding daughter decay energy, nuclear-mass release, or any other energy reservoir not supplied by the incoming neutrino?

The prospective bound is

P_nu,max = N_T * 1e-36 s^-1 atom^-1 * (sum_i R_i <E_nu>_capture,i) * (MeV -> J),

where the energy-weighted capture moment is computed from the same B16 fluxes, pinned spectra, production-averaged day-side MSW Pee, and Bahcall-1997 71Ga response already used by the validated Ga SNU fold. Each successful event is credited with at most E_nu. Therefore this is an upper ceiling on neutrino-sourced deposited power, not a claim that all E_nu necessarily thermalizes locally.

## Implementation
- `src/nmir/ga71_power_ceiling.py`
- `tests/test_ga71_power_ceiling.py`
- `scripts/ga71_power_ceiling_benchmark.py`
- `.github/workflows/ga71-power-ceiling.yml`

No daughter half-life, daughter-decay Q value, or nuclear binding/mass-release term enters the ceiling.

## Hosted scientific authority
Workflow run: `34028394336`
Job: `101473373902`
Head: `a1bbb60f90cfd5146c24861098a15220db6bd1a1`
Conclusion: SUCCESS
Artifact: `9987793879`
Artifact ZIP SHA256: `bc0193112f2bdfb63438322a0b5cb702145dd6fd1e938f1be99ae4d5b66ade65`

### GS98
- total capture rate: `65.0099389504 SNU`
- energy-weighted capture moment: `75.7810357468 SNU MeV`
- capture-weighted incident neutrino energy: `1.1656838473 MeV`
- pure-71Ga neutrino-energy ceiling: `1.03091848153e-22 W/kg`

Dominant energy moments (SNU MeV): B8 `42.69685`, Be7 `15.80371`, pp `12.58974`; despite pp dominating event rate, B8 dominates the neutrino-carried energy moment because captured B8 neutrinos are much more energetic.

### AGSS09met
- total capture rate: `62.3178684931 SNU`
- energy-weighted capture moment: `66.3745623979 SNU MeV`
- capture-weighted incident neutrino energy: `1.0650968013 MeV`
- pure-71Ga neutrino-energy ceiling: `9.02953653311e-23 W/kg`

Dominant energy moments (SNU MeV): B8 `35.16880`, Be7 `14.42236`, pp `12.69393`.

## Classification
Scientific PASS for the **Ga-71 neutrino-carried energy upper-bound observable**. This does not yet close G3 globally: the matched Cl-37 power ceiling and a broader statement about the maximum achievable Standard-Model solar-neutrino deposited power across candidate targets remain open.

The result is already extremely small: even the larger GS98 pure-isotope ceiling is only about `1.03e-22 W/kg`, before accounting for incomplete local thermalization. Reaching 1 W/kg would therefore require a factor of about `9.7e21` relative to this validated Ga-71 neutrino-energy ceiling.

NMIR_READINESS: 36%

Next gate: compute the analogous Cl-37 neutrino-only energy ceiling with the frozen Be7 source-average authority and the residual 0.814–1.0 MeV envelope kept explicit; then combine Ga/Cl into the first quantitative G3 SM power ledger before moving to resonance-integrated-strength and other engineering claims.
