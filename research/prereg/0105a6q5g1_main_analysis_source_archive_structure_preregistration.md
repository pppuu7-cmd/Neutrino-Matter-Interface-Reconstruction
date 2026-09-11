# 0105a6q5g1 — main Analysis-A source archive structure locator preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5G1`
Scope: archive structure/member metadata only; NONDISCOVERY.

Parent q5g validated PASS record: `10b40838dfd2b7a120dea5da5791c729476acde4`.
Frozen source endpoint: `https://arxiv.org/e-print/2003.10630`.
Frozen exact source identity: bytes `446096`, SHA256 `2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114`.

## Frozen procedure

Reacquire the exact source under arXiv-only redirects. Before opening archive metadata, require exact byte count and SHA256. Inspect only archive member names, member types and declared sizes; never read member payload bytes.

Retain the complete member list. Mark a deterministic source-text candidate iff the member is a regular file and its normalized name ends in `.tex`, `.sty`, `.cls`, `.bib`, `.bbl`, `.txt`, `.md`, or `.rst`. Retain all candidates; no ranking or pruning after seeing names.

## Frozen outcomes

- `PASS_0105A6Q5G1_MAIN_ANALYSIS_SOURCE_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY` iff exact source identity matches, archive metadata opens, and >=1 source-text candidate is returned.
- `FAIL_0105A6Q5G1_SOURCE_BYTE_IDENTITY_MISMATCH` if acquired bytes disagree with q5g.
- `BLOCKED_0105A6Q5G1_SOURCE_TRANSPORT_OR_ARCHIVE_STRUCTURE_FAILURE` if acquisition/archive metadata fails.
- `BLOCKED_0105A6Q5G1_NO_SOURCE_TEXT_CANDIDATES` if archive opens but candidate set is empty.

PASS permits only a separately prospectively frozen semantic-evidence gate over the complete returned candidate set, restricted initially to unresolved F1 elementary count law and F7 3152/3154 precedence/distinct-role authority. No member content inspection, likelihood, pseudo-data, systematic Monte Carlo or observed residual is permitted here.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`