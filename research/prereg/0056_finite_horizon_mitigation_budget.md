# NMIR 0056 preregistration — finite-horizon factorized LEE mitigation budget

Date: 2026-09-07
Gate: G2 finite-horizon detector mitigation budget
Status at preregistration: OPEN

## Question
After closing the 0055 waiting-only requirement map, what independently demonstrated non-time-domain background suppression is still required within a practical <=3-year program, once CEvNS signal acceptance is charged explicitly rather than treated as free?

## Frozen baseline
- 0053 stress background: `B0053 = 4.482974815542e9 accepted events/year`.
- 0053 5σ, 30% nuisance improvement requirement: `G0053 = 4.1485517170734453e9`.
- 0051 design point: `S0=10 accepted signal events/year`, `Z=5`, fractional background-normalization nuisance `delta_B=0.30`.
- 0051 background ceiling is recomputed with the existing `background_nuisance` implementation whenever signal acceptance changes.

## Frozen 3-year time branches
1. `authority_cap`: `R_time=100`. This is the last directly published CRESST waiting benchmark (~900 d / roughly multi-year operation). It is the conservative authority-limited branch.
2. `stress_extrapolation`: `R_time=10^(3*365.25/450)=272.27013080779125`. This is the 0055 mathematical continuation only, not a CRESST forecast.

The two factors are alternatives and must never be multiplied.

## Signal-acceptance accounting
For a combined remaining mitigation handle with CEvNS signal acceptance `epsilon_S`:

### Fixed-exposure mode
Keep the 0053 exposure fixed. The accepted signal becomes `S=10*epsilon_S`; recompute the 5σ/30% background ceiling `Bmax(S)`. Required independent background rejection is

`R_other_fixed = (B0053/R_time) / Bmax(10*epsilon_S)`.

### Signal-restored exposure mode
Increase exposure by `1/epsilon_S` to restore `S=10/year`. This also scales the pre-selection background by `1/epsilon_S`. Required independent rejection is

`R_other_restored = (B0053/(R_time*epsilon_S)) / Bmax(10)`.

This branch is a requirements map, not permission to assume unlimited detector mass/exposure.

Evaluate `epsilon_S={1.0,0.9,0.8,0.7,0.5,0.3}`.

## Factorization diagnostic
At `epsilon_S=1`, report the equal-factor value required if the remaining rejection were provided by `n={2,3,4,5}` truly independent handles: `F_n = R_other^(1/n)`. This is only a scale diagnostic; no independence is assumed.

## PASS criteria
- reproduce the frozen 0051 `Bmax(10)=1.0806120114381677/year` within numerical tolerance;
- `R_time(stress)>R_time(authority_cap)` and therefore leaves a smaller residual requirement;
- at `epsilon_S=1`, `R_other = G0053/R_time` in both exposure modes;
- decreasing `epsilon_S` never improves the required rejection in either exposure mode;
- restored-exposure mode obeys exactly `R_other = G0053/(R_time*epsilon_S)`;
- equal-factor products reconstruct the parent requirement;
- all values finite and positive.

Classification on PASS: `PASS_FINITE_HORIZON_MITIGATION_BUDGET`.

## Interpretation guard
Public DoubleTES evidence demonstrates a topology handle but does not publish a directly comparable rejection×signal-acceptance factor over the 0053 10–300 eV stress window. Segmentation/veto likewise has no frozen comparable LEE rejection factor here. Therefore 0056 may quantify what is required but must not fill missing factors with guessed performance.

## Exact next action after PASS
Compare the required factor scale against newly published/measured detector-specific rejection and intrinsic-LEE suppression data. If no independent quantitative anchors close the budget, retain G2 as `QUANTITATIVE_GAP_OPEN` rather than multiplying projections or correlated handles.