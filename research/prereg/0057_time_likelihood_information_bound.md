# NMIR 0057 preregistration — unbinned time-likelihood information bound

Date: 2026-09-07
Gate: G2 time-domain discrimination
Status at preregistration: OPEN

## Question
Can the full event-time distribution of a decaying LEE background versus a steady solar CEvNS signal materially close the 0056 finite-horizon rejection gap, even under an optimistic model with perfectly known background normalization and time shape?

## Frozen baseline
- Horizon: `T = 3*365.25 = 1095.75 d`.
- Accepted solar CEvNS signal: `S = 30` events over the 3-year horizon (10/year), constant in time.
- Initial accepted 0053 stress background rate: `B0_year = 4.482974815542e9/year`, interpreted only for this stress calculation as the rate at `t=0`.
- Log-linear waiting law inherited from 0055: `k = ln(10)/450 d^-1` and `b(t)=b0 exp(-k t)`.

## Frozen time branches
1. `stress_3y`: continue `b(t)=b0 exp(-k t)` through all 1095.75 d. This is a mathematical stress continuation, not a CRESST forecast.
2. `authority_capped_900d`: use the same constructed log-linear interpolation through 900 d, then freeze the background at `b0/100` for the remainder of the 3-year horizon. This prevents any benefit from extrapolating the published 100× benchmark beyond 900 d.

These branches are alternatives and are never multiplied.

## Likelihood
Use the exact extended-Poisson Asimov discovery statistic for a known time-dependent background and constant signal intensity `s=S/T`:

`q0 = 2 integral_0^T [(s+b(t)) ln(1+s/b(t)) - s] dt`, `Z_A=sqrt(q0)`.

This deliberately gives the time model every advantage: the background shape and normalization are treated as perfectly known. A realistic nuisance treatment cannot improve on the same model's known-background likelihood.

For a uniform independent background-rejection factor `R` with perfect signal retention, replace `b(t)` by `b(t)/R` and solve the exact equation `q0(R)=25` for the 5σ requirement. Do **not** scale the weak-signal Fisher information linearly up to 5σ.

## Count-only comparator
For the same integrated background `B=int b(t)dt` and signal `S`, compute the exact one-bin Asimov statistic

`q_count(R)=2[(S+B/R) ln(1+S/(B/R)) - S]`

and solve `q_count(R)=25`.

The ratio `R_count/R_time` measures the best-case rejection-equivalent value of using event times under the frozen model.

## Numerical requirements
- use a cancellation-safe implementation of `h(x)=(1+x)ln(1+x)-x`;
- integrate with deterministic composite Simpson quadrature and demonstrate convergence;
- solve rejection factors by monotone log-space bisection;
- report unsuppressed `Z_time`, integrated background, exact `R_time_5sigma`, exact `R_count_5sigma`, and `R_count/R_time` for both branches.

## PASS criteria
- all outputs finite and positive;
- stress branch has end reduction >100 and authority-capped branch exactly 100 after day 900;
- numerical integration converges under a factor-two grid refinement to relative tolerance <=1e-8 for the key 5σ rejection factors;
- exact `R_time_5sigma < R_count_5sigma` for both branches;
- exact 5σ rejection factors remain >1e6 for both branches;
- weak-signal Fisher estimate is reported only as a local diagnostic and is not substituted for the exact 5σ solve.

Classification on PASS: `PASS_TIME_LIKELIHOOD_BOUND / TIME_SHAPE_USEFUL_BUT_INSUFFICIENT`.

## Interpretation guard
This is a model-conditional optimistic time-domain bound, not a detector prediction and not a universal theorem about all LEE components. Multi-component/floor/reset behavior and uncertainty in decay parameters can only invalidate the simple model or reduce its practical usefulness; they are not silently assigned numerical penalties here.

## Exact next action after PASS
Return to the factorized detector budget with the exact time-likelihood requirement. If public current-generation DoubleTES rejection×bulk-acceptance data are still unavailable, quantify what detector-specific rejection factor must be demonstrated jointly with time-likelihood to reach 5σ; do not invent a topology multiplier.