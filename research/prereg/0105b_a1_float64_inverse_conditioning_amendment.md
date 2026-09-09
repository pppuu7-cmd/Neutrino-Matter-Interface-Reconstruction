# 0105b-a1 — float64 inverse-conditioning amendment

Date: 2026-09-10
Parent: `research/prereg/0105b_vector_mediator_cross_regime_bridge.md`
Trigger: infrastructure/mathematical test failure only; no experimental result has been inspected through 0105b.

## Observed numerical issue

The frozen six-decade round-trip test includes `mX/q = 10^3`, for which

`r = mX^2/(mX^2+q^2) ≈ 0.999999000001`.

The inverse map is

`mX/q = sqrt[r/(1-r)]`.

Its logarithmic conditioning with respect to `r` is

`d ln(mX/q) / dr = 1 / [2 r (1-r)]`.

Near `r≈0.999999`, this amplification is approximately `5e5`. Float64 machine precision is approximately `2.22e-16`, so an inverse relative error at order `1e-10` is numerically expected before implementation-specific rounding. The originally coded `2e-11` relative tolerance was therefore stricter than the conditioning of the frozen endpoint warrants.

The failed hosted value was `40.0000000012229` for exact synthetic target `40.0`, a relative difference of about `3.06e-11`; all other tests passed (`653 passed, 1 failed`).

## Amendment

Keep the frozen physics domain and all seven `mX/q` points unchanged. Change only the round-trip numerical tolerance from `2e-11` to `5e-10` relative tolerance.

This tolerance is still far below any physical precision used by 0105 and is approximately a small multiple of the float64 conditioning floor at the most ill-conditioned frozen endpoint.

No formula, mass range, momentum range, operator convention, acceptance classification, or experimental parameter is changed.

This amendment is explicitly non-result-dependent with respect to BSM data and may not be used to relax any later experimental fit tolerance.