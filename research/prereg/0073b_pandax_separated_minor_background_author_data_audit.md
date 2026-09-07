# Iteration 0073b — PandaX separated minor-background primary-data audit

Status: PROSPECTIVE / frozen before inspecting candidate numerical background releases.
Date frozen: 2026-09-07.
Parent: 0073a `PARTIAL_PASS_VECTOR_DATA_EFFICIENCY_ONLY`.

## Question
Can a primary PandaX / author / publisher numerical source supply the **separate 0–30 keV reconstructed-energy templates** needed for the four minor backgrounds that Fig. 3 of arXiv:2206.02339v3 publishes only as a grouped curve: neutron, solar-8B, accidental, and wall/surface?

This is a source/materialization gate only. It may not evaluate a B-L likelihood or contour.

## Frozen already-accepted inputs
0073a has independently materialized and validated:
- exact observed 1-keV-bin counts `[3,39,67,73,90,71,70,53,54,64,57,41,38,44,26,29,18,23,24,22,8,26,18,23,26,20,19,7,3,2]`, sum 1058;
- primary 301-point PandaX efficiency central curve;
- primary source archive SHA256 `b077b657e30a2efc07fb37f3c389d365ef670c408a5dc42cafc7af06a5e75db3`;
- Fig. 3 groups neutron + 8B + accidental + wall/surface, while Table I assigns distinct nuisance widths: 50%, 28%, 20%, 25% respectively.

## Frozen permitted authority routes, in order
1. Official PandaX data-release files or supplementary numerical files explicitly tied to the same 2021/2022 PandaX-4T data selection and detector configuration.
2. Publisher supplementary material / HEPData / SCOAP3 or equivalent author-provided numerical tables explicitly tied to the paper.
3. Author public repository/code/data with explicit provenance to the same analysis.
4. Independent reconstruction from primary detector/model inputs **only if** each component's normalization, selection, detector response and energy shape are completely specified by primary authority.

A data file from a different PandaX analysis may be used only if primary provenance establishes that the relevant template and detector response are identical for the 0–30 keV selection; superficial similarity is insufficient.

## Required PASS payload
For each of `neutron`, `8B`, `accidental`, and `surface/wall`:
- 30 bin values for exact 1-keV bins 0–30 keV, or a higher-resolution deterministic representation that integrates uniquely to those bins;
- units and normalization convention;
- provenance tying the template to the same PandaX data selection/configuration;
- hash of every external numerical file;
- sum/integral consistency with the corresponding Table-I best-fit expectation to within 1% (or tighter explicit source precision if given).

All four components must pass. No proportional decomposition of the grouped Fig. 3 curve is allowed.

## Frozen classifications
- `PASS_PANDAX_SEPARATED_MINOR_BACKGROUNDS_MATERIALIZED`: all four templates pass provenance and normalization checks. Next: prospective SM/background benchmark reproduction.
- `PARTIAL_PASS_PANDAX_SEPARATED_BACKGROUNDS`: one to three exact named components are materialized but at least one named component remains missing; no likelihood permitted.
- `BLOCKED_PRIMARY_LIKELIHOOD_INPUTS`: after exhausting the permitted public-primary routes, at least one controlling minor-background component remains available only as the grouped Fig. 3 curve / total Table-I rate / non-authoritative inference. Retire the PandaX full-profile route without weakening the nuisance model.
- `SCIENTIFIC_FAIL_BACKGROUND_PROVENANCE_MISMATCH`: candidate numerical release belongs to a materially different selection/configuration and cannot be mapped without an unfrozen assumption.
- `INFRASTRUCTURE_FAIL`: transport/parser/runtime prevents assessment of source availability.

## Guards
No raster/manual digitization. No splitting the grouped curve in proportion to Table-I totals. No Asimov substitution. No borrowing XENON/LZ shapes. No assuming a generic/earlier PandaX efficiency or background shape is identical without explicit same-configuration provenance. No B-L calculation in 0073b. No post-result relaxation.
