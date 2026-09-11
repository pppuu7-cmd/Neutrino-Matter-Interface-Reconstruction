# 0105a5b R1m1 — CSMS 2011 archive-structure locator preregistration

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Scope: NMIR v2 authority work only; NMIR v1 remains frozen.

## Validated prerequisite
R1m is validated `PASS_0105A5B_R1M_CSMS2011_SOURCE_BYTES_ACQUIRED_NONDISCOVERY` at execution `e68885886344bbf3cf13e0f164146312cdb2679c`, run/job/artifact `34600275535 / 103265599412 / 10264645345`. Provider + independent artifact ZIP SHA256 is `1d73a3986a4fd03574e83ca9561b00d02d33ec9049b3928191dfe96c7a7c48a2`; exact CSMS source SHA256 is `274b459c38d54c7b874a3353c622f9c807a1e55dcd2fc27214541e2d9f6015ce`, bytes `1358795`.

## Frozen input
Exact URL: `https://export.arxiv.org/e-print/1106.3723v1`.
Before any archive parsing R1m1 must independently require exact SHA256 `274b459c38d54c7b874a3353c622f9c807a1e55dcd2fc27214541e2d9f6015ce`.

## Allowed operations
After byte-lock verification only: open the local archive; enumerate every member name/type/size without reading member payloads; mechanically define the complete source-text candidate set using all regular files with case-insensitive extensions `.tex`, `.ltx`, `.txt`, `.bib`, `.sty`, `.cls`; emit canonical manifest/hash.

No ranking, pruning, keyword selection, member-payload read, source semantic inspection, CSMS nuisance inference, DeepCore 3nu, systematic MC, or observed residual is allowed.

## Frozen classification
`PASS_0105A5B_R1M1_CSMS2011_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY` iff the exact source SHA matches before parsing, archive enumeration succeeds safely, complete manifest and exact all-extension candidate set are emitted, and no payload is read. Otherwise `INFRASTRUCTURE_FAIL_0105A5B_R1M1`.

A PASS authorizes only a separately preregistered semantic authority locator over the entire frozen candidate set.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
