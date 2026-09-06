# Iteration 0050 — inverse accepted-background requirement for solar CEvNS

Date: 2026-09-06
Classification: `PASS_BACKGROUND_REQUIREMENT_MAP`

## Prospective contract
`research/detector_background_requirement_prereg.md`, commit `15ad880cdcf0168eaa3fb1a1447bd35d4c251d9a`, frozen before implementation/result inspection.

## Question
After iteration 0049 established accepted-signal rate feasibility, how small must the analysis-indistinguishable accepted background be to reach nominal one-year 3σ or 5σ counting-only discovery significance?

## Frozen metric
For known background expectation B and signal S, use the standard Asimov median discovery significance

`Z_A = sqrt(2[(S+B) ln(1+S/B) - S])`.

For each frozen S and target Z, numerically solve for the largest `B_max` satisfying `Z_A=Z`.

This is a counting-only known-background requirement; nuisance/systematic uncertainty is not included.

## Hosted authority
- scientific head: `488d23bfd6c4a84a750860e6fe1128807a4bf0eb`
- run/job: `34057997407 / 101553304948`
- artifact: `9996559867`
- artifact ZIP SHA256: `44a5dac90c92741a09bc25e531aa192a0c4ddb8064a0de30e8c5991a82cc66c5`
- raw dedicated tests: `4 passed`
- max relative inversion residual: `9.880984919163893e-15`
- fail-closed benchmark PASS token and artifact upload inspected.

## Raw requirements
### Generic design signal S=10 accepted events/year
- 3σ: `B_max = 8.22524098773645 events/year`, `B/S = 0.8225241`.
- 5σ: `B_max = 1.7175266766193094 events/year`, `B/S = 0.1717527`.

### Ar40, 10 kg, 10 eV, eta=0.50
Accepted signal `S = 11.84624201853375/year`.
- 3σ: `B_max = 12.098668408825569/year = 1.20986684/(kg year)`.
- 5σ: `B_max = 2.7565547482229014/year = 0.275655475/(kg year)`.

### Ar40, 10 kg, 20 eV, eta=0.75
Accepted signal `S = 9.909735084/year`.
- 3σ: `B_max = 8.05522455930435/year = 0.805522456/(kg year)`.
- 5σ: `B_max = 1.6734179605645096/year = 0.167341796/(kg year)`.

## Scientific interpretation
The low-threshold Ar survivor now has a quantitative accepted-background design requirement. O(10) accepted solar CEvNS events/year is not enough by itself; a one-year 5σ counting-only observation with a roughly ten-event signal requires the indistinguishable accepted background to be of order only 1–3 events/year, depending on the signal scenario.

The 3σ requirement is substantially looser and allows background comparable to the signal.

## Strict scope guards
- `B` is the *accepted, analysis-indistinguishable* background after cuts/response, not raw environmental, trigger, neutron or ER rates.
- Site-specific background rates are not imported as universal detector properties.
- Background normalization uncertainty, spectral/time/directional discrimination and multi-bin likelihood information are outside this gate.
- Adding a nuisance uncertainty can only make the simple known-background requirement more demanding for a fixed analysis.
- This is detector sensitivity engineering, not interaction enhancement or neutrino-energy gain.

## Next gate
Introduce a prospectively frozen nuisance-aware background-normalization uncertainty and quantify how the 3σ/5σ accepted-background targets tighten; subsequently map these requirements to actual calibrated transfer functions and detector-specific background models.
