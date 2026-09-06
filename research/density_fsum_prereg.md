# NMIR density-response f-sum gate — prospective contract

Date: 2026-09-06
Status: PREREGISTERED before benchmark execution.
Funnel scope: F5/F6, many-body density response and structured/layered matter.

## Question
Can a passive many-body medium, phonon system, crystal, staggered stack, or other engineered density response create a parametrically larger **energy-weighted neutrino coupling** merely by concentrating spectral weight into coherent or low-energy collective modes?

## Exact scoped identity
For a nonrelativistic Hamiltonian

H = sum_i p_i^2/(2 m_i) + V({r_i})

with a coordinate-local interaction V that commutes with the weighted density operator

rho_q = sum_i g_i exp(i q·r_i),

the positive-frequency dynamic structure factor obeys the energy-weighted f-sum rule (using q as momentum transfer and omega as transferred energy)

m1(q) = integral_0^infinity d omega omega S(q,omega)
      = q^2/2 * sum_i g_i^2/m_i.

Equivalently this follows from the double commutator 1/2 <[rho_-q,[H,rho_q]]>.

For any non-negative neutrino kernel K(q,omega) bounded at fixed q by K_max(q),

D(q) = integral d omega omega K(q,omega) S(q,omega)
     <= K_max(q) m1(q).

Thus rearranging the same constituents can redistribute spectral weight but cannot generate arbitrary energy-weighted density strength.

## Frozen numerical tests
The benchmark must construct at least four non-negative discrete response spectra with the same m1:
1. one broad/single-particle-like mode;
2. one very low-energy collective mode;
3. one multi-peak response;
4. one narrowed resonance family spanning at least 1e6 in linewidth/characteristic scale.

Acceptance criteria, fixed before execution:
- every constructed spectrum preserves m1 to relative error <= 1e-12;
- for K=1, the energy-weighted deposition proxy equals m1 to relative error <= 1e-12 for every spectrum;
- for arbitrary non-negative sampled kernels satisfying K<=K_max, D<=K_max*m1 to numerical tolerance 1e-12;
- lowering a single collective-mode energy by >=1e6 may increase the unweighted event-strength proxy by >=1e6, but must change the energy-weighted deposition proxy by <=1e-12 relative;
- scaling constituent count N from 1 to 1e6 must scale m1 linearly in N, not N^2.

## Classification rules
PASS_DENSITY_FSUM: all frozen identities/tests pass. Scientific meaning is scoped: passive density-coupled many-body engineering can strongly redistribute/detect low-energy events but cannot create superextensive integrated **energy-weighted density response** at fixed constituents under the stated Hamiltonian assumptions.

FAIL: any exact identity or frozen numerical test fails. No tolerance relaxation after result.

## Explicit exclusions
This gate does NOT by itself bound:
- spin/axial response with spin-dependent Hamiltonian terms;
- charged-current transmutation of the target;
- nonlocal/momentum-dependent interactions that modify the double commutator;
- actively pumped/non-equilibrium media where external energy must be tracked separately;
- BSM interactions;
- gravitational focusing.

These remain separate funnel branches.
