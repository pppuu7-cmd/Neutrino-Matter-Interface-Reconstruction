# Iteration 0092 — G9 Model-S solar-column authority PASS

Date: 2026-09-08
Classification: `PASS_G9_0092_MODEL_S_COLUMN_AUTHORITY`

## Frozen contract
Parent preregistration: `research/prereg/0092_g9_solar_transmission_authority.md`.
Prereg commit: `29ad32defe3d18983bb26f6e1e58005bc3d95e9e`.
Parent G9 result: 0091 `BLOCKED_G9_REAL_SOURCE_AUTHORITY`.

This record closes only the solar density/chord-column authority required by 0092. It is not an energy-dependent transmission classification and does not authorize a transparent-Sun claim, detector/material gain, event-rate fold, deposited-energy claim, or BSM response.

## Hosted authority
Execution head: `cf2093e46acd2770bdead2963a8444d5cb4f4d71`.
Workflow run/job: `34274667136 / 102224608870`.
Artifact: `10075203769` (`nmir-g9-0092-model-s-column-authority`).

Raw Actions log was inspected. The hosted run fetched the official Christensen-Dalsgaard Model-S table directly from:
`https://users-phys.au.dk/jcd/solar_models/cptrho.l5bi.d.15c`.

Downloaded Model-S exact SHA256:
`65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc`.
Byte count: `193762`; parsed rows: `2482`.

The artifact was downloaded independently after the run. Independent hashes:
- artifact ZIP SHA256: `21037786abe3cd62d9b6baf1ee2a4414c5dc9d5de92ca12cf26eef9a33e2d396`;
- inner `g9_0092_model_s_column.json` SHA256: `23fe3a1d43b4483225c30184e818e16beb61e3fe3c02b847152fcb623a7f24e9`;
- inner Model-S file SHA256: `65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc`.

The ZIP digest and inner JSON digest agree with the raw hosted log; the independently hashed Model-S bytes agree with the value printed during the hosted fetch.

## Frozen geometry and result
For the preregistered reference ray
- `b/Rsun = 0.024`;
- `Rsun = 6.957e10 cm`;
- `z = 24.073780819657056 AU`,

the frozen chord definition was

`Sigma(b)=2*Rsun*integral_0^sqrt(1-b^2) rho(sqrt(b^2+x^2)) dx`.

Primary method: deterministic linear interpolation in tabulated `rho(r)` and composite Simpson integration in chord coordinate.

Hosted result:
- `Sigma_fine = 2.9324883602905845e12 g cm^-2`;
- `Sigma_coarse = 2.9324883602809995e12 g cm^-2`;
- coarse/fine relative difference = `3.2685418524731032e-12`, well below the frozen `1e-4` requirement;
- log-rho sensitivity result = `2.9324808240625723e12 g cm^-2`;
- linear-vs-log-rho relative difference = `2.5699089258994556e-6`;
- nucleon column `N_N = 1.7659857664161126e36 cm^-2` using `m_u = 1.66053906892e-24 g`;
- interpolated density at the impact radius is `147.10789302575807 g cm^-3`.

Therefore the official solar-profile provenance and numerical chord-column calculation are reproducible and pass their preregistered authority requirement.

## Interpretation
The G9 reference ray traverses an enormous solar mass/nucleon column. That fact alone is not yet a source-regime transmission result: 0092 still requires independently authoritative Standard-Model interaction cross sections in the frozen 5–50 MeV, 1.5–15 TeV, and 290 TeV regimes before `tau=N_target*sigma` and `T0=exp(-tau)` may be classified.

No post-result source substitution is allowed. MeV and TeV/PeV regimes must remain separately classified.

## Next admissible gate
Freeze and execute a separate cross-section-authority subgate before evaluating source-regime optical depths. The subgate must use primary/review Standard-Model cross-section authority valid in each energy regime, preserve exact source/table provenance where numerical values are extracted, and must not extrapolate a TeV DIS approximation into the MeV regime.
