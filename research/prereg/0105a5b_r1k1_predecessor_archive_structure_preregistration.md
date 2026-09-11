# 0105a5b R1k1 — predecessor DeepCore archive-structure locator preregistration

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`

Prerequisite: validated R1k opaque source byte lock.

## Frozen source

Exact URL: `https://export.arxiv.org/e-print/1902.07771`
Exact required source SHA256: `d095d23daf4dc08848b7f3ff5977daaf554db966034ca9d3460e4b88d7c3790a`

The SHA256 must be verified before archive parsing. Any mismatch is `BLOCKED_0105A5B_R1K1_SOURCE_BYTE_IDENTITY_MISMATCH` and no archive member may be inspected.

## Allowed operations

After exact byte identity succeeds, R1k1 may open the container only to enumerate member metadata: member name, member type, and size. It may mechanically freeze the complete candidate set whose names end case-insensitively in `.tex`, `.txt`, `.bib`, `.sty`, or `.cls`.

No candidate ranking or pruning is allowed.

## Hard prohibitions

R1k1 must not read any member payload, search source text, inspect scientific semantics, fetch PISA repository content, compare PISA outputs, select a PISA tag/commit, execute standard 3nu, run systematic Monte Carlo, or inspect observed BSM residuals.

## Frozen classification

- `PASS_0105A5B_R1K1_PREDECESSOR_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY` iff exact source SHA256 matches, archive enumeration succeeds, and at least one member is returned.
- `BLOCKED_0105A5B_R1K1_SOURCE_BYTE_IDENTITY_MISMATCH` on SHA mismatch.
- transport/container runtime errors are `INFRASTRUCTURE_FAIL_0105A5B_R1K1`.

A PASS authorizes only a separately preregistered semantic locator over the complete returned source-text candidate set.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
