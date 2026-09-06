# NMIR 0058 preregistration — required measured topology-performance envelope

Date: 2026-09-07
Gate: G2 detector-specific rejection × signal-acceptance requirement
Status at preregistration: OPEN

## Question
Given the exact 0057 three-year time-aware likelihood, what *measured* detector/topology background rejection must a future DoubleTES-like handle provide as a function of retained CEvNS-like bulk-event acceptance in order to reach 5σ?

## Evidence state frozen before calculation
A fresh public-source audit through 2026-09-07 finds:
- the 2024 DoubleTES paper demonstrates event-origin discrimination and defines an absorber/bulk selection, but does not publish a directly comparable detector-wide rejection × bulk acceptance factor over the 0053 10–300 eV stress window;
- the CRESST next-generation perspective (Communications Physics 9, 163, published 2026-05-12, DOI `10.1038/s42005-025-02476-5`) treats DoubleTES as a future baseline and uses 10×/100× LEE reductions as performance scenarios/projections, not frozen measured rejection factors;
- ICHEP 2026 material is indexed as reporting the most recent LEE identification/rejection updates, but the publicly searchable contribution text does not expose a numerical rejection × bulk-acceptance pair comparable to the frozen NMIR window.

Therefore 0058 is a **requirements envelope**, not an assignment of achieved DoubleTES performance.

## Frozen 0057 model
- horizon `T=1095.75 d`;
- pre-selection accepted solar CEvNS signal `S0=30` events over 3 years;
- 0053 stress background normalization and the two 0057 time branches are unchanged:
  1. `authority_capped_900d`;
  2. `stress_3y`.
- use the exact extended-Poisson time-domain Asimov statistic from 0057 with known background shape and normalization:

`q0 = 2 integral [(s+b(t)) ln(1+s/b(t)) - s] dt`.

This remains deliberately optimistic and gives time discrimination its best case.

## Topology performance variables
Let `epsilon_S` be the CEvNS-like bulk-event signal acceptance of the detector/topology selection and `R_topo` the background rejection supplied by that same selection.

Evaluate `epsilon_S={1.0,0.9,0.8,0.7,0.5,0.3}` in two exposure-accounting modes.

### Fixed exposure
The accepted signal becomes `S=epsilon_S*S0`, while the background is divided by `R_topo`. Solve the exact equation

`q0(S=epsilon_S*S0, b/R_topo)=25`

for `R_topo`.

### Signal-restored exposure
Scale exposure by `1/epsilon_S` so that the accepted signal returns to `S0=30`. The pre-selection background scales by the same factor, so after topology rejection the background is `b/(epsilon_S R_topo)`. Therefore the exact requirement must obey

`R_topo,restored = R_0057(epsilon_S=1)/epsilon_S`.

This is a requirements map only; it does not assume unlimited mass or exposure.

## PASS criteria
- at `epsilon_S=1`, both modes reproduce the exact 0057 `R_time,5sigma` for each time branch within numerical tolerance;
- decreasing `epsilon_S` never improves the topology-rejection requirement;
- restored-exposure mode obeys exactly `R_base/epsilon_S`;
- fixed-exposure requirement is >= restored-exposure requirement for every `epsilon_S<1`;
- all requirements remain >1e6 throughout the frozen acceptance grid;
- 4096→8192 quadrature refinement changes key fixed-exposure requirements by <=1e-8 relative;
- no value is labelled as measured or achieved DoubleTES performance.

Classification on PASS: `PASS_REQUIRED_TOPOLOGY_PERFORMANCE_ENVELOPE / PUBLIC_ACHIEVEMENT_ANCHOR_OPEN`.

## Interpretation guard
The resulting `R_topo` already includes the remaining uniform rejection needed *when the full 0057 time likelihood is used*. It must not be multiplied by the 0056 waiting factors or by the 0057 rejection requirement. It is the detector-performance target conditional on the frozen time-aware analysis.

## Exact next action after PASS
Use the envelope as a direct acceptance criterion for new CRESST/DoubleTES underground publications or public data. A future result closes this subgate only if its measured background rejection and bulk-event acceptance can be mapped to a comparable low-energy interval without hidden correlated cuts or projection-only assumptions.