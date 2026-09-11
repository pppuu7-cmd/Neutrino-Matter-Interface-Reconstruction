# 0105a6q5a — Argon official-release provenance/inventory preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5A`
Scope: provenance/inventory only; NONDISCOVERY.

## Scientific question

Can the already byte-locked COHERENT argon release authority from 0105a3 be bound prospectively to a public first-party metadata chain identifying the official COHERENT argon data release, without re-downloading/re-hashing the 24 Ar scientific files and without inspecting their scientific contents?

This gate does **not** ask whether the release contains a count-generation law. It only establishes the authority/provenance substrate on which a later, separately preregistered code/text locator may operate.

## Frozen prior authority

The following 0105a3 facts are frozen inputs and must be verified from the repository-local immutable recovery record `research/iterations/0105a3_coherent_direct_byte_lock_recovery_pass_20260910.md`; q5a must not reconstruct or alter them:

- classification: `PASS_0105A3_COHERENT_ZENODO_DIRECT_BYTE_LOCK_NONTERMINAL`;
- implementation/execution SHA: `6ab2b940be4431c6fd7cad8048e10764a88eb086`;
- successful run/attempt/job: `34418207408/3/102834981270`;
- artifact: `10147580844`, `nmir-v2-0105a3-coherent-byte-lock`;
- artifact ZIP SHA256: `b4d93c5e121ddbf503f9dd837fff1c356fd704342d48c5d243213ac599e26da4`;
- Ar Zenodo record: `3903810`;
- Ar DOI: `10.5281/zenodo.3903810`;
- frozen Ar version: `1.0`;
- Ar file count: `24/24`;
- total release split: CsI `13/13`, Ar `24/24`;
- normalized 37-file byte-manifest SHA256: `5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091`;
- all provider MD5 values matched and independent SHA256 values were recorded for every frozen file.

## Frozen public endpoints

Only these endpoints may be requested by q5a:

1. COHERENT/ORNL Data Releases page: `https://coherent.ornl.gov/data-releases/`
2. Zenodo record metadata API: `https://zenodo.org/api/records/3903810`
3. arXiv metadata page: `https://arxiv.org/abs/2006.12659`

Redirects are allowed only within the same named provider, except that the ORNL page's already-rendered link target may literally point to `zenodo.org/record/3903810` or `zenodo.org/records/3903810`. No discovered links may be followed.

## Frozen metadata predicates

String comparisons are Unicode-normalized, whitespace-collapsed and case-insensitive unless an exact identifier is specified.

### ORNL predicate

PASS component iff HTTP 200 and the page contains an anchor whose visible text contains both `Data release` and `argon`, and whose href resolves to Zenodo record `3903810` (singular `/record/3903810` or plural `/records/3903810`, optional fragment/query tolerated).

### Zenodo predicate

PASS component iff HTTP 200, JSON parses, record id is exactly integer `3903810`, DOI is exactly `10.5281/zenodo.3903810`, metadata version is exactly `1.0`, and title contains the normalized phrase `COHERENT Collaboration data release from the first detection of coherent elastic neutrino-nucleus scattering on argon`. The metadata must expose exactly 24 file entries. File bytes must **not** be downloaded. Their names/sizes/provider checksums may be inventoried only as metadata.

### arXiv predicate

PASS component iff HTTP 200 and provider metadata identifies arXiv id exactly `2006.12659` and title contains the same normalized release-title phrase above. The audit may use HTML `<title>`, citation metadata or other document-head metadata only. Abstract/body/scientific prose must not be retained or semantically inspected.

## Frozen local-binding predicate

The repository-local 0105a3 immutable record must contain every frozen prior-authority value listed above. q5a may parse only this existing record; it must not download any of the 37 release files or regenerate 0105a3 hashes.

## Frozen terminal classes

Exactly one terminal class must be emitted:

- `PASS_0105A6Q5A_ARGON_OFFICIAL_RELEASE_PROVENANCE_INVENTORY_BOUND_NONDISCOVERY` iff local 0105a3 binding + ORNL + Zenodo + arXiv predicates all PASS;
- `BLOCKED_0105A6Q5A_LOCAL_0105A3_AUTHORITY_BINDING_FAILURE` iff the frozen repository-local 0105a3 values do not match;
- `BLOCKED_0105A6Q5A_ORNL_RELEASE_ROUTE_FAILURE` iff the ORNL predicate fails after transport succeeds;
- `BLOCKED_0105A6Q5A_ZENODO_RECORD_METADATA_FAILURE` iff the Zenodo identity/version/title/file-count predicate fails after transport succeeds;
- `BLOCKED_0105A6Q5A_ARXIV_METADATA_FAILURE` iff the arXiv identity/title predicate fails after transport succeeds;
- `BLOCKED_0105A6Q5A_PROVIDER_TRANSPORT_FAILURE` iff any frozen public endpoint cannot be fetched successfully under the transport rule.

Precedence when multiple predicates fail: local binding > transport > ORNL > Zenodo > arXiv.

## Artifact contract

Retain only:

- requested/final URLs, status codes and redirect counts;
- payload SHA256 and byte size for the three metadata payloads;
- boolean predicate results;
- normalized identifiers/title-match booleans;
- Zenodo metadata-only file count and optional filename/size/checksum inventory;
- the frozen 0105a3 identifiers/hashes copied from the local authority record;
- terminal classification.

Do not retain ORNL/arXiv page text, Zenodo descriptions, abstracts, scientific prose, release-file bytes, plots, event counts, model parameters, or fitted quantities.

## Hard prohibitions

q5a does not authorize and must not perform:

- downloading or re-hashing any of the 24 Ar or 13 CsI scientific release files;
- scientific inspection of release code/text;
- pseudo-data generation or random sampling;
- likelihood evaluation or fitting;
- nuisance profiling;
- observed residual inspection;
- BSM/model-family reconstruction;
- tuning any q5b lexical/code locator after seeing q5a payload content.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

A q5a PASS would authorize only preparation of a **new prospectively preregistered q5b count-generation/code-text locator** over an explicitly frozen subset of already-authoritative release material. It would not authorize semantic count-law conclusions or execution of pseudo-data.
