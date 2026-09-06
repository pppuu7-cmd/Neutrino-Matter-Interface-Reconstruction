# NMIR Iteration 0008 — spectral-manifest and oscillation-convention freeze

Date: 2026-09-06

## Objective

Advance the G3 prerequisite chain without yet claiming a Ga-71/Cl-37 rate: freeze immutable identities for the solar-neutrino spectral-shape inputs and freeze the first oscillation convention prospectively, before any capture-rate fit/integration.

## Pre-iteration authority

- `research/RECOVERY.md` blob before this iteration: `5851650729bb7b2a6d54f13aa11f3de0489f29b7`;
- iteration 0007 head: `a4372f98965b3705f3b56363539805672772e3e6`;
- iteration-0007 CI run `34007336474` completed SUCCESS. This validates repository tests/infrastructure but is not, by itself, a Ga/Cl scientific PASS.

No queued/in-progress duplicate heavy scientific task was found.

## Spectral provenance freeze

The modern open solar-neutrino propagation package PEANUTS (Gonzalo & Lucente, Eur. Phys. J. C 84, 119 (2024), arXiv:2303.15527) documents its default spectral sources as:

- pp and hep: J.N. Bahcall, Phys. Rev. C 56, 3391 (1997);
- B8: C.E. Ortiz et al., Phys. Rev. Lett. 85, 2909 (2000);
- N13/O15/F17: J.N. Bahcall and R.K. Ulrich, Rev. Mod. Phys. 60, 297 (1988);
- Be7 line profiles: J.N. Bahcall, Phys. Rev. D 49, 3923 (1994).

NMIR freezes these table identities by both upstream repository commit
`59e3a2ae102d58f42cc1146eaca2cae68be879ce` and exact blob SHA in
`data/solar_spectrum_manifest.csv`. This prevents a later upstream update or a silent B8 Ortiz↔Winter substitution from changing the baseline calculation.

Pinned continuum components: `pp, hep, B8, N13, O15, F17`. Both thermally broadened Be7 profiles are pinned as separate profile entries. Bookkeeping line conventions are also explicit: pep 1.442 MeV; Be7 0.862 MeV weight 0.897 and 0.384 MeV weight 0.103. For precision Be7 integration the broadened tables, not delta-function bookkeeping lines, remain authoritative.

## Oscillation convention freeze

Added `data/solar_oscillation_convention.csv` with the first prospective Ga/Cl baseline:

- `sin^2(theta12)=0.307`;
- `sin^2(theta13)=0.0220`;
- `Delta m^2_21=7.53e-5 eV^2`;
- normal ordering;
- standard three-flavour adiabatic MSW propagation in the Sun;
- Earth regeneration OFF for the first benchmark and reserved as a later robustness branch.

The numerical central values use the PDG-2025 solar/reactor convention. The propagation formalism is chosen to be compatible with PEANUTS, but this iteration does **not** yet freeze a solar production-radius/electron-density integration table. Therefore it does not yet produce a fully numerical `P_ee(E)` curve.

## Code and tests

Added:

- `src/nmir/solar_spectra.py`: strict spectral-manifest loader, git-identity checks and Be7 bookkeeping normalization;
- `tests/test_solar_spectra.py`: required component set, exact B8 baseline identity, line-energy/weight checks;
- `src/nmir/solar_oscillation.py`: strict frozen-parameter loader;
- `tests/test_solar_oscillation.py`: numerical and scope regression gates.

## Scientific classification

- **Spectral-source identity gate: PARTIAL PASS.** Primary-source-derived tables are now immutably identified and provenance frozen.
- **Oscillation-parameter convention: PASS for baseline definition.** Parameters and scope are frozen before rate integration.
- **Numerical survival-probability curve: OPEN.** Component production distributions/electron-density averaging are still missing.
- **Ga-71/Cl-37 reproduction: OPEN.** It remains forbidden to claim precision capture rates until the survival curve and target-specific capture kernels are frozen and reproduced.

## Negative/scope result

A commit-pinned spectrum manifest is sufficient to prevent silent spectral drift, but it does not by itself make the repository self-contained for offline integration. The exact table bytes must either be vendored with license/provenance or fetched and SHA-verified by a dedicated materialization step. No readiness credit is assigned for a Ga/Cl rate until this is done and `P_ee(E)` is numerical.

## Readiness

`NMIR_READINESS: 24%`

Increase from 23% to 24% is credited only for prospective spectral identity + oscillation convention freeze and regression guards. The still-open numerical survival and Ga/Cl kernels prevent larger credit.

## Exact next gate

Materialize/verify the pinned spectrum bytes and component production/electron-density inputs; implement the day-averaged three-flavour MSW `P_ee(E)` under the frozen parameters; then reproduce a published Ga-71 component/total rate before Cl-37 and W/kg ranking.
