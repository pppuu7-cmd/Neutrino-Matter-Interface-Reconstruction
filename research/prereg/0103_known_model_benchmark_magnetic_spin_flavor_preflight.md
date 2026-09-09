# 0103 — known-model benchmark: neutrino magnetic-moment / spin-flavor extension

Date frozen: 2026-09-09
Benchmark ID: NMIR-BENCHMARK-0103
State: ACTIVE_PREFLIGHT_ONLY
Parent protocol: `research/benchmarks/KNOWN_MODEL_BENCHMARK_MATRIX.md`

## Purpose

Test whether the NMIR funnel can carry a coherent spin/flavor extension without confusing magnetic-field or magnetic-moment uncertainty with a failure of standard oscillation physics.

## Frozen mathematical contract

The preflight state is six-component,

`Psi = (nu_e,nu_mu,nu_tau,anti-nu_e,anti-nu_mu,anti-nu_tau)`.

The effective mass-squared evolution matrix is a Hermitian block matrix

`M2_6 = [[M2_nu, C], [C^dagger, M2_anti]]`.

`M2_nu` and `M2_anti` are inherited from benchmark 0100. The magnetic block is derived from a transverse-field coupling `mu_nu B_perp` and converted to the effective mass-squared convention used by the 0100 propagator through

`C = 2 E * mu_nu * mu_B * B_perp * T`,

where `mu_nu` is expressed in Bohr magnetons, `mu_B = 5.7883818060e-5 eV/T`, `E` is in eV, and `T` is the frozen dimensionless transition-flavor matrix.

The synthetic transition matrix has only an e-mu antisymmetric pair nonzero. This is a mathematical fixture, not a claim about Dirac/Majorana phenomenology.

## Synthetic fixture

- `mu_nu = 1e-11 mu_B`
- `B_perp = 1e8 T`
- `E = 5 MeV`
- path length chosen prospectively in code so that the nonzero branch is numerically resolvable.

The extreme synthetic field is a code-path stress fixture only and must not be interpreted as an astrophysical estimate.

## Mandatory preflight gates

1. Six-state effective matrix Hermiticity error `<=1e-12`.
2. Six-state probability normalization error `<=1e-12`.
3. `mu_nu=0` exactly recovers two uncoupled 0100 neutrino/antineutrino sectors to `<=1e-12`.
4. `B_perp=0` gives the same decoupling limit.
5. The nonzero synthetic fixture produces finite nonzero spin/flavor transfer.
6. Rephasing/sign conventions do not change total probability.
7. No magnetic-field effect may be absorbed into a G9 ray refit.

## Authority gates

A terminal 0103 result requires before execution:

- an immutable experimental authority for the tested magnetic-moment value/range;
- a source magnetic-field profile with geometry/orientation provenance;
- a declared Dirac/Majorana transition-moment convention;
- source matter profile and detector interaction authority as separately frozen inputs.

Until these are pinned, the maximum status is

`BLOCKED_0103_MAGNETIC_AND_FIELD_AUTHORITY_UNPINNED`.

## Allowed preflight result

`PASS_0103_MAGNETIC_SPIN_FLAVOR_MATHEMATICAL_PREFLIGHT_NONTERMINAL`

A preflight PASS is neither evidence for a magnetic moment nor a Betelgeuse magnetic-field prediction.
