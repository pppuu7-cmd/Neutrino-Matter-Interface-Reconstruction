# NMIR local spin/axial response sum-rule gate — prospective contract

Date: 2026-09-06
Status: PREREGISTERED before hosted execution.
Funnel scope: F5/F6, passive spin/axial/magnon response.

## Question
Can a passive magnet, polarized spin medium, magnonic material or other **locally interacting** spin system create superextensive energy-weighted neutrino axial response merely by softening or coherently organizing collective spin modes?

## Exact general identity
For a response operator `O` and Hamiltonian `H`, the positive-frequency first moment is represented by the standard double-commutator sum rule

`m1 = 1/2 < [O^dagger, [H,O]] >`

(up to the explicitly chosen structure-factor normalization convention).

Let

`H = sum_X h_X`,

where each bounded local term `h_X` acts only on a finite support `X`, and

`O = sum_i g_i S_i^a`.

For one spin component with local operator norm `||S_i^a|| <= s`, only `O_X = sum_{i in X} g_i S_i^a` contributes to the commutator with `h_X`. Using `||[A,B]|| <= 2||A||||B||`,

`|m1| <= 2 sum_X ||h_X|| ||O_X||^2`

and therefore, with `|g_i|<=gmax`,

`|m1| <= 2 s^2 gmax^2 sum_X ||h_X|| |X|^2`.

For pairwise spin-1/2 terms (`s=1/2`, `|X|=2`, `gmax=1`):

`|m1| <= 2 sum_bonds ||h_ij||`.

For an isotropic Heisenberg bond `h_ij=J_ij S_i·S_j`, `||h_ij||=3|J_ij|/4`, hence

`|m1| <= (3/2) sum_bonds |J_ij|`.

If each site has bounded coordination `z` and `|J_ij|<=Jmax`,

`|m1| <= (3/4) N z Jmax`,

which is extensive in `N`.

This is intentionally a norm envelope, not a precise material prediction. It is compatible with the Hohenberg-Brinkman/first-moment literature in which the spin first moment is set by exchange energies and static correlations.

## Frozen tests
Before looking at hosted output, require:
1. generic local-term bound computes exactly the pairwise spin-1/2 specialization;
2. Heisenberg bond norm is `3|J|/4` and the resulting envelope is `(3/2) sum |J|`;
3. for fixed `z,Jmax`, scaling `N:1 -> 1e6` changes the bound by exactly `1e6` within relative `1e-12`, not `1e12`;
4. a soft-mode toy at fixed first-moment budget, with mode energy reduced by `1e6`, increases unweighted spectral strength by at least `1e6` but changes the energy-weighted budget by <=`1e-12` relative;
5. an explicit all-to-all pair-count diagnostic must show `O(N^2)` bond-count scaling when couplings are **not** Kac/extensivity scaled. This is to expose, not hide, the nonlocal loophole.

## Classification
`PASS_LOCAL_SPIN_SUM`: all frozen identities/tests pass.

Scientific meaning if PASS: passive bounded-coordination local spin/magnon engineering cannot obtain a free superextensive energy-weighted axial-response gain solely by mode softening/coherence. A large gain must instead come from unusually large microscopic axial kernel, genuinely long-range/nonlocal interactions, active pumping, charged-current physics, gravity or BSM.

## Explicit exclusions / surviving loopholes
- long-range/all-to-all interactions whose interaction-energy norm itself grows superextensively;
- active/cavity/pumped systems unless external energy is separately accounted;
- itinerant relativistic electrons outside a local-spin representation;
- charged-current nuclear transitions;
- BSM operators;
- gravitational focusing.

No W/kg ceiling is claimed from this gate alone; it is a scaling/no-free-lunch gate for the passive local spin-response branch.

## Literature anchors
- P. C. Hohenberg and W. F. Brinkman, Phys. Rev. B 10, 128 (1974), exact frequency sum rules for Heisenberg/XY chains.
- G. Müller, Phys. Rev. B 26, 1311 (1982), dynamical spin-chain sum rules.
- S. Stringari, Phys. Rev. B 49, 6710 (1994), spin excitations and sum-rule bounds in the Heisenberg antiferromagnet.
