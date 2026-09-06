# Iteration 0051 — detector background-normalization nuisance requirement

Date: 2026-09-06
Gate: G2 real detector transfer / accepted-background systematics
Classification: `PASS_BACKGROUND_NUISANCE_REQUIREMENT_MAP`

## Frozen authority
Prospective contract: `research/prereg/0051_detector_background_nuisance_requirement.md`.
Prereg commit: `3fb9b44309888e710ed748bac07f372162ecafad`.
Scientific head: `be3706d409b5018519be7b6dfcd0bc0581ed0135`.
Hosted run/job: `34058564427 / 101554849279`.
Artifact: `9996725207`, `background-nuisance-result`.
Artifact ZIP SHA256: `148d4b3c877f52dc5813a4fe7247d20430aff45496105460b98714163766dfb8`.
Raw hosted log inspected: `5 passed`; fail-closed benchmark status PASS.

## Statistic
For `sigma_b = delta_B * B`, used the standard profile-likelihood Asimov discovery significance with Gaussian background-normalization nuisance:

`Z_A^2 = 2[(s+b) ln(((s+b)(b+sigma_b^2))/(b^2+(s+b)sigma_b^2)) - (b^2/sigma_b^2) ln(1 + sigma_b^2 s/(b(b+sigma_b^2)))]`.

At `delta_B=0`, the implementation exactly reduces to the 0050 known-background statistic.

## Frozen uncertainty grid
`delta_B = {0, 0.10, 0.30, 0.50}`.
Signals unchanged from 0050.

## Results
### Design signal S = 10 accepted/year
| delta_B | Bmax 3σ /yr | ratio to known-B | Bmax 5σ /yr | ratio to known-B |
|---:|---:|---:|---:|---:|
| 0% | 8.22524 | 1.000 | 1.71753 | 1.000 |
| 10% | 7.25026 | 0.8815 | 1.60068 | 0.9320 |
| 30% | 4.27497 | 0.5197 | 1.08061 | 0.6292 |
| 50% | 2.64504 | 0.3216 | 0.692095 | 0.4030 |

### Ar40, 10 kg, 10 eV, eta=0.50; S=11.846242/year
| delta_B | Bmax 3σ /yr | Bmax 5σ /yr |
|---:|---:|---:|
| 0% | 12.09867 | 2.75655 |
| 10% | 10.28082 | 2.52016 |
| 30% | 5.62863 | 1.59026 |
| 50% | 3.38631 | 0.979890 |

At 5σ this corresponds to accepted indistinguishable background densities of `0.27566`, `0.25202`, `0.15903`, `0.09799 events/(kg yr)` for delta_B = 0,10,30,50% respectively.

### Ar40, 10 kg, 20 eV, eta=0.75; S=9.909735/year
| delta_B | Bmax 3σ /yr | Bmax 5σ /yr |
|---:|---:|---:|
| 0% | 8.05522 | 1.67342 |
| 10% | 7.11271 | 1.56097 |
| 30% | 4.21040 | 1.05743 |
| 50% | 2.60926 | 0.678692 |

## Frozen criteria audit
- delta_B=0 reproduces 0050: PASS; maximum relative error `0.0`.
- Bmax strictly tightens with increasing delta_B: PASS.
- 5σ stricter than 3σ at every delta_B: PASS.
- maximum relative inversion residual: `1.0658141036401503e-14` <= `1e-10`: PASS.
- all solutions finite/positive: PASS.

## Scientific interpretation
Background-normalization systematics materially tighten the already-small accepted-background budget. For the representative Ar10 scenario, moving from exactly-known background to a 30% normalization nuisance reduces the 5σ accepted-background ceiling by ~42.3%; at 50% it is reduced by ~64.5%.

This is a detector-design requirement, not evidence that any detector currently achieves these accepted-background levels or uncertainties. The numbers refer to analysis-indistinguishable accepted events, not raw environmental or trigger rates.

## Exact next gate
Freeze a detector-specific recoil transfer function from measured calibration data. Highest-priority positive control: CRESST-III silicon 10-eV detector because the ledger already contains a measured `10.0±0.2 eV_nr` threshold and `1.36±0.05 eV_nr` baseline resolution. Extract the published trigger/cut efficiency vs recoil energy and fold it into the NMIR solar-CEvNS Si spectrum. If the publication does not provide a defensible nuclear-recoil efficiency curve in the required range, classify the low-energy transfer branch as evidence-blocked rather than inventing a step function.