# 0105a6f — Ar implementation-contract semantic closure: transport BLOCKED

Date: 2026-09-10
Gate: `NMIR-V2-0105A6F`
Classification: `BLOCKED_0105A6F_ARGON_AUTHORITY_BYTE_OR_TRANSPORT`
Scope: official authority semantic classification only; NONDISCOVERY.

## Frozen gate

Execution/preregistration head: `a94e86d4238011a71c9b71154c9036b442c0a2e7`
Preregistration: `research/prereg/0105a6f_argon_implementation_contract_semantic_closure.md`

The gate froze seven semantic fields F1-F7 and required all seven to be COMPLETE before any separate Standard-Model/null reproduction could be authorized. The gate itself was forbidden from fitting data.

## Hosted execution evidence

Workflow run: `34487597716`
Frozen attempts: 1, 2, 3
Attempt-3 job: `102907687763`
Dedicated deterministic guards: `5 passed`
Attempt-3 workflow conclusion: `success` (infrastructure/CI conclusion only)
Attempt-3 artifact: `10156613203`, `nmir-v2-0105a6f-argon-semantic-authority`
Attempt-3 artifact ZIP SHA256: `8714229935f563e1ad010bc40ec9ecaee8103a0810aa02269b241c47491f770e`
Attempt-3 result JSON SHA256: `73c6fdf6d3d7849eb71a55f1bf15bd53d6eb89fc8102e820cddabd94246aeb70`

## Stable success on the arXiv half

All attempts preserved the exact frozen Ar source identity:

- arXiv source: `2003.10630v7`
- source archive SHA256: `2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114`
- `main.tex` SHA256: `9e7785c68173921361722af9b95d99c05ff2cdafbf7565fc6b8a057b626b2c86`
- `supplemental.tex` SHA256: `183ec77ea668c91611fef8f8e117f3796e36eed36d27026608d1830b11a60a57`

The exact source contains strong collaboration-level semantic evidence including:

- an extended maximum-likelihood fit in reconstructed energy, trigger time and F90;
- CEvNS, BRN and steady-state components;
- an unconstrained CEvNS event yield in Analysis A;
- Gaussian-constrained steady-state and BRN normalizations for Analysis A and an explicit delayed-BRN component;
- RooFit pseudo-data validation;
- an explicit statement that the listed fit-shape systematic contributions are treated as independent and added in quadrature;
- a profile statistic `-2 Delta ln L`, with the null evaluated at `N_CEvNS = 0` and profiled over SS and BRN yields;
- collaboration numerical anchors, including the Analysis-A predicted/fitted event yields and null significances.

These observations make F1/F2/F5/F7 strong candidates for COMPLETE and provide substantial evidence for portions of F3/F6. They are not a semantic PASS by themselves because the preregistered gate also requires the exact released configuration/templates needed to settle F3/F4/F6 without analyst invention.

## Repeated transport failure on the Zenodo half

The frozen gate required provider record `3903810` metadata and text-decodable released analysis/configuration assets. In all three unchanged attempts, the exact arXiv source was recovered successfully but the Zenodo API stage returned:

`HTTPError: HTTP Error 504: Gateway Time-out`

The fail-closed script therefore emitted:

`BLOCKED_0105A6F_ARGON_AUTHORITY_BYTE_OR_TRANSPORT`

A green workflow cannot override that scientific/status field.

## Why no F1-F7 semantic classification is issued

The missing Zenodo half contains the authority required to test exact nuisance values, released component PDFs/systematic variations, and executable rate/shape mappings. Under the frozen all-fields rule, no field may be upgraded by common practice or by memory of prior runs.

Therefore 0105a6f ends as a transport BLOCK, not as `PASS` and not as `IMPLEMENTATION_CONTRACT_INCOMPLETE`.

## Authorization state

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

No observed fit or BSM/model-agnostic residual inspection is authorized.

## Authority-preserving recovery route

0105a3 already byte-locked the exact same official Ar release and recorded provider MD5, independent SHA256, byte size and direct official Zenodo file URL for all 24 Ar files. A new prospective gate may therefore use the immutable 0105a3 manifest identity to retrieve those exact provider bytes directly, requiring exact hash equality, while bypassing only the currently failing Zenodo metadata API endpoint.

Such a recovery gate must not change provider, release, filename inventory, hashes, scientific semantics or F1-F7 completion criteria, and must not use secondary mirrors.
