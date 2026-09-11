# NMIR 0103M preregistration — coherent synthetic magneto-matter pipeline

Status: PREREGISTERED_BEFORE_RESULT
Scope: NONTERMINAL_SYNTHETIC_ENGINEERING_ONLY

## Question
Can one co-registered 3-D state containing vector magnetic field and matter variables be sampled on one ray and propagated through the six-state Majorana interface without introducing a new numerical or representation failure?

## Frozen fixture
- One deterministic Cartesian grid on [-1,1]^3 with one state identifier shared by Bx, By, Bz, rho and Ye.
- Each scalar component is an analytic trilinear polynomial so ordinary trilinear interpolation has an exact analytic reference.
- One fixed interior ray; no extrapolation is allowed.
- B_perp is derived only from the interpolated vector field and the normalized ray direction.
- Matter potential is a dimensionless synthetic function proportional to rho*Ye. It is not astrophysical authority.
- Vacuum/mixing parameters and the Majorana 1-2 transition coupling are synthetic fixtures only.
- Six-state propagation uses midpoint piecewise-unitary evolution from Hermitian eigendecomposition.

## Locked gates
1. All sampled channels carry one common state/grid/ray identity and every sample lies inside the grid.
2. Maximum trilinear interpolation residual <= 1e-12.
3. max |n dot B_perp| <= 1e-12 and transverse-magnitude consistency residual <= 1e-12.
4. Maximum Hamiltonian Hermiticity residual <= 1e-12.
5. Final norm residual <= 1e-10 and probability-sum residual <= 1e-10.
6. All final probabilities are finite and lie in [-1e-12,1+1e-12].
7. With magnetic coupling g=0, total antineutrino leakage <= 1e-12.
8. Repeating the identical calculation changes final probabilities by <= 1e-14.
9. A nonzero positive-control coupling produces finite nonzero antineutrino probability (>1e-8).
10. Scope guard remains NONTERMINAL_SYNTHETIC_ENGINEERING_ONLY.

PASS label: `PASS_0103M_COHERENT_SYNTHETIC_MAGNETO_MATTER_PIPELINE_NONTERMINAL`.

A PASS cannot close Betelgeuse authority. Terminal astrophysical use still requires a recoverable co-registered magneto-matter state with documented coordinates, units, snapshot identity and composition/electron-density semantics.
