# 0105a4 authority inventory erratum — 2026-09-10

Status: `ERRATUM_0105A4_RESULT_NOTE_TRANSCRIPTION`

This erratum corrects the later human-written result note for 0105a4. The hosted 0105a4 artifact itself was correct; the error occurred when its contents were transcribed into `research/iterations/0105a4_deepcore_b4ritm_authority_inventory_result.md`.

## Authoritative hosted artifact

- dataset: `doi:10.7910/DVN/B4RITM`
- Dataverse release: version `1.0` (`versionNumber=1`, `versionMinorNumber=0`, `RELEASED`)
- workflow run: `34418458353`
- job: `102688456198`
- head SHA: `abde96ad8226dbf2e426b92093efa5b4df8e55dc`
- artifact ID: `10129986472`
- artifact digest: `sha256:9eb6259647f7479e1b05a5c1a841737a5a577f454575fc9eb2484dd44a9f132b`
- raw Dataverse metadata SHA256: `50b0e1ed9d939d1a2b2f4e497dd3841c9c73eb8ecaa4a589268d3ba75ad3d0db`
- normalized inventory SHA256: `1cfc666849a7cf200ef4cdaf47b926e9ece44b63a92d4e29710c5a0cba441baa`
- authoritative file count: **11**, not 4.

The raw artifact records these exact 11 files:

| ID | file | bytes | provider MD5 |
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

The four `.pckl` files and IDs `6660755`–`6660758` written into the later result note are **not** part of the authoritative 0105a4 artifact and must not be used for NMIR v2.

## Classification

The hosted 0105a4 result remains:

`PASS_0105A4_DEEPCORE_B4RITM_AUTHORITY_INVENTORY_NONTERMINAL`

because the original artifact correctly pinned the DOI, released version and full 11-file inventory. However, the later result-note transcription is superseded by this erratum for all downstream work.

The already executed 0105a4b preflight was built from the incorrect four-file transcription and is therefore invalid as a descendant authority gate. Its failure must be preserved separately and cannot be repaired by changing its frozen inventory post hoc.

Observed BSM residual permission remains `0%`.
