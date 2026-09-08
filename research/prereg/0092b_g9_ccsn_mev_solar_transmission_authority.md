# Preregistration 0092b — G9 CCSN-MeV solar transmission authority

Date frozen: 2026-09-08
Parent mixed result: `research/iterations/0092a_g9_cross_section_authority_mixed_blocked.md`, record commit `975838ae5150e9e4295e3e902f1946d659492c93`.
Parent solar-column authority: 0092 `PASS_G9_0092_MODEL_S_COLUMN_AUTHORITY`.
Numerical focusing parent: 0090f `PASS_G9_FULL_GRID_FINITE_NONZERO_SURVIVORS`.

## Question
For the frozen generic Galactic CCSN source regime `5–50 MeV`, is the ordinary Standard-Model interaction optical depth through the exact G9 Model-S reference chord demonstrably thin (`tau_total <= 0.1`) after prospectively freezing solar composition and all materially relevant low-energy weak channels?

This gate addresses only propagation/transmission of the CCSN-MeV branch. It does not repair the prospective alignment blocker from 0091 and does not authorize a detector/material/BSM gain fold.

## Frozen ray / density authority
Use only the validated 0092 chord:
- `b/Rsun = 0.024`;
- `z = 24.073780819657056 AU`;
- `Sigma = 2.9324883602905845e12 g cm^-2`;
- `N_N = 1.7659857664161126e36 nucleons cm^-2`;
- official Model-S density-file SHA256 `65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc`.

No alternate density profile or chord is allowed.

## Frozen source regime
Energy interval: `5 <= E_nu <= 50 MeV`.
The terminal thinness classification must cover the entire interval. A diagnostic grid may be denser, but at minimum it must include `5, 10, 20, 30, 40, 50 MeV`.

The calculation must report neutrino and antineutrino/flavor assumptions explicitly. If a single flavor/channel cannot upper-bound the total interaction probability for all CCSN components, the gate remains BLOCKED rather than silently generalizing.

## Composition authority rule
Before any terminal optical-depth calculation, freeze a primary/review solar-composition authority sufficient to determine or conservatively bound number columns of H, He and metals along the same reference chord.

Preferred hierarchy:
1. an official/primary standard-solar-model radial composition table tied to a documented solar model;
2. if no compatible radial table can be made reproducible, a rigorously conservative composition-independent upper bound over physically admissible solar nuclei may be used only if its derivation is prospectively written into an amendment before evaluating `tau`.

A photospheric abundance alone must not be treated as the core/chord composition. The Model-S density table `cptrho.l5bi.d.15c` does not contain composition columns and is insufficient by itself.

## Low-energy channel ledger
The terminal total interaction upper bound must prospectively include or upper-bound every material channel capable of removing a neutrino from the unchanged-energy straight-ray beam at 5–50 MeV. At minimum audit:
- neutrino-electron elastic scattering;
- elastic/inelastic neutral-current scattering on nucleons/nuclei;
- charged-current reactions on free/bound nucleons or nuclei where kinematically allowed;
- coherent elastic neutrino-nucleus scattering (CEvNS), with finite nuclear recoil treated as a scattering/removal event for the strict unscattered `T0` sentinel.

Oscillation/refraction effects may change flavor but are not, by themselves, removal from the beam; if flavor conversion materially changes the interaction upper bound it must be included conservatively or the gate remains BLOCKED.

Cross-section authorities must be valid in the MeV regime. High-energy DIS linearizations are forbidden.

## Frozen statistics
For each target species/channel `i`,

`tau_i(E) = N_i * sigma_i(E)`.

Define the strict unscattered optical-depth upper bound

`tau_total_upper(E) = sum_i tau_i_upper(E)`

with no double counting of mutually exclusive definitions of the same interaction.

`T0_lower(E) = exp(-tau_total_upper(E))`.

## Frozen numerical / authority criteria
- All external source tables/data used numerically must have exact URL/citation and SHA256 or immutable table/version provenance in the artifact.
- Number-column integration must have two deterministic numerical resolutions/tolerances agreeing to relative `<=1e-4` for each dominant species column.
- Every cross-section formula/table must have units and valid energy range recorded.
- Any analytical upper bound must state exactly which targets/channels it dominates.
- No result-selected composition, channel omission, energy endpoint or uncertainty multiplier.

## Frozen classifications
- `PASS_G9_CCSN_MEV_SOLAR_TRANSMISSION_THIN` if an authority-backed upper bound satisfies `tau_total_upper(E) <= 0.1` for every frozen energy point and the argument covers the full `5–50 MeV` interval.
- `ESCALATE_G9_CCSN_MEV_SOLAR_TRANSPORT_NONNEGLIGIBLE` if the best authority-backed result has `0.1 < tau < 1` anywhere in the interval and transport/regeneration matters.
- `SCIENTIFIC_FAIL_G9_CCSN_MEV_TRANSPARENT_SUN_ASSUMPTION` if an authority-backed lower optical depth reaches `tau >= 1` at a frozen energy.
- `BLOCKED_G9_0092B_SOLAR_COMPOSITION_AUTHORITY` if chord composition cannot be made reproducible or conservatively bounded prospectively.
- `BLOCKED_G9_0092B_MEV_CHANNEL_AUTHORITY` if the total low-energy interaction ledger cannot be upper-bounded reproducibly.
- `INFRASTRUCTURE_FAIL_G9_0092B` only for execution/tool/download failure.

## Consequences
PASS would establish only that ordinary solar matter is sufficiently transparent for the frozen CCSN-MeV ray under the strict unscattered sentinel; 0091's prospective alignment/unknown-event-direction blocker would remain.

FAIL would invalidate the transparent-Sun approximation for CCSN MeV on this ray but would not erase 0090f's gravitational geometry PASS.

BLOCKED may not be repaired by adopting a convenient abundance mix after seeing the answer.

## Guards
No DIS extrapolation to MeV. No photospheric composition promoted to core composition. No detector/material/BSM gain multiplication. No claim that the NGC-1068 TeV opacity result determines this branch. No post-hoc named CCSN progenitor selection.
