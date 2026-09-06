# Iteration 0058 — required measured topology-performance envelope

Date: 2026-09-07
Gate: G2 detector-specific rejection × signal-acceptance requirement
Scientific classification: `PASS_REQUIRED_TOPOLOGY_PERFORMANCE_ENVELOPE / PUBLIC_ACHIEVEMENT_ANCHOR_OPEN`

## Prospective authority
Contract: `research/prereg/0058_required_topology_performance_envelope.md`.
Preregistration commit: `447dedd4d39414b1dbc113b6f291f9490d31f2d1`.
Scientific workflow head: `7ee2d1598d49146a98d39d71a2b7c4cb18b1d234`.
Hosted run/job: `34061477253 / 101562663106`.
Artifact: `9997604078`, `topology-performance-result`.
Artifact ZIP SHA256: `ff0ad8d14663358cb8d3136570c2297ecfdce21895e500b05a71f93d133274fa`.
The dedicated job completed successfully; pytest and the fail-closed benchmark steps both completed successfully. The downloaded machine-readable artifact was inspected directly and returned the frozen PASS/classification strings.

## Frozen model
The 0057 exact three-year extended-Poisson time likelihood is unchanged. Horizon is `1095.75 d`, pre-selection solar CEvNS signal is `S0=30`, and the two alternative background-time branches remain `authority_capped_900d` and `stress_3y`. They are alternatives and are never multiplied.

For topology signal acceptance `epsilon_S`, two accounting modes were frozen prospectively:
- fixed exposure: solve `q0(S=epsilon_S*S0,b/R_topo)=25`;
- signal-restored exposure: increase exposure by `1/epsilon_S`, giving exactly `R_topo=R_base/epsilon_S`.

Acceptance grid: `epsilon_S={1.0,0.9,0.8,0.7,0.5,0.3}`.

## Hosted result
At full signal acceptance the calculation exactly recovers the 0057 rejection requirements:
- authority-capped 900 d: `R_base=1.77570304169906e7`;
- stress continuation 3 y: `R_base=1.4440370654436817e7`.

Required topology rejection at fixed exposure:

| epsilon_S | authority-capped 900 d | stress 3 y |
|---:|---:|---:|
| 1.0 | `1.77570304169906e7` | `1.4440370654436817e7` |
| 0.9 | `2.310222726990198e7` | `1.8903238652537644e7` |
| 0.8 | `3.1182821573522978e7` | `2.5694624324020274e7` |
| 0.7 | `4.416626004869545e7` | `3.668765355142948e7` |
| 0.5 | `1.1095483713662188e8` | `9.407539776651382e7` |
| 0.3 | `5.248261401309289e8` | `4.58373974654573e8` |

Signal-restored exposure gives the exact frozen relation `R_base/epsilon_S`; representative values are:
- at `epsilon_S=0.5`: `3.55140608339812e7` (authority-capped) and `2.8880741308873635e7` (stress);
- at `epsilon_S=0.3`: `5.919010138996867e7` and `4.813456884812272e7`.

The artifact satisfies all preregistered qualitative guards: decreasing acceptance never improves the requirement; fixed exposure is always more demanding than signal-restored exposure for `epsilon_S<1`; all requirements stay above `1e6`; and no number is labelled as measured DoubleTES performance.

## Scientific interpretation
This gate converts the previously qualitative DoubleTES/topology survivor into a direct quantitative technology target. With the optimistic 0057 time information already fully credited, a detector/topology selection still needs background rejection of order `1e7` at near-unity CEvNS-like bulk acceptance. Signal loss is very costly: at 50% acceptance and fixed exposure the requirement rises to roughly `9.4e7–1.11e8`, and at 30% acceptance to roughly `4.6e8–5.25e8`.

These factors are not additional multipliers to combine with 0056 waiting factors or the 0057 rejection. They are the remaining detector/topology requirement conditional on the full 0057 time-aware likelihood.

No comparable public underground measured rejection × bulk-acceptance anchor is frozen here. Therefore the mechanism remains a detection survivor with a large quantitative technology gap.

## Exact next gate
G2 is now blocked on a genuinely measured comparable topology-performance anchor rather than another algebraic requirements map. The highest-value independent OPEN class-level gate is therefore G3: prospectively audit whether Standard-Model/chiral-EFT theory supplies any defensible universal renormalized contact/two-body-current coefficient bound that can close the residual left by 0047–0048 without treating EFT naturalness as a theorem. If no hard universal bound exists, record that negative result and preserve the residual; do not invent a coefficient ceiling.