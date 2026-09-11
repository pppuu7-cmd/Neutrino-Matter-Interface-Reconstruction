# 0105a5b R1m3 — CSMS→B4RITM/IceCube experimental-authority mapping

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Frozen preregistration: `research/prereg_0105a5b_r1m3_csms_b4ritm_mapping.md`, prereg commit `1b0293766466ca178648ce1ed60407915788f8bf`.

## Authoritative scientific classification

`BLOCKED_0105A5B_R1M3_CSMS_B4RITM_EXPERIMENTAL_MAPPING_INCOMPLETE`

This is an authority/implementation BLOCKED result. It is not a scientific null, not a BSM result, and does not authorize standard-3nu, systematic Monte Carlo, or observed-residual inspection.

## Hosted provenance

- implementation commit: `36524388457f614460cc077780decc696a089173`
- deterministic guards commit: `be6649cbabc31424bb10bf00e8ab5ca023f2444c`
- execution head: `10c128f016b127d1ea8b3c2c9feaf13ff510f8dd`
- workflow run/job: `34617899333/103324284516`
- artifact: `10270512595`, `nmir-v2-0105a5b-r1m3-csms-b4ritm-authority-mapping`
- provider artifact digest: `sha256:94f9f77949fce9c13108bffdc46a3c4c2e7e807219a4d6c8dddfd1ee8f73cf43`
- independently downloaded ZIP SHA256: `94f9f77949fce9c13108bffdc46a3c4c2e7e807219a4d6c8dddfd1ee8f73cf43`
- inner `result.json` SHA256: `9d7d0c6f8a93da92bf2b2b983faa96701a23f00ed9925117246556e452531921`
- hosted job and all dedicated steps completed successfully.

## Why the hosted self-label is not a scientific PASS

The hosted JSON self-labelled `PASS_0105A5B_R1M3_CSMS_B4RITM_EXPERIMENTAL_MAPPING_COMPLETE_NONDISCOVERY`, but the frozen preregistration explicitly requires **actual experimentally authorized evidence for all five mapping elements**, with cross-file evidence allowed only when explicit cross-references make the mapping unambiguous. Green CI or a machine self-label is not scientific authority.

Artifact inspection shows that the implementation used lexical bucket matches in bounded contexts. Those buckets can be satisfied by statements that explicitly say the required mapping is **missing**. In particular, the frozen corpus itself contains the authoritative prior statements:

- R1d Stage-1: DIS-CSMS semantics are substantial, but **the exact executable event-reweighting function still must be pinned** before R1d PASS;
- R1d Stage-2: the allowed IceCube/CSMS authority **does not recover a complete provider-backed event-level transformation contract** sufficient to reproduce the released `DIS-CSMS` nuisance direction exactly;
- R1m2: primary CSMS uncertainty semantics are present, but R1m2 **does not itself define** the DeepCore nuisance identifier, event-level reweighting transform, sign/orientation, experimental prior/range, covariance/correlation structure, or normalization convention.

The R1m3 artifact's `covariance` evidence is a concrete example of this problem: its matched snippets come from R1m2 text saying that covariance/correlation/normalization are **not defined** there. Therefore `mandatory_elements_present=true` is a lexical false positive and cannot override the frozen semantic contract.

## Frozen-gate evaluation

The available IceCube publication authority fixes useful DIS-CSMS semantics: GENIE/GRV98 nominal, CSMS alternative, dependence on energy and inelasticity, one event-reweighting nuisance, a below-100-GeV continuation rule, nuisance value 0 versus 1 semantics, and prior centered at 0 with width 1.0. However, the frozen repository authority still lacks a provider-backed **complete executable event-level transformation** and a fully instantiated covariance/correlation/normalization contract sufficient to reproduce the released `DIS-CSMS` direction without analyst fill-in.

Hence the R1m3 PASS contract is not met. The exact repository-only CSMS→B4RITM route is exhausted as BLOCKED. No computational-contract realization may be launched from this result.

## Guards preserved

- standard 3nu executed: no
- systematic Monte Carlo executed: no
- observed BSM residual inspected: no
- network target inspected by R1m3: no
- analyst-chosen amplitude/sign/covariance/normalization introduced: no

DeepCore R1d remains `BLOCKED_0105A5B_R1D_EXTERNAL_COMPUTATIONAL_AUTHORITY_INCOMPLETE`; standalone standard-3nu remains unauthorized.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
