# NMIR iteration 0031 — long-range/nonlocal interaction-budget gate

Date: 2026-09-06
Classification: **PASS_LONG_RANGE_BUDGET / STRONG-NEGATIVE scoped**

## Funnel target
Iteration 0028 left unscaled all-to-all response open because the local-spin first-moment theorem does not apply to growing coordination. This iteration asks whether that superextensive response remains a free gain when the passive medium's own pair-interaction norm budget is included.

## Prospective contract
`research/long_range_budget_prereg.md`, commit `fb6e777b9306a5d1cbaef409cf72b19d597bdf52`, frozen before implementation and result inspection.

## Analytic bound
For

`H=sum_{i<j} h_ij`,

`O=sum_i o_i`, `||o_i||<=o0`,

only `o_i+o_j` contributes to the double commutator of pair `(i,j)`. Therefore

`m1=(1/2)<[O,[H,O]]>`

obeys

`|m1| <= 8 o0^2 W_N`,

where

`W_N=sum_{i<j} ||h_ij||`.

Hence an extensive absolute interaction budget `W_N<=epsilon N` implies an extensive energy-weighted first moment and a bounded per-particle response:

`|m1|/N <= 8 o0^2 epsilon`.

For all-to-all pair norm `||h_ij||=J0/N^kappa`,

`W_N ~ (J0/2) N^(2-kappa)`,

and both the interaction budget per particle and the first-moment upper bound per particle scale as `N^(1-kappa)`.

## Literature consistency
Modern long-range many-body reviews distinguish a strong/nonadditive regime, where the energy can be superextensive, from energy-extensive long-range regimes obtained by appropriate normalization. The NMIR result is a scoped response-budget application of that distinction, not a claim of a new universal thermodynamic theorem.

## Hosted authority
- run `34041247733`
- job `101508285576`
- head `fa6b254c999c4f215da23b9b033f770d8190ef15`
- artifact `9991728037`
- artifact ZIP SHA256 `81c116433a5ab711de870e150710057f97bd10916f081949592e06f736e5245e`
- dedicated tests: `7 passed`
- raw benchmark inspected.

## Raw result
For `N1=1000`, `N2=1,000,000`, `o0=0.5`:

| all-to-all scaling | interaction budget / particle gain | response bound / particle gain |
|---|---:|---:|
| `kappa=0` | **`1001.0`** | **`1001.0`** |
| `kappa=0.5` | **`31.6543993783`** | **`31.6543993783`** |
| `kappa=1` | **`1.001`** | **`1.001`** |

Additional diagnostics:
- first-moment identity relative error `0.0`;
- maximum response-vs-budget gain mismatch `2.21823e-16`;
- unscaled analytic-gain error `0.0`;
- Kac-normalized power-law factor error `0.0`.

Frozen power-law diagnostics in `d=3` reproduce the expected raw per-particle budget scaling:
- `alpha=1`: gain `100` over the N range;
- `alpha=2`: gain `10`;
- `alpha=3`: logarithmic gain `2`;
- `alpha=4`: gain `1`;
while the explicit Kac-normalized diagnostic is `1` at both sizes.

## Scientific interpretation
The all-to-all loophole does not provide a free passive energy-weighted enhancement at fixed extensive absolute pair-interaction budget. In this class, any parametric superextensive response upper bound tracks a parametric growth of the medium's own interaction norm budget. Kac/extensivity normalization removes both together.

This substantially narrows the surviving many-body route:
- ordinary local density response: already class-bounded;
- ordinary bounded-local spin response: already class-bounded;
- passive long-range pair response with O(N) absolute interaction budget: now class-bounded;
- unnormalized/nonadditive superextensive matter is not ruled out mathematically, but its growing internal energy scale must be counted and cannot be called neutrino-supplied power.

## Remaining loopholes
1. A dynamical mediator/field omitted by an effective pair Hamiltonian; its field energy and stability must be included explicitly.
2. Active/non-equilibrium pumping; external power is not neutrino-supplied.
3. Genuine higher-body interactions outside the pair theorem.
4. Nuclear-current/resonance sectors, which are different microscopic channels.
5. BSM neutrino couplings, still locked until the SM funnel is mature.
