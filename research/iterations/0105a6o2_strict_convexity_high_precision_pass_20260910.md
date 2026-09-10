# 0105a6o2 — strict-convexity and high-precision optimum certificate

Date: 2026-09-10
Classification: **PASS_0105A6O2_STRICT_CONVEX_UNIQUE_HIGH_PRECISION_OPTIMUM_NONDISCOVERY**

## Frozen provenance

- parent preregistration commit: `07a61181b7fb2b8f7041250c3b9bf1de1aeee0e4`;
- pre-hosted precision-strengthening amendment commit: `29c529ccdf1c4d586367e0dd1f7822e1e6999291`;
- implementation commit: `eda308f0237eda26ee24f628cbdb882658542edf`;
- guards commit: `2e3a7bb893056ba3394a9a148601485a5fd7b6ff`;
- execution head: `73209a16876b6627f8580740c4adf093cbe1be13`;
- run/job: `34505089165/102965178498`;
- artifact: `10163470626`, `nmir-v2-0105a6o2-argon-high-precision-certificate`;
- provider artifact ZIP SHA256: `8ca17ecfeeabe05bee6305a3bbb2dc6ac2eb5877ffeb67a14e74df165c2dbcc0`;
- independently downloaded artifact ZIP SHA256: `8ca17ecfeeabe05bee6305a3bbb2dc6ac2eb5877ffeb67a14e74df165c2dbcc0`;
- inner `result.json` SHA256: `e3790cb7e2459ef900fda2cfe430be8d47fe497c1365f9c12762bef3f9599d73`.

No hosted 0105a6o2 execution occurred before the precision amendment.

## C1 — algebraic uniqueness

PASS for both anchors from exact official decimal-text inputs.

The machine certificate found `395` bins with both observed count `n_i > 0` and normalized CEvNS shape `S_i > 0`. Since the three background Gaussian penalties have strictly positive curvature, the frozen quadratic-form identity

`v^T H v = 2 sum_{i:n_i>0} n_i (a_i dot v)^2/mu_i^2 + 2 v_P^2/160^2 + 2 v_D^2/33^2 + 2 v_B^2/25^2`

can vanish only when `v_P=v_D=v_B=0`, after which any positive-count/nonzero-signal bin forces `v_C=0`. Therefore the central objective is strictly convex throughout its positive-`mu` interior and can have at most one interior stationary point.

## C2/C3 — arbitrary-precision stationarity

Both preregistered starts converged at P80 and at the amended P200 precision for both anchors. Every frozen C2/C3 check passed.

### R3152 certified P200 root

`[NC, NP, ND, NB] =`

`[160.2049532080454801680147250894639634793903754579391537743567266229869688250067,`
` 552.1173817719572419593459356782581526327571336569928046824985009496296796205594,`
` 10.53624250236967647885542490920539807736283207617965643170907603904385986736556,`
` 3131.396818877543581118379356288858238589363794706078559445667926604582716562898]`.

- P200 gradient infinity norm: `3.862901079...e-91`;
- maximum P200 root spread between the two frozen starts: `2.315760168...e-89` event;
- P200 objective difference between starts: `4.430494068...e-180`;
- all four leading principal Hessian minors are positive; full determinant `1.483035966...e-10`.

### R3154 certified P200 root

`[NC, NP, ND, NB] =`

`[159.7098081384421305213390980312155327024133518257247977872155175431329481291062,`
` 552.0960524101103449755924467158521569674531986636692588445011400027462262043044,`
` 10.50657649044405070581159390403701505712208557236345263909483054191172300158259,`
` 3133.164757618587749943079393030541217301638908195150516986834874491038179052070]`.

- P200 gradient infinity norm: `5.306334768...e-91`;
- maximum P200 root spread between frozen starts: `3.180980190...e-89` event;
- P200 objective difference between starts: `8.359850421...e-180`;
- all leading principal Hessian minors are positive; full determinant `1.483131002...e-10`.

P80-to-P200 coordinate differences are many orders of magnitude below the frozen `1e-40` event criterion.

## Interpretation

0105a6o1 remains historically BLOCKED under its frozen `1e-5` all-coordinate multi-start requirement. 0105a6o2 does not alter that result.

Instead, 0105a6o2 independently proves strict convexity of the exact central objective and exhibits the unique interior stationary point at arbitrary precision. The approximately `3e-5` event NC spread that blocked 0105a6o1 is therefore consistent with ordinary double-precision optimizer stopping-coordinate resolution and cannot represent distinct local minima of this frozen objective.

This is still NONDISCOVERY and does not itself classify agreement with the published COHERENT central/null result.

## Permission semantics

A new prospectively recorded Tier-B central/null reproduction gate is now authorized. It must reuse the publication targets, dual-anchor robustness thresholds and null/profile definitions frozen in 0105a6o commit `a94cbdf5a65618545bd4b1fb4f9fd6c120ae340e` without post-result adjustment.

- Tier-A exact collaboration-internal likelihood: BLOCKED;
- systematic excursions: not yet authorized for execution until central/null reproduction passes;
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`.
