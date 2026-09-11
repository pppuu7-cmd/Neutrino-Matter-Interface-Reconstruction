# NMIR v2 0105a6q4fs1 — validated result

Date recorded: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`

Classification: `PASS_0105A6Q4FS1_IUSCHOLARWORKS_METADATA_ENDPOINT_CONTRACT_VALIDATED_NONDISCOVERY`.

This is transport/API-contract authority only. It is NONDISCOVERY and does not resolve COHERENT F1/F7.

## Frozen gate provenance

- preregistration commit: `31bb1aaf7e889fa8e36550c7635f331568f5c0aa`
- execution head: `45275e44fc7096a78944657786cb1892d75ee5ce`
- workflow run: `34559527681`
- job: `103139213700`
- artifact: `10183803724`
- provider artifact digest: `sha256:f53e3702174917aee32e5673e6edce6a8e47af1c5546f59eeb4f738a75f52bf5`
- independently downloaded ZIP SHA256: `f53e3702174917aee32e5673e6edce6a8e47af1c5546f59eeb4f738a75f52bf5`
- independent inner `result.json` SHA256: `9fc4fe96633d280660f9316b32256a7a617d645d2c4b12e0ad7e22a1dcd33018`
- dedicated guards: 4 passed

## Frozen sentinel result

Endpoint: `https://scholarworks.iu.edu/iuswrrest/api/discover/search/objects`.

The exact frozen sentinel request completed HTTP 200 with `application/json;charset=UTF-8`; response length `3043` bytes; response SHA256 `297e2bd912a56da273687301b748d7fa1486b5810e9839abab5f27fd200cf87c`. The payload was parseable JSON and exposed HAL/discovery structure (`_embedded`, `_links`; embedded relations `facets`, `searchResult`).

The hosted result records `target_specific_search_executed=false`, `item_links_followed=false`, `pdf_downloaded=false`, `pdf_content_inspected=false`, `likelihood_evaluated=false`, `pseudo_data_generated=false`, `systematic_monte_carlo_executed=false`, and `observed_bsm_residual_inspected=false`.

## Authorization consequence

q4fs1 PASS authorizes only a separately prospectively preregistered metadata-only target locator using the frozen endpoint and only the standard `query` and `size` keys. It does not authorize item-link following, UUID inference, bitstream/PDF acquisition, dissertation scientific-text inspection, systematic Monte Carlo, observed residual construction, BSM fitting, significance claims, or generic Wilks thresholds.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
