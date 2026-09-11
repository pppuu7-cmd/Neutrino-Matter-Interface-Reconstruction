# 0103 Majorana mu12 basis-invariance preregistration

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Status: PREREGISTERED REPRESENTATION AUDIT — NONTERMINAL

## Purpose

Test whether a single antisymmetric Majorana transition moment `mu_12` can be represented consistently in mass and flavor coordinates inside the six-state `(nu, anti-nu)` Hamiltonian, without importing any unpinned Betelgeuse field profile or claiming physical PMNS parameter authority.

This is a representation/invariance audit only. It is not a Betelgeuse propagation result and not a neutrino-magnetic-moment detection claim.

## Frozen coordinate convention

For three-component coordinate vectors,

- `nu_f = U nu_m`,
- `anti_nu_f = U* anti_nu_m`,
- `T6 = block_diag(U, U*)`,
- `Psi_f = T6 Psi_m`,
- `H6_f = T6 H6_m T6^dagger`.

Therefore the upper-right magnetic block must transform by unitary congruence,

`M_f = U M_m U^T`.

The mass-basis transition fixture is antisymmetric with only the 1-2 pair nonzero:

`K_m[0,1]=+1`, `K_m[1,0]=-1`.

`M_m = g K_m`, where `g` is a dimensionless synthetic audit scale.

## Explicit non-physical unitary fixture

The audit uses a deterministic PMNS-shaped complex unitary matrix constructed from frozen test angles

- `theta12 = 0.57`,
- `theta13 = 0.15`,
- `theta23 = 0.79`,
- `delta = 1.17` radians.

These are **test fixtures only**. They are deliberately not labelled as NuFIT/PDG/physical NMIR inputs. The repository currently has no full production 3x3 PMNS parameter authority frozen for 0103.

## Structured Hamiltonian fixture

Use deterministic dimensionless values

- vacuum diagonal `D = diag(0, 0.13, 0.41)`,
- electron matter term in flavor coordinates `V_f = diag(0.07,0,0)`,
- magnetic scale `g = 0.025`,
- propagation coordinate `L = 3.7`.

Mass-basis blocks are constructed consistently:

- `Hnu_m = D + U^dagger V_f U`,
- `Hanti_m = D - U^T V_f U*`,
- `H6_m = [[Hnu_m,M_m],[M_m^dagger,Hanti_m]]`.

The corresponding flavor-basis Hamiltonian is obtained both analytically from the transformed 3x3 blocks and independently through `T6 H6_m T6^dagger`.

## Frozen initial state

Use a normalized deterministic complex six-component mass-coordinate vector with nonzero support in both neutrino and antineutrino sectors. Flavor coordinates are `Psi_f0=T6 Psi_m0`.

## Evolution

For each Hermitian constant Hamiltonian, construct the exact unitary propagator with Hermitian eigendecomposition:

`S = V diag(exp(-i lambda L)) V^dagger`.

No ODE discretization enters this audit.

## Gates

All must pass:

1. `U` unitarity residual <= `1e-12`.
2. `T6` unitarity residual <= `1e-12`.
3. mass and flavor six-state Hamiltonian Hermiticity residuals <= `1e-12`.
4. explicit flavor Hamiltonian and similarity-transformed Hamiltonian differ by <= `1e-12`.
5. transformed magnetic block satisfies `M_f = U M_m U^T` within `1e-12`.
6. transformed magnetic block remains antisymmetric within `1e-12`.
7. direct flavor evolution and transformed mass-basis evolution differ by <= `1e-11` in state amplitude.
8. component probabilities differ by <= `1e-11`.
9. both evolutions conserve norm within `1e-12`.
10. with `g=0`, neutrino and antineutrino sectors decouple to numerical precision <= `1e-12` for a neutrino-only initial state.

## Interpretation ceiling

PASS establishes only:

`PASS_0103_MAJORANA_MU12_BASIS_INVARIANCE_NONTERMINAL`.

PASS does not close:

- full physical PMNS parameter authority for a terminal 0103 implementation;
- Betelgeuse pathwise `B_perp(r)` authority;
- any terminal spin-flavor prediction.

The current Betelgeuse-specific ceiling remains `BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY` unless a machine-readable vector field is separately recovered and preregistered.
