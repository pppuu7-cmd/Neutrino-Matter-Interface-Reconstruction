# NMIR iteration 0027 — passive density-response f-sum gate

Date: 2026-09-06
Classification: **PASS_DENSITY_FSUM / STRONG-NEGATIVE scoped for superextensive energy-weighted density engineering**

## Funnel target
F5/F6 many-body density response and the density-coupled part of G10 staggered/layered matter. This iteration asks whether rearranging the same passive constituents into phonons, crystals, narrow collective modes or staggered layers can create parametrically new **energy-weighted** neutrino coupling, rather than merely redistributing event strength.

## Prospective contract
`research/density_fsum_prereg.md`, commit `0fbc3f1977630add7eb15896f7da2458742e8df7`, was committed before the hosted benchmark.

For

`H = sum_i p_i^2/(2m_i) + V({r_i})`

with coordinate-local `V` commuting with

`rho_q = sum_i g_i exp(i q·r_i)`,

the positive-frequency dynamic structure factor obeys

`m1(q) = integral dω ω S(q,ω) = q^2/2 * sum_i g_i^2/m_i`.

For a non-negative bounded kernel `K(q,ω)<=Kmax(q)`,

`D(q)=integral dω ω K(q,ω) S(q,ω) <= Kmax(q) m1(q)`.

The gate therefore tests whether spectral rearrangement can change unweighted event strength without manufacturing extra energy-weighted density response.

## Implementation and hosted authority
- implementation: `src/nmir/density_fsum.py`, commit `95b1d2d9c05e5d3172e6394f0e531470817edc47`
- tests: `tests/test_density_fsum.py`, commit `a6e20725efd30dfc52411e51c7c840c9e8d5da91`
- benchmark: `scripts/density_fsum_benchmark.py`, commit `f7bf1d801c1462fbd7e260dd85e719cb2649696e`
- hosted head: `1b1b4c388648d5f0ee75b96bd0cb61c283ae9863`
- workflow run: `34039755966`
- job: `101504245884`
- artifact: `9991299921`
- artifact ZIP digest: `sha256:064566b0bf75040f35c0308f0b8fe53103e995a175ce5c06bb6d694467cde6be`
- dedicated tests: **5 passed**

Raw job log was inspected before classification.

## Raw scientific result

| frozen diagnostic | result |
|---|---:|
| `max_m1_relative_error` | `0.0` |
| `max_unit_kernel_deposition_relative_error` | `1.7985613162596616e-16` |
| max `D/(Kmax*m1)` | `0.9999999995` |
| collective-mode unweighted-strength gain | `1.0e6` |
| collective-mode energy-weighted gain | `1.0` |
| f-sum gain from `N=1` to `N=1e6` | `999999.9999999999` |
| characteristic narrowing/energy-scale ratio tested | `1.0e6` |
| status | **PASS_DENSITY_FSUM** |

All prospective numerical criteria passed without modification.

## Scientific meaning
A passive coordinate-local density-coupled medium may move response into narrow peaks or very low-energy collective modes and thereby greatly increase an **unweighted event-count/detectability proxy** at selected energies. It does not, under this scoped sum rule, create superextensive integrated energy-weighted density strength from the same constituents. The exact first moment scales linearly with constituent count, not as `N^2`.

This materially narrows the original staggered-layer/phonon idea for **energy harvesting**: geometry or collective density modes can still redirect/sculpt the response and may be useful for detection, but a claimed energy gain must come from a kernel/channel that escapes the assumptions of this density f-sum gate rather than from spectral rearrangement alone.

## Explicit surviving loopholes
This result does **not** close:
- spin/axial response and magnons;
- charged-current nuclear transmutation;
- nonlocal/momentum-dependent interactions that modify the double commutator;
- actively pumped/non-equilibrium media (external energy must be accounted separately);
- two-body weak currents not reducible to this density operator;
- gravitational focusing;
- BSM interactions.

## Funnel consequence
The highest-value many-body survivor is now the **spin/axial response** branch. Its energy-weighted sum rule contains Hamiltonian-dependent spin commutators and therefore cannot be imported from the density result. The next useful gate is to construct a prospective spin-sum response bound/toy that distinguishes magnon event enhancement from neutrino-supplied deposited energy.

`NMIR_READINESS` credit recommendation: +2 percentage points, because this is a prospectively frozen, hosted/raw-inspected class-level F5/F6 result rather than another target scan.