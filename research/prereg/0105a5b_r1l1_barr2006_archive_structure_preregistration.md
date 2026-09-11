# 0105a5b R1l1 — Barr 2006 archive-structure locator preregistration

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Scope: NMIR v2 authority work only. NMIR v1 remains frozen.

## Validated prerequisite

R1l is validated `PASS_0105A5B_R1L_BARR2006_SOURCE_BYTES_ACQUIRED_NONDISCOVERY` at:

- execution commit `461376a00bb9e088c26a6341928d9ebacdde2855`
- run/job/artifact `34600258408 / 103265543016 / 10264640376`
- provider + independent artifact ZIP SHA256 `ef815c6197c45ebe123ceb068ecf00c7bf520b45ada2438f0b3abd9609491dcf`
- exact Barr source SHA256 `f128800ae1eb18fb58c27ce91941b726f1bbf42a7f7ac17a273664f3a81da0f7`
- exact source bytes `114518`

R1l1 is frozen only after this validated PASS.

## Frozen input and acquisition contract

R1l1 may re-fetch only the exact R1l URL:
`https://export.arxiv.org/e-print/astro-ph/0611266v1`

Before any archive parsing, it must independently compute SHA256 and require exact equality to:
`f128800ae1eb18fb58c27ce91941b726f1bbf42a7f7ac17a273664f3a81da0f7`.

A byte mismatch, non-200 response, empty payload, decompression/container failure, unsafe archive member, or non-tar/gzip response fails closed as `INFRASTRUCTURE_FAIL_0105A5B_R1L1`. Scientific criteria must not be changed to repair transport/runtime.

## Allowed operations

Only after the exact byte-lock check passes, R1l1 may:

1. open the archive/container locally;
2. enumerate every member name, type and byte size without reading member payloads;
3. mechanically define the complete future source-text candidate set using the frozen extension rule below;
4. emit a canonical manifest and hashes.

Frozen source-text extensions (case-insensitive):
`.tex`, `.ltx`, `.txt`, `.bib`, `.sty`, `.cls`.

All matching regular-file members are included. No ranking, pruning, keyword-based selection or semantic inspection is allowed.

## Hard prohibitions

R1l1 must not:

- read/decode/search any archive member payload;
- inspect Barr nuisance definitions, equations or tables;
- infer Barr-to-B4RITM transformations;
- run DeepCore standard 3nu;
- run systematic Monte Carlo;
- inspect any observed BSM residual.

## Frozen classification

`PASS_0105A5B_R1L1_BARR2006_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY` iff:

- exact R1l source SHA256 matches before parsing;
- archive enumeration succeeds safely;
- a complete member manifest is emitted;
- the source-text candidate set is exactly the mechanically defined all-member extension set;
- no member payload is read.

Otherwise classify fail-closed as `INFRASTRUCTURE_FAIL_0105A5B_R1L1`.

A PASS authorizes only a separately preregistered semantic authority locator over the entire frozen candidate set. It does not authorize selective source inspection or any nuisance mapping.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
