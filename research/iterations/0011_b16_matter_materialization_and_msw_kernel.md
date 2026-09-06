# Iteration 0011 — exact B16 matter materialization + adiabatic MSW kernel

Date: 2026-09-06

## Starting authority

- `research/RECOVERY.md` through iteration 0010.
- Candidate B16 matter freeze on commit `ec3082e9b08bce1f6ec46fb52fb970ee62c67b20`.
- Required order: consume head CI -> exact materialization/parse -> production integrals -> prospective MSW kernel.

## Consumed CI

Run `34012590342`, job `101430836362`, head `ec3082e9b08bce1f6ec46fb52fb970ee62c67b20` completed SUCCESS. Raw log: `56 passed in 0.15s`.

Classification: infrastructure/test PASS and validation of the frozen B16 matter manifest/loader contract. This alone is not a numerical solar-survival PASS.

## Exact hosted B16 matter materialization

Added:

- `src/nmir/solar_matter.py` exact downloader/parser/diagnostics;
- `tests/test_solar_matter_numeric.py`;
- `.github/workflows/matter-materialize.yml`.

Hosted authority:

- run `34014923087`;
- job `101436936728`;
- head `37267d5c75103d8ff07ba2104bc8330d10878128`;
- conclusion SUCCESS;
- artifact ID `9983598047`;
- artifact ZIP SHA256 `9b7baa133f74d616b62e158c27de71984ff025b209639a46c423f73acfc7c1e9`.

Exact identities reproduced:

- B16_AGSS09met blob `d9bd29f3374c63e8ea898733a55fb7aa566a2c96`;
- B16_GS98 blob `f73c47cf6f2d77086634a5c180b50039e10805e7`.

Both tables contain 1000 rows on `r/Rsun = 0.0005 ... 0.5`. Parsed electron-density ranges are positive and finite. Most importantly, trapezoidal integrals of every component production distribution are numerically unity to better than about `8e-5`, independently confirming the column interpretation and giving a clean native-grid production measure.

Representative extrema across the two branches:

- central sampled `n_e/N_A ≈ 100.9253 mol cm^-3`;
- outer sampled `n_e/N_A ≈ 1.15 mol cm^-3`.

Production integral ranges:

- GS98: `0.99992238 ... 0.99999162`;
- AGSS09met: `1.00001814 ... 1.00006286`.

Classification: **scientific input/provenance PASS** for the B16 matter + component-production distributions. The small deviations from exactly one are compatible with tabulation/quadrature precision and are not renormalized silently; explicit normalized quadrature weights are constructed when averaging.

## Prospective adiabatic MSW kernel

Implemented in `src/nmir/solar_oscillation.py` before inspecting any real B16 survival result:

\[
P_{ee}=c_{13}^4\frac{1+\cos2\theta_{12}\cos2\theta_{12}^m}{2}+s_{13}^4,
\]

with

\[
\cos2\theta_{12}^m=\frac{\cos2\theta_{12}-A_{eff}/\Delta m_{21}^2}{\sqrt{(\cos2\theta_{12}-A_{eff}/\Delta m_{21}^2)^2+\sin^22\theta_{12}}},
\]

and `A_eff = 2 E sqrt(2) G_F n_e c13^2`. The direct-density conversion uses
`2 E V = 1.526494e-7 eV^2 * E[MeV] * (n_e/N_A)[mol cm^-3]`.

Frozen first-benchmark scope remains: normal ordering, adiabatic propagation, Earth regeneration OFF, small 1-3 solar matter corrections neglected in the standard decoupled approximation.

Prospective tests cover:

1. exact zero-density agreement with phase-averaged vacuum `P_ee`;
2. high-density adiabatic limit;
3. physical monotonic low/high benchmark behavior;
4. production averaging on the native B16 quadrature.

Current MSW head: `9a2cdc3e8ba6a35043ca50e4f7f632d89b65763f`. CI run `34014950750` was still active when this note was prepared. Therefore the numerical MSW implementation remains **PENDING head CI** and no Ga/Cl claim is promoted yet.

## Gate updates

- G3 prerequisite B16 matter/prod-distribution identity: PASS.
- G3 exact hosted B16 matter materialization/parse: PASS.
- G3 numerical adiabatic MSW kernel: PENDING CI.
- Ga-71 / Cl-37: OPEN.
- BSM remains LOCKED.

## Readiness

`NMIR_READINESS: 26%`

Increase 25 -> 26 is credited only to the newly closed exact B16 matter materialization + production-normalization gate. The MSW code itself earns no readiness credit until validated and benchmarked.

## Exact next gate

1. Consume CI `34014950750` and classify the MSW tests.
2. Run the validated kernel on exact B16 GS98/AGSS09met tables and publish component-resolved `P_ee(E)` checkpoints including pp/Be7/pep/B8 energies.
3. Cross-check low-energy ~vacuum and high-energy MSW plateaus against primary/standard references without retuning parameters.
4. Freeze Ga-71 capture response, reproduce published total/component SNU, then Cl-37.
5. Convert validated capture to W/kg and advance quantitative G3.
