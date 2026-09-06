# Iteration 0056 — finite-horizon factorized LEE mitigation budget

Date: 2026-09-07
Gate: G2 finite-horizon detector mitigation budget
Hosted-audit status: `PASS_FINITE_HORIZON_MITIGATION_BUDGET`
Scientific classification: `REQUIREMENTS_MAP_CLOSED / INDEPENDENT_QUANTITATIVE_ANCHORS_STILL_OPEN`

## Frozen authority
Prospective contract: `research/prereg/0056_finite_horizon_mitigation_budget.md`.
Scientific workflow head: `21fd967077782c29502a3ab8fedaf63c245e63c2`.
Hosted run/job: `34060855059 / 101560998357`.
Artifact: `9997410337`, `finite-horizon-mitigation-result`.
Artifact ZIP SHA256: `294695f827e9758dcbce96c248d3ce5c8eab7e472d83456729fd0e46cf1c0f84`.
Raw hosted log inspected: `6 passed`; fail-closed benchmark returned `PASS_FINITE_HORIZON_MITIGATION_BUDGET`.

## Frozen baseline
- 0053 stress background: `B0053 = 4.482974815542e9 accepted events/year`.
- 0053 5σ, 30% nuisance improvement requirement: `G0053 = 4.1485517170734453e9`.
- design signal: `S0=10 accepted CEvNS events/year`.
- exact recomputed nuisance-aware ceiling: `Bmax(S=10,Z=5,delta_B=0.30)=1.0806120114381677/year`.

## Finite 3-year time branches
Two **alternative**, never multiplied branches were frozen:
1. `authority_cap_100x`: `R_time=100`, the last directly published CRESST benchmark scale;
2. `stress_extrapolation_3y`: `R_time=272.27013080779125`, the 0055 log-linear continuation `10^(t/450d)` evaluated at 3 years, used only as a mathematical stress law and not as a CRESST forecast.

At full CEvNS acceptance, the remaining independently supplied rejection must therefore be:

| Time branch | Remaining rejection | Remaining decades |
|---|---:|---:|
| authority cap 100× | `4.148551717073445e7` | `7.6178965085` |
| 3-y stress extrapolation 272.27× | `1.5236896183820141e7` | `7.1828965085` |

Even the deliberately optimistic stress branch leaves >15 million-fold independent rejection to be demonstrated.

## Signal-acceptance penalty
For a combined remaining mitigation handle with CEvNS signal acceptance `epsilon_S`, two accounting modes were validated.

### Fixed exposure
Signal falls to `S=10*epsilon_S`, so the allowed nuisance-aware background ceiling is recomputed and the required rejection is
`R_other_fixed=(B0053/R_time)/Bmax(10 epsilon_S)`.

### Signal-restored exposure
Exposure is increased by `1/epsilon_S` to restore `S=10`; the pre-cut background scales by the same factor. Then
`R_other_restored=G0053/(R_time epsilon_S)`.

Key hosted values:

| `epsilon_S` | 100×: fixed | 100×: restored | 272.27×: fixed | 272.27×: restored |
|---:|---:|---:|---:|---:|
| 1.0 | `4.1486e7` | `4.1486e7` | `1.5237e7` | `1.5237e7` |
| 0.9 | `5.3739e7` | `4.6095e7` | `1.9738e7` | `1.6930e7` |
| 0.8 | `7.3121e7` | `5.1857e7` | `2.6856e7` | `1.9046e7` |
| 0.7 | `1.0643e8` | `5.9265e7` | `3.9089e7` | `2.1767e7` |
| 0.5 | `3.1703e8` | `8.2971e7` | `1.1644e8` | `3.0474e7` |
| 0.3 | `2.8711e9` | `1.3829e8` | `1.0545e9` | `5.0790e7` |

Thus topology/veto cuts cannot be treated as free background multipliers: loss of CEvNS acceptance can increase the residual requirement by orders of magnitude at fixed exposure.

## Equal-factor scale diagnostic
At full signal acceptance, if the residual rejection were hypothetically split among `n` truly independent equal handles, the per-handle factors would be:

| n | 100× authority cap | 272.27× stress branch |
|---:|---:|---:|
| 2 | `6440.93` | `3903.45` |
| 3 | `346.18` | `247.91` |
| 4 | `80.26` | `62.48` |
| 5 | `33.39` | `27.33` |

This is a scale diagnostic only. Independence is not experimentally established and these factors must not be multiplied as if it were.

## Fresh 2026 evidence audit
The peer-reviewed CRESST next-generation perspective, published 12 May 2026 (DOI `10.1038/s42005-025-02476-5`), states that DoubleTES can reject a single-TES-origin LEE component while maintaining high signal efficiency, but it does not publish a directly comparable numerical rejection × signal-acceptance factor over the frozen 0053 10–300 eV stress window. Its 10× and 100× LEE levels remain benchmark/projection scales.

A CRESST talk at *Superconducting Technologies for Dark Matter* (11 May 2026) advertises the latest LEE mitigation results but has no public presentation material on the conference page. The ICHEP 2026 CRESST talk by S. Banik (30 July 2026) explicitly advertises the most recent updates on identification and rejection of LEE; the current conference index lists `cresst.pdf`, but the accessible public text available to this audit does not expose a comparable numerical rejection×acceptance value. Therefore no new multiplier is frozen from these conference sources.

## Scientific result
`PASS_FINITE_HORIZON_MITIGATION_BUDGET / REQUIREMENTS_MAP_CLOSED / INDEPENDENT_QUANTITATIVE_ANCHORS_STILL_OPEN`.

0056 closes the mathematical detector-budget question. It does **not** close G2 experimentally. Under the strongest 3-year stress branch and perfect signal retention, an independently demonstrated factor `1.523689618e7` remains. Under the authority-capped 100× branch it is `4.148551717e7`.

## Exact next gate
Freeze a fresh-evidence gate for underground/current-generation DoubleTES and other architecture-specific LEE mitigation data. A factor may enter the product only if the source supplies enough information to map both background rejection and CEvNS-like bulk-event acceptance in a comparable energy interval. If such quantitative public anchors remain unavailable, keep G2 `QUANTITATIVE_GAP_OPEN` and move the theoretical subgate to an unbinned time-likelihood information bound rather than assuming arbitrary multiplicative rejection.