# NMIR-0103E — six-state end-to-end surrogate spin-flavor audit

Status: PREREGISTERED BEFORE RESULT

## Scope
Close only the numerical/interface chain from a path-dependent matter potential and transverse magnetic coupling through a six-state Majorana spin-flavor propagator. This is a dimensionless synthetic positive-control calculation, not a Betelgeuse prediction.

## Frozen conventions
- Synthetic PMNS-shaped unitary fixture: theta12=0.57, theta13=0.15, theta23=0.79, delta=1.17 rad. These are test fixtures, not NuFIT authority.
- Six-state transform `T6 = block_diag(U,U*)`.
- Single real antisymmetric mass-basis transition generator: `K12=+1`, `K21=-1`.
- Dimensionless path `s in [0,1]`.
- Matter fixture `v(s)=0.6 exp(-2s)+0.05`.
- Magnetic-path fixture `b(s)=sin(pi s)^2`.
- Positive-control coupling `g=0.35`; zero-control `g=0`.
- Vacuum fixture `diag(0,0.4,1.1)`.
- Piecewise-constant midpoint evolution using Hermitian eigendecomposition; primary N=400, convergence comparison N=200.
- Initial state is pure electron-flavor neutrino.

## Frozen gates
1. PMNS and T6 unitarity residual <=1e-12;
2. Hamiltonian Hermiticity residual <=1e-12;
3. g=0 antineutrino leakage <=1e-13;
4. final norm residual <=1e-12;
5. direct flavor-basis and transformed mass-basis final states agree <=1e-11;
6. corresponding probabilities agree <=1e-11;
7. N=200 vs N=400 probability convergence <=1e-5;
8. g=0.35 produces antineutrino probability >1e-6 as a positive control;
9. exact repeated N=400 calculation agrees in probabilities <=1e-14;
10. scope guard remains `NONPHYSICAL_INTERFACE_ONLY`.

No conversion from raw Pencil code units to gauss, no Borexino upper-bound insertion, and no terminal Betelgeuse interpretation are allowed in this audit.
