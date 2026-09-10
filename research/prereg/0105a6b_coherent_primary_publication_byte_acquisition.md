# 0105a6b — COHERENT primary-publication byte acquisition

Date: 2026-09-10
Gate: `NMIR-V2-0105A6B`
Stage: external collaboration authority acquisition only
Parent: `NMIR-V2-0105A6`

## Purpose

Acquire and byte-pin the two collaboration primary publications explicitly associated with the already byte-locked COHERENT releases so that a later, separate gate may test whether they close the likelihood/nuisance semantics missing after 0105a6 Stage A.

This gate does not execute an SM fit and does not inspect any BSM residual.

## Frozen authority targets

Only the following versioned collaboration publications are admissible:

### CsI[Na]

- title: `Observation of Coherent Elastic Neutrino-Nucleus Scattering`;
- arXiv identifier/version: `1708.01294v1`;
- versioned PDF URL: `https://arxiv.org/pdf/1708.01294v1`;
- publication DOI: `10.1126/science.aao0990`;
- relation to release: the CsI release companion explicitly identifies the 2017 collaboration result and arXiv `1708.01294` as the analysis corresponding to the released data.

### CENNS-10 Ar Analysis A

- title: `First Measurement of Coherent Elastic Neutrino-Nucleus Scattering on Argon`;
- arXiv identifier/version: `2003.10630v7`;
- versioned PDF URL: `https://arxiv.org/pdf/2003.10630v7`;
- publication DOI: `10.1103/PhysRevLett.126.012002`;
- relation to release: the Ar data release states that it corresponds to Analysis A of arXiv `2003.10630`.

No phenomenology reanalysis, review, repository reconstruction or later COHERENT dataset may substitute for either frozen target.

## Acquisition predicates

For each frozen target the hosted acquisition must:

1. retrieve the exact versioned arXiv PDF after bounded retries;
2. record the resolved URL, byte size and SHA256;
3. parse the PDF successfully;
4. verify the frozen title is present in extracted text;
5. verify the arXiv identifier appears in the document text or PDF provenance strongly enough to reject a wrong-document response;
6. record page count and extracted-text SHA256;
7. emit a normalized JSON manifest containing both entries.

The first successful hosted execution satisfying all predicates freezes the observed PDF SHA256 values for subsequent 0105a6 semantic gates. A later byte mismatch must BLOCK rather than silently update the authority.

## Frozen classifications

- `PASS_0105A6B_PRIMARY_PUBLICATION_BYTE_ACQUISITION_NONDISCOVERY`: both exact versioned collaboration PDFs are retrieved, parsed and identity-validated, and both SHA256 values are recorded.
- `BLOCKED_0105A6B_PRIMARY_PUBLICATION_TRANSPORT_OR_IDENTITY`: either exact versioned target cannot be retrieved after bounded retries or fails identity validation.
- `INFRASTRUCTURE_FAIL_0105A6B`: runner/dependency/runtime failure before the frozen acquisition can execute.

## Prohibited operations

0105a6b must not:

- compute or reconstruct the COHERENT likelihood;
- compare observed data with an SM prediction;
- calculate an observed-minus-SM residual;
- fit nuisance parameters;
- fit any BSM model;
- choose a statistic, threshold or tolerance based on observed behavior;
- use the publications' numerical result as an acceptance target for anything other than document identity.

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact next step after PASS

A separate prospective 0105a6c semantic-completeness gate may refetch only these frozen PDFs, require exact SHA256 equality with the 0105a6b manifest, and inventory literal publication evidence for the missing likelihood functional form, nuisance constraints/couplings, profiling prescription and published null/SM benchmarks. Only that later gate may decide whether a standalone SM/null reproduction can be preregistered.
