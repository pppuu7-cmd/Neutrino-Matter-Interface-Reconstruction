# NMIR v2 0105a5b-R1j1 — PISA methodology archive-structure locator

Date frozen: 2026-09-11
Parent: validated R1j source-byte PASS.

## Frozen input
Acquire only `https://export.arxiv.org/e-print/1803.05390` and require whole-body SHA256 exactly `e8d26d85195764037765661fb2e5236ec4284a712adbfd9738b7c3908593c6be` before archive parsing.

## Allowed inspection
Open the archive and record only member name, regular-file flag, and byte size. Do not read any member payload. Define the complete future source-text candidate set mechanically as all regular files whose case-insensitive suffix is one of `.tex`, `.txt`, `.bib`, `.sty`, `.cls`. Preserve all such candidates without ranking/pruning.

## Classification
`PASS_0105A5B_R1J1_PISA_METHODOLOGY_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY` iff source hash matches, archive parses, and at least one source-text candidate exists. Empty candidate set is `BLOCKED_0105A5B_R1J1_NO_SOURCE_TEXT_CANDIDATES`; hash/archive/transport failure is `INFRASTRUCTURE_FAIL_0105A5B_R1J1`.

PASS permits only a separately preregistered semantic locator over the complete returned candidate set. No member payload may be read in this gate.

Hard prohibitions: source_text_inspected=false; PISA repository content inspected=false; standard 3nu=false; systematics MC=false; observed residual=false.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
