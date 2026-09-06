# Iteration 0053 — CRESST low-energy-excess scaling/rejection gap

Date: 2026-09-06
Gate: G2 detector background / scalability
Classification: `PASS_LEE_SCALING_GAP_STRESS`

## Frozen authority
Prospective contract: `research/prereg/0053_cresst_lee_scaling_gap.md`.
Prereg commit: `018f6410c8bfa6bad9ebb321f621a75b785cd293`.
Scientific workflow head: `567b7ffc2bad067c91f10023fbd2ff260ef24fbe`.
Authoritative hosted run/job: `34059182934 / 101556510236`.
Artifact: `9996911051`, `cresst-lee-scaling-result`.
Artifact ZIP SHA256: `cc03b4c6264ba5c187eaf5c3b483b1e253f5d9811de950e0452eb4b795e0dc92`.
Raw hosted log inspected: `6 passed`; fail-closed benchmark returned `PASS_LEE_SCALING_GAP_STRESS`.

## Frozen inputs
Primary experimental source: CRESST Collaboration, G. Angloher et al., Phys. Rev. D 107, 122003 (2023), arXiv:2212.12513.

Frozen central low-energy-excess fit over 10–300 eV:
`f(E)=A E^{-alpha}+B E^{-beta}` with E in keV and
- `A=7.6e-2`, `alpha=5.02`;
- `B=7.2e2`, `beta=2.22`.

Frozen 0052 factorized accepted-event surrogate:
`epsilon_sur(E)=0.6591 * 0.5 * [1+erf((E_eV-10)/(sqrt(2)*1.36))]`, for `E>=10 eV`.

Frozen scaled mass for exactly 10 accepted solar CEvNS/year under that surrogate:
`M10=9.766089763088724 kg`.

Frozen nuisance-aware accepted-background ceilings from 0051 for `S=10/year`:
- 3 sigma, delta_B=30%: `Bmax=4.274968302863348/year`;
- 5 sigma, delta_B=30%: `Bmax=1.0806120114381677/year`;
- 5 sigma, delta_B=50%: `Bmax=0.692094879071742/year`.

## Results
Numerical integration over 0.010–0.300 keV gives:
- efficiency-corrected central-fit LEE rate: `2.232922324133041e6 events/(kg day)`;
- accepted stress rate after the 0052 surrogate: `1.2567687196378214e6 events/(kg day)`;
- accepted/corrected ratio: `0.5628358434392818`;
- point-doubling relative change: `7.734699103423281e-9`, passing the frozen `1e-5` convergence criterion.

At the published blind exposure `0.05506 kg day`, the central-fit + surrogate stress gives `69197.68570325845` accepted events. This is an extrapolation of the fitted central spectrum through the frozen surrogate, not a reclassification of all such events as a known physical background species.

Per kg-year, the accepted stress rate is:
`4.590347748477143e8 events/(kg year)`.

Stress-scaling the same per-kg accepted LEE population to `M10=9.766089763088724 kg` gives:
`4.482974815542e9 accepted events/year`.

Required rejection/suppression factors relative to the 0051 discovery budgets are:
- 3 sigma, delta_B=30%: `1.0486568549617854e9`, surviving fraction `9.536007849168557e-10`;
- 5 sigma, delta_B=30%: `4.1485517170734453e9`, surviving fraction `2.4104797726987e-10`;
- 5 sigma, delta_B=50%: `6.477399199304432e9`, surviving fraction `1.5438295050695408e-10`.

All prospective criteria pass.

## Interpretation
This is a deliberately severe technology stress, not a forecast that the CRESST low-energy excess must scale linearly with detector mass or remain unchanged in a future kg-scale design. The current primary source does not provide a defensible mapping from every accepted low-energy event to an analysis-indistinguishable nuclear-recoil background, so NMIR reports the required total reduction/rejection factor instead of relabeling the LEE as known NR background.

The result is nevertheless quantitatively important: if the present central per-kg LEE shape and accepted-event transfer were preserved unchanged, the gap to a 10-event/year solar-CEvNS discovery design would be of order `10^9–10^10` in accepted competing-event population, depending on significance and background-normalization nuisance.

This gap may in principle be closed by a combination of: intrinsic LEE suppression per kg, event-by-event or statistical discrimination, spectral/time/source modeling, altered detector architecture, or reduced live accepted background. It is not weak-interaction enhancement and not neutrino-energy amplification.

## Exact next gate
Freeze newer primary CRESST/SOS measurements that directly compare LEE levels between detector generations/configurations and quantify any demonstrated per-kg suppression or altered spectral shape. Convert those measured changes into a multiplicative technology-gap reduction relative to the 0053 stress, keeping intrinsic LEE suppression distinct from discrimination/rejection. If no primary dataset provides a defensible comparable per-kg metric in the 10–300 eV window, classify that subgate `BLOCKED_BY_NONCOMPARABLE_PRIMARY_DATA` rather than inventing an improvement factor.