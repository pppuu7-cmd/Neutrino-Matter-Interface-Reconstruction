# 0105a — NMIR v2 cross-experiment authority audit for BSM residual reconstruction

Date: 2026-09-10
Parent gate: `research/prereg/0105_v2_model_agnostic_bsm_residual_reconstruction.md`
State: `PARTIAL_AUTHORITY_PASS_WITH_BLOCKS`

## Question

Which current public experimental releases can support an independently reproducible Stage-A residual analysis, and which should remain constraint-only or prospective held-out validation authorities?

This audit classifies **data/statistical usability**, not the scientific quality of an experiment.

## A. IceCube DeepCore — strongest current propagation-side candidate

### A1. Standard atmospheric-oscillation replication release

Publication:
- IceCube Collaboration, *Measurement of atmospheric neutrino mixing with improved IceCube DeepCore calibration and data processing*, Phys. Rev. D 108, 012014 (2023), DOI `10.1103/PhysRevD.108.012014`.

Official public replication dataset:
- Harvard Dataverse DOI `10.7910/DVN/B4RITM`;
- linked from IceCube's official data-release page in 2025.

Recovered authority description:
- the public release is explicitly a replication dataset for the published DeepCore oscillation measurement;
- IceCube documentation and the associated public analysis ecosystem describe binned detector data, simulated neutrino/muon events and detector-response information for systematics;
- the source sample uses atmospheric neutrino energy/zenith information and a detailed nuisance treatment.

0105a decision:

`PASS_0105A_ICECUBE_DEEPCORE_PROPAGATION_AUTHORITY_CANDIDATE`

This is currently a better Stage-A propagation residual candidate than using a published contour alone because an independent forward model can, in principle, be confronted with binned data and detector/systematic response objects.

Mandatory next lock before a fit:
- enumerate exact Dataverse version/files/checksums;
- identify which nuisance morphing/response functions are sufficient to reproduce the collaboration control fit;
- reproduce the Standard-Model/3-flavor benchmark before adding any residual coefficient.

### A2. DeepCore 7.5-year sterile release

Publication:
- IceCube Collaboration, *Search for a light sterile neutrino with 7.5 years of IceCube DeepCore data*, Phys. Rev. D 110, 072007 (2024), DOI `10.1103/PhysRevD.110.072007`.

Official IceCube data-release route:
- public IceCube data-release page (2025) -> Harvard Dataverse;
- existing NMIR 0101 audit already treats this as a factorized sterile constraint authority, not a fabricated global likelihood.

0105a decision:

`PASS_0105A_ICECUBE_STERILE_CONTROL_AUTHORITY`

Use it as a known-model/sterile control and consistency axis. Do not let a sterile-specific fit silently define the generic 0105 propagation residual likelihood if the standard-oscillation replication release above provides the more general response model.

### A3. IceCube Upgrade

Status at 2026-09-10:
- hardware deployment completed in 2026;
- commissioning is ongoing / observed Upgrade oscillation results suitable for this gate are not yet an authority already used by 0105;
- IceCube has public projected-sensitivity data for atmospheric oscillations, but simulation sensitivity is not observed discovery evidence.

0105a decision:

`RESERVED_0105A_ICECUBE_UPGRADE_HELDOUT_VALIDATION`

Observed Upgrade matter/oscillation data remain a high-value prospective validator and must not be replaced by sensitivity projections in a discovery claim.

## B. COHERENT — current finite-q scattering authority

Official COHERENT data-release page currently exposes at least:

1. first CsI CEvNS observation release, DOI `10.5281/zenodo.1228631`;
2. first Ar CEvNS detection release, DOI `10.5281/zenodo.3903810`.

The Ar release is particularly useful for an independent reconstruction because its public description includes binned on-beam/off-beam data, CEvNS signal PDFs, beam-related/steady-state background PDFs, detector response/efficiency information, flux/systematic quantities and example analysis code. The release explicitly discusses refitting an alternative hypothesis with nuisance-normalization treatment.

0105a decision:

`PASS_0105A_COHERENT_FINITE_Q_AUTHORITY_CANDIDATE`

This authorizes **authority pinning and control-fit reproduction only**. It does not yet authorize a BSM residual scan.

Important limitations:
- the currently obvious fully documented public releases are older CsI/Ar datasets; newer Ge evidence/measurements must not be assumed to have equivalent likelihood-level public releases unless separately pinned;
- nuclear form factors, flux, quenching/response and nuisance treatment remain part of the physical/statistical model;
- propagation coefficients cannot be compared to CEvNS by a phenomenological `Delta H` alone; the 0105 microscopic operator bridge is mandatory.

Mandatory next lock before a fit:
- download/hash exact CsI and Ar releases;
- reproduce collaboration SM control observables;
- freeze whether both targets are used jointly or one is discovery and one internal validation;
- preserve target-dependent coherent charge and form-factor treatment.

## C. JUNO first 59.1-day result — high-value but currently likelihood-incomplete for primary residual discovery

Publication:
- JUNO Collaboration, *Measurement of reactor neutrino oscillation with the first JUNO data*, Nature 654, 343–348 (2026), DOI `10.1038/s41586-026-10538-z`.

The collaboration reports the first 59.1 days of valid data and high-precision values of `sin^2(theta12)` and `Delta m^2_21`.

Critical data-availability fact:
- raw experimental data are not publicly accessible;
- source data for selected figures are public;
- inquiries for the data/posteriors used in the result may be directed to the collaboration;
- analysis code is not publicly distributed.

0105a decision:

`BLOCKED_0105A_JUNO_PRIMARY_RESIDUAL_LIKELIHOOD_INCOMPLETE`

JUNO is scientifically valuable now as a precision constraint/cross-check, but figure source data alone must not be elevated to a collaboration-equivalent residual likelihood with invented covariance/nuisance semantics.

Prospective status:

`RESERVED_0105A_JUNO_FUTURE_LIKELIHOOD_VALIDATION`

A future public likelihood/posterior+nuisance release, or an immutable collaboration-provided object sufficient for independent reproduction, can upgrade this status under a new authority lock.

## D. ICARUS / SBN

### D1. First ICARUS BNB disappearance result

Publication/result:
- ICARUS Collaboration, *First search for sterile neutrino oscillation leading to nu_mu disappearance in the Booster Neutrino Beam at ICARUS*, arXiv `2603.22557`; accepted to Phys. Rev. D in 2026 (existing NMIR 0101 authority audit records DOI `10.1103/2vms-z2j8`).

Result semantics:
- no statistically significant muon-neutrino disappearance;
- 90% exclusion contours in a two-neutrino approximation;
- the analysis is explicitly systematics-limited without a near-detector constraint.

0105a decision:

`PASS_0105A_ICARUS_PUBLIC_CONTROL_NOT_BLIND_VALIDATION`

Because its result is already public and inspected at the level of null/non-null status during authority design, this specific Run-2 result cannot later be advertised as a blind 0105 confirmation.

### D2. Future joint SBND + ICARUS analysis

The intended two-detector SBN architecture uses SBND as the near detector to constrain flux/interactions and ICARUS as the far detector. As of this audit, the future joint result remains distinct from the already-seen first ICARUS-only result.

0105a decision:

`RESERVED_0105A_JOINT_SBN_HELDOUT_VALIDATION`

Its held-out status is preserved only if 0105 does not inspect result-dependent joint-fit information before freezing a prediction.

## E. Current discovery/validation split

### Discovery/calibration side — allowed to be opened after child preregistration

- IceCube DeepCore standard atmospheric-oscillation replication release `10.7910/DVN/B4RITM` — propagation/matter-response candidate;
- COHERENT CsI/Ar public releases — finite-q scattering candidates;
- existing 0100–0104 synthetic/known-model benchmarks — controls only.

### Constraint-only / partial side

- JUNO 2026 first result — precision cross-check while likelihood/nuisance authority is incomplete;
- ICARUS 2026 first disappearance result — already-seen control/constraint;
- IceCube 7.5-year sterile release — sterile control/constraint under 0101 semantics.

### Held-out prospective side

- future joint SBND+ICARUS SBN result;
- observed IceCube Upgrade oscillation/matter-effect release;
- future JUNO collaboration-level reproducible likelihood/posterior release;
- future independent CEvNS target/data release not used to select the operator.

## F. Strongest new scientific opportunity exposed by the audit

There is already enough public authority to attempt, after reproducibility locks, a genuinely cross-regime test without waiting for DUNE:

`IceCube DeepCore q->0 matter propagation  <->  COHERENT finite-q CEvNS`.

For a shared vector mediator, the same microscopic coupling product enters both regimes but the finite-q propagator changes from `1/m_X^2` to `1/(m_X^2+|q|^2)`. Therefore the combination can test more than an NSI contact coefficient: in the finite-range regime it can potentially constrain the mediator scale through the **shape** of recoil-dependent suppression relative to the forward potential.

This is a stronger scientific target than simply fitting one epsilon parameter or one sterile contour.

## G. What is not yet authorized

No 0105 Stage-A BSM residual fit is authorized yet.

Open prerequisites:

1. immutable file/version/checksum inventories for `10.7910/DVN/B4RITM` and selected COHERENT releases;
2. exact reproduction tests for the published Standard-Model/3-flavor and CEvNS controls;
3. 0105b analytic finite-q bridge tests;
4. 0105c frozen low-complexity residual basis/statistic and trial-factor treatment.

Current classification:

`PARTIAL_PASS_0105A_PUBLIC_CROSS_REGIME_AUTHORITIES_IDENTIFIED_REPRODUCTION_LOCKS_OPEN`

This is an authority result, not evidence for a BSM residual.