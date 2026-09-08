# Iteration 0092b-a1 r3 — Model-S composition authority PASS

Date: 2026-09-08
Classification: `PASS_G9_0092B_MODEL_S_COMPOSITION_AUTHORITY`

## Frozen authority
Parent preregistration: `research/prereg/0092b_g9_ccsn_mev_solar_transmission_authority.md`, frozen commit `66341d7eb7322e958a52dc30fb24d4e2b3e44647`.
Prospective amendment: `research/amendments/0092b_a1_model_s_gong_composition_authority.md`, frozen commit `8e7466013f0e978be9c036ec9ca10f4aa005cb66`.

Two earlier candidates remain immutable infrastructure failures only:
- r1 parser record-boundary failure: `research/iterations/0092b_a1_r1_gong_parser_infrastructure_fail.md`;
- r2 whitespace-vs-fixed-width parser failure: `research/iterations/0092b_a1_r2_gong_fixed_width_infrastructure_fail.md`.

The r3 change only implemented the already documented official GONG `1p5e16.9` fixed-width file format. No scientific source, formula, ray, numerical resolution, tolerance or classification threshold changed.

## Hosted execution
Execution head: `e1c2e584f7d5b80ce00f7b8c34c2c8011573e5a8`.
Workflow run/job: `34277614693 / 102234398138`.
Artifact: `10076333882` (`nmir-g9-0092b-a1-model-s-composition-authority`).
Dedicated tests: `3 passed`.

Raw Actions job log was read before classification. The artifact was then independently downloaded and all hashes recomputed.

Validated hashes:
- artifact ZIP SHA256: `bf9a7dcdfab0bf05d7ca936c61bba54f2cd39841cd380316bf4a421da71aa4ec`;
- inner `g9_0092b_a1_model_s_composition.json` SHA256: `1edda4508f0ce73ffc025adce7c0a867c301cd301a8e65a0509ac75d70df2291`;
- official limited Model-S density file SHA256: `65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc`;
- official extensive GONG Model-S file SHA256: `a30c31b9f6af2e5918f49d3808c0dade54f9946133b679b86949fc73625c2393`;
- official GONG format PDF SHA256: `9614e18f6eed3f7121352539651c502ae84b7b13bb308b091a66157b45a597b5`.

The independent ZIP/JSON/source hashes exactly match raw hosted evidence.

## Frozen format/provenance checks
The official extensive file reports the frozen header
`nn=2482, iconst=15, ivar=25, ivers=210`.

The preregistered official-format interpretation was used:
- `var(1)=r`;
- `var(6)=X` hydrogen mass fraction;
- for version 210, `var(17)=Z` heavy-element mass fraction;
- `Y=1-X-Z` helium mass fraction.

GONG composition was interpolated versus normalized radius onto the already validated 0092 chord. The GONG density did not replace the 0092 limited-file density authority.

At closest approach `b/Rsun=0.024`:
- `X = 0.35554806874807887`;
- `Y = 0.6241438995900526`;
- `Z = 0.02030803166186854`.

Maximum pointwise `|X+Y+Z-1| = 2.220446049250313e-16`.

## Component chord columns
Frozen fine-resolution result (`N=262144` Simpson panels):
- `Sigma_H = 1.5217827389419937e12 g cm^-2`;
- `Sigma_He = 1.3518482663979014e12 g cm^-2`;
- `Sigma_Z = 5.8857354950716446e10 g cm^-2`;
- component sum `Sigma_sum = 2.9324883602906113e12 g cm^-2`.

Against the independently validated 0092 total column `2.9324883602905845e12 g cm^-2`, closure relative error is `9.157911456241502e-15`, far below the frozen `1e-8` gate.

Corresponding fine number columns:
- hydrogen nuclei `N_H = 9.16438985041013e35 cm^-2`;
- helium nuclei `N_He = 2.035255134462346e35 cm^-2`.

The metal result remains a mass column only; no representative metal nucleus was selected post-result.

Coarse/fine relative discrepancies:
- H column `1.2873598714965283e-11`;
- He column `7.508347450372221e-12`;
- Z column `2.9128071530783575e-12`.

All are far below the frozen `1e-4` numerical-convergence threshold.

## Scientific interpretation
This closes the previously explicit deep-solar/chord composition authority blocker for H/He/Z on the exact G9 `b/Rsun=0.024` ray.

It does **not** establish a 5–50 MeV CCSN solar-transmission result. The parent 0092b gate still requires a prospectively frozen, MeV-valid total interaction-channel/cross-section ledger (at minimum neutrino-electron, CC, NC and CEvNS/removal accounting) before any `tau_total` is evaluated.

No high-energy DIS formula may be imported into the MeV branch. No detector/material/BSM gain is authorized. The 0091 prospective event-direction/alignment blocker also remains even if the later MeV transmission gate passes.

## Next admissible gate
Freeze a separate 0092b-a2 low-energy Standard-Model interaction authority ledger, including exact formulas/units/energy ranges and a conservative handling of the unresolved metal mixture, before computing any 5–50 MeV total optical depth.
