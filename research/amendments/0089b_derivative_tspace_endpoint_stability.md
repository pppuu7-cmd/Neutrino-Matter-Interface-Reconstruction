# NMIR amendment 0089b — endpoint-centered t-space derivative stability repair

Date frozen: 2026-09-08
Parent scientific preregistration: `5d99cd6cd4d3a5f1f9defecfbd7f4036c93b8636`.
Diagnostic contract: `0460ed7026167db314959c51509b7b6a9fd04328`.
Validated diagnostic run/job: `34212969375/102018040810`, artifact `10050562702`, independently verified ZIP SHA256 `3ce57426e607ab3258381b9a653732d656a1b4f8b84e0f4ddc35ad1ffeb04fcc`, inner JSON SHA256 `74b235e0ac5160ef7538a11f85db99322a52b7a06cf2e67f454559aceb7cdf4b`.

## Diagnostic authority
At the frozen V1 failure point `x=0.99999825`, independent 100-digit theta-space and t-space direct integrations agree with symmetric relative difference `3.08298265610274e-97` and give

`dM/dx = 1.590879155969468360896719110293463881945341317308596311057270360341024e24 g/x`.

The unchanged production evaluator gives `1.5908792145016913e24`, symmetric relative mismatch `3.6792373931063796e-08 > 1e-9`.

The only active source interval is `[0.9999965,1]`; its existing double decomposition has
`term_A=-1.4612752221252747e-6`, `term_B=1.4616507138625827e-6`, sum `3.754917373080439e-10`, cancellation ratio `7784.261664298522`.

This is a diagnosed production derivative stability defect, not a scientific G9 failure.

## Frozen algebraically equivalent production repair
No production quadrature, smoothing, source-point deletion, threshold change, or series cutoff is allowed.

For each active source interval with lower bound `L=max(lo,x)`, upper bound `H=hi`, slope `a=(rho_hi-rho_lo)/(hi-lo)`, define

`t(u)=sqrt((u-x)(u+x))`, `t_L=t(L)`, `t_H=t(H)`, `Delta_t=t_H-t_L`,

and evaluate the local density at L as

`rho_L = rho_lo + a*(L-lo)`.

Under `t=sqrt(u^2-x^2)`, the shell contribution before the global `4*pi*R^3*x` factor is

`I = integral_L^H u*rho(u)/sqrt(u^2-x^2) du`

and, because `dt = u/sqrt(u^2-x^2) du` and `rho(u)=rho_L+a(u-L)`, exactly

`I = rho_L*Delta_t + a*Delta_K`,

where

`Delta_K = [S(t_H)-S(t_L)] - L*Delta_t`,

`S(t) = 0.5 * [ t*sqrt(x^2+t^2) + x^2*asinh(t/x) ]`.

Since `sqrt(x^2+t_H^2)=H` and `sqrt(x^2+t_L^2)=L`, production shall evaluate

`Delta_K = 0.5*(H*t_H - L*t_L) + 0.5*x^2*(asinh(t_H/x)-asinh(t_L/x)) - L*Delta_t`

using `math.fsum` for the signed sum, then shell `I` using `math.fsum([rho_L*Delta_t, a*Delta_K])`.

This expression is mathematically identical to the preregistered `a*Delta J_A + b*Delta J_B` integral but avoids both `acosh(u/x)` at `u/x≈1` and the large `a/b` cancellation diagnosed above. It introduces no approximation or new branch threshold.

## Frozen non-changes
- `continuous_projected_mass_g` is unchanged.
- Model-S bytes/hash/parser/constants/domain are unchanged.
- V0/V1/V2/V3 points and thresholds are unchanged.
- The corrected independent V1 mass theta reference remains as frozen by commit `2300db976ba40d7d2bc7c4d87316baecc0162b38`.
- The V1 observability diagnostics remain enabled.
- No V2/V3 values have been inspected before this amendment.

## Required regression
Before hosted 0089b classification, add a unit regression that confirms the endpoint-centered shell formula agrees with the prior closed form at a well-conditioned moderate-x toy interval and remains finite/non-negative near a surface-like high-x interval. The hosted frozen V1 80-digit reference remains the authority for numerical accuracy.

## Taxonomy
After this repair, rerun the original 0089b contract unchanged. V1 mismatch remains infrastructure failure. Only if V1 passes may V2/V3 be classified under the original preregistered BLOCKED/PASS rules. This amendment itself cannot produce a scientific PASS.
