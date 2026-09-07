# Iteration 0074 — COHERENT CsI+Ar B-L primary likelihood materialization

Status: PROSPECTIVE / frozen before inspecting numerical likelihood outputs.
Date frozen: 2026-09-07.
Parent: 0073b `BLOCKED_PRIMARY_LIKELIHOOD_INPUTS`.

## Question
Can the explicit gauged-`U(1)_{B-L}` COHERENT CsI+Ar constraint of Cadeddu et al. (JHEP 01 (2021) 116, arXiv:2008.05022) be independently reproduced from primary/public COHERENT data in one fixed `(m_V,g_BL)` convention, with a benchmark that validates the SM/data likelihood before any B-L exclusion is accepted?

This is an F8 external-constraint gate. It is not an NMIR response/enhancement scan.

## Frozen model convention
`L_int = g_BL V_mu J_{B-L}^mu`, with lepton charge `-1`, quark charge `1/3`, and coherent nuclear B-L charge approximately baryon number `A` subject to the exact convention implemented by the primary authority. Parameters: mediator mass `m_V` and gauge coupling magnitude `g_BL`.

No universal-vector contour may be relabelled as B-L. If the primary paper uses a different normalization symbol, the exact algebraic conversion must be frozen before numerical comparison.

## Frozen authority order
1. Cadeddu et al., JHEP 01 (2021) 116 / arXiv:2008.05022 for the B-L signal convention, fit construction, nuisance treatment, and published benchmark contour.
2. Official COHERENT CsI and liquid-Ar public data releases for observed bins, response/acceptance, backgrounds, flux, covariance/nuisance inputs and timing/energy binning used by the fit.
3. Publisher/arXiv source or author code/data only to materialize quantities explicitly tied to the same analysis.

Different-generation COHERENT releases may not be mixed unless the primary analysis explicitly maps them.

## Required materialization payload before any B-L scan
For each detector dataset actually used by the primary fit:
- exact observed binning/counts (energy and timing if applicable);
- neutrino source/flux normalization and spectra;
- detector response/acceptance/quenching inputs;
- background templates and normalization/systematic treatment;
- covariance matrices or nuisance priors;
- CEvNS SM prediction formula and nuclear form-factor convention;
- exact B-L modification/interference formula and coupling normalization;
- hashes/provenance for every external numerical file.

## Mandatory pre-BSM benchmark
Before scanning `(m_V,g_BL)`, reproduce a frozen SM/background benchmark from the primary analysis. The benchmark numerical targets/tolerances must be copied verbatim or otherwise frozen from primary authority before the reproduction output is inspected. If the paper does not give enough numerical benchmark information to define a non-circular tolerance, classify BLOCKED rather than invent one after the result.

## Frozen classifications
- `PASS_COHERENT_B_MINUS_L_LIKELIHOOD_MATERIALIZED`: all controlling primary inputs materialized, SM/background benchmark passes its prospectively frozen tolerance, and the B-L convention is unambiguous. Next: separately preregister the B-L contour scan/materialization.
- `PARTIAL_PASS_COHERENT_INPUTS`: useful primary inputs materialize but at least one controlling likelihood ingredient remains missing; no B-L contour permitted.
- `BLOCKED_PRIMARY_COHERENT_LIKELIHOOD_INPUTS`: permitted public-primary routes exhausted with at least one controlling input unavailable.
- `SCIENTIFIC_FAIL_COHERENT_BENCHMARK`: all required inputs exist but the independently implemented SM/background benchmark fails the preregistered numerical tolerance.
- `SCIENTIFIC_FAIL_B_MINUS_L_CONVENTION`: coupling/charge/interference convention cannot be reconciled unambiguously with the primary B-L authority.
- `INFRASTRUCTURE_FAIL`: transport/parser/runtime fails before scientific assessment.

## Guards
No reading contour points by eye. No post-result tolerance relaxation. No replacing missing covariance/background information with diagonal or Asimov approximations. No mixing CsI/Ar releases across incompatible selections. No B-L response calculation for NMIR. No F9 multiplication with unvalidated gains.
