# Iteration 0073 — PandaX-4T / De Romeri B-L likelihood input materialization

Status: PROSPECTIVE / frozen before any reproduced likelihood or B-L exclusion result is inspected.
Date frozen: 2026-09-07.
Parent gate: F8 BSM constraints-only, following 0072d `SCIENTIFIC_FAIL_WAGNER_BLUE_IDENTITY` decision tree.

## Question
Can the independent PandaX-4T electron-recoil route be reconstructed from primary/public inputs with enough fidelity to support a reproducible `U(1)_{B-L}` likelihood and contour, without raster/manual contour digitization?

This iteration is an **input-materialization gate only**. It may not emit a new B-L exclusion contour.

## Frozen authorities
1. De Romeri, Papoulias, Ternes, *Light vector mediators at direct detection experiments*, JHEP 05 (2024) 165, arXiv:2402.05506v2 (published version).
2. PandaX Collaboration, D. Zhang et al., *A Search for Light Fermionic Dark Matter Absorption on Electrons in PandaX-4T*, Phys. Rev. Lett. 129 (2022) 161804, arXiv:2206.02339v3.
3. Primary solar-spectrum/normalization references explicitly adopted by De Romeri et al.; these must be hash-pinned/materialized before the later likelihood run.

## Frozen analysis structure from De Romeri et al.
The target reproduction is PandaX-4T only first, not the combined XENONnT+LZ+PandaX fit.

- exposure: `0.63 ton*year`;
- signal components: solar `pp` and `7Be` neutrino electron scattering in the current-experiment analysis;
- reconstructed-bin event rate is Eq. (8) of arXiv:2402.05506v2, including efficiency `A(T_e)`, resolution `R(T_e,T'_e)`, oscillated solar-flux components and differential neutrino-atom/electron cross section;
- total prediction is Eq. (10): signal plus each PandaX background component separately;
- observed PandaX data are those used by De Romeri et al. from Fig. 3 of the PandaX primary paper;
- background-normalization uncertainties are those used by De Romeri et al. from Table I of the PandaX primary paper, preserving any nuisance explicitly left free;
- statistic is the Poissonian least-squares / profile expression Eq. (11) of arXiv:2402.05506v2, including separate background nuisances and solar-flux nuisances;
- PandaX detector efficiency and energy resolution must come from the PandaX primary authority as used by De Romeri et al.; no guessed smoothing or efficiency is permitted.

## Required materialized input ledger
The gate may PASS only if the repository can freeze, with provenance and hashes where applicable:

1. exact PandaX reconstructed-energy bin edges used for the Fig. 3 data;
2. observed counts (or rate plus exact exposure/bin conversion) for every included bin;
3. each background component entering the fit in those bins;
4. Table-I normalization uncertainty for each such background and identification of nuisances left unconstrained/free;
5. detector acceptance/efficiency function over the fit range;
6. detector energy-resolution function and its units;
7. exact fit energy range and any omitted bins;
8. `0.63 ton*year` exposure and target normalization convention;
9. pp and 7Be source spectra/normalizations and frozen oscillation convention, including `sin^2(theta_23)=0.5` as in De Romeri et al.;
10. exact `B-L` charge/coupling convention and mediator propagator appearing in the De Romeri cross section;
11. the exact confidence-level rule to be used in the later contour reproduction (published B-L bounds are 90% CL), including the later frozen Delta-chi2 threshold and parameter-count treatment.

## Permitted extraction routes, ordered
1. author/publisher machine-readable tables or public code;
2. arXiv TeX/source numerical arrays, vector graphics, or embedded tables that permit deterministic calibrated extraction;
3. independent reconstruction from primary experimental numerical tables/functions.

Manual raster digitization is forbidden. A raster figure alone is not numerical authority.

## Validation before later B-L contour calculation
0073 itself does not calculate a contour. It prepares a later preregistered reproduction. The later calculation may start only if 0073 PASSes and must first reproduce a PandaX published background/data spectrum or De-Romeri SM prediction under a separately frozen numerical tolerance. A B-L contour may be emitted only after that benchmark passes.

## Frozen classifications
- `PASS_PANDAX_LIKELIHOOD_INPUTS_MATERIALIZED`: all required inputs above are independently materialized with sufficient numerical authority for a fail-closed likelihood implementation. Next: prospectively freeze a PandaX SM/benchmark reproduction gate.
- `PARTIAL_PASS_PANDAX_INPUTS_NEED_ONE_NAMED_COMPONENT`: most inputs are materialized but one or more precisely named required inputs remain unavailable; no likelihood calculation permitted. Next: pursue only the named missing primary input/public code.
- `BLOCKED_PRIMARY_LIKELIHOOD_INPUTS`: at least one controlling input is only available through prohibited raster/manual inference or is not public enough to reconstruct the fit. Next: retire this route and return to another preregistered primary B-L constraint family.
- `SCIENTIFIC_FAIL_CONVENTION_MISMATCH`: primary PandaX quantities cannot be mapped consistently to the De-Romeri likelihood/coupling convention without an extra unfrozen assumption.
- `INFRASTRUCTURE_FAIL`: source transport/parser/runtime fails before scientific availability can be assessed. This is not a scientific result.

## Guards
No B-L response/enhancement scan. No reading De-Romeri Fig. 1 contour by eye. No substitution of XENON/LZ detector functions for PandaX. No replacement of observed data/backgrounds by Asimov values. No post-result relaxation of required inputs or validation criteria. BSM remains `UNLOCKED_FOR_CONSTRAINT_LEDGER_ONLY`.
