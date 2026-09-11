# NMIR 0103Z — six-state rephasing covariance result

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Status: `PASS_0103Z_SIX_STATE_REPHASING_COVARIANCE_NONTERMINAL`
Scope: `NONTERMINAL_SYNTHETIC_REPHASING_COVARIANCE_ONLY`

## Prospective record

Preregistration was committed before implementation/results:

- preregistration: `research/prereg/0103yz_independent_solver_and_rephasing_prereg.md`
- preregistration commit: `d247e18dabf02fe26fce64f50700c8ce453fd4f6`
- implementation commit: `eea0c2730aeb64048450a80ff7275f386a195f83`

The audit applies deterministic diagonal unitary phase redefinitions to all six coordinates, transforms the Hamiltonian covariantly as `H'=D H D^dagger`, transforms the initial state as `psi0'=D psi0`, propagates both representations, and checks recovery of the original final state and invariance of physical probabilities.

## Authoritative GitHub execution

- workflow: `.github/workflows/0103z-rephasing-covariance.yml`
- trigger commit: `80f373f3e590030430a7c0c3366492a215f06abc`
- run: `34659349484`
- job: `103458418531`
- focused pytest: `1 passed in 1.70s`
- artifact: `nmir-0103z-rephasing-covariance`
- artifact ID: `10287170655`
- artifact ZIP SHA256: `f4e35e174b9b3bd3a4cbcb6298049d54bd186c95eb4b3747ec6675fe97b3e3bb`

## Frozen configuration

- couplings: `g=[0,0.1,1.0]`
- resolution: `N=1024`
- three deterministic nontrivial phase vectors spanning both neutrino and antineutrino blocks, exactly as preregistered.

## Result

All seven preregistered gates passed.

Key maxima:

- diagonal-unitary residual: `1.1292751170957362e-16`
- transformed-Hamiltonian Hermiticity residual: `2.5476231888929306e-16`
- recovered-state residual: `1.7678101127436524e-14`
- probability residual: `3.852473895449293e-14`
- norm residual: `7.527312106958561e-14`
- zero-coupling antineutrino leakage: `0.0`

The probability and state residuals are far below the preregistered `2e-12` ceilings.

## Interpretation

The six-state implementation is covariant under the frozen arbitrary diagonal rephasings: coordinate-phase conventions do not create observable probability changes in this audit. Together with the earlier mass/flavor basis-invariance audit, this removes another internal representation-risk class.

This is a numerical/representation closure only. It supplies no missing Betelgeuse magnetic or matter authority and cannot authorize a terminal Betelgeuse spin-flavor probability.

Terminal ceiling remains the need for one physically admissible coherent magneto-matter state.