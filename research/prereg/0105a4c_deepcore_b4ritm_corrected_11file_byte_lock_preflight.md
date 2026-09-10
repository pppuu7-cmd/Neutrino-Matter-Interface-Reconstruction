# 0105a4c — corrected DeepCore B4RITM 11-file byte-lock preflight

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105A4C
State: ACTIVE_PREREGISTRATION_ONLY
Parent authority: hosted 0105a4 artifact from run `34418458353`, job `102688456198`, artifact `10129986472`.
Supersedes for downstream use: invalid 0105a4b four-file transcription branch of authority.

## Purpose

Create a byte-level lock for the exact **11-file** Harvard Dataverse inventory already contained in the raw 0105a4 B4RITM artifact. This is provenance-only. All payloads remain opaque bytes.

No `.tab`, `.ipynb`, or `.md` content may be parsed for scientific meaning in this gate. No event inspection, likelihood evaluation, 3nu fit, residual construction, or BSM interpretation is allowed.

## Frozen dataset identity

- persistent ID: `doi:10.7910/DVN/B4RITM`
- release version: `1.0`
- version state: `RELEASED`
- raw parent metadata SHA256: `50b0e1ed9d939d1a2b2f4e497dd3841c9c73eb8ecaa4a589268d3ba75ad3d0db`
- normalized parent inventory SHA256: `1cfc666849a7cf200ef4cdaf47b926e9ece44b63a92d4e29710c5a0cba441baa`

## Frozen 11-file inventory

| file id | filename | bytes | provider MD5 |
|---:|---|---:|---|
| 11646859 | `data.tab` | 4091 | `59d03738e7fe61fe06a06b2140708373` |
| 11674675 | `example.ipynb` | 231264 | `fd9ac548e6a6f136efb6c61058cc822f` |
| 11646858 | `hs_numu_cc.tab` | 543795 | `d9cfa0e209bb82af43c78474765be5e3` |
| 11646854 | `hs_nu_nc_nue_cc.tab` | 543327 | `75cffca2d2d099373c680a5f4088c195` |
| 11646853 | `hs_nutau_cc.tab` | 544770 | `cd3c6335d25d1163c5df30aaff50be2a` |
| 11646851 | `mc_mu.tab` | 5815 | `bc7133f3da6c1acf830a9e8d686bef4c` |
| 11646852 | `mc_nue_cc.tab` | 6234527 | `2150abf034ed873b798dfa61cbe7ac78` |
| 11646856 | `mc_numu_cc.tab` | 44626533 | `b60ccf0e0e447698d35b953a6e22552d` |
| 11646850 | `mc_nu_nc.tab` | 3975602 | `fb5eac7230c1ab1b4e8b1f019ed33e2b` |
| 11646855 | `mc_nutau_cc.tab` | 7266105 | `cb62a96ed14491deef10bb8253a786ca` |
| 11674676 | `readme.md` | 7141 | `848778cd0b870da83a6b925b89ba3d3d` |

The exact set, not only the count, is frozen.

## Procedure

1. Re-fetch B4RITM dataset metadata from Harvard Dataverse.
2. Require DOI, version 1.0, RELEASED state, and exact equality of the live file tuples `(id, filename, size, MD5)` to the frozen 11-file parent inventory before any byte download.
3. For each frozen file, retrieve `https://dataverse.harvard.edu/api/access/datafile/<FILE_ID>`.
4. Record resolved transport URL, but do not infer scientific identity from the redirect target alone.
5. Treat response as opaque bytes; compute actual size, MD5, SHA256.
6. Require actual size and MD5 to equal the frozen parent values.
7. Upload only manifest/hash/stdout artifacts; do not upload or commit experimental payload bytes.
8. Discard payloads after hashing.

Transient HTTP 429/500/502/503/504 and network timeouts may receive at most four retries. No scientific criterion, file set, DOI, version, size, or checksum may change under retry.

## PASS contract

PASS requires simultaneously:

- live metadata identity = B4RITM;
- live version = 1.0 RELEASED;
- live inventory exactly equals all 11 frozen tuples;
- all 11 byte sizes match;
- all 11 provider MD5 hashes match;
- all 11 SHA256 hashes are recorded;
- `binary_content_parsed=false`;
- `observed_residual_execution_allowed=false`;
- `bsm_interpretation_allowed=false`;
- no QKL28Z substitution.

PASS label:

`PASS_0105A4C_DEEPCORE_B4RITM_11FILE_BYTE_LOCK_NONDISCOVERY`

Any metadata/file/checksum mismatch:

`BLOCKED_0105A4C_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE`

Transport exhaustion:

`BLOCKED_0105A4C_TRANSPORT`

A PASS may authorize a **new separately preregistered** DeepCore 3nu/null-reproduction gate, but does not itself authorize BSM residual analysis.
