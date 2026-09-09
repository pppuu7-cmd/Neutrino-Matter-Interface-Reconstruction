# 0100 — known-model benchmark: standard three-flavor oscillations + MSW

Date frozen: 2026-09-09
Benchmark ID: NMIR-BENCHMARK-0100
State: ACTIVE_PREFLIGHT_ONLY
Parent protocol: `research/benchmarks/KNOWN_MODEL_BENCHMARK_MATRIX.md`

## Purpose

Use standard unitary three-flavor massive-neutrino oscillation phenomenology with the ordinary charged-current MSW matter potential as the control / known-limit calibration model. This benchmark is not allowed to absorb NSI, sterile states, collective neutrino-neutrino terms, magnetic moments, new mediators, modified gravity, or new detector/nuclear-response parameters.

A numerical workflow success is not itself a physics PASS. A terminal physics result is forbidden until every external source/environment input used by the terminal calculation is pinned by immutable identity/hash.

## Frozen theory contract

Flavor amplitudes obey

\[
i\,\frac{d}{dx}\nu_f = H_f\nu_f,
\]

with, for neutrinos,

\[
H_\nu(E,x)=\frac{1}{2E}U\,\mathrm{diag}(0,\Delta m^2_{21},\Delta m^2_{31})U^\dagger
+\mathrm{diag}(V_{CC}(x),0,0),
\]

\[
V_{CC}(x)=\sqrt{2}\,G_F N_e(x),\qquad N_e(x)=N_A\rho(x)Y_e(x).
\]

For antineutrinos the frozen convention is

\[
U\rightarrow U^*,\qquad V_{CC}\rightarrow -V_{CC}.
\]

The PMNS matrix uses the standard PDG three-angle + one Dirac-phase convention. Majorana phases are irrelevant to oscillation probabilities and are absent from this benchmark.

For numerical propagation in piecewise-constant matter, the equivalent effective mass-squared term is

\[
A_{CC}=2EV_{CC}=1.52588\times 10^{-7}\,\rho[\mathrm{g\,cm^{-3}}]Y_e E[\mathrm{MeV}]\;\mathrm{eV^2}.
\]

Each radial segment is evolved by exact diagonalization of the Hermitian effective mass-squared matrix; no non-unitary damping is permitted in 0100.

## Parameter authority frozen before execution

Primary global-fit authority: NuFIT 6.1 (2025), fit based on data available in November 2025, retrieved 2026-09-09.

Primary branch: **Normal Ordering, IC24 with Super-Kamiokande atmospheric data**.

- `sin^2(theta12) = 0.3088`
- `sin^2(theta23) = 0.470`
- `sin^2(theta13) = 0.02248`
- `delta_CP = 212 deg`
- `Delta m^2_21 = 7.537e-5 eV^2`
- `Delta m^2_31 = +2.511e-3 eV^2`

Mandatory alternate branch: **Inverted Ordering, IC24 with Super-Kamiokande atmospheric data**.

- `sin^2(theta12) = 0.3088`
- `sin^2(theta23) = 0.550`
- `sin^2(theta13) = 0.02262`
- `delta_CP = 274 deg`
- `Delta m^2_21 = 7.537e-5 eV^2`
- NuFIT convention: `Delta m^2_32 = -2.483e-3 eV^2`
- implementation conversion: `Delta m^2_31 = Delta m^2_32 + Delta m^2_21`

Authority URLs:
- https://www.nu-fit.org/?q=node/309
- https://www.nu-fit.org/sites/default/files/v61.tbl-parameters.pdf
- PDG neutrino-mixing review: https://pdg.lbl.gov/2024/reviews/rpp2024-rev-neutrino-mixing.pdf

The primary terminal result must report NO and IO separately. The ordering may not be chosen after seeing which one produces a preferred NMIR outcome.

### Nuisance/robustness rule

NuFIT one-dimensional 3-sigma endpoints are not to be interpreted as an uncorrelated six-dimensional confidence hypercube. Before any uncertainty scan is called statistical, the corresponding NuFIT multi-dimensional Delta-chi-squared assets must be pinned and parsed. Until then, endpoint scans are allowed only as explicitly labelled one-at-a-time stress tests.

## Source / propagation authority gate

A terminal stellar-MSW calculation requires a traceable radial pair `rho(r), Ye(r)` from the same stellar model and evolutionary snapshot. `Ye` may not be guessed from density, set to 0.5 everywhere, or reconstructed from unrelated observables for a terminal claim.

Candidate public authorities identified before execution include MESA pre-supernova model/profile datasets associated with Patton–Lunardini–Farmer and the Farmer et al. pre-supernova profile archive. Their existence does **not** count as pinning. The exact dataset record/version, selected progenitor mass, evolutionary snapshot, member filename, and file hash must be recorded before the terminal run.

Until that is done the maximum permissible status for the physical source-propagation axis is:

`BLOCKED_0100_SOURCE_PROFILE_UNPINNED`

Synthetic profiles may be used only for mathematical preflight tests and must never be reported as Betelgeuse predictions.

## Energy / source-spectrum gate

The terminal energy grid and source spectra must come from an already validated NMIR source/detector input or from a separately pinned external pre-supernova neutrino source asset. No spectrum may be reconstructed from a published plot.

Until the exact source-spectrum asset is pinned, detector-level terminal event predictions are forbidden.

## Mandatory mathematical preflight checks

All must pass before a terminal authority run can be enabled:

1. PMNS unitarity: `max|U^dagger U - I| <= 1e-12` for NO and IO best fits.
2. Probability normalization: for each pure initial flavor, `|sum_beta P(alpha->beta)-1| <= 1e-12` in constant-density test points.
3. Vacuum reduction: the matrix propagator at `rho=0` agrees with the direct vacuum eigenstate-amplitude formula to `<= 1e-12` in probability.
4. Zero-density matter reduction: setting `rho=0` removes the matter term exactly to numerical precision.
5. Antineutrino convention: the vacuum mixing matrix is complex conjugated and the matter-potential sign is reversed.
6. High-density qualitative limit: at a declared synthetic high-density point, the electron-flavor matter term dominates the vacuum mass-squared scale by at least `1e4`.
7. Radial step convergence: on the frozen synthetic exponential profile, the probability vector at 3200 and 6400 equal radial segments differs by `< 1e-4` in every flavor.
8. Finite-output check: all amplitudes/probabilities are finite and probabilities remain in `[0,1]` up to `1e-12` tolerance.

The synthetic convergence profile is frozen as

\[
r\in[0,10000]\;\mathrm{km},\quad \rho(r)=10^4\exp(-r/1500\,\mathrm{km})+1\;\mathrm{g\,cm^{-3}},\quad Y_e=0.5,
\]

at `E = 5 MeV`, initial `nu_e`, NO best fit. It is a numerical test fixture only.

## G9 geometry dependency

0100 changes flavor amplitudes/weights; it does not introduce a new gravitational interaction or a new ray equation. Therefore the already-certified G9 lens/receiver geometry is inherited and may not be refit inside 0100.

As a conservative kinematic guard, the latest direct KATRIN limit available at freeze time is `m_beta < 0.45 eV/c^2` (90% CL, 2025). At the pre-supernova energies relevant to this project, the ultra-relativistic correction scale `~m^2/(2E^2)` is tiny; for the explicit guard point `m=0.46 eV`, `E=0.5 MeV`, it is `< 5e-13`. This benchmark therefore treats standard-mass corrections to the previously certified G9 geometry as below the geometry-resolution budget. This is a scale-separation statement, not a new G9 PASS.

Authority URL: https://www.katrin.kit.edu/1271.php

## Interaction / transport boundary

0100 is coherent flavor evolution only. It may reweight already validated flavor-dependent detector channels. It may **not** create or modify:

- neutrino-nucleus cross sections;
- CEvNS nuclear form factors;
- absorption/opacity;
- detector efficiency/threshold functions;
- deposited-energy mapping;
- source luminosity normalization;
- G9 geometric amplification.

Those quantities must be inherited from already validated NMIR artifacts or tested in their own benchmark.

## Distinguishing-prediction contract

The control prediction is restricted to energy- and ordering-dependent flavor redistribution generated by the standard PMNS+MSW Hamiltonian. A measured effect that requires a non-unitary flavor map, an additional matter potential, spin/flavor conversion, sterile leakage, extra interaction/opacity, or a change of the G9 ray geometry lies outside 0100 by construction.

Conversely, a flavor-ratio or detector-rate difference that can be closed entirely by the frozen standard Hamiltonian is **not** evidence for a new NMIR interaction.

## Terminal result axes

A future terminal record must report separately:

- `MATHEMATICAL_CONSISTENCY`
- `KNOWN_LIMIT_RECOVERY`
- `PARAMETER_AUTHORITY`
- `SOURCE_PROPAGATION_AUTHORITY`
- `INTERACTION_TRANSPORT_AUTHORITY`
- `G9_GEOMETRY_DEPENDENCY`
- `DISTINGUISHING_PREDICTION`
- `REPRODUCIBILITY_PROVENANCE`

Allowed overall result classes:

- `PASS_0100_STANDARD_3FLAVOR_MSW_WITHIN_FROZEN_SCOPE`
- `FAIL_0100_<SCOPED_GATE>`
- `BLOCKED_0100_<MISSING_AUTHORITY_OR_INPUT>`

`PASS` must never be phrased as proof that the Standard Model is true. `FAIL` must never be generalized beyond the frozen tested claim. `BLOCKED` must never be relabeled as a physics failure.

## Prospective-lock rule

Once a terminal numerical run is started, formulas, parameter branches, source/profile identities, energy grid, convergence tolerance, result classes, and interpretation guards in this file are immutable for that run. Any later correction requires a new amendment file and new benchmark run ID.