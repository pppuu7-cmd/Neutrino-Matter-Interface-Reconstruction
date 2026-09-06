# Iteration 0038 — passive linear multi-mode mediator gate

Date: 2026-09-06
Funnel gate: G2 / F5-F6
Prospective contract: `research/multimode_mediator_prereg.md`
Prereg commit: `ee2280967b419383ffd50595ae8700840669a95f`
Scientific workflow head: `37449c4e72adecab40e22d57cb73a592050e2e8b`
Hosted run: `34047675712`
Hosted job: `101525546661`
Artifact: `9993592020`
Artifact ZIP SHA256: `68ca855f7d3fbd9ba7553040f6efa3303fee24ac3d9692fda7a88ea9e9fe207f`

## Question
Can multiple passive linear field/cavity/collective modes, including a near-gapless mode, evade the single-harmonic-mediator energy-budget gate and generate a parametrically larger neutrino-coupled collective response for free?

## Exact result
For

`H_med(x,O)=1/2 x^T K x - x^T G O`

with real symmetric positive-definite stiffness matrix `K`, completing the square gives

`H_med = 1/2 (x-K^-1GO)^T K (x-K^-1GO) - 1/2 O^T G^T K^-1 G O`.

At the passive equilibrium displacement,

`E_field = 1/2 O^T G^T K^-1 G O = |E_induced|`.

This identity is independent of the number of modes and of the mediator basis.

## Hosted validation
Raw log inspected. Dedicated tests: `7 passed in 0.03s`.

Benchmark:
- 100 random SPD 5-mode systems;
- max square-completion relative error: `8.215955708232927e-16`;
- max field-vs-induced relative error: `8.215955708232927e-16`;
- max basis-invariance relative error: `2.220446049250313e-16`;
- soft eigenvalue `1 -> 1e-9`: induced-energy gain `9.999999999999999e8`;
- same softening: mediator field-energy gain `9.999999999999999e8`;
- field/induced gain ratio: `1.0`;
- exact null mode with nonzero source projection: `UNSTABLE_NO_PASSIVE_EQUILIBRIUM`;
- exact null mode orthogonal to source: `FINITE_POSITIVE_SUBSPACE`.

## Classification
**PASS_MULTIMODE_LINEAR_BUDGET / STRONG-NEGATIVE scoped.**

Adding, mixing, or softening passive stable *linear* mediator modes cannot create a free parametrically larger induced collective interaction when the displacement energy of the mediator is included. A coupled exact zero-stiffness mode does not define a stable passive equilibrium in this static model.

## Scope guards
This is not a theorem for nonlinear, driven/active, time-dependent, higher-body fundamental interactions, BSM neutrino operators, or gravity. Near criticality/nonlinearity must be investigated under a separate gate with complete preparation/free-energy accounting.

## Side finding — RIOEC target search
The RIOEC paper (Akhmedov, Lasserre, Maturi, arXiv:2608.25001) explicitly states that its preliminary candidate ranking sets the squared nuclear matrix element to `0.1` for all targets and requires future explicit matrix-element evaluation/charge-exchange input. Therefore NMIR does not promote that ranking to an authority rate.

`63Cu -> 63Ni*(87.2 keV)` is a clean allowed-transition control but has resonance energy near `~0.16 MeV`, while the thermal-solar antineutrino source is concentrated at eV-keV energies. Modern shell-model calculations for the reverse 87.2-keV transition span B(GT) values from `1.21e-3` to `4.48e-2` before detailed-balance conversion, illustrating substantial target-strength uncertainty. It is therefore not selected as the thermal-solar authority target.

## Next funnel priority
1. G8: identify a genuinely eV-keV RIOEC candidate with evaluated/independently constrained entrance strength; if unavailable, classify candidate-specific rate as BLOCKED rather than adopting the paper's screening `|M|^2=0.1`.
2. G2: passive nonlinear/near-critical mediator gate with full field/free-energy accounting.
3. G3: global finite-range two-/higher-body residual bound.
4. G9: distant-source flux x alignment-duty-cycle usefulness.
