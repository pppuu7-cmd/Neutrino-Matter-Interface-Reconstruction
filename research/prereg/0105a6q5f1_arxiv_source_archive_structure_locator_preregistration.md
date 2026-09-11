# 0105a6q5f1 — arXiv:2006.12659 source archive structure locator preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5F1`
Scope: archive structure/member metadata only; NONDISCOVERY.

Parent q5f validated source-byte PASS record: `bb9910e91b833e26c6560f3ac878855acfe380e0`.
Frozen exact source SHA256: `5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde`, bytes `23805`, exact acquisition endpoint `https://arxiv.org/e-print/2006.12659`.

## Frozen procedure

Reacquire only the exact q5f endpoint under arXiv-only redirects. Before opening archive metadata, require exact source SHA256 and byte count. Treat payload as gzip/tar archive only after this identity check. Inspect only archive member names, member types and declared sizes; never read member payload bytes.

Retain the complete member list. Mark a deterministic source-text candidate iff the member is a regular file and its normalized member name ends in `.tex`, `.sty`, `.cls`, `.bib`, `.bbl`, `.txt`, `.md`, or `.rst`. Retain all candidates; do not rank or prune after seeing names.

## Frozen outcomes

- `PASS_0105A6Q5F1_ARXIV_SOURCE_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY` iff source identity matches, archive metadata opens successfully, and >=1 source-text candidate is returned.
- `BLOCKED_0105A6Q5F1_SOURCE_TRANSPORT_OR_ARCHIVE_STRUCTURE_FAILURE` if acquisition/archive metadata cannot complete.
- `FAIL_0105A6Q5F1_SOURCE_BYTE_IDENTITY_MISMATCH` if payload is acquired but disagrees with frozen q5f byte identity.
- `BLOCKED_0105A6Q5F1_NO_SOURCE_TEXT_CANDIDATES` if archive opens but candidate set is empty.

PASS permits only a separately prospectively frozen semantic-evidence gate over the complete returned source-text candidate set. No member content inspection, likelihood, pseudo-data, systematic MC, or observed residual is permitted here.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`