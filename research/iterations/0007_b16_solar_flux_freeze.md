# NMIR Iteration 0007 — B16 solar-flux freeze

Date: 2026-09-06

## Objective

Close the first prerequisite of G3: replace informal solar-flux numbers with a machine-readable, provenance-frozen Standard Solar Model input before any Ga-71/Cl-37 precision rate calculation or multi-isotope optimization.

## Pre-iteration authority

- recovery source: `research/RECOVERY.md` at blob `9a74c0bdfb23d6aa85ebf7cdd2020cf603957bcc`;
- main commit before this iteration: `9c8256b605c87ec75ee5dd120f22ba05dc408750`;
- latest completed CI on that commit: run `34004949382`, job `101410320717`, conclusion SUCCESS. Green CI is treated as infrastructure validation only; the iteration-0006 tritium scientific benchmark remains separately validated by its numerical comparison.

No queued/in-progress heavy scientific calculation was found that this work would duplicate.

## Primary source

N. Vinyoles et al., **A New Generation of Standard Solar Models**, Astrophys. J. 835, 202 (2017), DOI `10.3847/1538-4357/835/2/202`, arXiv:`1611.09867`.

The paper defines two B16 solar-model ensembles based on GS98 high metallicity and AGSS09met low metallicity and reports the corresponding neutrino-flux predictions. The frozen values were independently cross-checked against later literature reproducing the B16 table before repository insertion.

## Frozen data

Added `data/solar_flux_b16.csv` with the eight standard components `pp, pep, hep, Be7, B8, N13, O15, F17`, storing both B16-GS98 and B16-AGSS09met central number fluxes and relative model uncertainties in `cm^-2 s^-1`.

Examples:

- GS98 pp: `5.98e10 cm^-2 s^-1`, relative uncertainty `0.006`;
- GS98 Be7: `4.93e9 cm^-2 s^-1`, relative uncertainty `0.06`;
- GS98 B8: `5.46e6 cm^-2 s^-1`, relative uncertainty `0.12`;
- AGSS09met B8: `4.50e6 cm^-2 s^-1`, relative uncertainty `0.12`.

The component CNO sums are derived rather than stored as a ninth component to prevent double counting:

- GS98: `N13+O15+F17 = 4.8829e8 cm^-2 s^-1`;
- AGSS09met: `3.5126e8 cm^-2 s^-1`.

## Code and regression gates

Added:

- `src/nmir/solar_flux.py` — strict loader for the two B16 model choices and derived CNO/total bookkeeping diagnostics;
- `tests/test_solar_flux.py` — regression checks for pp, Be7, B8, uncertainties, both metallicity choices, CNO sums, and invalid model rejection;
- `data/solar_flux_b16_provenance.md` — provenance and scope guards.

## Important negative/scope result

This iteration freezes **integrated source fluxes, not full energy spectra**. It is scientifically invalid to claim a precision Ga-71 or Cl-37 capture prediction from these rows alone. The next gate must prospectively freeze:

1. continuum spectral shapes for pp/hep/B8/N13/O15/F17;
2. Be7 line energies and branching convention;
3. pep line energy convention;
4. electron-neutrino survival probability / oscillation convention;
5. target-specific capture cross-section/transition inputs.

This restriction prevents an apparent rate reproduction from silently mixing incompatible legacy spectra or oscillation assumptions.

## Scientific classification

- **G3 prerequisite: PARTIAL PASS.** A primary-source B16 flux normalization is now machine-readable and regression-tested.
- **Ga/Cl precision rate reproduction: remains OPEN.** Spectral and oscillation inputs are not yet frozen.
- No claim is made that B16-GS98 is uniquely preferred; both high- and low-metallicity vectors are retained as an explicit systematic branch.

## Readiness

`NMIR_READINESS: 23%`

Increase from 21% to 23% is credited only for freezing a primary-source solar-model normalization with model-systematic alternatives, code loader, provenance guard and regression tests. No readiness credit is assigned for the not-yet-frozen spectral shapes.

## Exact next gate

Freeze primary-source spectral shapes/line definitions plus a current oscillation survival-probability convention, then reproduce at least one published Ga-71 component or total capture rate before expanding to Cl-37 and W/kg ranking.
