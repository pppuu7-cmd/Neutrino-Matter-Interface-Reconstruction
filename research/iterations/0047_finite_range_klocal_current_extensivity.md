# Iteration 0047 — finite-range k-local higher-body current extensivity

Date: 2026-09-06
Classification: `PASS_KLOCAL_EXTENSIVITY`
Prospective contract: `research/klocal_higher_body_current_prereg.md`, commit `1e669c71a10784120d831c5c57560129146df333` (frozen before implementation and before the hosted result)
Scientific workflow head: `21e42755ed237074601f45a48a401a52586c0de2`
Hosted run/job: `34056195172` / `101548425397`
Artifact: `9996023078`, ZIP SHA256 `7203aaec5cb567c1ac8cac3ca661198f5d8673bf132497bc3eb4b7edd5b402cb`

## Frozen class and theorem
For `O=sum_X o_X` and `H=sum_Y h_Y`, with current supports `|X|<=k`, Hamiltonian supports `|Y|<=l`, bounded operator norms `||o_X||<=o0`, `||h_Y||<=h0`, and fixed site incidences `d_O,d_H`, the first energy-weighted moment is

`m1 = (1/2) <[O†,[H,O]]>`.

Only triples with `X∩Y != empty` and `Z∩(X∪Y) != empty` contribute. The preregistered loose support count and norm inequality give

`N_trip <= N k(k+l) d_O^2 d_H`

and therefore

`|m1| <= 2 N k(k+l) d_O^2 d_H o0^2 h0`.

At fixed locality, norms and coordination this is extensive: the bound per site is N-independent.

## Raw-inspected hosted result
Decoded job log shows:
- dedicated regressions: `4 passed`;
- exhaustive support-enumeration benchmark: 72 cases;
- random explicit finite-dimensional Hermitian/Pauli matrix benchmark: 24 cases;
- max exact triplet-count / frozen count bound = `0.75`;
- max local nested-commutator amplitude / `4 o0^2 h0` = `0.7822716656423147`;
- max measured `|m1|` / frozen global bound = `0.0020054905582118808`;
- scaling benchmark bound/site = exactly `240.0` for N = 6,8,10,12,16,20,32,64;
- all-to-all pair supports have `d_O=N-1` and were explicitly classified `OUTSIDE_SCOPE_GROWING_COORDINATION`;
- benchmark status: `PASS_KLOCAL_EXTENSIVITY`.

## Scientific interpretation
This closes the *free superextensive collective-scaling loophole* for bounded finite-range k-local Standard-Model current classes, including genuine finite-range two-/higher-body terms under the frozen assumptions. It does **not** establish a universal small absolute two-body coefficient. It also does not cover genuinely long-range/growing-coordination operators, active/driven systems, or BSM currents.

The correct next G3 task is therefore no longer another collective-coherence toy model. It is an absolute-strength envelope: freeze chiral-EFT/power-counting and empirical two-body-current authorities, bound physically allowed coefficients/operator norms, and translate that coefficient envelope into the same solar-neutrino deposited-power score without multiplying unvalidated gains.
