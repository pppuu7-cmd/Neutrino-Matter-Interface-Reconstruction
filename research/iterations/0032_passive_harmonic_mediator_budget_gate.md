# NMIR iteration 0032 — passive harmonic-mediator budget gate

Date: 2026-09-06
Classification: **PASS_HARMONIC_MEDIATOR_BUDGET / STRONG-NEGATIVE scoped**

## Funnel target
Iteration 0031 bounded passive long-range pair Hamiltonians at fixed extensive absolute interaction budget. This iteration closes the most obvious effective-Hamiltonian loophole: a common dynamical cavity/field mode whose own energy might be omitted when deriving an all-to-all material interaction.

## Prospective contract
`research/harmonic_mediator_prereg.md`, commit `059b66d1e12f58bf520eef59a6b54d7d3030f682`, frozen before implementation/result.

## Model and identity
For a passive stable harmonic mediator,

`H_med(x,O) = (kappa/2)x^2 - g_N x O`, `kappa>0`, `|O|<=oN`.

Completing the square,

`H_med = (kappa/2)(x-g_N O/kappa)^2 - g_N^2 O^2/(2kappa)`.

At the minimizing displacement `x_*=g_N O/kappa`,

`E_field = kappa x_*^2/2 = g_N^2 O^2/(2kappa)`,

while the induced collective interaction has equal magnitude

`|E_induced| = g_N^2 O^2/(2kappa)`.

Freeze `g_N=g0/N^gamma`. Then both field and induced energy per constituent scale as

`E/N ~ N^(1-2 gamma)`.

The extensive Dicke scaling `gamma=1/2` therefore yields O(1) energy per particle and effective all-to-all pair scale `J_eff~g_N^2/kappa~1/N`.

## Literature consistency
Standard Dicke-model thermodynamic-limit formulations use a light-matter coupling proportional to `1/sqrt(N)`. The NMIR calculation makes the associated field-energy accounting explicit rather than treating the induced all-to-all term as a free material interaction.

## Hosted authority
- run `34041392001`
- job `101508681617`
- head `4202062883478258ee0a53378235002f3ceda234`
- artifact `9991770130`
- artifact ZIP SHA256 `c87d7ed2ed6ef8918fa30e1c67510db715be56067200eed1355b0d80287919c2`
- dedicated tests: `7 passed`
- raw benchmark inspected.

## Raw result
For `N1=1000`, `N2=1,000,000`:

| `gamma` in `g_N~N^-gamma` | field energy / particle gain | induced energy / particle gain |
|---:|---:|---:|
| `0` | **`1000.0`** | **`1000.0`** |
| `0.25` | **`31.62277660`** | **`31.62277660`** |
| `0.5` | **`1.0`** | **`1.0000000000000002`** |
| `0.75` | **`0.03162277660`** | **`0.03162277660`** |

Additional controls:
- completion-of-square identity relative error `0.0`;
- max field-vs-induced energy mismatch `2.30e-16`;
- max scaling mismatch `2.22e-16`;
- at `gamma=1/2`, `J_eff(N2)/J_eff(N1)=0.0010000000000000002`, matching `N1/N2` with `2.17e-16` relative error.

## Scientific interpretation
A passive stable single harmonic mediator does not generate a free superextensive collective interaction when the mediator energy is included. The same coupling that creates an `O(N^2)` induced term at fixed `g_N` also creates an `O(N^2)` field displacement-energy scale. Enforcing extensive total energy requires `g_N~1/sqrt(N)`, which maps the effective all-to-all interaction onto the Kac `1/N` class already bounded in iteration 0031.

This closes the simplest cavity/common-mode route to a free passive energy-weighted neutrino enhancement. It does not exclude:
1. genuinely multi-mode or gapless fields;
2. nonlinear mediators whose stable-energy scaling differs from a harmonic mode;
3. active/driven-dissipative media, whose pump power must be excluded from neutrino-supplied energy;
4. higher-body interactions;
5. new BSM neutrino operators.
