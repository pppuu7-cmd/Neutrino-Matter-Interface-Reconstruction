# 0105a4b — DeepCore B4RITM direct byte-lock preflight

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105A4B
State: ACTIVE_PREREGISTRATION_ONLY
Parent: `research/iterations/0105a4_deepcore_b4ritm_authority_inventory_result.md`

## Purpose

Create an immutable byte-level authority lock for the exact four unrestricted files prospectively pinned by 0105a4 from Harvard Dataverse dataset version 1.1:

`doi:10.7910/DVN/B4RITM`.

This gate is provenance-only. Payloads are treated as opaque bytes. No pickle deserialization, event inspection, likelihood evaluation, oscillation fit, residual construction, or BSM interpretation is allowed.

## Frozen files

The following file IDs, names, byte sizes and provider MD5 values are frozen before byte retrieval:

| file id | filename | expected bytes | provider MD5 |
|---:|---|---:|---|
| 6660756 | `DNN_uncertainty_splines.pckl` | 438500 | `cf76ce7b74baa183f54930c21918a3df` |
| 6660758 | `oscNext_data_IC86.11-18.pckl` | 1445962 | `95e1236193931562959b8547312c74ed` |
| 6660757 | `oscNext_genie_level7_v02.00_pass2.120000.pckl` | 25054422 | `b2dcbf606438088bdee3a8a7b8a1df4e` |
| 6660755 | `oscNext_muongun_level7_v02.00_pass2.140000.pckl` | 12162293 | `9c25d2ff8c16ea944d58a9eaa56dc60a` |

Frozen Dataverse byte route for each file:

`https://dataverse.harvard.edu/api/access/datafile/<FILE_ID>`

Redirects within the Dataverse-authorized retrieval route are transport details only and must be recorded in the output manifest.

## Frozen procedure

For each of the four files, in the order above:

1. retrieve the file bytes from the frozen Dataverse file ID;
2. do not deserialize or interpret the bytes;
3. record the resolved URL and actual byte size;
4. compute MD5 and require equality with the provider MD5 frozen by 0105a4;
5. require actual byte size to equal the frozen provider size;
6. compute and record SHA256;
7. discard the payload after hashing; the workflow artifact must contain manifests/hashes only, not the experimental payloads.

Transient HTTP 429/500/502/503/504, URL errors and timeouts may receive at most four transport retries with bounded backoff. Other HTTP errors fail closed immediately. Retry behavior must not change any scientific or authority criterion.

## PASS gates

PASS requires all of the following:

- exact frozen file count = 4;
- exact frozen dataset identity remains `doi:10.7910/DVN/B4RITM`;
- all four provider MD5 values match the downloaded bytes;
- all four byte sizes match the frozen sizes;
- a 64-hex SHA256 is recorded for every file;
- no file is deserialized or parsed;
- `QKL28Z` is not used or resolved as authority;
- observed residual execution remains prohibited;
- BSM interpretation remains prohibited.

PASS status:

`PASS_0105A4B_DEEPCORE_B4RITM_DIRECT_BYTE_LOCK_NONTERMINAL_NONDISCOVERY`

Any missing/mismatched file, size or checksum is:

`BLOCKED_0105A4B_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE`.

Transport exhaustion is separately classified as:

`BLOCKED_0105A4B_TRANSPORT`.

## Mandatory guards

Always preserve:

- `deepcore_b4ritm_byte_lock_complete` according to the gate result;
- `binary_content_parsed=false`;
- `observed_residual_execution_allowed=false`;
- `bsm_interpretation_allowed=false`;
- `sterile_authority_substitution_forbidden=true`.

Only after a PASS plus an immutable result note may a separate prospective 0105a5b preflight define how the standard 3nu/null model will consume these bytes.
