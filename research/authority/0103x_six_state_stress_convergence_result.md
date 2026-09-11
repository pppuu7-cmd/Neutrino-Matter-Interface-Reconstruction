# 0103X six-state stress/convergence matrix — result

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Scope: `NONTERMINAL_SYNTHETIC_NUMERICAL_STRESS_ONLY`
Preregistration commit: `5f381b4c06c462f69b2a464cba9c6220e46bc9af`
Implementation commit: `8340994380ceaf55621b74f74f9cc393f04e4776`

## Authoritative execution

- workflow: `0103X six-state stress convergence`
- run: `34657252689`
- job: `103452217875`
- conclusion: `success`
- focused pytest: `1 passed in 1.48s`
- artifact: `nmir-0103x-six-state-stress-convergence`
- artifact ID: `10285532220`
- artifact ZIP SHA256: `fa38c8c14fc21cf0fe0cf754d829d54a81171a85cd0c4aa891416818c2453a5e`
- artifact payload: `0103x_metrics.json`, `0103x_convergence_matrix.csv`

## Frozen-gate result

Status: `PASS_0103X_SIX_STATE_STRESS_CONVERGENCE_NONTERMINAL`

All preregistered gates passed.

Frozen coupling multipliers: `[0, 1e-3, 1e-2, 1e-1, 1]`.
Frozen production resolutions: `[64, 128, 256, 512, 1024]`.
Reference resolution: `4096`.

Key metrics:

- convergence improves from N=64 to N=1024 for every nonzero coupling: `true`
- worst N=1024 final-probability L-infinity error versus N=4096: `1.1071636862869383e-07`
- preregistered accuracy ceiling: `1e-6`
- max Hamiltonian Hermiticity residual: `1.1102230246251565e-16`
- max final norm residual: `9.14823772291129e-14`
- max probability-sum residual: `9.14823772291129e-14`
- zero-coupling maximum antineutrino leakage: `0.0`
- maximum nonzero-coupling antineutrino probability: `0.2598682411798712`
- identical N=1024 repeat probability residual: `0.0`

## Interpretation

The synthetic noncommuting six-state Hamiltonian remains unitary, deterministic and convergent across the preregistered coupling/refinement matrix. The worst N=1024 error is about nine times below the frozen `1e-6` ceiling.

This strongly reduces numerical convergence as a candidate explanation for a future 0103 signal in the same solver architecture, but it is not physical evidence for spin-flavor conversion in Betelgeuse. Physical inference remains blocked until a valid astrophysical magneto-matter state is supplied.
