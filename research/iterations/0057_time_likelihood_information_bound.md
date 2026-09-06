# Iteration 0057 — unbinned time-likelihood information bound

Date: 2026-09-07
Gate: G2 time-domain discrimination
Hosted-audit status: `PASS_TIME_LIKELIHOOD_BOUND`
Scientific classification: `TIME_SHAPE_USEFUL_BUT_INSUFFICIENT`

## Frozen authority
Prospective contract: `research/prereg/0057_time_likelihood_information_bound.md`.
Scientific workflow head: `66008c2478e3145175b165e7481ad84f9862f073`.
Hosted run/job: `34061194530 / 101561925452`.
Artifact: `9997513698`, `time-likelihood-result`.
Artifact ZIP SHA256: `b907eff49815716ce1a026af68453cab0808f9cdd098e330d58ff18e9357d796`.
Raw hosted log inspected: `6 passed`; fail-closed benchmark returned `PASS_TIME_LIKELIHOOD_BOUND` and `TIME_SHAPE_USEFUL_BUT_INSUFFICIENT`.

## Frozen model
Horizon: `T=1095.75 d` (3 years).
Accepted steady solar CEvNS signal: `S=30` events over the horizon, so `s=S/T`.
Initial 0053 stress background rate: `B0=4.482974815542e9/year`, used here as the constructed `t=0` stress rate.
Time constant law: `k=ln(10)/450 d^-1`.

Two alternative time branches are frozen and never multiplied:
1. `stress_3y`: `b(t)=b0 exp(-k t)` through the full 3-year horizon; this is a mathematical stress continuation and not a CRESST forecast.
2. `authority_capped_900d`: the same constructed interpolation to day 900, then `b(t)=b0/100` through the remainder of the horizon; this prevents extrapolated waiting benefit beyond the published 100× benchmark scale.

## Exact time-domain likelihood
For perfectly known background normalization and time shape, the extended-Poisson Asimov discovery statistic is

`q0 = 2 integral_0^T [(s+b(t)) ln(1+s/b(t)) - s] dt`,

with `Z_A=sqrt(q0)`.

For an additional uniform independent background-rejection factor `R` with perfect signal retention, `b(t)` is replaced by `b(t)/R` and the exact equation `q0(R)=25` is solved. The implementation uses a cancellation-safe small-`x` form of `(1+x)ln(1+x)-x`, deterministic composite Simpson quadrature, and monotone log-space bisection. The 4096→8192 grid refinement passed the preregistered relative-convergence criterion.

The weak-signal Fisher quantity `integral s^2/b(t) dt` is retained only as a local diagnostic. It is not extrapolated linearly to 5σ.

## Hosted numerical result

| Branch | Integrated background, 3 y | Unsuppressed `Z_time` | Exact `R_time,5σ` | Exact count-only `R_count,5σ` | Time-shape advantage `R_count/R_time` |
|---|---:|---:|---:|---:|---:|
| authority-capped 900 d | `2.398722200944235e9` | `0.001541785192223862` | `1.77570304169906e7` | `8.801822811314675e7` | `4.956810122312319` |
| stress continuation 3 y | `2.389873295001078e9` | `0.001799372658294259` | `1.4440370654436817e7` | `8.769352814506759e7` | `6.072803132523726` |

Local weak-signal Fisher diagnostics are `2.377101712220705e-6` and `3.2377422923570367e-6` in `q`, respectively, agreeing with the unsuppressed exact likelihood in the genuinely weak-signal regime. They are deliberately not used to infer the 5σ rejection requirement.

## Scientific result
`PASS_TIME_LIKELIHOOD_BOUND / TIME_SHAPE_USEFUL_BUT_INSUFFICIENT`.

Using every event time is substantially better than collapsing the same 3-year data set to one count: in this deliberately optimistic known-background model it is rejection-equivalent to roughly a `4.96×` to `6.07×` improvement. Nevertheless, even this best-case time-shape analysis still needs an additional independent uniform background rejection of about `1.44e7`–`1.78e7` for a 5σ, 30-event discovery.

This is a model-conditional optimistic bound, not a detector prediction and not a theorem about all LEE components. The calculation gives the time method perfect knowledge of the background normalization and time law. Multi-component LEE, non-decaying floors, thermal resets and nuisance uncertainty can reduce practical discrimination and are not assigned guessed penalty factors.

## Accounting guard versus 0056
The 0057 `R_time,5σ` is a full three-year likelihood requirement. It is not the same accounting object as the 0056 one-year accepted-background/end-time factorized budget. Therefore the 0057 factor must not be multiplied by the 0056 time factor or interpreted as an extra independent rejection gain. Instead 0057 supersedes the simplistic treatment of temporal evolution as a free analysis multiplier when designing a three-year time-aware search.

## Exact next gate
Audit current-generation underground DoubleTES and architecture-specific CRESST results for a quantitative LEE rejection × CEvNS-like bulk-event acceptance anchor in a comparable energy interval. If no public anchor can be frozen, build a required-measured-topology-performance envelope using the exact 0057 time-aware likelihood, including explicit signal acceptance, rather than inventing or multiplying a topology factor.