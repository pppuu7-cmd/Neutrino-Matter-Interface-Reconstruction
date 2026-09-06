# Iteration 0015 — Cl-37 response freeze and solar-fold sensitivity

Date: 2026-09-06

## Goal
Advance G3 from validated Ga-71 folding to `37Cl(nu_e,e-)37Ar` using an authoritative energy-dependent response, while exposing rather than hiding the missing numerical authority between the 0.814-MeV physical threshold and the first published 1-MeV response point.

## Primary numerical response
John Bahcall's IAS neutrino-data page provides chlorine absorption cross sections versus neutrino energy in MeV, in units of `1e-46 cm^2`. The improved second column is identified as Bahcall et al., Phys. Rev. C 54, 411 (1996); the third is the older Bahcall-Ulrich/book response. The downloadable table has 19 energies from 1 to 30 MeV.

Repository freeze:
- `data/cl37_bahcall1996_response.csv`: exact 19-point improved + older columns.
- `src/nmir/cl37_response.py`: threshold `0.814 MeV`, piecewise-linear response, fail-closed above 30 MeV, branch-explicit response.
- `tests/test_cl37_response.py`: exact point/threshold/fail-closed regression tests.

Baseline CI after the response/fold implementation: run `34020442734`, job `101451908216`, SUCCESS.

## First full oscillated solar fold
Run `34020427430`, job `101451868492`, head `ab8c31251a746a0b02185ea5c7fcbc8dd11d7b55`: SUCCESS. Artifact `9985296780`, ZIP SHA256 `900526f17c6a7f3990de0a3e46d4f5a8b42d27d74fd6b662005c6a9964312f2f`.

With the explicit threshold-linear convention from 0.814 to the first tabulated 1-MeV point:
- GS98 total: `2.71950666 SNU`; B8 `2.13958564`, Be7 `0.31710921`, pep `0.14335972`, remaining hep+CNO `~0.11945`.
- AGSS09met total: `2.28573197 SNU`; B8 `1.76235780`, Be7 `0.28939128`, pep `0.14530311`, remaining hep+CNO `~0.08868`.

The final Homestake measured rate used in modern radiochemical analyses is `2.56 ± 0.23 SNU`; the GS98 fold is therefore on the observed radiochemical scale, but measurement agreement is NOT used as a normalization or PASS criterion.

## Mandatory sub-1-MeV sensitivity
The primary numerical table begins at 1 MeV. A second prospective sensitivity mode `zero_to_1` was therefore added in commits `731a6b10e3dca13652fcb33dc617f212fed26ab6`, `08b99c8d5da3155c8c6370fe01cd2c24405a7ad1`, and `8781012e35e92c12aee9ea83e07992fc5adc8843`. It sets the unresolved 0.814–1.0 MeV interval to zero while leaving all >=1-MeV response identical.

Sensitivity run `34020504315`, job `101452083142`, head `8781012e35e92c12aee9ea83e07992fc5adc8843`: SUCCESS. Artifact `9985321559`, ZIP SHA256 `347a2e3fbf53ecac44221ab8feb1aa91fb760ebe13e6919c7bb0796e02b771f2`.

Totals:
- GS98: threshold-linear `2.71951 SNU` versus zero-to-1 `2.38893 SNU`; unresolved low-energy response moves the total by `0.33057 SNU` (`~12.2%` of the threshold-linear total).
- AGSS09met: `2.28573` versus `1.98662 SNU`; shift `0.29911 SNU` (`~13.1%`).

Almost all of the shift is the 0.862-MeV Be7 line: `0.31711 SNU` GS98 / `0.28939 SNU` AGSS09met under threshold-linear versus zero in the deliberately conservative zero-to-1 mode. B8 changes by only a few `1e-6 SNU`; the high-energy chlorine result is therefore insensitive to this unresolved interval.

## Scientific interpretation
- Published >=1-MeV Cl response identity: PASS.
- Full high-energy B16/MSW/Cl folding: PASS, B8-dominated and robust to the sub-1-MeV convention.
- Full Cl total: PARTIAL PASS / UNCERTAINTY BLOCKED because the primary tabulation does not directly constrain the 0.814–1-MeV response needed for Be7.
- The historical Homestake threshold is 0.814 MeV and the experiment is mainly sensitive to B8; modern reviews quote the final observed `2.56 ± 0.23 SNU`.
- No result-dependent retuning was performed.

NMIR_READINESS: 32%

Increase `31% -> 32%` credits the authoritative Cl response freeze, hosted B8-dominated fold and quantified low-energy sensitivity; full Cl closure is deliberately withheld.

## Exact next gate
1. Resolve or externally bound the `37Cl` response at the 0.862-MeV Be7 line from primary nuclear/capture literature rather than interpolation.
2. Independently reproduce the standard-spectrum B8-on-Cl average (`~1.1e-42 cm^2` scale) using a matched B8 spectral convention.
3. Then freeze the final Cl component/total interval.
4. In parallel, begin neutrino-only deposited-energy accounting for validated Ga capture: distinguish kinetic/de-excitation energy sourced by the incident neutrino from later daughter-decay/nuclear-mass energy, then convert to W/kg.
