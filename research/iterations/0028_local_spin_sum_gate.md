# NMIR iteration 0028 — local spin/axial first-moment gate

Date: 2026-09-06
Classification: **PASS_LOCAL_SPIN_SUM / STRONG-NEGATIVE scoped against free superextensive local-magnon energy gain**

## Funnel target
F5/F6 passive polarized spin media and magnonic/axial response after iteration 0027 closed the analogous coordinate-local density loophole.

## Prospective contract
`research/spin_local_sum_prereg.md`, commit `c68cc0da22abc5a11ee248d341473733b7f1084d`, was committed before hosted execution.

For `H=sum_X h_X`, `O=sum_i g_i S_i^a`, the standard first-moment identity is

`m1 = 1/2 <[O^dagger,[H,O]]>`.

Using only local support and `||[A,B]||<=2||A||||B||`,

`|m1| <= 2 sum_X ||h_X|| ||O_X||^2`

and with `||S_i^a||<=s`, `|g_i|<=gmax`,

`|m1| <= 2 s^2 gmax^2 sum_X ||h_X|| |X|^2`.

For pairwise spin-1/2 Heisenberg bonds, `||J S_i·S_j||=3|J|/4`, giving

`|m1| <= (3/2) sum_bonds |J_ij|`.

For bounded coordination `z` and `|J|<=Jmax`,

`|m1| <= (3/4) N z Jmax`,

so the energy-weighted response envelope is extensive in `N`.

## Hosted authority
- implementation commit `2bb9b4349a3971ef9f87546f82cf8fc423396956`
- tests commit `86980ca25eec2b9342128b897f87c381e5e1bd5d`
- benchmark commit `5660d98feffd265ae2560b0851fce6748e41e2eb`
- hosted head `336d01532d9ed2fdcc5665e63a3fc5e4329e6b26`
- run `34040105285`
- job `101505185065`
- artifact `9991400307`
- artifact ZIP SHA256 `c0dc0698997fa43b54be8d93a247068a1d213785b7e3922f20a260047c4e7ece`
- dedicated tests: **5 passed**

Raw job log was inspected before scientific classification.

## Raw result
| frozen diagnostic | result |
|---|---:|
| pair-specialization relative error | `0.0` |
| Heisenberg bond norm at `|J|=1` | `0.75` |
| local first-moment gain, `N=1 -> 1e6` | **`1.0e6`** |
| soft-mode unweighted-strength gain | **`1.0e6`** |
| soft-mode energy-weighted gain | **`1.0`** |
| unscaled all-to-all gain, `N=1000 -> 1e6` | **`1001000.0`** |
| Kac-scaled all-to-all gain, `N=1000 -> 1e6` | **`1000.0`** |
| reference linear gain | `1000.0` |
| status | **PASS_LOCAL_SPIN_SUM** |

## Scientific meaning
For passive bounded-coordination local spin Hamiltonians, simply softening/organizing magnons can create a very large low-energy event-strength/detectability gain without creating corresponding new neutrino-supplied energy-weighted strength. The first moment is controlled by the local interaction-energy norm budget and scales extensively.

The deliberately included all-to-all control is essential: a genuinely unscaled complete-graph interaction is superextensive. Therefore the funnel does not rule out long-range/nonlocal collective interfaces; it identifies them as a distinct loophole that must pay the physical price of a nonlocal/superextensive interaction-energy budget or an extensivity-restoring scaling.

## Scope / survivors
This is not an absolute W/kg ceiling. Still open:
- long-range/cavity-mediated/nonlocal spin couplings;
- active/pumped spin media with separate external-energy accounting;
- itinerant/relativistic electron response outside the local-spin model;
- charged-current and genuine two-body nuclear currents;
- gravitational focusing;
- BSM.

## Literature consistency
The result is structurally consistent with Hohenberg-Brinkman and subsequent magnetic-neutron-scattering first-moment sum rules, where the spin spectral first moment is tied to exchange energies and static correlations rather than freely determined by magnon peak height.

## Funnel consequence
The ordinary passive local-density and local-spin collective routes are now both class-level constrained against free superextensive **energy** gain. The next highest-value interfaces are those that escape locality/ordinary response bookkeeping: G9 gravitational focusing, genuinely nonlocal/active media, and the remaining nuclear-current/G8 target-specific resonance loopholes.

Readiness recommendation: `NMIR_READINESS: 54%` (audit estimate), +2 only for this prospectively frozen hosted/raw-inspected class gate.