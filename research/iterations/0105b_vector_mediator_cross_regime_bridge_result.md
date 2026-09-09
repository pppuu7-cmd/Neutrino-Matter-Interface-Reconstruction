# 0105b — vector-mediator cross-regime bridge result

Date recorded: 2026-09-10
Parent preregistration: `research/prereg/0105b_vector_mediator_cross_regime_bridge.md`
Preregistration commit: `bc8b66c5bd7be7beab7ef2395875c24752c2dd9c`
Conditioning amendment: `research/prereg/0105b_a1_float64_inverse_conditioning_amendment.md`, commit `5320cca36d8daa06801e858099bd18796e626d74`

## Frozen scientific question

Can one neutral-vector propagator be represented consistently in both the zero-momentum forward coefficient and finite-spacelike-momentum scattering coefficient, with prospectively frozen algebra/domain/unit invariants, before any result-dependent NMIR-v2 BSM fit?

## Implementation provenance

Implementation:
- `src/nmir/vector_mediator_bridge_0105b.py`
- commit `0be15e38cc520be1b5d32b5492f4516d886f5248`

Initial tests:
- `tests/test_vector_mediator_bridge_0105b.py`
- commit `4c0896d7cb3918dc934161688199466054129337`

The implemented control identities are

`C0 = gprod / mX^2`,

`Cq = gprod / (mX^2 + q^2)`,

`r = Cq/C0 = mX^2/(mX^2+q^2)`,

`mX = q sqrt[r/(1-r)]`,

and the nonrelativistic CEvNS scale control

`q = sqrt(2 M T)`.

The module deliberately contains no event-rate, likelihood, confidence-level or discovery-statistic function.

## Initial hosted execution

Baseline CI run: `34412502527`
Job: `102669922305`
Head: `4c0896d7cb3918dc934161688199466054129337`

Result:
- `653 passed`
- `1 failed`

The sole failure was the frozen inverse round-trip at the most ill-conditioned point `mX/q=10^3`: synthetic target `mX=40.0` was recovered as `40.0000000012229` under the initially coded relative tolerance `2e-11`.

This did not indicate a physical or algebraic contradiction. Near `r -> 1`,

`d ln(mX/q)/dr = 1/[2 r (1-r)]`,

so the inverse map amplifies float64 rounding strongly. At the frozen endpoint `r≈0.999999`, the conditioning factor is about `5e5`. The observed relative difference was about `3.06e-11`.

## Prospectively documented numerical amendment

Before any experimental result-dependent use of 0105b, amendment `0105b-a1` changed only the synthetic round-trip numerical tolerance from `2e-11` to `5e-10`.

No formula, physical domain, mediator-mass point, momentum point, operator convention, experimental input or scientific classification criterion changed.

Amended test commit:
`0882f49bfc01fb44b68dfa8b171138e218977a0a`.

## Authoritative hosted execution

Baseline CI run: `34412759225`
Job: `102670720577`
Head: `0882f49bfc01fb44b68dfa8b171138e218977a0a`

Result:
- full pytest: `654 passed in 35.46 s`;
- `python -m nmir.baseline`: success;
- workflow conclusion: success.

Therefore all prospectively frozen 0105b mathematical/domain/unit invariants pass after the explicitly documented float64-conditioning amendment.

## Scientific interpretation

The validated bridge establishes only the following non-discovery statement:

> a single neutral-vector propagator can be encoded consistently in the frozen NMIR-v2 forward and finite-q coefficient conventions, and its finite-range coefficient ratio is invertible for `0<r<1` away from singular endpoints.

It does **not** establish:
- a residual in IceCube, COHERENT or any other experiment;
- preference for a vector mediator over scalar, magnetic or sterile families;
- a joint oscillation+CEvNS likelihood;
- a new interaction;
- novelty of combining propagation and CEvNS constraints.

The separate prior-art audit `research/authority/0105_prior_art_novelty_audit.md` explicitly records that oscillation+CEvNS NSI/light-mediator complementarity is established literature. The possible NMIR-v2 novelty target is instead the full residual -> common-operator -> frozen held-out prediction architecture.

## Classification

`PASS_0105B_VECTOR_MEDIATOR_CROSS_REGIME_MATHEMATICAL_BRIDGE_NONDISCOVERY`

## Next gate

0105b is closed. Do not tune it against observed residuals.

Proceed independently with:
- 0105a immutable authority inventories + control-fit reproduction;
- 0105c nuisance-orthogonal residual implementation and synthetic validation;
- no observed Stage-A BSM residual scan until both prerequisites are sufficiently locked.