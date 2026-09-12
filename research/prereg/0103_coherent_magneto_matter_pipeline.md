# NMIR 0103M — coherent magneto-matter pipeline preregistration

Status: PREREGISTERED_NONTERMINAL_ENGINEERING_AUDIT

Purpose: test whether the six-state 0103 propagation machinery closes end-to-end when magnetic field and matter variables are supplied on one co-registered 3-D state. This is deliberately synthetic and MUST NOT be interpreted as Betelgeuse authority.

## Frozen construction

A deterministic Cartesian cube supplies Bx, By, Bz, rho, and Ye on the same coordinates. One oblique ray is sampled by trilinear interpolation. The transverse field is computed only from the sampled vector field,

B_perp = sqrt(|B|^2 - (B dot n_hat)^2).

The matter profile and B_perp then enter the same piecewise-constant six-state Majorana propagation chain. The magnetic fixture is the antisymmetric mass-basis 1-2 transition matrix already used by the 0103 basis-invariance audit. Mixing parameters remain synthetic test fixtures.

## Prospective gates

1. all five 3-D state arrays have exactly the same shape and coordinate grid;
2. rho is strictly positive and 0 < Ye < 1 along the ray;
3. the ray remains inside the interpolation domain;
4. B_perp projection identity closes to <= 1e-12;
5. every six-state step is Hermitian to <= 1e-12;
6. final-state norm error <= 1e-10;
7. g=0 produces antineutrino leakage <= 1e-12 for a neutrino-only initial state;
8. final probabilities at 256 and 512 propagation cells differ by <= 2e-4 in max norm.

A PASS closes only the engineering question: a genuinely co-registered magneto-matter snapshot can be consumed without a missing numerical interface. It does not close the Betelgeuse vector-field or matter-state authority gate.
