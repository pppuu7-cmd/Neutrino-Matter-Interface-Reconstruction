# Iteration 0092b-a2 — terminal external-authority closure for NMIR v1

Date: 2026-09-08
Classification: `BLOCKED_G9_0092B_A2_NUCLEAR_CHANNEL_AUTHORITY_TERMINAL_V1`

## Purpose
Convert the already recorded 0092b-a2 nuclear-channel authority blocker into an explicit **NMIR v1 terminal external-data classification**, without promoting the CCSN-MeV solar branch to transparent or opaque.

This record is an authority-closure result, not a cross-section calculation and not a physical PASS/FAIL.

## Frozen parents
- 0092b-a2 preregistration: `research/prereg/0092b_a2_mev_interaction_envelope_authority.md`, commit `4d0736b9ce5c1a44a467d81d63f0767805a3af1c`.
- validated composition authority: `research/iterations/0092b_a1_r3_model_s_composition_authority_pass.md`, record commit `684f8c47ea7b438fac3289665c6136340ffd05ef`.
- non-terminal sum-rule diagnostic/blocker: `research/iterations/0092b_a2_allowed_sumrule_diagnostic_blocked.md`, record commit `ff11ea06bbbc0af4d4409a7f31b30d3496ffa022`.
- NMIR v1 100%-readiness contract: `research/NMIR_V1_READINESS_100_CONTRACT.md`.

The parent 0092b-a2 contract requires a six-flavor `5–50 MeV`, non-double-counted total-removal upper envelope including materially relevant allowed and forbidden/inelastic CC/NC nuclear responses. It explicitly forbids choosing a convenient representative O/Fe target after seeing the optical-depth scale.

## Authority fact 1 — Model S does not contain the required isotope-resolved deep-solar metal state
Christensen-Dalsgaard's 2021 review of solar structure documents the construction of Model S and is explicit about the treatment of heavy elements:
- the initial composition was calibrated to the Grevesse & Noels (1993) heavy-element mixture with present surface `Z_s/X_s = 0.0245`;
- diffusion and settling of helium and heavy elements were included;
- **the evolution of total `Z` was computed neglecting nuclear reactions and representing the diffusion quantities for the heavy-element component by fully ionized `16O`**;
- the model follows the CN part of the CNO cycle and the conversion of `16O` into `14N`, but the standard Model-S structure authority used by NMIR exposes `X(r)` and total `Z(r)`, not a complete isotope-resolved radial abundance vector for every heavy target required by a target-specific neutrino-response sum.

Primary/review authority:
- J. Christensen-Dalsgaard, `Solar structure and evolution`, Living Reviews in Solar Physics 18, 2 (2021), section 4.1 Model S: https://doi.org/10.1007/s41116-020-00028-3

Therefore the validated 0092b-a1 `Sigma_Z` is a total heavy-element mass column. Turning it into exact target-specific nuclear columns would require an additional externally specified composition/evolution model not present in the frozen Model-S authority. Choosing such a model after seeing the result would be a new assumption and a new prospective gate, not a repair inside frozen 0092b-a2.

## Authority fact 2 — complete tens-of-MeV nuclear response remains target-specific
The 0092b-a2 allowed-transition operator-norm diagnostic already showed substantial numerical headroom to the parent `tau=0.1` threshold, but the frozen gate requires **complete** removal accounting.

Recent state-of-the-art low-energy work reinforces that forbidden nuclear responses cannot simply be deleted at tens of MeV. Gardiner et al. (2026) revisit `nu_e + 40Ar` with a hybrid discrete + HF-CRPA treatment and explicitly include forbidden contributions in the continuum. The calculation is a refined **40Ar-specific** inclusive charged-current model; it is not a universal all-nucleus bound.

Authority:
- S. Gardiner et al., `Continuum contribution to charged-current absorption of low-energy nu_e on 40Ar`, arXiv:2604.26801 (2026): https://arxiv.org/abs/2604.26801

Existing multipole calculations in the tens-of-MeV regime likewise show that forbidden contributions become relevant in a target- and energy-dependent manner. Such calculations can populate a target-specific ledger once the target set is prospectively fixed, but they do not supply the single composition-independent inequality demanded by frozen route B.

## Exhausted admissible routes under the frozen 0092b-a2 contract
### Route A — exact/deep-solar target mixture
Not reproducibly closed by the frozen Model-S authority. The available Model-S state supplies total `Z(r)`, not the complete isotope-resolved radial vector needed to fold target-specific forbidden-inclusive CC/NC responses.

A GN93-based reconstructed isotope mixture, a modern SSM abundance table, or an assumed fixed metal ratio could be scientifically reasonable in a **new** prospective model, but selecting it now would add a physical assumption after the 0092b-a2 result scale is known.

### Route B — composition-independent total weak-response upper bound
The allowed Fermi+Gamow-Teller sector admits useful closure/operator-norm diagnostics, and those diagnostics strongly suggest optical thinness. They do not dominate the complete frozen channel set.

No recovered primary/review authority provides a single reproducible inequality that simultaneously and conservatively dominates, over every physically admissible solar-metal target in `5–50 MeV`:
- allowed and forbidden charged-current multipoles;
- allowed and forbidden/inelastic neutral-current multipoles;
- target thresholds and excitation continuum;
- final charged-lepton Coulomb distortion where applicable;
- target-dependent one- and many-body nuclear-current corrections;
while retaining enough quantitative tightness to evaluate the frozen `tau_total_upper <= 0.1` criterion from `Sigma_Z` alone.

Inventing a post-result safety multiplier or promoting an allowed-only sum rule to a total-response theorem remains forbidden.

## Terminal v1 classification
The authority state is therefore

**`BLOCKED_G9_0092B_A2_NUCLEAR_CHANNEL_AUTHORITY_TERMINAL_V1`**.

Interpretation:
- this is **not** evidence that 5–50 MeV CCSN neutrinos are opaque on the G9 solar chord;
- this is **not** a transparent-Sun PASS;
- the allowed-sector diagnostic remains evidence that ordinary opacity is plausibly small, but it is not a certified total bound;
- closing the physical question beyond v1 requires new external target information/authority or a new prospectively derived all-multipole theorem.

The exact missing external information is now explicit: either an isotope/element-resolved deep-solar chord composition compatible with a prospectively chosen solar model **plus** complete 5–50 MeV target-specific CC+NC response authorities, or a rigorously proved target-independent full weak-response envelope tight enough to evaluate the frozen optical-depth threshold.

## Relation to NMIR v1 readiness
This result satisfies only the **external-authority terminal route** of R100-2 in `NMIR_V1_READINESS_100_CONTRACT.md`. It closes the *v1 research classification* of the MeV propagation authority gap while preserving the physical uncertainty.

It does not by itself increase `NMIR_READINESS` and does not satisfy the remaining R100 conditions. In particular:
- 0093 CCSN alignment-footprint execution remains independent;
- a post-0093 source actionability gate remains required;
- recovery/funnel reconciliation and all running scientific workflows must be terminal before 100%.

## Reopening rule
This v1 terminal block may be reopened only by a new prospective contract that supplies one of the missing external-authority objects above. The historical BLOCKED record must remain immutable.

No detector/material/BSM gain or neutrino-supplied power claim is authorized.
