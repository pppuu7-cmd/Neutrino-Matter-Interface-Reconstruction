# NMIR prereg — detector-transfer rate requirement from validated ideal CEvNS

Date: 2026-09-06
Status: prospective; frozen before implementation/result inspection.

## Question
Given already validated ideal full-solar CEvNS rates, what average recoil acceptance × live fraction is required for a realistic target mass to produce an experimentally useful accepted-event count?

This gate does not assume a measured low-energy efficiency curve. It derives the transfer-function requirement that future detector data must satisfy.

## Frozen design objective
Primary practical proxy: pure Ar40, detector mass `M=10 kg`, target yield `N_goal=10 accepted solar CEvNS events/year`.

Use validated iteration-0045 ideal rates:
- Ar40, 10 eV: `R=6.486648607e-3 events/(kg day)`;
- Ar40, 20 eV: `R=3.617516800e-3 events/(kg day)`;
- Ar40, 40 eV: `R=1.161110164e-3 events/(kg day)`.

Secondary exposure controls:
- Si28, 10 eV: `4.3476963498860904e-3 events/(kg day)`;
- Ge74, 10 eV: `7.871654050e-3 events/(kg day)`;
- Se82, 10 eV: `8.212077955e-3 events/(kg day)`.

Use `365.25 day/year`.

## Factorized first design envelope
Define the spectrum-averaged accepted fraction

`eta = <epsilon_NR> * f_live`, with `0<=eta<=1`.

For this design gate only,

`N_acc/year = M_kg * R_ideal * 365.25 * eta`.

Thus

`eta_required = N_goal / (M_kg R_ideal 365.25)`.

Equivalent effective mass/exposure requirement for `N_goal` events/year is

`M_eff_required = N_goal/(R_ideal*365.25)`

where `M_eff = M*eta`.

This factorized form is not a substitute for the later full recoil-dependent convolution `epsilon_NR(T,state)`; it is a necessary exposure condition.

## Frozen classifications for 10-kg Ar / 10 events per year
- `RATE_FEASIBLE_TRANSFER_TARGET` if `eta_required <= 1`.
- `RATE_IMPOSSIBLE_AT_FIXED_MASS` if `eta_required > 1`.

Prospective topology criterion:
- 10 eV and 20 eV must be classified individually from their frozen rates;
- 40 eV is an independent boundary control;
- no threshold criterion may be changed after inspection.

## Additional outputs
Report:
- ideal events/year at eta=1;
- eta required for 1 and 10 events/year for Ar10/20/40;
- effective kg required for 1 and 10 events/year for Si10, Ge10, Se10 and Ar10/20/40;
- ratio of required effective kg for Ar10 relative to Se10 optimum.

## Scope guards
- This is event-rate feasibility, not interaction enhancement and not neutrino-energy gain.
- `eta<=1` feasibility does not mean such efficiency/background performance has been demonstrated.
- Backgrounds, false triggers, threshold dispersion and a full `epsilon_NR(T)` remain the next detector-specific gate.
- Metastable avalanche energy remains stored-target energy.
- Do not import Fermilab calibration-site background rates as universal detector backgrounds.

## Required evidence
Deterministic module, dedicated tests, JSON benchmark, fail-closed hosted workflow, raw log/artifact inspection, numbered iteration note and RECOVERY reconciliation.
