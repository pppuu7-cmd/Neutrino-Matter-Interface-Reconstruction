# 0102 — known-model benchmark: neutral-current-like NSI in matter

Date frozen: 2026-09-09
Benchmark ID: NMIR-BENCHMARK-0102
State: ACTIVE_PREFLIGHT_ONLY
Parent protocol: `research/benchmarks/KNOWN_MODEL_BENCHMARK_MATRIX.md`

## Purpose

Test a standard non-standard-interaction deformation of the three-flavor matter Hamiltonian while preserving a strict zero-NSI recovery of benchmark 0100.

## Frozen mathematical contract

The three-flavor effective mass-squared matrix is

`M2_eff = U diag(0,dm21,dm31) U^dagger + A_CC [diag(1,0,0) + epsilon]`

for neutrinos. `epsilon` is a dimensionless Hermitian 3x3 matrix. For antineutrinos the PMNS matrix is complex-conjugated and the complete matter contribution changes sign, with the appropriate complex conjugation of `epsilon`.

The common identity component of `epsilon` is unobservable in oscillation probabilities; preflight comparisons therefore use a trace-subtracted representative when needed.

## Synthetic fixture

The nonzero mathematical fixture is not a best fit:

- `epsilon_ee = +0.05`
- `epsilon_mumu = 0`
- `epsilon_tautau = -0.02`
- `epsilon_emu = 0.01 exp(+i*pi/5)`
- all other independent off-diagonal entries zero.

Hermiticity fixes the conjugate entry.

## Mandatory preflight gates

1. Effective Hamiltonian Hermiticity error `<=1e-12`.
2. Probability normalization error `<=1e-12`.
3. `epsilon=0` recovers benchmark 0100 probabilities to `<=1e-12`.
4. Adding a real multiple of the identity to `epsilon` leaves probabilities unchanged to `<=1e-12`.
5. The nonzero synthetic fixture produces a finite, nontrivial difference from 0100 at a declared matter point.
6. Antineutrino convention changes the sign/conjugation of the full matter deformation consistently.
7. G9 geometry is inherited; no new ray equation is introduced in this preflight.

## Authority gates

A terminal 0102 benchmark requires an immutable NSI parameter authority and a declared operator/flavor convention. Bounds from incompatible mediator assumptions may not be mixed into one statistical region. Source/profile provenance is inherited from 0100/0100a.

Until parameter authority is pinned, the maximum status is

`BLOCKED_0102_NSI_PARAMETER_AUTHORITY_UNPINNED`.

## Allowed preflight result

`PASS_0102_NSI_MATHEMATICAL_PREFLIGHT_NONTERMINAL`

A preflight PASS demonstrates only that the funnel/code correctly handles the frozen NSI deformation and known limit.
