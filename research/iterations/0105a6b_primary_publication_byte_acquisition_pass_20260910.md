# 0105a6b — COHERENT primary-publication byte acquisition PASS

Date: 2026-09-10
Gate: `NMIR-V2-0105A6B`
Classification: `PASS_0105A6B_PRIMARY_PUBLICATION_BYTE_ACQUISITION_NONDISCOVERY`

## Frozen authority targets

The prospectively frozen authority targets remained unchanged throughout acquisition:

- CsI[Na]: arXiv `1708.01294v1`, DOI `10.1126/science.aao0990`, exact versioned endpoint `https://arxiv.org/pdf/1708.01294v1`.
- CENNS-10 Ar Analysis A: arXiv `2003.10630v7`, DOI `10.1103/PhysRevLett.126.012002`, exact versioned endpoint `https://arxiv.org/pdf/2003.10630v7`.

No alternate publication, later version, phenomenology reanalysis, review, mirror, or collaboration data release was substituted.

## Historical implementation false negative

Hosted run `34472808643`, job `102856431879`, successfully retrieved and parsed both frozen PDFs and verified both frozen titles, but the initial implementation incorrectly required the resolved arXiv URL to end in `.pdf`. arXiv returned the exact frozen versioned endpoints without a `.pdf` suffix, so `versioned_url_identity_ok` was falsely set to `false` for both documents.

The byte payloads from that false-negative run were already:

- CsI SHA256 `a47539271203e0d0ea71a45ede2535011bcd2b0cdb2a846beecb1f54302fe9fc`, 1,676,215 bytes, 52 pages;
- Ar SHA256 `2f875bda728739a85a2568db44761d7f164e113e77613d8f884e6c4b071acef2`, 947,798 bytes, 10 pages.

Thus the initial failure was an implementation/identity-predicate false negative, not a transport failure, publication-identity failure, or authority change.

## Corrected identity predicate

Commit `63b6b8c247c298fc29af3a1b2c93e8b9b4126027` replaced the suffix assumption with an exact HTTPS `arxiv.org` host plus exact versioned `/pdf/<arxiv-id>` path predicate, allowing only the semantically equivalent optional `.pdf` suffix. PDF magic, successful parsing and exact frozen-title presence remained independent identity checks.

The scientific authority target, version, DOI, title and acceptance scope were unchanged.

## Successful hosted execution

- execution head: `63b6b8c247c298fc29af3a1b2c93e8b9b4126027`;
- run/job: `34472943887/102856865246`;
- dedicated guards: `3 passed`;
- workflow conclusion: `success`;
- result/manifest SHA256: `84c8c3e3a04597ab2516a741b7fa2c12b6f16253d1d6830c6cf9bd75d42eee11`;
- artifact: `10150274006`, `nmir-v2-0105a6b-coherent-primary-publication-byte-manifest`;
- artifact ZIP SHA256: `f48c27d4a8cc9a66fb1a5522c8aa49bfc4ce44767d620898289dc8107617e384`.

### CsI[Na]

- exact resolved endpoint: `https://arxiv.org/pdf/1708.01294v1`;
- byte SHA256: `a47539271203e0d0ea71a45ede2535011bcd2b0cdb2a846beecb1f54302fe9fc`;
- size: 1,676,215 bytes;
- pages: 52;
- extracted-text SHA256: `624265ab22c728743c313ddf1ec2356b26df1aacb02435d4d6899f7ba0eb557c`;
- PDF magic: PASS;
- frozen title identity: PASS;
- exact versioned URL identity: PASS.

### CENNS-10 Ar Analysis A

- exact resolved endpoint: `https://arxiv.org/pdf/2003.10630v7`;
- byte SHA256: `2f875bda728739a85a2568db44761d7f164e113e77613d8f884e6c4b071acef2`;
- size: 947,798 bytes;
- pages: 10;
- extracted-text SHA256: `6de9701f58985c81ea027c24edd39316b9459e49dfae4a2b8cb09c633eef8c4d`;
- PDF magic: PASS;
- frozen title identity: PASS;
- exact versioned URL identity: PASS.

The byte SHA256 values are identical to the payloads retrieved in the initial false-negative run, independently demonstrating that only the validator logic changed.

## Permission boundary

This PASS closes only primary-publication byte acquisition. It does not classify semantic completeness and does not authorize a fit.

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact next gate

A prospective `NMIR-V2-0105A6C` gate may refetch only these two exact versioned PDFs, require exact SHA256 equality with the frozen hashes above, and inventory literal collaboration evidence for:

1. likelihood family and elementary objective structure;
2. nuisance priors/constraints and parameter couplings;
3. profiling prescription;
4. published SM/null numerical benchmarks and coverage checks;
5. any ambiguity that would require an analyst-invented convention.

If an executable or mathematically complete likelihood contract cannot be recovered from the frozen collaboration authority, the SM/null reproduction remains BLOCKED rather than being filled in from common statistical practice.
