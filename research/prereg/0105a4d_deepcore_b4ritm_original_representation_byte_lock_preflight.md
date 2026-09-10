# 0105a4d — DeepCore B4RITM original-representation byte-lock preflight

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105A4D
State: ACTIVE_PREREGISTRATION_ONLY
Parent authority: hosted 0105a4 metadata artifact, run `34418458353`, job `102688456198`, artifact `10129986472`.
Predecessor diagnostic: `0105a4c` demonstrated that Dataverse default access returns the archival representation for ingested tabular files, for which the frozen original-file MD5 predicate is not appropriate.

## Purpose

Lock the exact B4RITM bytes corresponding to the Dataverse provider checksum representation without parsing scientific content.

For files whose parent metadata has `tabularData=true`, use Dataverse's documented saved-original route:

`/api/access/datafile/<FILE_ID>?format=original`

For non-tabular files, use the ordinary route:

`/api/access/datafile/<FILE_ID>`

No table, notebook or markdown content may be interpreted in this gate. The byte payloads are opaque inputs used only for size/checksum/provenance validation.

## Frozen dataset identity

- DOI: `10.7910/DVN/B4RITM`
- Dataverse release: `1.0`, `RELEASED`
- parent raw metadata SHA256: `50b0e1ed9d939d1a2b2f4e497dd3841c9c73eb8ecaa4a589268d3ba75ad3d0db`
- parent normalized inventory SHA256: `1cfc666849a7cf200ef4cdaf47b926e9ece44b63a92d4e29710c5a0cba441baa`

## Frozen representation contract

The exact 11-file set is frozen below. `saved-original` means the request must include `format=original`; `direct` means no format transformation is requested.

| file id | Dataverse archival name | representation | expected returned name | expected bytes | provider MD5 |
|---:|---|---|---|---:|---|
| 11646859 | `data.tab` | saved-original | `data.csv` | 4091 | `59d03738e7fe61fe06a06b2140708373` |
| 11674675 | `example.ipynb` | direct | `example.ipynb` | 231264 | `fd9ac548e6a6f136efb6c61058cc822f` |
| 11646858 | `hs_numu_cc.tab` | saved-original | `hs_numu_cc.csv` | 543795 | `d9cfa0e209bb82af43c78474765be5e3` |
| 11646854 | `hs_nu_nc_nue_cc.tab` | saved-original | `hs_nu_nc_nue_cc.csv` | 543327 | `75cffca2d2d099373c680a5f4088c195` |
| 11646853 | `hs_nutau_cc.tab` | saved-original | `hs_nutau_cc.csv` | 544770 | `cd3c6335d25d1163c5df30aaff50be2a` |
| 11646851 | `mc_mu.tab` | saved-original | `mc_mu.csv` | 5815 | `bc7133f3da6c1acf830a9e8d686bef4c` |
| 11646852 | `mc_nue_cc.tab` | saved-original | `mc_nue_cc.csv` | 6234527 | `2150abf034ed873b798dfa61cbe7ac78` |
| 11646856 | `mc_numu_cc.tab` | saved-original | `mc_numu_cc.csv` | 44626533 | `b60ccf0e0e447698d35b953a6e22552d` |
| 11646850 | `mc_nu_nc.tab` | saved-original | `mc_nu_nc.csv` | 3975602 | `fb5eac7230c1ab1b4e8b1f019ed33e2b` |
| 11646855 | `mc_nutau_cc.tab` | saved-original | `mc_nutau_cc.csv` | 7266105 | `cb62a96ed14491deef10bb8253a786ca` |
| 11674676 | `readme.md` | direct | `readme.md` | 7141 | `848778cd0b870da83a6b925b89ba3d3d` |

For every saved-original row the parent raw metadata additionally freezes:

- `tabularData=true`
- `originalFileFormat=text/csv`
- `originalFileName=<expected returned name>`
- `originalFileSize=<expected bytes>`

For `example.ipynb` and `readme.md`, `tabularData=false`.

## Frozen procedure

1. Re-fetch the B4RITM metadata endpoint.
2. Require DOI identity, release `1.0`, `RELEASED`, and exact equality of all 11 authority tuples including tabular/original representation fields.
3. Do not download any file if this metadata equality gate fails.
4. Retrieve the nine tabular assets through `?format=original` and the two non-tabular assets directly.
5. Treat each response as opaque bytes.
6. Require actual byte size to equal the frozen expected size.
7. Require actual MD5 to equal the frozen provider MD5.
8. Compute an independent SHA256 for every consumed payload.
9. Record request URL and resolved transport URL for provenance.
10. Upload only manifest/hash/stdout artifacts; never upload the experimental payloads themselves.
11. Discard payloads after hashing.

Transient HTTP 429/500/502/503/504 and network timeouts may receive at most four bounded retries. A retry cannot change DOI, file IDs, representation mode, checksums, sizes, thresholds, or any scientific rule.

## PASS contract

PASS requires all simultaneously:

- exact B4RITM identity and release 1.0;
- exact 11-file representation metadata match;
- exactly 9 saved-original and 2 direct retrievals;
- all 11 byte sizes match;
- all 11 provider MD5 values match;
- all 11 SHA256 values are present;
- no payload scientific content was parsed;
- QKL28Z was not substituted;
- observed residual remains locked;
- BSM interpretation remains locked.

PASS label:

`PASS_0105A4D_DEEPCORE_B4RITM_ORIGINAL_REPRESENTATION_BYTE_LOCK_NONDISCOVERY`

Metadata/checksum/size/representation mismatch:

`BLOCKED_0105A4D_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE`

Transport exhaustion:

`BLOCKED_0105A4D_TRANSPORT`

A PASS may authorize a separately preregistered DeepCore 3nu/null-reproduction gate. It does not authorize BSM residual analysis.
