# 0105a5b R1d Stage-2 — external computational authority classification

Date: 2026-09-10
Branch: `research/0105-bsm-residual-reconstruction`
Frozen parent gate: `research/prereg/0105a5b_r1d_deepcore_external_computational_authority_preregistration.md`, prereg commit `19f4db34117256529e475a7f5e514614899a9f04`.

## Classification

`BLOCKED_0105A5B_R1D_EXTERNAL_COMPUTATIONAL_AUTHORITY_INCOMPLETE`

This is an authority/provenance BLOCKED classification, not a scientific null, not an infrastructure failure, and not a BSM result.

## Hosted execution

- execution head: `66e90f5cc14d24a41eea10d44d13fed206b35884`
- workflow run: `34456783644`
- job: `102804927331`
- artifact: `10143804090`
- dedicated tests: `3 passed`
- provider artifact digest / independently downloaded ZIP SHA256: `456592cb8a88092d44e9300e7e4bebc725f73b8de04d8a9024ff4eb327b35c41`
- inner `r1d_stage2_result.json` SHA256: `8ecf5f6e6c2e2b9dff647cd52ec6c304ec23fb276e43204e6892317c80e67db8`
- execution provenance JSON SHA256: `96ef27bfa633df1254f38371f2a3e632204f24023ccac8609a0e978d6e161fe5`

Exact frozen upstream-source bytes recovered by the hosted collector:

- Barr 2006 source SHA256: `f128800ae1eb18fb58c27ce91941b726f1bbf42a7f7ac17a273664f3a81da0f7`
- CSMS 2011 source SHA256: `274b459c38d54c7b874a3353c622f9c807a1e55dcd2fc27214541e2d9f6015ce`
- Sibyll/MCEq 2019 source SHA256: `f31660851e50c140ea03f932141a1a61b6a2634e103a037305f7748d7f03eedb`

The workflow itself emitted `EVIDENCE_BUNDLE_ONLY_0105A5B_R1D_STAGE2_UNCLASSIFIED`; classification was performed only after raw log and artifact inspection.

## Frozen-gate evaluation

The allowed authority chain establishes the physical/upstream context for hadronic-flux uncertainties and the GENIE-to-CSMS cross-section variation, but it does **not** satisfy the frozen R1d requirement for all seven released nuisance transformations.

### Barr/MCEq six directions

The upstream Barr and Sibyll/MCEq sources provide Barr-region and meson/charge physics, but the inspected authority bundle contains no literal provider-backed mapping from the released B4RITM nuisance column names

`BarrWP`, `BarrWM`, `BarrYP`, `BarrYM`, `BarrZP`, `BarrZM`

to an exact six-direction transformation contract with all of: region identity, charge/sign convention, normalization, units, nominal state, and executable interpolation/reweighting rule. Numerical or mnemonic inference from `W/Y/Z` and `P/M` is forbidden by the frozen gate.

### DIS-CSMS

The allowed IceCube/CSMS authority establishes the nominal/alternative physical semantics (GENIE/GRV98 nominal versus CSMS-like variation) and dependence on energy/inelasticity, but Stage-2 does not recover a complete provider-backed event-level transformation contract sufficient to reproduce the released `DIS-CSMS` nuisance direction exactly from the locked B4RITM inputs. An undocumented interpolation/reweighting implementation is not authorized.

Therefore the full R1d PASS criterion is not met. No nuisance may be dropped, guessed, renamed, hand-normalized, or reconstructed from observed residuals.

## Scientific guards preserved

No oscillated expectation was built. No likelihood or nuisance fit was executed. No observed-minus-null residual was formed. No BSM scan, significance, Wilks threshold, operator-family selection, bin selection, or normalization choice was made.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`.

## Consequence

Standalone DeepCore standard-3nu reproduction remains BLOCKED because the full seven-direction nuisance implementation authority is incomplete. The frozen R1d gate is not weakened after seeing the evidence.

The next scientifically permissible independent work is authority-preserving recovery of the already-preregistered COHERENT 0105a3 complete 37-file byte lock, or a genuinely new prospective external-authority acquisition gate for the missing DeepCore transformation contract. A conformance implementation of the seven DeepCore nuisance transformations is **not** authorized by this BLOCKED result.
