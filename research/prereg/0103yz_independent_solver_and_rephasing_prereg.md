# NMIR 0103Y/Z preregistration — independent solver and basis rephasing audits

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Scope: `NONTERMINAL_NUMERICAL_VALIDATION_ONLY`

This preregistration is written before implementation/results. It does not alter the terminal astrophysical authority ceiling. Betelgeuse-specific propagation remains blocked until a coherent magneto-matter state with vector B and matter variables is recovered.

## 0103Y — independent propagation algorithm cross-check

Purpose: detect an implementation-specific false PASS in the midpoint eigendecomposition propagator by comparing it against an independently coded fourth-order Runge–Kutta integration of the six-state Schrödinger equation.

Frozen synthetic fixture:
- same six-state Majorana-style Hamiltonian family used by 0103X;
- PMNS-shaped synthetic unitary fixture only; it is not physical parameter authority;
- couplings `g = [0, 1e-2, 1e-1, 1]`;
- midpoint-eigensolver resolution `N = 4096`;
- RK4 resolution `N = 4096`;
- identical initial flavor state and Hamiltonian function.

Prospective gates:
1. Hamiltonian Hermiticity residual `<= 1e-12`.
2. Maximum probability-vector difference between midpoint eigensolver and RK4 `<= 5e-6` for every frozen coupling.
3. RK4 norm residual `<= 5e-8`.
4. Midpoint eigensolver norm residual `<= 1e-10`.
5. At `g=0`, antineutrino leakage for both solvers `<= 1e-12`.
6. At nonzero coupling, at least one branch must produce antineutrino probability `> 1e-8` as a positive control.
7. No probability may be non-finite or lie outside `[-1e-10, 1+1e-10]`.

PASS label: `PASS_0103Y_INDEPENDENT_SOLVER_CROSSCHECK_NONTERMINAL`.

## 0103Z — six-state rephasing covariance

Purpose: verify that arbitrary diagonal phase redefinitions of the six basis coordinates do not change physical probabilities and transform the evolved state covariantly.

Frozen transformation:
- choose deterministic diagonal unitary matrices `D = diag(exp(i*phi_j))` from three fixed six-phase vectors;
- transform `H'(s) = D H(s) D^dagger` and `psi0' = D psi0`;
- propagate original and transformed systems with the same midpoint eigensolver;
- compare `psi_final` with `D^dagger psi'_final` and compare component probabilities directly.

Frozen cases:
- `g = [0, 0.1, 1.0]`;
- `N = 1024`;
- three deterministic phase vectors, including nontrivial phases in both neutrino and antineutrino blocks.

Prospective gates:
1. `D` unitarity residual `<= 1e-14`.
2. Transformed-Hamiltonian Hermiticity residual `<= 1e-12`.
3. Maximum recovered-state residual `<= 2e-12`.
4. Maximum probability residual `<= 2e-12`.
5. Norm residual in both representations `<= 1e-10`.
6. `g=0` antineutrino leakage remains `<= 1e-12`.

PASS label: `PASS_0103Z_SIX_STATE_REPHASING_COVARIANCE_NONTERMINAL`.

## Scope guard

A PASS in 0103Y/Z means only that the internal numerical representation is more strongly cross-validated. It cannot create missing Betelgeuse magnetic/matter authority, cannot convert an experimental upper bound into a detection, and cannot authorize a terminal Betelgeuse probability.