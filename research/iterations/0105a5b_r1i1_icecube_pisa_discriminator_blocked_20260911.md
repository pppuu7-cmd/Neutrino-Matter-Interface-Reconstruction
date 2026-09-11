# NMIR v2 0105a5b-R1i1 — IceCube-source PISA usage/version discriminator

Status: `BLOCKED_0105A5B_R1I1_PISA_REFERENCED_VERSION_NOT_UNIQUELY_DISCRIMINATED`

This is authority/provenance BLOCKED, not a standard-3nu scientific failure and not BSM evidence.

## Frozen provenance
- execution/workflow head: `8fdf5cc3b7f0e7a8f5f4e7fa9d3bc8e2c267e483`
- run/job/artifact: `34581353367 / 103205394469 / 10191727131`
- provider artifact digest: `sha256:26c43e1991c297e251b91ee8b5badeb1ed22ef240bb6be374cd51e3464c38c1d`
- independent downloaded ZIP SHA256: `26c43e1991c297e251b91ee8b5badeb1ed22ef240bb6be374cd51e3464c38c1d`
- inner `result.json` SHA256: `627f588b9c560d7c15acab3ea25f36cc946bb6c34a13e96867754cedd75e6485`

## Hosted result
The exact already-byte-locked IceCube `arXiv:2304.12236` source was required at SHA256 `111c41e49dd50880bc6b00aca95a2479216622b47235fcb68e2a02e22456a149`. Exactly the two preregistered byte-locked members were inspected:
- `main.tex`: `2c25f03bfadc482a81a8f490efd15df3481988485630f92a255bb3f3c4c3708e`
- `MyBibFile.bib`: `0055d6eb0585c44f2074b8f29712c38e1c645154d88830074fb7bff37b00e20c`

The frozen locator found two PISA occurrences but zero qualifying explicit references to any of the 18 frozen R1i tags:
- `main.tex` explicitly states that oscillation-probability computation is implemented in a custom Python code cited as `pisa`;
- `MyBibFile.bib` resolves citation `pisa` to the IceCube paper `Computational techniques for the analysis of small signals in high-statistics neutrino oscillation experiments`, arXiv `1803.05390`.

`matched_tags = []`; qualifying version matches = 0. Therefore the IceCube analysis establishes PISA usage but does not uniquely identify a PISA software tag under the prospectively frozen version forms. Version selection by publication date, release timing, compatibility, or output agreement remains prohibited.

## Consequence
R1d remains `BLOCKED_0105A5B_R1D_EXTERNAL_COMPUTATIONAL_AUTHORITY_INCOMPLETE`; standard DeepCore 3nu remains closed. The directly cited IceCube PISA methodology publication `arXiv:1803.05390` is an independently provenance-qualified next authority source, but its contents were not inspected by R1i1. Any use requires a new prospectively frozen gate beginning with byte acquisition only.

Observed BSM residual permission: 0%.
Systematic Monte Carlo execution permission: 0%.
