# NMIR preregistration 0068 — Cu63 RIOEC primary normalization/materialization gate

Date frozen: 2026-09-07
Status: PROSPECTIVE
Parent authority: iteration 0067 `PASS_SOURCE_TAIL_RECOMPUTED / RATE_FOLD_OPEN`.

## Scientific question
Can the exact Resonant Induced Orbital Electron Capture (RIOEC) rate normalization needed for the Cu63 channel be recovered from primary authority with enough detail to make the final source-fold reproducible and dimensionally unambiguous?

This gate is intentionally separated from the numerical rate fold because the 0067 source-tail result is already known. No numerical Cu63 rate may be calculated before this contract is satisfied.

## Frozen target/source inputs inherited without modification
- channel: `63Cu(g.s.,3/2-) + anti-nu_e + e_K -> 63Ni*(87.220 keV,5/2-)`;
- resonance energy `E_R = 162.496486 keV`;
- reverse-strength envelope `B_reverse = 2.85e-3 ... 6.72e-2`;
- K-vacancy natural-width comparator about `1.39 eV`, with source-column ambiguity retained;
- validated thermal-solar source tail: `dPhi_anti-nu_e/dE(E_R) = 3.528363521736758e-41 cm^-2 s^-1 MeV^-1` from 0067;
- source result artifact `10003691395`, ZIP SHA256 `22cc917e5ac275fb509d78b69565736a0d73f433f45461bb20d4d0e01232bfb9`.

## Required primary normalization package
Before any rate calculation, freeze from the primary RIOEC paper (Akhmedov, Lasserre, Maturi, arXiv:2608.25001 or its journal version if available):
1. exact resonance cross-section or rate formula for a continuous antineutrino spectrum;
2. exact line-shape convention and normalization, including whether the continuous-source limit uses peak flux density or an explicit convolution;
3. relation between the weak nuclear matrix element/B(GT) and the entrance partial width or integrated strength;
4. electron-shell wavefunction/atomic factor and its normalization for K capture;
5. spin/statistical factors;
6. all constants and unit conventions required to obtain a rate per target atom;
7. target-number conversion to events/(kg s).

If the primary paper does not expose enough information for an independent implementation, classify `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY` rather than filling missing factors from secondary reviews or guesses.

## Acceptance criteria
- `PASS_RIOEC_NORMALIZATION_MATERIALIZED` only if the full formula chain above is recoverable from primary authority and can be written in an internally dimensionally consistent machine-readable ledger.
- `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY` if one or more required factors cannot be recovered unambiguously.
- `SCIENTIFIC_FAIL_NORMALIZATION` if a recovered implementation fails a dimensional or published-benchmark consistency check.

A green CI or a secondary review is not sufficient evidence.

## Next action on PASS
Freeze a new prospective numerical-fold contract before computing the Cu63 rate. That next contract must preserve the full B(GT) envelope and must report events/(kg s), events/(kg day), and the neutrino-supplied deposited-power ceiling with `0 <= E_dep,nu <= E_nu`. No daughter/atomic relaxation energy may be credited as neutrino power.

## Next action on BLOCKED/FAIL
Keep G8 explicitly blocked at normalization authority. Reconsider BSM unlock only under the existing blocker-limited criterion; do not invent the missing RIOEC normalization.
