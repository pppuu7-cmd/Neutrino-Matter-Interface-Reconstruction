# NMIR G2 preregistration — passive linear multi-mode mediator gate

Date: 2026-09-06
Status: prospectively frozen before hosted benchmark inspection.

## Question
Can a passive stable collection of many common field/cavity/collective modes evade the single-harmonic-mediator energy-budget gate and generate a parametrically large neutrino-coupled collective response without importing an equally large medium/field energy scale?

## Scope
Consider real mediator coordinates `x` and bounded collective matter observables `O`, with

`H_med(x,O) = 1/2 x^T K x - x^T G O`,

where `K` is a real symmetric stiffness matrix and `G` is an arbitrary coupling matrix. This gate covers any finite passive *linear* multi-mode mediator with a stable quadratic energy. It does not cover nonlinear, driven/active, explicitly time-dependent, unstable, higher-body fundamental interactions, BSM neutrino operators, or gravity.

## Exact identity for K positive definite
Completing the square gives

`H_med = 1/2 (x-K^-1 G O)^T K (x-K^-1 G O) - 1/2 O^T G^T K^-1 G O`.

At the passive equilibrium displacement `x*=K^-1 G O`,

`E_field = 1/2 x*^T K x* = 1/2 O^T G^T K^-1 G O`,

while the induced effective matter interaction is

`E_induced = -1/2 O^T G^T K^-1 G O`.

Therefore `E_field = |E_induced|` exactly. Adding modes, mixing modes, or making one mode soft changes the quadratic form but cannot make the induced interaction parametrically larger than the mediator displacement-energy scale that accompanies it.

## Gapless/null-mode guard
If `K` has an exact zero mode:
- if `G O` has nonzero projection on that nullspace, the static energy is unbounded along that coordinate and there is no stable passive equilibrium in this model;
- if the source is orthogonal to the nullspace, that exact zero mode does not contribute to the induced static interaction.
A near-gapless eigenvalue `lambda_min>0` is allowed and must show the same `1/lambda_min` growth in both `E_field` and `|E_induced|`.

## Frozen numerical tests
1. Random positive-definite multi-mode matrices: square-completion identity relative error `<1e-12`.
2. `E_field/|E_induced| = 1` to `<1e-12` at the minimizing displacement.
3. Orthogonal changes of mediator basis leave the induced quadratic form invariant to `<1e-12`.
4. Soft-mode scan `lambda: 1 -> 1e-9` with fixed aligned coupling: both field and induced energies must gain `1e9` within `1e-9` relative tolerance, and their gain ratio must be 1.
5. Exact null mode with nonzero source projection must be classified `UNSTABLE_NO_PASSIVE_EQUILIBRIUM`.
6. Exact null mode orthogonal to source must reduce to the positive subspace and remain finite.

## Classification contract
- `PASS_MULTIMODE_LINEAR_BUDGET` if all exact/numerical checks pass.
- Scientific interpretation: **STRONG-NEGATIVE scoped** against free superextensive/soft-mode gain from passive stable *linear* multi-mode mediators when mediator energy is explicitly accounted.
- Nonlinear/driven/active/higher-body classes remain OPEN regardless of PASS.
