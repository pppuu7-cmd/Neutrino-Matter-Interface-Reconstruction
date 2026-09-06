# NMIR Iteration 0009 — fail-closed solar-spectrum materialization

Date: 2026-09-06
Authoritative head: `f207836f32496b7e78990a485f27568ee659ee15`

## Goal

Close the gap between a provenance-only spectral manifest and actual numerical spectral bytes suitable for later solar-neutrino capture integration. A spectrum is accepted only if its downloaded bytes reproduce the exact Git blob SHA frozen prospectively in `data/solar_spectrum_manifest.csv`.

## Prior-state validation

The previous iteration head `f4abcd98dbaf7eb0cd1b203d0b4adffb11124985` was rechecked through GitHub Actions run `34010081786`, job `101424245067`; raw pytest output was `42 passed`. This validates the spectral-manifest and SHA-verification code from iteration 0008, but was not by itself a numerical spectrum materialization PASS.

## Implementation

`src/nmir/solar_spectra.py` now provides:

- immutable raw URL construction from frozen repository + commit + path;
- fail-closed materialization with exact canonical Git-blob SHA verification before any file is accepted;
- atomic local write after verification;
- all-spectrum materialization for the six continua plus the two thermally broadened Be7 profiles.

`tests/test_solar_spectra.py` now checks successful fixture materialization, wrong-byte rejection before write, immutable commit URLs, complete blob-backed component enumeration, and invalid line-materialization rejection.

A dedicated hosted workflow `.github/workflows/spectra-materialize.yml` materializes all pinned spectrum/profile tables and publishes a provenance artifact.

## Validated materialization result

GitHub Actions workflow: `NMIR pinned solar spectra`

- run: `34012460541`
- job: `101430502114`
- head: `f207836f32496b7e78990a485f27568ee659ee15`
- conclusion: SUCCESS
- artifact ID: `9982880231`
- artifact name: `nmir-solar-spectra-f207836f32496b7e78990a485f27568ee659ee15`
- artifact ZIP SHA256: `c506de14cf1c0f0d02c706143449ae4a2fea887195f41de66763651e4f65cda6`

Exact Git-blob SHA identities printed by the validated run:

| component | Git blob SHA |
|---|---|
| B8 | `570e8016d4cfd79808441d6275b8c651341bc3a6` |
| Be7_excited | `41dc3f45c2db215af0b4f0f1746f85646e0a26d2` |
| Be7_ground | `19d97e87e8b03678d2e4629598f7d7fd7794eae0` |
| F17 | `aabf02ee7ca01ec984a0a86cc3dd1597639fc08e` |
| N13 | `08321b17fe4be69db6e98f9c1f6cd296d79fef53` |
| O15 | `5cf6297795f268390cffd557e005db14daa0d32a` |
| hep | `6611f1ce46d59574e41e174cfaa656f437ff6070` |
| pp | `4b00947ad0a27fd5634465f3009025193251e4e0` |

The workflow asserted exactly eight CSV inputs and uploaded nine artifact files including the SHA ledger.

## Head regression result

Head CI run `34012460563`, job `101430502143`, on the same head completed SUCCESS with raw output `48 passed in 0.08s`. The CEvNS/magnetic baseline command also reproduced the previously frozen numerical benchmarks.

## Scientific classification

**PASS — spectral-byte identity/materialization prerequisite.**

This PASS means NMIR now has a reproducible path from frozen spectral provenance to exact verified numerical input bytes. It does **not** mean the solar survival probability, Ga-71 rate, Cl-37 rate, or G3 deposited-power ceiling is closed.

## New prerequisite reconnaissance

Inspection of the pinned PEANUTS `Data/` snapshot confirms the spectral files and Earth-density tables but did not immediately expose a self-evident solar production-radius/electron-density table in that directory listing. Therefore NMIR must separately identify and freeze a primary/provenance-controlled solar electron-density profile and component production distributions rather than silently invent an effective production radius.

## Gate status

- spectral source identity: PASS;
- exact spectral byte materialization: PASS;
- numerical day-averaged solar `P_ee(E)`: OPEN;
- Ga-71 reproduction: OPEN;
- Cl-37 reproduction: OPEN;
- G3 SM deposited-power ceiling: OPEN.

## Exact next gate

1. Identify and freeze solar electron-density profile + component production-radius distributions with primary/source provenance.
2. Implement day-side adiabatic three-flavour `P_ee(E,r)` and component production averaging under the already frozen oscillation parameters.
3. Reproduce a published Ga-71 component/total rate, then Cl-37.
4. Convert those validated rates to W/kg and begin the quantitative G3 ceiling.

`NMIR_READINESS: 25%`

The increase from 24% to 25% is credited only for a real hosted materialization PASS with exact byte identities, artifact provenance, and regression validation.