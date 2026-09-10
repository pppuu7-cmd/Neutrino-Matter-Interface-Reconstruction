# 0105a6j — Zettlemoyer thesis provenance and byte-lock result

Date: 2026-09-10
Scope: **NONDICOVERY / SOURCE-ACQUISITION ONLY**

## Frozen gate

Preregistration: `research/prereg/0105a6j_zettlemoyer_thesis_provenance_byte_lock_preregistration.md`

Preregistration commit: `b53dec91a3b43b31d64714a294aa939a793216b3`

The gate asked only whether Jacob C. Zettlemoyer's 2020 Indiana University PhD dissertation could be admitted as a provenance-qualified collaboration-author/institutional **secondary implementation source** for a later, separately preregistered semantic audit. It did not inspect or classify thesis likelihood details and could not authorize an SM/null fit or observed residual.

## Hosted execution provenance

- execution head: `79b9c5879262125c71bc33f76aa38beeeff7e57e`
- workflow run: `34494089256`
- job: `102928006886`
- artifact: `10159022944`, `nmir-v2-0105a6j-zettlemoyer-thesis-provenance`
- artifact size: `2403` bytes
- artifact ZIP digest: `sha256:7e3208a1800c6b1d3d2efe7b03ffb8bf9570334d6a57e7210daf917a2b0a3d55`
- inner `result.json` SHA256: `8e07fc3ca0583371c7854734494c3e8bed4b42b192d3df021599381c8863ec3b`
- deterministic guards: `5 passed`

## Frozen provenance outcome

All five preregistered provenance gates passed:

- **P1 COHERENT index identity — PASS.** Official `coherent.ornl.gov/theses/` identified Jacob C. Zettlemoyer, the frozen dissertation title, and DOI `10.5967/3wza-6w73`.
- **P2 institutional custody — PASS.** Indiana University ScholarWorks identified the same author/title, 2020 PhD scope and DOI/handle.
- **P3 collaboration-author linkage — PASS.** The frozen COHERENT Ar measurement e-print `2003.10630v7` identified `J. Zettlemoyer` as an author.
- **P4 PDF byte acquisition — PASS.** The institutional bitstream resolved to a PDF payload of `34641327` bytes.
- **P5 custody consistency — PASS.** The resolved PDF remained under Indiana University ScholarWorks institutional custody.

Exact institutional PDF identity:

- resolved URL host/path: `scholarworks.iu.edu/iuswrrest/api/core/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/content`
- content type: `application/pdf;charset=UTF-8`
- byte length: `34641327`
- SHA256: `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`

Source receipts:

- official COHERENT theses page: `79179` bytes, SHA256 `a04263fb0f11a01b52bd07f27dd38adfb55309e89f4e42e23076e573961594a0`;
- IU item page: `413899` bytes, SHA256 `bd3180824400c47e59b4d4431d189979d602309b09d3f842579e74d4b52f70bd`;
- measurement e-print: `446096` bytes, SHA256 `2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114`.

Terminal classification:

`PASS_0105A6J_ZETTLEMOYER_THESIS_PROVENANCE_BYTE_LOCK_NONDISCOVERY`

## Authority ceiling

This PASS is deliberately narrow:

- `collaboration_release_authority = false`
- `secondary_collaboration_author_source = true`
- `SM_NULL_REPRODUCTION_PERMISSION = 0%`
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

The dissertation is therefore admitted only as a byte-locked, provenance-qualified secondary source written by a collaboration measurement author and held by the degree-granting institution. It does **not** become collaboration-release authority.

Any later use must first prospectively freeze the exact thesis scope/section to be read. Thesis-specific statistical choices may contribute evidence only if they are demonstrated to describe the same CENNS-10/Analysis-A implementation, and conflicts with the collaboration publication/release must be preserved rather than silently resolved in favor of the thesis.
