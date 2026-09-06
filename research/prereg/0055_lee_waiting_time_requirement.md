# NMIR 0055 preregistration — LEE waiting-time requirement map

Date: 2026-09-06
Gate: G2 time-domain mitigation / long-term cryogenic operation
Status at preregistration: OPEN

## Question
Can the observed/projected time dependence of CRESST low-energy-excess populations, by itself, retire the 0053 billion-scale detector gap on a practical timescale while preserving a steady solar-CEvNS signal?

## Frozen baseline
Use the 0053 total improvement requirement for the 0051 design point `S=10/year`, 5σ, 30% accepted-background normalization nuisance:

`G0053 = 4.1485517170734453e9`.

This is a deliberately severe stress requirement under fixed present LEE-per-kg scaling, not a prediction of future kg-scale detectors.

## Frozen time-dependence authorities
### Projection/benchmark branch
CRESST next-generation report, DOI `10.1038/s42005-025-02476-5`, arXiv:2505.01183:
- ~10× LEE reduction after ~450 d;
- ~100× after ~900 d;
- these are upgrade benchmark/projection factors, not a demonstrated detector-wide exponential law over arbitrary times.

For a **mathematical stress extrapolation only**, define the log-linear continuation exactly consistent with those two points:

`R_proj(t) = 10^(t / 450 d)`.

Do not call values beyond 900 d a CRESST prediction.

### Measured fast-component branch
DoubleTES 2024, DOI `10.1140/epjc/s10052-024-13282-8`, arXiv:2404.02607:
- absorber-band above-ground LEE component in 28–50 eV has measured single-exponential decay time `tau_fast = 10.2 ± 1.1 d`.

Define the **counterfactual component-only** reduction
`R_fast(t;tau) = exp(t/tau)`.
This branch is forbidden from being interpreted as the full detector-wide LEE because DoubleTES also observes other components and explicitly notes that a single-TES component can be constant or slowly decaying.

## Frozen outputs
1. Exact stress-extrapolation waiting time `t_req_proj = 450 d * log10(G0053)` needed for `R_proj=G0053`.
2. Residual gap `G0053/R_proj(t)` at horizons 450 d, 900 d, 3 y, 5 y, 10 y, with `365.25 d/y`.
3. Counterfactual fast-component time `t_req_fast=tau ln(G0053)` for tau=10.2 d and tau±1.1 d.
4. Projection reduction and residual gap after one year.
5. The first integer number of years for which the stress-extrapolated projection reaches `R_proj>=G0053`.

## Scientific PASS criteria
All must hold:
- 450 d gives exactly 10× and 900 d gives exactly 100× within floating-point tolerance;
- residual gap decreases monotonically with time;
- `t_req_proj > 900 d`, showing the published 10×/100× benchmarks themselves do not close 0053;
- the counterfactual fast-component time is reported but explicitly barred from whole-LEE promotion;
- all values finite/positive.

Classification on PASS: `PASS_WAITING_TIME_REQUIREMENT_MAP`.

## Interpretation guard
This gate answers a requirements question, not a forecast. Extrapolating `10^(t/450d)` beyond 900 d is a stress law chosen to quantify what would be required if the benchmark trend continued. Actual LEE can contain multiple components, plateaus, thermal resets, architecture dependence, and non-exponential behavior.

## Exact next action after PASS
Use the result to define a realistic factorized mitigation budget over a finite experimental horizon (e.g. <=3 years): time reduction may contribute at most the frozen projection factor at that horizon; the remaining gap must be closed by independently demonstrated intrinsic suppression, topology discrimination, segmentation/veto and/or a stronger statistical model. Do not multiply correlated handles.