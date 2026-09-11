# NMIR 0103X preregistration — six-state stress and convergence matrix

Status: PREREGISTERED_BEFORE_RESULT
Scope: NONTERMINAL_SYNTHETIC_NUMERICAL_STRESS_ONLY

## Question
Does the six-state Majorana propagation remain unitary, deterministic and convergent across a coupling/refinement matrix when H(s) varies noncommutatively along the path?

## Frozen fixture
- Deterministic path s in [0,1].
- Smooth path-varying three-state vacuum/matter blocks with off-diagonal structure.
- Smooth amplitude and phase modulation of an antisymmetric Majorana 1-2 magnetic block, so Hamiltonians at different s do not generally commute.
- Coupling multipliers g = [0, 1e-3, 1e-2, 1e-1, 1].
- Production resolutions N = [64,128,256,512,1024].
- Reference resolution N_ref = 4096.
- Midpoint piecewise-unitary propagation by Hermitian eigendecomposition; all quantities are dimensionless synthetic fixtures.

## Locked gates
1. Maximum Hamiltonian Hermiticity residual <= 1e-12.
2. Maximum final-state norm residual <= 1e-10.
3. Maximum probability-sum residual <= 1e-10.
4. All probabilities finite and bounded in [-1e-12,1+1e-12].
5. At g=0, total antineutrino leakage <= 1e-12 at every tested resolution.
6. For every nonzero g, 1024-step final-probability L-infinity error versus N_ref is lower than the 64-step error.
7. Maximum 1024-step L-infinity probability error versus N_ref across all g <= 1e-6.
8. Identical repeated N=1024 calculations differ in final probabilities by <= 1e-14.
9. At least one nonzero g yields antineutrino probability >1e-8, providing a positive control.
10. Scope guard remains NONTERMINAL_SYNTHETIC_NUMERICAL_STRESS_ONLY.

PASS label: `PASS_0103X_SIX_STATE_STRESS_CONVERGENCE_NONTERMINAL`.

A PASS is numerical evidence only; it cannot substitute for a physical Betelgeuse magneto-matter snapshot or turn an experimental magnetic-moment upper bound into a detection.
