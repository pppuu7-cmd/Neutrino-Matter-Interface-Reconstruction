# 0103 Majorana mu12 basis-invariance result

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Status: `PASS_0103_MAJORANA_MU12_BASIS_INVARIANCE_NONTERMINAL`

Preregistration: `research/prereg/0103_majorana_mu12_basis_invariance.md`
Implementation: `scripts/audit_0103_majorana_mu12_basis_invariance.py`
Test: `tests/test_audit_0103_majorana_mu12_basis_invariance.py`
Workflow: `.github/workflows/0103-majorana-mu12-basis-invariance.yml`

## Reproducible run

- commit: `432c18dbc477b237e67f09fa93ad425cd49a2ac1`
- workflow run: `34649315896`
- job: `103427496108`
- conclusion: `success`
- focused pytest: `1 passed`
- artifact ID: `10283163796`
- artifact ZIP SHA256: `95ece0995d7d3dd501b9c023520e1dd0262c7340dedb7c114af965d699228571`

## Machine-checkable metrics

All frozen gates passed.

- `U_unitarity_residual = 2.220446049250313e-16`
- `T6_unitarity_residual = 2.220951345334711e-16`
- `H6_mass_hermiticity_residual = 1.788112030672749e-18`
- `H6_flavor_hermiticity_residual = 2.7755575615628914e-17`
- `flavor_similarity_residual = 5.551115123125783e-17`
- `magnetic_congruence_residual = 0.0`
- `magnetic_antisymmetry_residual = 3.471615371691416e-18`
- `evolved_state_basis_residual = 4.910462595695867e-16`
- `probability_basis_residual = 3.3306690738754696e-16`
- `mass_norm_residual = 7.771561172376096e-16`
- `flavor_norm_residual = 4.440892098500626e-16`
- `zero_g_antineutrino_leakage = 0.0`

## Meaning

The six-state coordinate contract

- `nu_f = U nu_m`,
- `anti_nu_f = U* anti_nu_m`,
- `T6 = block_diag(U,U*)`,

is numerically self-consistent for the conditional Majorana single-transition branch. In particular, the magnetic transition block transforms by the expected unitary congruence

`M_f = U M_m U^T`,

and an antisymmetric mass-basis `mu_12` transition remains antisymmetric after transformation. Full six-state evolution and component probabilities are invariant to machine precision under the frozen test fixture.

## Authority ceiling

This result removes **basis-representation ambiguity** as a blocker for the chosen conditional Majorana `mu_12` branch. It does not turn the synthetic unitary fixture into physical PMNS authority and does not close Betelgeuse field authority.

The Betelgeuse-specific terminal prediction remains blocked by

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.

A future terminal implementation must separately freeze its physical full three-flavor oscillation parameters and, above all, recover or prospectively define an admissible pathwise vector magnetic-field authority before propagation.
