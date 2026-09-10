# 0105a6h — Ar content-addressed semantic-file recovery

Date: 2026-09-10
Gate: `NMIR-V2-0105A6H`
Parent: `BLOCKED_0105A6G_ARGON_DIRECT_PROVIDER_TRANSPORT_OR_BYTE_MISMATCH`
Stage: content-addressed transport recovery only; NONDISCOVERY

## Rationale

0105a6f and 0105a6g established a contemporaneous Zenodo transport outage affecting both metadata and direct file delivery. 0105a3 nevertheless already froze authoritative official Zenodo hashes for all Ar files.

A public repository contains files with the same release filenames. It is **not** treated as scientific authority. This gate tests it only as an untrusted byte carrier: a recovered file is admissible iff its bytes exactly equal the already-authoritative 0105a3 SHA256, provider MD5 and size.

## Frozen untrusted transport source

Repository: `Newtrinos-org/Newtrinos.jl`
Commit: `fa87689ddedae1929e33d66ad1f0efa1b7cce206`
Directory: `src/experiments/coherent/coherent_2020/lAr`

No other commit, branch tip, mirror, or path is admissible in this gate.

## Frozen official parent identity

0105a3 normalized manifest SHA256:
`5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091`

Official record: `3903810`, DOI `10.5281/zenodo.3903810`.

The four requested semantic files and their official identities are:

1. `LArParametersAnlA.yaml`
   - size 4906
   - MD5 `cc9f2c60ce0c17809453e0caad9c4a38`
   - SHA256 `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`
2. `readYAMLParameters.py`
   - size 1814
   - MD5 `708becd2d56cec1c2e672038581b8c7c`
   - SHA256 `3f1660c54987b9d87f47eda2d19306c2fd061ada72cfb7d3857d996164dd3cd6`
3. `PlotExtractedData.C`
   - size 14020
   - MD5 `1161762465460efdda35d4494a0d8547`
   - SHA256 `c669946d425148fab271d97f99d079b83dbd8f060fea3dd57ac7e00ebecf7d5f`
4. `CENNS10AnlAEfficiency.txt`
   - size 1804
   - MD5 `77139f1bb79dcf972a3a0ecc28a4a8f5`
   - SHA256 `21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2`

## Acceptance rule

For each named file independently:

`ACCEPTED_AS_OFFICIAL_BYTE_EQUIVALENT` iff raw bytes from the frozen mirror commit have exact size + MD5 + SHA256 equality to 0105a3.

Otherwise:

`REJECTED_NOT_BYTE_EQUIVALENT`.

No newline normalization, decoding/re-encoding, whitespace repair, parser-based equivalence, numeric tolerance, or semantic similarity is allowed before hashing.

The overall gate passes only if all four files are byte-equivalent:

`PASS_0105A6H_FOUR_SEMANTIC_FILES_BYTE_EQUIVALENT_NONDISCOVERY`.

If any differs:

`BLOCKED_0105A6H_SEMANTIC_FILE_BYTE_EQUIVALENCE_INCOMPLETE`.

## Semantic use after hash acceptance

Only a file classified `ACCEPTED_AS_OFFICIAL_BYTE_EQUIVALENT` may be read semantically. Because byte identity is exact, scientific authority remains the original official 0105a3 Zenodo lock; the mirror contributes transport only.

The gate may emit line-numbered/full-text evidence for accepted small files, but may not classify F1-F7, run a fit, or inspect an observed residual.

## Authorization

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`
