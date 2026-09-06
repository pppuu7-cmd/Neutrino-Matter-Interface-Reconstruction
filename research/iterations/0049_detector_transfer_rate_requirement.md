# Iteration 0049 — detector-transfer rate requirement from validated ideal CEvNS

Date: 2026-09-06
Classification: `PASS_DETECTOR_TRANSFER_RATE_REQUIREMENT`

## Prospective contract
`research/detector_transfer_rate_requirement_prereg.md`, commit `ab8610005f8e174fd6838f5491edab804f0a32ed`, frozen before implementation/result inspection.

## Question
Given the validated full-solar CEvNS rates from iteration 0045, what average recoil acceptance times live fraction is minimally required for a 10-kg Ar40 detector to produce an experimentally useful event yield?

This is a necessary exposure/rate condition only, not a measured detector-response claim.

## Frozen formula
Define

`eta = <epsilon_NR> * f_live`, `0 <= eta <= 1`.

Then

`N_acc/year = M_kg * R_ideal * 365.25 * eta`,

and

`eta_required = N_goal/(M_kg R_ideal 365.25)`.

Equivalent effective mass:

`M_eff = M*eta`,
`M_eff_required = N_goal/(R_ideal*365.25)`.

Primary design point: `M=10 kg`, `N_goal=10 accepted events/year`.

## Hosted authority
- scientific head: `01186655d07883ce7d0a14f5d29c4ff16f207f1b`
- run/job: `34057771059 / 101552695624`
- artifact: `9996491115`
- artifact ZIP SHA256: `6154810eff9116c69407e2a89052817783c75fbe2eab3a246f2d2235d6528e86`
- raw dedicated tests: `4 passed`
- workflow is fail-closed with `set -o pipefail` plus explicit PASS-token grep; raw benchmark and artifact metadata inspected.

## Raw Ar40 results
| threshold | ideal events/year for 10 kg | eta for 1 event/year | eta for 10 events/year | classification for 10/year |
|---:|---:|---:|---:|---|
| 10 eV | `23.6924840371` | `0.04220748` | `0.42207478` | `RATE_FEASIBLE_TRANSFER_TARGET` |
| 20 eV | `13.2129801120` | `0.07568315` | `0.75683153` | `RATE_FEASIBLE_TRANSFER_TARGET` |
| 40 eV | `4.24095487401` | `0.23579595` | `2.35795954` | `RATE_IMPOSSIBLE_AT_FIXED_MASS` |

Thus 10-kg Ar needs only a ~42.2% average accepted fraction at 10 eV to reach 10/year, but ~75.7% at 20 eV. At 40 eV, even eta=1 cannot reach 10/year at 10 kg.

## Effective-mass requirements for 10 accepted events/year
- Ar40 10 eV: `4.220747805 kg_eff`
- Ar40 20 eV: `7.568315335 kg_eff`
- Ar40 40 eV: `23.57959539 kg_eff`
- Si28 10 eV: `6.297244717 kg_eff`
- Ge74 10 eV: `3.478113710 kg_eff`
- Se82 10 eV: `3.333931804 kg_eff`

At 10 eV, Ar40 requires only `1.265997×` the effective mass of the ideal Se82 winner.

## Scientific interpretation
This closes a necessary rate/exposure gate for the practical low-threshold survivor. It shows that the 10–20 eV Ar40 region is not merely kinematically interesting: at 10 kg the ideal SM signal is large enough that a non-unity but substantial detector transfer function could still yield O(10) accepted solar CEvNS events per year.

The 40-eV boundary is qualitatively different: the ideal signal itself is too small for 10 events/year at 10 kg, independent of detector efficiency.

## Strict scope guards
- `eta<=1` feasibility is not evidence that the required efficiency, threshold stability, or background rejection has been demonstrated.
- This is detector/event-rate feasibility, not enhanced weak interaction probability.
- Avalanche/free-energy amplification is not neutrino-energy gain.
- Full recoil-dependent `epsilon_NR(T,state)`, false-trigger/background rate, threshold distribution, calibration uncertainty and live-time/reset dynamics remain OPEN.

## Next gate
Derive a signal-vs-background inverse requirement using a preregistered counting-statistics metric and then connect it to experimentally grounded detector transfer functions without importing site-specific backgrounds as universal properties.
