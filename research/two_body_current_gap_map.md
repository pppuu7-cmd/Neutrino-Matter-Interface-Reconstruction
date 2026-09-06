# NMIR two-body weak-current gap sensitivity map

Date: 2026-09-06
Status: conditional diagnostic, **not a theorem** and not a G3 closure credit.

## Motivation
Iteration 0026 bounds the leading finite-q one-body vector-charge + axial-spin multipole sector at

`P_1,max = 1.2056895107775174e-9 W/kg`

under an already extreme `A<=300`, zero-threshold, 20-MeV, 2000-W/m2-neutrino-energy-flux envelope. Genuine two-body meson-exchange/axial currents are a separate response class and must not be hidden inside the one-body result.

This note asks only: **how large would an individual pair current have to be to bridge the remaining gap by coherent combinatorics?**

## Conditional norm model
Let the norm of the largest single-nucleon current contribution be `j1`. Assume only for this sensitivity map that every two-nucleon pair current is norm-bounded by

`||j2_ij|| <= r * j1`.

For `A` nucleons,

`||J1|| <= A*j1`,

`||J2|| <= A(A-1)/2 * r*j1`.

Therefore

`||J1+J2|| / ||J1|| <= 1 + (A-1)r/2`,

and the maximally coherent cross-section/power amplification relative to the iteration-0026 one-body envelope is conditionally bounded by

`G_2body(r,A) = [1 + (A-1)r/2]^2`.

This assumes identical normalization units for `j1` and `j2`; it is a sensitivity parametrization, not a claim about EFT operator coefficients.

## Worst-case A=300 gap
With `A=300` and `P_1,max=1.2056895107775174e-9 W/kg`, the pair-current ratio required to reach `1 W/kg` is

`r_required = 2*(sqrt(1/P_1,max)-1)/(A-1) = 192.63`.

Illustrative values:

| per-pair norm ratio r | maximally coherent conditional power |
|---:|---:|
| 0.1 | `~3.08e-7 W/kg` |
| 1 | `~2.73e-5 W/kg` |
| 10 | `~2.70e-3 W/kg` |
| 100 | `~2.69e-1 W/kg` |
| 192.63 | `~1 W/kg` |

Thus, within this deliberately maximally coherent pair-counting model, each pair current would need a norm roughly **193 times the reference maximum single-nucleon current** to bridge the finite-q G3 gap.

## Empirical/EFT sanity anchors — not global bounds
This conditional requirement is qualitatively far above published low-energy few-body weak-current effects:
- Baroni & Schiavilla, Phys. Rev. C 96, 014002 (2017), DOI `10.1103/PhysRevC.96.014002`: beyond-leading-order weak-current contributions increase deuteron neutrino cross sections by only a couple percent over 0–150 MeV.
- Acharya & Bacca, Phys. Rev. C 101, 015505 (2020), DOI `10.1103/PhysRevC.101.015505`: chiral-EFT uncertainties including electroweak-current truncation are at the few-percent level at 100 MeV; axial two-body strength is constrained through `L_1,A`.
- Ando et al., Phys. Rev. C 101, 054001 (2020), DOI `10.1103/PhysRevC.101.054001`: at 20 MeV, NLO contribution is 5.2–9.9% and P waves 2.4–2.8% for neutrino-deuteron reactions.
- Carlson et al., Phys. Rev. C 86, 035503 (2012), DOI `10.1103/PhysRevC.86.035503`: two-body contributions to deuteron neutrino cross sections are below about 10% over the studied range.

These are **few-body empirical/theory anchors only**. They do not prove an all-nucleus two-body-current bound and cannot be extrapolated as a theorem to A=300.

## Consequence for next gate
A rigorous G3 closure should now attempt either:
1. a chiral-EFT/current-algebra norm bound on two-body electroweak operators over the solar-neutrino momentum domain; or
2. an inclusive response/sum-rule bound that covers one- and two-body currents together.

Until then, two-body currents remain an explicit open loophole, albeit one with an enormous required coherent per-pair strength under the current sensitivity map.
