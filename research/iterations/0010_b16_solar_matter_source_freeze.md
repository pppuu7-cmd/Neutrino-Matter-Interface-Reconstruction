# NMIR Iteration 0010 — B16 solar matter / production-distribution source freeze

Date: 2026-09-06
Status: SOURCE IDENTITY FROZEN; HEAD CI PENDING

## Motivation

A numerical solar survival probability must be averaged over where each neutrino component is produced and over the local electron density. NMIR therefore forbids replacing the solar interior by an ad-hoc single effective density/radius.

## Source discovery

The pinned `michelelucente/PEANUTS` snapshot used for spectral provenance contains B16 solar-model distribution tables whose own headers cite Vinyoles et al. (2017), arXiv:1611.09867. PEANUTS `peanuts/solar.py` explicitly reads these tables and uses radius, electron density and component production fractions to production-average the adiabatic solar mass-eigenstate flux.

Frozen upstream snapshot: `59e3a2ae102d58f42cc1146eaca2cae68be879ce`.

Frozen files:

- B16 GS98: `Data/nudistr_b16_gs98.dat`, Git blob `f73c47cf6f2d77086634a5c180b50039e10805e7`;
- B16 AGSS09met: `Data/nudistr_b16_agss09.dat`, Git blob `d9bd29f3374c63e8ea898733a55fb7aa566a2c96`.

## Column contract

Both tables define:

- column 0: radius `r/R_sun`;
- column 2: `log10` electron density in `cm^-3/N_A`, i.e. density recovered in `mol/cm^3` by `10**column`;
- columns 4–11: production distributions for pp, pep, hep, Be7, B8, N13, O15, F17 respectively.

`data/solar_matter_manifest.csv` freezes these exact identities and column assignments. `src/nmir/solar_matter.py` provides a fail-closed loader and exact Git-blob verifier. `tests/test_solar_matter.py` prospectively guards model identities, column mapping, component completeness, immutable URLs and corrupt-byte rejection.

## Scientific scope

This closes the *source-selection ambiguity* for the first production-averaged MSW benchmark, subject to head CI. It does not yet close numerical `P_ee(E)` because the table bytes still need a hosted exact materialization/parse gate and the adiabatic three-flavour matter-angle implementation needs an independent numerical benchmark.

## Live CI

Latest code head at creation of this note: `be19c861bd6bbd47638e0353ec82123eb5558c32`.

CI run `34012558642`, job `101430756547` was queued when this note was written. Therefore no PASS is claimed yet for the new loader/tests.

## Exact next gate

1. Consume head CI and diagnose any failure without weakening the frozen table contract.
2. Materialize both B16 matter tables with exact blob verification.
3. Parse radius/density/production columns; verify positive finite density and production integrals for all eight components.
4. Implement `P_ee(E,r)` and production averaging under the already frozen oscillation convention.
5. Cross-check limiting low/high-energy survival behavior before Ga/Cl integration.

`NMIR_READINESS: 25%`

No readiness credit is assigned until the new provenance/loader gate is validated by head CI and materialization.