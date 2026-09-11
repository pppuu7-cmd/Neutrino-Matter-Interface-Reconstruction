# 0105a6q5c — Argon official semantic four-file byte-lock preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5C`
Scope: official Zenodo direct transport + exact byte identity only; NONDISCOVERY.

## Parent authorization

Parent q5b validated class: `PASS_0105A6Q5B_ARGON_OFFICIAL_SEMANTIC_FILE_CANDIDATES_LOCATED_NONDISCOVERY`, record commit `dcafed65cf9cbce3d8d87329425bf75e1c68b209`. q5b returned exactly four candidates; this gate freezes the complete set before any direct file download.

## Frozen expected identities

All four files must be downloaded only from the exact Zenodo API self links returned by q5b and must simultaneously satisfy exact size + provider MD5 + previously recorded 0105a3 SHA256:

- `CENNS10AnlAEfficiency.txt`: URL `https://zenodo.org/api/records/3903810/files/CENNS10AnlAEfficiency.txt/content`; size `1804`; MD5 `77139f1bb79dcf972a3a0ecc28a4a8f5`; SHA256 `21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2`.
- `readYAMLParameters.py`: URL `https://zenodo.org/api/records/3903810/files/readYAMLParameters.py/content`; size `1814`; MD5 `708becd2d56cec1c2e672038581b8c7c`; SHA256 `3f1660c54987b9d87f47eda2d19306c2fd061ada72cfb7d3857d996164dd3cd6`.
- `PlotExtractedData.C`: URL `https://zenodo.org/api/records/3903810/files/PlotExtractedData.C/content`; size `14020`; MD5 `1161762465460efdda35d4494a0d8547`; SHA256 `c669946d425148fab271d97f99d079b83dbd8f060fea3dd57ac7e00ebecf7d5f`.
- `LArParametersAnlA.yaml`: URL `https://zenodo.org/api/records/3903810/files/LArParametersAnlA.yaml/content`; size `4906`; MD5 `cc9f2c60ce0c17809453e0caad9c4a38`; SHA256 `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`.

No normalization, newline conversion, reconstruction, alternate carrier or semantic substitution is allowed. Redirects must remain within `zenodo.org`.

## Frozen terminal classes

- `PASS_0105A6Q5C_ARGON_OFFICIAL_FOUR_SEMANTIC_FILES_BYTE_LOCKED_NONDISCOVERY` iff all four exact URL fetches succeed and each exact size+MD5+SHA256 matches.
- `BLOCKED_0105A6Q5C_ZENODO_DIRECT_TRANSPORT_FAILURE` if any direct fetch fails under the frozen transport rule.
- `FAIL_0105A6Q5C_OFFICIAL_BYTE_IDENTITY_MISMATCH` if transport succeeds but any fetched payload disagrees with a frozen identity.

A PASS permits only a separately prospectively preregistered semantic audit over all four exact bytes. It does not by itself close F1/F4/F6/F7, authorize systematic MC, or authorize observed residual fitting.

Artifact must retain per-file requested/final URL, HTTP status, byte count, MD5, SHA256, exact-match booleans and classification, but not file contents.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`