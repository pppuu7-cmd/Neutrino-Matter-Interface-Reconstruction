# 0103 NuFIT 6.1 PMNS integration preregistration

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Status: PREREGISTERED NONTERMINAL PARAMETER-INTEGRATION AUDIT

## Purpose

Verify that the prospectively frozen NuFIT 6.1 central values for both mass orderings can be converted into internally consistent three-flavor PMNS matrices and mass-squared spectra for the six-state Majorana `mu_12` architecture, without choosing an ordering based on any magnetic-propagation output.

This audit does not use a Betelgeuse magnetic field and cannot produce a terminal spin-flavor prediction.

## Frozen authority input

`research/authority/0103_nufit61_three_flavor_manifest.json`

Use the NuFIT 6.1 `IC24 with SK atmospheric data` central values exactly as frozen there, for both NO and IO.

## PMNS convention

Use the standard three-angle/one-Dirac-phase parameterization

`U = R23 * U13(delta) * R12`

with `theta_ij = asin(sqrt(sin2_theta_ij))` and `delta = delta_cp_deg * pi/180`.

No Majorana phases are required for the oscillation Hamiltonian or for the representation-invariance test of the single transition-moment operator used here.

## Mass-squared convention

An overall identity shift is physically irrelevant for oscillations. Build a representative spectrum with `m1^2 = 0`:

- NO: `m2^2 = dm2_21`, `m3^2 = dm2_31`.
- IO: NuFIT tabulates `dm2_32`; therefore `m2^2 = dm2_21` and `m3^2 = dm2_32 + dm2_21`.

The audit must reconstruct the tabulated differences exactly within floating tolerance.

## Gates

For both NO and IO:

1. PMNS unitarity residual <= `1e-14`.
2. Reconstructed `sin^2(theta12,13,23)` values agree with the manifest to <= `1e-14`.
3. Reconstructed `dm2_21` agrees to <= `1e-16 eV^2`.
4. Reconstructed `dm2_3l` agrees to <= `1e-16 eV^2` using the ordering-specific NuFIT convention.
5. The six-state transform `T6 = block_diag(U,U*)` is unitary to <= `1e-14`.
6. A mass-basis antisymmetric `mu_12` transition matrix remains antisymmetric after `U M U^T` to <= `1e-14`.
7. No ordering-selection function is present: both branches must be emitted in one machine-readable result.

## PASS ceiling

`PASS_0103_NUFIT61_PMNS_INTEGRATION_NONTERMINAL`

PASS closes only the internal conversion/integration of the official NuFIT numerical inputs. It does not convert the failed TLS byte-fetch workflow into a byte-level authority pin and it does not close Betelgeuse `B_perp(r)` authority.
