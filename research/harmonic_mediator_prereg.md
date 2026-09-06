# NMIR preregistration — passive harmonic-mediator all-to-all gate

Date: 2026-09-06
Status: **PROSPECTIVE / FROZEN BEFORE IMPLEMENTATION**

## Funnel question
Iteration 0031 class-bounds passive pair Hamiltonians at fixed extensive absolute interaction budget. A remaining loophole is that all-to-all interactions may arise only after integrating out a common dynamical field/cavity mode, so the mediator energy could be hidden if one works only with the effective pair Hamiltonian.

This gate asks whether a single passive stable harmonic mediator can provide a free superextensive collective interaction when its own field energy is included.

## Literature anchor
The Dicke model couples a single cavity mode to N two-level systems. Standard thermodynamic-limit formulations scale the collective light-matter coupling as `1/sqrt(N)`. Reviews explicitly identify this scaling as the assumption that yields a meaningful large-N thermodynamic description.

## Frozen mediator model
Take a static quadrature control of a stable harmonic mediator,

`H_med(x,O) = (kappa/2) x^2 - g_N x O`,

with `kappa>0` and an additive bounded material operator satisfying `|O|<=o*N`.

Completing the square gives

`H_med = (kappa/2) (x - g_N O/kappa)^2 - g_N^2 O^2/(2 kappa)`.

At the energy-minimizing displacement,

`x_* = g_N O/kappa`,

field energy magnitude

`E_field = kappa x_*^2/2 = g_N^2 O^2/(2 kappa)`,

and induced collective interaction

`E_induced = -g_N^2 O^2/(2 kappa)`.

Thus the characteristic mediator and induced-interaction energy scales have identical `g_N^2 N^2` scaling.

Freeze

`g_N = g0 / N^gamma`.

Then the induced/field energy per constituent scales as

`E/N ~ N^(1-2 gamma)`.

Interpretation:
- `gamma=0`: unscaled common-mode coupling -> energy per particle ~N;
- `0<gamma<1/2`: still divergent;
- `gamma=1/2`: extensive Dicke/Kac scaling -> O(1) energy per particle;
- `gamma>1/2`: subextensive collective energy per particle.

The induced pair coefficient is proportional to

`J_eff ~ g_N^2/kappa ~ N^(-2 gamma)`.

At `gamma=1/2`, `J_eff~1/N`, matching the Kac-normalized all-to-all class already bounded in iteration 0031.

## Prospective computational gates
For `N1=1e3`, `N2=1e6`, benchmark `gamma=0,0.25,0.5,0.75` and require:
1. completion-of-square energy identity to relative error <=1e-15;
2. field-energy and induced-interaction magnitudes agree to relative error <=1e-15 at the minimizing displacement;
3. their per-particle finite-N gains agree to relative error <=1e-12;
4. measured per-particle gain matches `(N2/N1)^(1-2 gamma)` to relative error <=1e-12 for the analytic scaling model;
5. `gamma=0.5` gain is exactly 1 within 1e-12;
6. effective pair-coupling ratio at `gamma=0.5` is `J_eff(N2)/J_eff(N1)=N1/N2` within 1e-12.

## Classification
If all gates pass: **PASS_HARMONIC_MEDIATOR_BUDGET / STRONG-NEGATIVE scoped** against free superextensive collective energy from a passive stable single harmonic mediator at fixed extensive total energy.

Surviving loopholes are narrower: multiple/gapless/nonlinear mediators, active driven-dissipative media (external power explicit), higher-body couplings, or BSM neutrino interaction strength. This gate does not claim a theorem for all quantum fields.
