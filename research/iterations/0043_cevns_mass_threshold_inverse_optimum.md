# Iteration 0043 — CEvNS mass-threshold inverse optimum

Date: 2026-09-06
Gate: G2 / F3–F7
Status: **PASS_CEVNS_MASS_THRESHOLD_OPTIMUM / CLASS-LEVEL INVERSE-DESIGN RULE**

## Question
At fixed detector mass and recoil threshold, does the competition between coherent weak charge (favoring heavier nuclei) and recoil kinematics (favoring lighter nuclei) produce a calculable interior optimum in target mass, before choosing a real material?

## Prospective authority
`research/cevns_mass_threshold_optimum_prereg.md` was frozen before hosted result inspection.

Scope: monoenergetic source, continuous mass number `A`, low-q CEvNS, `M=A m_u`, approximately fixed weak charge per nucleon `Q_W=q A`. This is a class-level design envelope, not a real-isotope recommendation.

## Analytic derivation
At fixed detector mass, number of nuclei scales as `1/A`. With `Q_W∝A`, the zero-threshold coherent rate per kg scales as `A`. In the frozen heavy-target low-q recoil approximation, finite threshold contributes the phase-space factor

`(1 - A/A_max)^2`,

where

`A_max = 2 E_nu^2/(m_u T_thr)`

is the approximate mass number whose recoil endpoint closes at threshold.

Therefore

`R(A) ∝ A (1-A/A_max)^2`,

with unique interior maximum

`A_star = A_max/3 = 2 E_nu^2/(3 m_u T_thr)`.

Equivalently, the optimum obeys

`T_max(A_star) ≈ 3 T_thr`.

This is an inverse-design rule: target mass should be chosen from the source energy and detector threshold rather than assumed in advance.

## Hosted exact-endpoint validation
Implementation: `src/nmir/cevns_mass_optimum.py`
Tests: `tests/test_cevns_mass_optimum.py`
Benchmark: `scripts/cevns_mass_optimum_benchmark.py`
Workflow: `.github/workflows/cevns-mass-optimum.yml`
Workflow head: `01087cfda391b9ea95fa273d6c8bd0765589d59c`
Run: `34051179823`
Job: `101534970552`
Artifact: `9994578242`
Artifact ZIP SHA256: `387536f9bee8889a3c48e5ac7d2149e33f4aa6f2824e4780cba081dec3a5b253`
Raw dedicated tests: `12 passed in 0.03s`.

Prospective tolerance was 1% for both the target-mass optimum and `Tmax/(3 Tthr)` check. Raw maxima were:
- maximum relative analytic-vs-numerical `A_star` residual: `5.003199810005299e-08`;
- maximum relative residual of `Tmax/(3 Tthr)` from unity: `1.391481982099263e-04`.

Both pass by a very large margin.

## Benchmark results

| Source / threshold | analytic `A*` | exact numerical `A*` | exact `Tmax/Tthr` at optimum |
|---|---:|---:|---:|
| Be7-like 0.86258 MeV / 40 eV | 13.31273872 | 13.31273939 | 2.99958256 |
| Be7-like / 20 eV | 26.62547744 | 26.62547771 | 2.99979131 |
| Be7-like / 10 eV | 53.25095489 | 53.25095459 | 2.99989568 |
| pp endpoint 0.420 MeV / 10 eV | 12.62487864 | 12.62487878 | 2.99978570 |
| pep 1.44 MeV / 40 eV | 37.10168418 | 37.10168515 | 2.99974994 |

## Scientific result
The low-energy CEvNS detector optimization has an interior target-mass optimum rather than monotonically favoring the heaviest possible nucleus. In the stated envelope,

`A_star ∝ E_nu^2/T_thr`.

Thus lowering the threshold shifts the optimum to heavier nuclei; raising the threshold shifts it to lighter nuclei. For Be7-like neutrinos the design center moves from roughly `A~13` at 40 eV to `A~27` at 20 eV and `A~53` at 10 eV.

This explains why Ar-40 is not generically optimal. At a 40-eV Be7 threshold it is near kinematic closure rather than near the fixed-mass event-rate optimum; around 10 eV, however, the ideal optimum has moved into the medium-mass region.

## Scope guards
✅ This is a validated analytic/numerical class-level design law inside the frozen low-q fixed-`Q_W/A` approximation.

❌ It is not a claim that an isotope with exactly `A=A_star` is experimentally optimal.

❌ It does not include real `Z/N`, isotopic abundance, nuclear form factors, detector chemistry, nucleation efficiency, backgrounds, threshold distributions or full solar spectra.

❌ It is not an interaction enhancement and not neutrino-energy gain.

## Next gate
Replace continuous `A` and fixed `Q_W/A` by a real-nucleus candidate set and fold the full frozen solar spectrum at fixed kg over thresholds, particularly 1–20 eV. Report total and source-resolved ideal CEvNS events/kg/day, include form factors where relevant, and compare the numerical real-isotope optimum with the analytic `A_star` rule.

Recommended reconciliation: `NMIR_READINESS: 73%` (audit estimate; +1% for a prospectively frozen, hosted, class-level inverse-design closure).
