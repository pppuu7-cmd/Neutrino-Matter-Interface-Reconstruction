# 0105a6q5b — validated Argon official semantic-file locator

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5B`
Classification: `PASS_0105A6Q5B_ARGON_OFFICIAL_SEMANTIC_FILE_CANDIDATES_LOCATED_NONDISCOVERY`
Scope: official Zenodo metadata-only locator; NONDISCOVERY.

## Prospective chain

- parent q5a2 record commit: `c7290228641ba8a8b6363481e98f49aa2a6081e1`
- preregistration: `8fb5121c97918b726a95f3440a1f15b5457c751d`
- implementation: `7ac95d444a01a84c8ee95efc8ea3c52e648c8e9a`
- guards: `d41921e2699b798cabd88bdccb28ab07813e2d11`
- execution head: `476e8b74ba19cba098a6c604188f92a98b98062e`

## Hosted validation

- run/job/artifact: `34548230167/103105373901/10179807293`
- dedicated guards: `6 passed`
- provider artifact ZIP SHA256: `01d42376bd95006de11d09cb39411ddfb7b9871d495a17dd8f34f85fc4c85236`
- independently downloaded ZIP SHA256: `01d42376bd95006de11d09cb39411ddfb7b9871d495a17dd8f34f85fc4c85236`
- independent inner `result.json` SHA256: `a4952c906ab7bbd513b0fafa661078ab3cfa181575bb5aeaaf48bf1cd7a22444`

Green CI was not treated as scientific PASS; raw job and artifact bytes were validated against the frozen gate.

## Complete returned candidate set

The frozen metadata-only selection returned exactly four candidates; all four are retained with no ranking or post-hoc subset:

1. `CENNS10AnlAEfficiency.txt`, size `1804`, provider checksum `md5:77139f1bb79dcf972a3a0ecc28a4a8f5`, official metadata link `https://zenodo.org/api/records/3903810/files/CENNS10AnlAEfficiency.txt/content`.
2. `readYAMLParameters.py`, size `1814`, provider checksum `md5:708becd2d56cec1c2e672038581b8c7c`, official metadata link `https://zenodo.org/api/records/3903810/files/readYAMLParameters.py/content`.
3. `PlotExtractedData.C`, size `14020`, provider checksum `md5:1161762465460efdda35d4494a0d8547`, official metadata link `https://zenodo.org/api/records/3903810/files/PlotExtractedData.C/content`.
4. `LArParametersAnlA.yaml`, size `4906`, provider checksum `md5:cc9f2c60ce0c17809453e0caad9c4a38`, official metadata link `https://zenodo.org/api/records/3903810/files/LArParametersAnlA.yaml/content`.

q5b followed none of these links and inspected no release-file content. No pseudo-data, likelihood, systematics fit or observed residual was evaluated.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact next allowed action

A new prospective gate may attempt official Zenodo direct byte acquisition of the complete four-file set. It must freeze all expected size/provider-MD5/0105a3-SHA256 identities before download and accept only exact byte equality. Semantic inspection remains a later separately preregistered step.