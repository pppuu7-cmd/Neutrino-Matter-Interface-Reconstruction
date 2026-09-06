# Iteration 0016 — Cl-37 source-average authority replaces sub-1-MeV interpolation

Date: 2026-09-06

## Motivation
Iteration 0015 showed that the published pointwise Cl-37 table begins at 1 MeV, making a naive 0.814–1.0 MeV interpolation dominate the 0.862-MeV Be-7 contribution. This iteration replaces that non-authoritative interpolation for Be-7 with a published source-averaged cross section.

## Primary authority
Bahcall & Ulrich, Rev. Mod. Phys. 60, 297 (1988) publishes source-averaged Cl-37 absorption cross sections, including Be-7 = 2.4e-46 cm^2 and B-8 = 1.06e-42 cm^2. The frozen table is `data/cl37_bahcall_ulrich1988_source_average.csv`.

## Implementation
- Added `src/nmir/cl37_source_average.py`.
- `oscillated_cl37_snu` now defaults to `be7_mode=source_average` while preserving `profile` as a sensitivity/history mode.
- Since the 0.384-MeV Be-7 line is below the 0.814-MeV Cl threshold, the published Be-7 source average is multiplied by the production-averaged Pee of the capture-active 0.862-MeV line.
- Added tests for exact frozen anchors and representative Be-7 rate scale.

## Hosted result
Run `34022999659` on head `4e29bef5f15ac39c5d97fc51274d0ff40235f893` completed SUCCESS. Artifact `9986121953`, SHA256 `ce64ed62d0fc50632d48815c0c0e42a8afdb14d00bee47ae292666cba3edfe7c`.

Authority-backed fold:
- GS98 threshold-linear residual mode: total 3.0259102626 SNU; Be7 0.6235128155 SNU; B8 2.1395856360 SNU.
- AGSS09met threshold-linear residual mode: total 2.5653534895 SNU; Be7 0.5690127947 SNU; B8 1.7623577975 SNU.
- If the remaining unresolved sub-1-MeV continuum response is zeroed instead, totals become 3.0124469721 SNU and 2.5556370910 SNU.

Thus the full-total sensitivity to the unresolved interval collapses from ~12–13% in iteration 0015 to ~0.4% once Be-7 uses primary source-average authority. The earlier threshold-linear Be-7 value (~0.317 SNU for GS98) is classified as a scientific failure of that interpolation model, not a failure of Cl capture physics.

## Independent B-8 gate — scientific FAIL under mixed conventions
Hosted workflow run `34023058360` on head `b423cd694069ae70c98d88d8d66cae560a59190a` completed SUCCESS. Artifact `9986140900`, SHA256 `7d4dd1071af57c95e6958b0670e37c303ea70053c416691e6ea6597044da2299`.

Using the currently frozen Ortiz B-8 spectral shape with the Bahcall-1996 pointwise Cl response gives

- threshold-linear: `1.1914503006e-42 cm^2`, relative difference `+12.40097%` from the Bahcall-Ulrich `1.06e-42 cm^2` source-average authority;
- zero-to-1: `1.1914494769e-42 cm^2`, relative difference `+12.40089%`.

Because the two low-energy conventions differ by less than `1e-6` fraction in this average, the discrepancy is not caused by the 0.814–1.0 MeV response gap. It is therefore classified as a **scientific convention-mismatch FAIL** for the attempted mixed `Ortiz spectrum × Bahcall response → Bahcall-Ulrich historical average` reproduction. No response normalization or acceptance criterion is retuned. The next requirement is to identify/freeze the B-8 spectral convention used by the historical source-average authority, or compare against a source-average prediction explicitly computed with the Ortiz convention.

## Classification
- Be-7 low-energy Cl blocker: PASS at source-average/component level.
- Pointwise sigma(0.862 MeV): remains not independently reconstructed and is no longer required for the solar-component fold.
- Residual 0.814–1.0 MeV continuum ambiguity: bounded and subdominant (~0.4% total effect).
- B-8 mixed-convention source-average reproduction: SCIENTIFIC FAIL (`+12.40%`), localized away from the low-energy gap.
- Baseline CI on recovery head `14b55306e55dd941373bda0d492590088dda0bff`: run `34023100498`, SUCCESS.

NMIR_READINESS: 33%
