# Iteration 0022 — 7Li ground-state crossed capture screen

Date: 2026-09-06

## Objective
Test the next G3 candidate, `7Li`, using only the directly defensible crossed weak transition from evaluated `7Be` electron capture. Do not promote a lithium power number until a complete nuclear response is independently validated.

## Frozen nuclear input
ENSDF `7Be` EC evaluation:
- `7Be(gs, 3/2-) -> 7Li(gs, 3/2-)`;
- `Q_EC = 861.815 keV`;
- branch `89.56%`;
- `log ft = 3.324`;
- identical ground-state spins, so the direct gs<->gs crossing has no spin-degeneracy ambiguity.

The evaluated branch to `7Li*(477.612 keV)` is **not** naively reused as capture on a ground-state `7Li` target into a different `7Be` external state. That strength remains outside the present response until separate mirror/isospin/direct authority is frozen.

## Implementation
Added:
- `src/nmir/li7_ground_response.py` — measured-ft crossed gs response;
- `src/nmir/li7_solar_fold.py` — same frozen B16 spectra + production-averaged three-flavour MSW fold used by Ga/Cl/Se;
- `tests/test_li7_ground_response.py` — threshold, normalization and monotonicity regressions;
- `scripts/li7_ground_screen_benchmark.py`;
- `.github/workflows/li7-ground-screen.yml`.

The response is fail-closed below the `861.815 keV` screening threshold. The near-threshold thermally broadened solar `7Be` line is retained explicitly; atomic/screening subtleties are not hidden.

## Hosted result
Scientific screen run: `34034095803`, job `101488884067`, head `d667d2362ce74630b6bd15e29c141c63b398cb01`.

Artifact: `9989580600`; uploaded ZIP SHA256:
`3b66dfe40cd3403ed97b87bedc4e7f76002170de715c5e264390d0184cdc5bc8`.

Raw job log was inspected before classification.

Fixed-energy ground-state cross sections:
- `sigma(1.442 MeV) = 5.56064206086e-44 cm^2`;
- `sigma(5 MeV) = 1.12294958203e-42 cm^2`;
- `sigma(10 MeV) = 4.85776257437e-42 cm^2`.

### GS98 + MSW, ground-state-only
- total rate: `15.9502837162 SNU`;
- energy moment: `54.4719486265 SNU MeV`;
- mean captured incident energy: `3.41510844545 MeV`;
- pure `7Li` neutrino-only screen: **`7.49107964965e-22 W/kg`**;
- natural lithium screen (`7Li` fraction 0.9241): **`6.99831856035e-22 W/kg`**.

Main components:
- B8: `4.76380594923 SNU`, `41.0074928277 SNU MeV`;
- Be7: `4.07166111036 SNU`, `3.51461158060 SNU MeV`;
- pep: `4.13874995360 SNU`, `5.96807743309 SNU MeV`;
- O15: `2.29147589437 SNU`, `3.08728582094 SNU MeV`;
- pp: zero by threshold.

### AGSS09met + MSW, ground-state-only
- total rate: `13.9439186187 SNU`;
- energy moment: `45.9024859132 SNU MeV`;
- pure `7Li` screen: `6.31259183421e-22 W/kg`;
- natural lithium screen: `5.89735133831e-22 W/kg`.

### No-oscillation sanity context
The same ground-state-only GS98 response gives `35.4339435349 SNU` without oscillations. Historical lithium-detector calculations quote a full-response total scale near `39.4 SNU`, but they use different solar-flux/nuclear conventions. The roughly 10% difference is therefore **not** used as a matched validation or as a scientific FAIL/PASS criterion.

## Scientific classification
- ✅ **PASS as a reproducible direct crossed ground-state screening calculation.** The evaluated `log ft` route is implemented and hosted raw output is inspected.
- 🟡 **NOT G3 authority.** The full `7Li` nuclear capture response has not yet reproduced an external source-average or matched-convention full-response benchmark.
- 🟡 The screen is physically interesting: its GS98 pure-isotope value is about `2.55x` the currently validated `82Se` leader (`2.94006655e-22 W/kg`), while natural lithium remains about `2.38x` the pure-82Se benchmark. This makes full lithium validation a high-priority gate.
- ❌ No claim is made that `7.49e-22 W/kg` is the validated lithium ceiling, and it is not inserted into the validated target ranking.

Baseline CI on the same head: run `34034095805` — SUCCESS.

## Exact next gate
Freeze a complete authoritative `7Li(nu_e,e-)7Be` response, including any excited-state strength and the near-threshold atomic convention, and prospectively reproduce at least one published source-average cross section or matched historical total/component set. Only then rerun the B16+MSW rate/energy fold and decide whether lithium replaces `82Se` as the validated G3 leader.

**NMIR_READINESS: 42%** — unchanged because a new target screen is not credited as a closed G3 target until external/full-response validation passes.
