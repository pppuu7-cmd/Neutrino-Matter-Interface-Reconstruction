# 0105a6q5g — main Analysis-A arXiv source acquisition preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5G`
Scope: provenance/source-byte acquisition only; NONDISCOVERY.

Parent q5f2 validated BLOCKED record: `81047ef0048a55f64aa1aff9ce4b14a7ce51b453`.

q5f2 exhausted the `arXiv:2006.12659` companion-source route and explicitly resolved F4/F6 while leaving F1 and F7 blocked. The companion source itself names/refers to the collaboration Analysis-A publication and contains the arXiv identifier `2003.10630`; this gate opens that genuinely additional collaboration-publication authority without selecting on residuals or scientific outcome.

Frozen target: COHERENT Collaboration, `arXiv:2003.10630`, *First Measurement of Coherent Elastic Neutrino-Nucleus Scattering on Argon*.
Frozen acquisition endpoint: `https://arxiv.org/e-print/2003.10630` with redirects restricted to arXiv-owned hosts.

## Frozen procedure

Acquire the endpoint once in the hosted workflow. Record HTTP status, final URL, byte count, content type, MD5 and SHA256. This gate MUST NOT open archive structure, list members, decompress, extract, read source text, search keywords, inspect figures, or adjudicate F1/F7. No exact source digest is assumed before this first byte acquisition; the successful hosted result freezes the digest for any later gate.

## Frozen outcomes

- `PASS_0105A6Q5G_MAIN_ANALYSIS_ARXIV_SOURCE_BYTES_ACQUIRED_NONDISCOVERY` iff transport returns HTTP 200, non-empty payload, final host remains arXiv-owned, and payload is retained only as byte identity metadata.
- `BLOCKED_0105A6Q5G_MAIN_ANALYSIS_SOURCE_TRANSPORT_FAILURE` on transport/provider failure or empty payload.
- `FAIL_0105A6Q5G_MAIN_ANALYSIS_PROVIDER_IDENTITY_FAILURE` if final host escapes arXiv ownership.

PASS permits only a separately prospectively frozen archive-structure locator bound to the newly frozen q5g SHA256. It does not permit source-text inspection.

No likelihood, pseudo-data, systematic Monte Carlo, nuisance profiling, observed residual, BSM scan, significance or Wilks threshold is permitted.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`