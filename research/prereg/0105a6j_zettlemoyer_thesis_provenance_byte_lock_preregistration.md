# 0105a6j — Zettlemoyer thesis provenance and byte-lock preregistration

Status: **PREREGISTERED / NONDISCOVERY / SOURCE-ACQUISITION ONLY**

## Purpose

Determine whether Jacob C. Zettlemoyer's 2020 Indiana University PhD dissertation can be admitted as a **provenance-qualified collaboration-author/institutional secondary implementation source** for a later, separately preregistered COHERENT Ar likelihood-semantics acquisition audit.

This gate does **not** grant the dissertation collaboration-release authority and does not inspect or classify its likelihood implementation details. It only freezes identity, provenance, institutional custody, collaboration linkage, and PDF bytes.

## Frozen candidate identity

- author: `Jacob C. Zettlemoyer`
- title: `First Detection of Coherent Elastic Neutrino-Nucleus Scattering on an Argon Target`
- degree/institution: PhD, Indiana University, Department of Physics, 2020
- DOI: `10.5967/3wza-6w73`
- Indiana University handle: `2022/25448`
- IU item page: `https://scholarworks.iu.edu/dspace/items/ae71e100-a414-4756-bf9e-be4808f675e5`
- frozen institutional bitstream candidate: `https://scholarworks.iu.edu/dspace/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/download`
- official COHERENT thesis index: `https://coherent.ornl.gov/theses/`
- collaboration measurement identity used only for author-link evidence: arXiv `2003.10630v7`.

## Frozen provenance gates

All must PASS:

- **P1 COHERENT index identity:** the official `coherent.ornl.gov` thesis page identifies Jacob C. Zettlemoyer, the dissertation title, and DOI `10.5967/3wza-6w73`.
- **P2 institutional custody:** the Indiana University ScholarWorks item identifies the same author/title, 2020 PhD thesis scope, DOI, and institutional handle.
- **P3 collaboration-author linkage:** the frozen COHERENT Ar measurement source `2003.10630v7` identifies `J. Zettlemoyer` as an author of the collaboration measurement.
- **P4 byte acquisition:** the frozen IU bitstream resolves to a PDF payload, is larger than 30,000,000 bytes, and an independent SHA256 is recorded.
- **P5 custody consistency:** the candidate PDF is reached from/frozen against the same IU institutional item identity; no ResearchGate, Scribd, secondary mirror, or reconstructed PDF may substitute.

## PASS/BLOCKED classes

If P1-P5 all pass:

`PASS_0105A6J_ZETTLEMOYER_THESIS_PROVENANCE_BYTE_LOCK_NONDISCOVERY`

This means only: the exact PDF may be used in a later prospectively frozen semantic audit as a **provenance-qualified collaboration-author/institutional secondary source**.

If any provenance/custody/byte condition fails:

`BLOCKED_0105A6J_ZETTLEMOYER_THESIS_PROVENANCE_OR_BYTE_AUTHORITY_INCOMPLETE`

Transport failure is recorded separately from semantic/scientific failure.

## Authority ceiling

Even a PASS must record:

- `collaboration_release_authority = false`
- `secondary_collaboration_author_source = true`
- `sm_null_reproduction_permission_percent = 0`
- `observed_bsm_residual_permission_percent = 0`

A later semantic gate may use thesis statements only within their demonstrated Analysis-A scope. Any conflict with collaboration publication/release authority must be preserved, not silently resolved in favor of the thesis.

## Hard prohibitions

- No likelihood reconstruction or numerical fit.
- No observed residual inspection.
- No BSM/model-family scan.
- No semantic search of the thesis in this gate beyond identity/custody validation.
- No promotion of thesis-specific implementation choices to collaboration-wide choices without a later explicit authority bridge.
