# NMIR 0103X — six-state stress/convergence preregistration

Status: PREREGISTERED_NONTERMINAL_ENGINEERING_AUDIT

Purpose: stress the 0103 six-state Majorana propagator across magnetic-coupling regimes and grid refinements, separating numerical artifacts from genuine model behavior. This audit is synthetic and carries no Betelgeuse-specific authority.

## Frozen matrix

Coupling fixtures: g = [0, 0.002, 0.01, 0.05].
Propagation resolutions: N = [128, 256, 512, 1024].
The path uses smooth deterministic matter and transverse-field profiles. The same antisymmetric mass-basis 1-2 magnetic transition fixture is used at every resolution. Mixing parameters are synthetic test fixtures.

## Prospective gates

1. Hamiltonian Hermiticity residual <= 1e-12 for every sampled step;
2. state norm error <= 1e-10 for every (g,N) run;
3. g=0 antineutrino leakage <= 1e-12 at every resolution;
4. max probability difference between N=512 and N=1024 <= 1e-4 for every g;
5. cumulative propagator unitarity residual <= 1e-10 at N=1024 for every g;
6. no monotonicity in conversion probability versus g is assumed or required.

PASS means the numerical solver is stable over this preregistered stress matrix. It does not close magnetic-moment, PMNS, stellar-field, or Betelgeuse magneto-matter authority.
