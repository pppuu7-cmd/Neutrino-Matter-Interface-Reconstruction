# 0103M coherent magneto-matter pipeline — result

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Scope: `NONTERMINAL_SYNTHETIC_ENGINEERING_ONLY`
Preregistration commit: `5f381b4c06c462f69b2a464cba9c6220e46bc9af`
Implementation commit: `8340994380ceaf55621b74f74f9cc393f04e4776`

## Authoritative execution

- workflow: `0103M coherent magneto-matter pipeline`
- run: `34657252656`
- job: `103452217733`
- conclusion: `success`
- focused pytest: `1 passed in 0.48s`
- artifact: `nmir-0103m-coherent-magneto-matter-pipeline`
- artifact ID: `10285457496`
- artifact ZIP SHA256: `553c214f5065c5c47a793b19fab821eca3dce7302552e6fcc949097c492142f3`
- artifact payload: `0103m_metrics.json`, `0103m_ray_samples.csv`

## Frozen-gate result

Status: `PASS_0103M_COHERENT_SYNTHETIC_MAGNETO_MATTER_PIPELINE_NONTERMINAL`

All preregistered gates passed.

Key metrics:

- shared co-registered state/grid/ray identity: `true`
- grid: `9 x 9 x 9`
- path samples: `257`
- extrapolation: `false`
- max trilinear interpolation residual: `6.661338147750939e-16`
- max `B_perp` orthogonality residual: `1.8041124150158794e-16`
- max `B_perp` magnitude-consistency residual: `3.3306690738754696e-16`
- max Hamiltonian Hermiticity residual: `6.938893903907228e-18`
- norm residual: `3.552713678800501e-15`
- probability-sum residual: `3.3306690738754696e-15`
- zero-coupling antineutrino leakage: `0.0`
- positive-control total antineutrino probability: `0.05692814750433409`
- deterministic-repeat probability residual: `0.0`

Final flavor-basis probabilities for the synthetic positive control:

`[0.8928776064524888, 0.04187731872895272, 0.008316927314227769, 3.6258580797712006e-07, 0.02820856263160426, 0.028719222286921843]`

## Interpretation

This closes a technical question: when vector magnetic field and matter variables are supplied as one co-registered 3-D state, the frozen ray extraction, `B_perp` construction, matter sampling and six-state Majorana propagation can operate as one deterministic pipeline without a newly exposed numerical/interface failure.

It does **not** supply Betelgeuse authority. The fixture is synthetic and dimensionless. No result here may be promoted to a Betelgeuse prediction or used to invent an internal field profile.

The terminal blocker therefore moves from generic pipeline uncertainty to the provenance of a real/recoverable Betelgeuse-like co-registered magneto-matter state.
