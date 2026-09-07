# NMIR iteration 0072 — reproducible U(1)_{B-L} contour materialization route audit

Date: 2026-09-07
Prospective contract: `research/prereg/0072_b_minus_l_contour_materialization_contract.md`, frozen commit `837a092a46d3b0d99f222c3777af8499f01c2062`.
Status: **IN PROGRESS / NO CONTOUR PASS YET**.

This immutable note records substantive progress inside the already frozen 0072 gate. It does not weaken the acceptance criteria and does not close 0072.

## Recovery and newer-work reconciliation
Before continuing, the mandatory recovery order was re-read and commits newer than the previous reconciliation were inspected. The unreconciled work consisted of:
- `bd686278ef20bdf7febaaa5c00b53a5b4e77dc33` — initial 0072 route audit ledger;
- `814e3dc8519c258c95649f66545c89ff9919fc16` — Yukawa/B-L convention helpers;
- `a78ce79fe41c594b91b2b2fdb78d181cd751318f` — tests for those helpers.

Baseline CI run `34102211415`, job `101678992936`, on head `a78ce79fe41c594b91b2b2fdb78d181cd751318f` was newly terminal. Its raw log was inspected: `356 passed in 14.10s`. This is infrastructure/convention-helper validation only, not a scientific contour PASS.

## Low-mass B-L fifth-force authority
Primary authority: Wagner, Schlamminger, Gundlach, Adelberger, *Class. Quantum Grav.* 29 (2012) 184002, arXiv:1207.2442v1.

The primary text explicitly gives the one-boson-exchange potential and the WEP Yukawa normalization

`alpha_tilde = +/- g_tilde^2/(4*pi*G*u^2)`

and states that the left panel of Fig. 6 is the 95% CL upper bound on a **vector** Yukawa interaction for `q_tilde=N=B-L`, derived from the lab-fixed Be-Ti/Be-Al measurements plus a geophysical source model.

Under the frozen NMIR current convention `L_int=g_BL V_mu J_{B-L}^mu`, the magnitude conversion is

`|g_BL| = sqrt(4*pi*G_N*u^2)*sqrt(|alpha_tilde|)`

with the implemented constant

`G_PER_SQRT_ALPHA = 2.70463357586823e-19`.

The range/mass conversion is

`m_V[eV] = (hbar*c)[eV m]/lambda[m]`,

with `hbar*c = 1.973269804e-7 eV m`. Thus the frozen lower mass edge `m_V=1e-6 eV` corresponds to `lambda=0.1973269804 m`.

These conversions are implemented in `src/nmir/b_minus_l_contour_convert.py` and tested in `tests/test_b_minus_l_contour_convert.py`.

## Route-2 materialization audit
The arXiv HTML rendering exposes Fig. 6 as `WEP_figure6.png`, i.e. a raster asset. The 0072 contract forbids manual point reading/raster digitization, so this asset cannot be numerical scientific authority.

The arXiv record also exposes a TeX source archive. The source archive/vector figure has not yet been materialized through the currently available tool route. Therefore the allowed calibrated-vector route is **not declared exhausted**. No BLOCKED classification is issued yet.

A secondary numerical curve (`cajohare/AxionLimits`, `EotwashEP.txt`) remains explicitly regression-only. One locator point near the frozen lower edge maps to `m=1.073903817077052e-6 eV`, `g_BL=5.10309948748322e-22`, corresponding to `alpha_tilde=3.559085604069644e-6`. It is not accepted as primary authority.

## Other 0072 routes
The De Romeri–Papoulias–Ternes JHEP 05 (2024) 165 primary analysis remains an actionable route-3 target: it supplies the B-L event-rate/likelihood convention, while primary PandaX-4T solar-pp electron-recoil data provide an experimental anchor. A reproduction has not yet been executed, so no direct-detection contour is accepted.

Esseili–Kribs (arXiv:2308.07955) and Hong–Shin–Yun (arXiv:2012.05427) remain the controlling cosmology/stellar authorities identified in 0071. No author numerical code/table product has yet been materialized from them.

## Current scientific classification
**`IN_PROGRESS_0072 / PRIMARY_CONTOURS_MATERIALIZED=0`**.

This is neither `PASS_B_MINUS_L_CONTOURS_MATERIALIZED` nor `BLOCKED_PRIMARY_NUMERICAL_DATA_UNAVAILABLE`. The latter would require exhausting the allowed materialization routes for a controlling contour; that has not happened because the arXiv source/vector route and the independent likelihood route remain actionable.

No global allowed B-L region is authorized. No B-L NMIR response/enhancement calculation is authorized.

## Exact next action
1. Materialize the Wagner et al. arXiv TeX/source archive and determine whether Fig. 6 is stored as EPS/PDF/vector data. If yes, perform calibrated extraction and validation; if not, preserve that route failure.
2. If low-mass route 2 remains unavailable, execute the frozen route-3 same-convention PandaX/De-Romeri reproduction instead of reading a plot.
3. Audit Esseili–Kribs and Hong–Shin–Yun source archives for code/tables before any reproduction.

## Readiness
No readiness increase. The gate remains open and no primary exclusion contour has yet been numerically materialized.
