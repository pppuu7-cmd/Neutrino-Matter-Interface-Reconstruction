# 0101 — known-model benchmark: 3+1 sterile-neutrino extension

Date frozen: 2026-09-09
Benchmark ID: NMIR-BENCHMARK-0101
State: ACTIVE_PREFLIGHT_ONLY
Parent protocol: `research/benchmarks/KNOWN_MODEL_BENCHMARK_MATRIX.md`

## Purpose

Test whether the NMIR funnel can represent a minimal unitary 3+1 oscillation extension without silently converting missing sterile-parameter authority into a physics failure.

0101 is a mathematical/known-limit preflight until an external sterile-neutrino parameter authority and source profile are pinned.

## Frozen mathematical contract

Flavor state order is

`(nu_e, nu_mu, nu_tau, nu_s)`.

The 4x4 vacuum mixing matrix is constructed prospectively as

`U4 = R34(theta34) R24(theta24) R14(theta14) diag(U_PMNS,1)`

for the synthetic preflight fixture. The three sterile rotations are real in the preflight; extra sterile CP phases are fixed to zero and may not be introduced after seeing the result.

Mass-squared eigenvalues are

`(0, dm21, dm31, dm41)`.

The active 3x3 parameters and NO/IO convention are inherited unchanged from benchmark 0100.

For matter preflight, the ordinary charged-current term acts on `nu_e`. A sterile-relative neutral-current term is included after subtraction of the common active NC phase. For electrically neutral matter with electron fraction `Ye`, the frozen effective mass-squared sterile contribution is

`A_s = A_CC * (1-Ye)/(2 Ye)`

for neutrinos, with the overall matter signs reversed for antineutrinos. This preflight uses only `0 < Ye <= 1`.

## Synthetic fixture

The nonzero synthetic point is deliberately not a best fit and may never be reported as one:

- `sin^2(theta14)=0.02`
- `sin^2(theta24)=0.01`
- `sin^2(theta34)=0.00`
- `dm41=1.0 eV^2`
- `E=5 MeV`

Its only role is to prove that the 4-state code path is nontrivial.

## Mandatory preflight gates

1. `U4` unitarity error `<=1e-12`.
2. Hermiticity of the effective mass-squared matrix `<=1e-12`.
3. Four-flavor probability normalization error `<=1e-12`.
4. Exact decoupling recovery: when all sterile angles are zero, the active 3x3 probabilities match benchmark 0100 to `<=1e-12` and sterile probability is `<=1e-12`.
5. The frozen nonzero fixture produces finite outputs and nonzero sterile leakage at at least one declared propagation point.
6. Antineutrino matter terms reverse sign consistently.
7. No G9 ray refit is permitted: 0101 changes flavor-state propagation only.

## Authority gates

A terminal 0101 physics result requires, before execution:

- an immutable global-fit/experimental authority defining the tested sterile parameter point or scan domain;
- explicit treatment of correlations/likelihood if a statistical exclusion is claimed;
- the same source-profile authority discipline as 0100;
- any detector cross-section or sterile-specific interaction assumption separately frozen.

Until those inputs are pinned, the maximum status is

`BLOCKED_0101_STERILE_PARAMETER_AUTHORITY_UNPINNED`.

## Allowed preflight result

`PASS_0101_3P1_MATHEMATICAL_PREFLIGHT_NONTERMINAL`

A successful preflight is not evidence for a sterile neutrino and is not an exclusion of any sterile parameter region.
