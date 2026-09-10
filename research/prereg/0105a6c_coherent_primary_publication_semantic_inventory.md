# 0105a6c — COHERENT frozen-primary-publication semantic inventory

Date: 2026-09-10
Gate: `NMIR-V2-0105A6C`
Stage: primary-publication semantic inventory only
Parent: `NMIR-V2-0105A6B`

## Purpose

Determine what likelihood/profile/nuisance semantics are literally present in the two primary COHERENT publications byte-pinned by 0105a6b, without constructing a likelihood or inspecting an observed BSM residual.

This gate is an evidence inventory. It does not itself declare the collaboration likelihood mathematically complete. Completeness classification must be made in a separate immutable record from the frozen evidence emitted here.

## Frozen byte authority

Only these exact bytes are admissible:

### CsI[Na]
- arXiv: `1708.01294v1`
- URL: `https://arxiv.org/pdf/1708.01294v1`
- PDF SHA256: `a47539271203e0d0ea71a45ede2535011bcd2b0cdb2a846beecb1f54302fe9fc`
- extracted-text SHA256 reference from 0105a6b: `624265ab22c728743c313ddf1ec2356b26df1aacb02435d4d6899f7ba0eb557c`

### CENNS-10 Ar Analysis A
- arXiv: `2003.10630v7`
- URL: `https://arxiv.org/pdf/2003.10630v7`
- PDF SHA256: `2f875bda728739a85a2568db44761d7f164e113e77613d8f884e6c4b071acef2`
- extracted-text SHA256 reference from 0105a6b: `6de9701f58985c81ea027c24edd39316b9459e49dfae4a2b8cb09c633eef8c4d`

Any PDF byte mismatch is an authority BLOCK and semantic extraction must stop for that target.

## Frozen semantic questions

For each target, the inventory must report page indices (1-based) for literal evidence of the following, where present:

1. maximum-likelihood / extended maximum-likelihood method;
2. binned observable dimensions used by the fit;
3. CEvNS signal component and its fit freedom/constraint;
4. prompt/beam-related neutron background treatment;
5. steady-state background treatment;
6. Gaussian or other explicit nuisance constraints;
7. profiling / profile-likelihood prescription;
8. published null/SM significance or best-fit benchmark;
9. pseudo-experiment / pseudo-data / coverage validation;
10. literal identification of an elementary counting likelihood such as a Poisson likelihood *for the fit objective*, as distinct from Poisson photoelectron/detector simulation;
11. a mathematically explicit complete likelihood/objective equation with all fit components and nuisance penalties, if present.

The script may use deterministic phrase families to locate candidate evidence pages. It must not equate phrase detection with semantic completeness.

## Completeness rule reserved for post-run classification

A later 0105a6c classification may authorize an exact standalone SM/null reproduction only if the frozen collaboration authority is sufficient to specify, without analyst invention:

- per-bin/data likelihood family and objective;
- component expectations entering that objective;
- nuisance parameters, penalty/constraint distributions and couplings;
- profiling/floating prescription;
- normalization/exposure and detector-response semantics;
- at least one collaboration numerical benchmark usable as an external reproduction check.

`maximum likelihood`, `extended maximum likelihood`, a profile plot, or a quoted significance alone is insufficient to infer the missing elementary likelihood or nuisance wiring.

If any required element is not literal or uniquely implied by the authority, classify BLOCKED rather than filling the gap from common practice.

## Prohibited operations

0105a6c must not:

- compute an observed SM-vs-data residual;
- reconstruct or minimize the collaboration likelihood;
- evaluate a new null significance;
- fit nuisance parameters;
- fit or scan a BSM model;
- select a residual basis;
- use a phenomenology reanalysis as collaboration authority.

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Gate classifications

- `PASS_0105A6C_PRIMARY_PUBLICATION_SEMANTIC_INVENTORY_NONDISCOVERY`: both frozen hashes match and semantic evidence pages are inventoried deterministically.
- `BLOCKED_0105A6C_FROZEN_BYTE_MISMATCH_OR_TRANSPORT`: an exact source cannot be recovered or its byte hash differs.
- `INFRASTRUCTURE_FAIL_0105A6C`: runtime/dependency failure before evidence inventory.

A PASS here means only that the inventory ran successfully. It does not mean likelihood completeness.
