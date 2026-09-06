# Iteration 0055 — CRESST LEE waiting-time requirement map

Date: 2026-09-07
Gate: G2 time-domain mitigation / long-term cryogenic operation
Hosted-audit status: `PASS_WAITING_TIME_REQUIREMENT_MAP`
Scientific classification: `WAITING_ONLY_OPERATIONALLY_INSUFFICIENT`

## Frozen authority
Prospective contract: `research/prereg/0055_lee_waiting_time_requirement.md`.
Prereg + scientific workflow head: `2b1908f250d36901368929b20f9f6a81b972275c`.
Hosted run/job: `34059603535 / 101557649153`.
Artifact: `9997041670`, `lee-waiting-time-result`.
Artifact ZIP SHA256: `dafce36c089f9917f7c89f3276ddd2c02fce8e14dd8ee42a6ba9488e245455f9`.
Raw hosted log inspected: `6 passed`; fail-closed benchmark returned `PASS_WAITING_TIME_REQUIREMENT_MAP`.

## Primary-source guard
CRESST DoubleTES 2024 (DOI `10.1140/epjc/s10052-024-13282-8`, arXiv:2404.02607) measures a single-exponential decay time `10.2 ± 1.1 d` for the absorber-band LEE component in the 28–50 eV interval. It also demonstrates multiple LEE populations, so that fast time constant is not promoted to the full LEE.

CRESST next-generation report (DOI `10.1038/s42005-025-02476-5`, arXiv:2505.01183) describes waiting as a backup strategy and projects roughly 10× LEE reduction after ~450 d and 100× after ~900 d. NMIR uses `R_proj(t)=10^(t/450 d)` beyond 900 d only as a mathematical stress extrapolation, never as a CRESST forecast.

## Frozen 0053 requirement
For the 0051 design point `S=10/year`, 5σ and 30% accepted-background normalization nuisance:

`G0053 = 4.1485517170734453e9`.

This remains a deliberately severe fixed-LEE-per-kg stress extrapolation, not a prediction for a future kg-scale CRESST detector.

## Hosted numerical result
The stress-extrapolated time needed for the projection law alone to reach the frozen gap is

`t_req = 450 d * log10(G0053) = 4328.053428827087 d = 11.84956448686403 y`.

The first integer-year horizon satisfying the stress requirement is therefore **12 years**.

| Horizon | Stress reduction `R_proj` | Residual required improvement `G0053/R_proj` |
|---|---:|---:|
| 1 y | 6.481367792287417 | 6.40073492204850e8 |
| 450 d | 10 | 4.1485517170734453e8 |
| 900 d | 100 | 4.148551717073445e7 |
| 3 y | 272.27013080779125 | 1.5236896183820141e7 |
| 5 y | 1.1437558630495389e4 | 3.627130448986176e5 |
| 10 y | 1.3081774742601955e8 | 31.712453384198096 |

Thus the published 450/900-d benchmark points do not close 0053, and even the deliberately optimistic indefinite continuation remains impractical as a waiting-only strategy.

## Counterfactual fast-component bound
If, contrary to the multi-component evidence, the entire 0053 stress population followed the measured DoubleTES fast-component exponential, the formal times to reach `G0053` would be:
- `tau=9.1 d`: `201.5288286506246 d`;
- `tau=10.2 d`: `225.8894562897111 d`;
- `tau=11.3 d`: `250.25008392879758 d`.

These numbers are **component-only counterfactuals**. They are not detector-wide waiting-time predictions and cannot be used to claim closure of the LEE problem.

## Scientific result
`PASS_WAITING_TIME_REQUIREMENT_MAP / WAITING_ONLY_OPERATIONALLY_INSUFFICIENT`.

The gate closes the requirements question: waiting alone does not provide a practical route from the frozen 0053 stress background to the 0051 5σ budget. At a finite 3-year horizon the most generous frozen log-linear stress law still leaves a required independent improvement of `1.523689618e7` (~7.183 decades).

## Exact next gate
Construct the <=3-year factorized mitigation budget. Treat the 3-year time contribution as an upper-bound stress factor only; quantify the remaining independent product required from intrinsic LEE reduction, DoubleTES/topology discrimination, segmentation/coincidence/veto and statistical modeling. Do not multiply factors whose independence is not experimentally established, and do not assign a numerical topology rejection factor when the public DoubleTES paper does not publish one comparable to the 0053 10–300 eV window.