# 0103 NuFIT 6.1 PMNS integration result

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Status: `PASS_0103_NUFIT61_PMNS_INTEGRATION_NONTERMINAL`

Preregistration: `research/prereg/0103_nufit61_pmns_integration.md`
Manifest: `research/authority/0103_nufit61_three_flavor_manifest.json`
Implementation: `scripts/audit_0103_nufit61_pmns_integration.py`
Test: `tests/test_audit_0103_nufit61_pmns_integration.py`
Workflow: `.github/workflows/0103-nufit61-pmns-integration.yml`

## Reproducible run

- commit: `9cc54cc814614854ed16342ca90b0b1535219273`
- workflow run: `34650187509`
- job: `103430262679`
- conclusion: `success`
- focused pytest: `1 passed in 0.14s`
- artifact ID: `10283258274`
- artifact ZIP SHA256: `1e2bfdbc68c711dddafaaa1f32050c3976a8ef802ffeda5c3774ecc7a1b179b7`

## Frozen ordering policy

Both NuFIT 6.1 orderings are carried as separate branches in the same machine-readable audit. No ordering is selected from 0103 magnetic-propagation output.

### Normal ordering

Frozen central values from the NuFIT 6.1 `IC24 with SK atmospheric data` fit:

- `sin^2(theta12)=0.3088`
- `sin^2(theta23)=0.470`
- `sin^2(theta13)=0.02248`
- `delta_CP=212 deg`
- `Delta m^2_21=7.537e-5 eV^2`
- `Delta m^2_31=+2.511e-3 eV^2`

Audit metrics:

- PMNS unitarity residual: `1.1102230246251565e-16`
- six-state `T6` unitarity residual: `1.110223083620729e-16`
- transformed `mu_12` antisymmetry residual: `4.6030272307414136e-17`
- `Delta m^2_21` reconstruction residual: `0.0`
- `Delta m^2_31` reconstruction residual: `0.0`

### Inverted ordering

Frozen central values:

- `sin^2(theta12)=0.3088`
- `sin^2(theta23)=0.550`
- `sin^2(theta13)=0.02262`
- `delta_CP=274 deg`
- `Delta m^2_21=7.537e-5 eV^2`
- `Delta m^2_32=-2.483e-3 eV^2`

Audit metrics:

- PMNS unitarity residual: `2.220446049250313e-16`
- six-state `T6` unitarity residual: `2.2204710397853543e-16`
- transformed `mu_12` antisymmetry residual: `4.16569040014935e-17`
- `Delta m^2_21` reconstruction residual: `0.0`
- `Delta m^2_32` reconstruction residual: `0.0`

## Authority caveat: byte pin

The earlier workflow `.github/workflows/0103-nufit61-authority-pin.yml` did **not** byte-pin the official NuFIT PDFs. Its HTTP requests failed because the GitHub-hosted runner could not validate the `nu-fit.org` TLS certificate chain. The workflow remained green only because fetch failure was logged rather than made fatal.

Therefore:

- official NuFIT 6.1 numerical inputs: **VERIFIED AND INTEGRATION-PASS**;
- internal PMNS/mass-spectrum conversion: **PASS for both NO and IO**;
- NuFIT PDF byte-level pin on the GitHub runner: **PENDING / INFRASTRUCTURE-LIMITED**;
- this TLS issue is not a physics FAIL and does not justify changing any fitted value.

## Meaning for 0103

The physical three-flavor parameter layer is no longer an internal implementation blocker. Combined with the previously passing Majorana `mu_12` basis-invariance audit, the remaining dominant Betelgeuse-specific terminal blocker is the absence of a recoverable path-resolved vector magnetic field from which `B_perp(r)` can be derived prospectively.

Current terminal ceiling remains:

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.
