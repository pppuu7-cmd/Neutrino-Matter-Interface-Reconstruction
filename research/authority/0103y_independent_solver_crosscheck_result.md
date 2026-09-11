# NMIR 0103Y — independent solver cross-check result

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Status: `PASS_0103Y_INDEPENDENT_SOLVER_CROSSCHECK_NONTERMINAL`
Scope: `NONTERMINAL_SYNTHETIC_NUMERICAL_CROSSCHECK_ONLY`

## Prospective record

Preregistration was committed before implementation/results:

- preregistration: `research/prereg/0103yz_independent_solver_and_rephasing_prereg.md`
- preregistration commit: `d247e18dabf02fe26fce64f50700c8ce453fd4f6`
- implementation commit: `eea0c2730aeb64048450a80ff7275f386a195f83`

The audit compares two independently coded propagation algorithms for the same synthetic six-state Hamiltonian: the midpoint eigendecomposition propagator and classical fourth-order Runge–Kutta (RK4). The PMNS-shaped unitary and Hamiltonian profile are synthetic numerical fixtures only.

## Authoritative GitHub execution

- workflow: `.github/workflows/0103y-independent-solver-crosscheck.yml`
- trigger commit: `3de8ee345ec441ca1568aa1f448841b739c1df28`
- run: `34659341596`
- job: `103458393806`
- focused pytest: `1 passed in 3.26s`
- artifact: `nmir-0103y-independent-solver-crosscheck`
- artifact ID: `10287005932`
- artifact ZIP SHA256: `b1363664f3a0622d33aafac3242f49218cce607be98461b44d0b25fed2bfa2ca`

## Frozen configuration

- couplings: `g=[0, 0.01, 0.1, 1.0]`
- midpoint resolution: `N=4096`
- RK4 resolution: `N=4096`

## Result

All eight preregistered gates passed.

Key maxima across all frozen couplings:

- Hamiltonian Hermiticity residual: `1.1102230246251565e-16`
- midpoint norm residual: `3.8191672047105385e-13`
- RK4 norm residual: `2.886579864025407e-15`
- midpoint-vs-RK4 probability L-infinity difference: `7.381154243368826e-09`
- zero-coupling antineutrino leakage: `0.0`
- maximum nonzero-coupling antineutrino probability: `0.2598388746440398`

Per-coupling probability agreement:

- `g=0`: `3.436251283517322e-12`
- `g=0.01`: `4.844902257161721e-12`
- `g=0.1`: `1.031543739316021e-10`
- `g=1`: `7.381154243368826e-09`

The preregistered solver-agreement tolerance was `5e-6`; the observed worst-case difference is therefore roughly three orders of magnitude smaller than the allowed ceiling. The positive-control branch produces substantial spin-flavor transfer while the exact zero-coupling control remains clean.

## Interpretation

This closes a specific internal numerical-risk class: the six-state result is not dependent on a single propagation algorithm in the frozen synthetic fixture. It is evidence against an implementation-specific false PASS in the midpoint eigensolver.

It does **not** establish a physical Betelgeuse conversion probability, does not validate a missing stellar magnetic profile, and does not turn the Borexino upper limit into a detected magnetic moment.

Terminal Betelgeuse authority remains blocked by the absence of an admissible coherent magneto-matter state.