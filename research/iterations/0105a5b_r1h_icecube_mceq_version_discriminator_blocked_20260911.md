# NMIR v2 0105a5b-R1h — IceCube-source MCEq version discriminator

Status: `BLOCKED_0105A5B_R1H_ICECUBE_MCEQ_VERSION_NOT_UNIQUELY_DISCRIMINATED`

This is an authority/provenance BLOCKED result, not a scientific failure of standard 3nu and not BSM evidence.

## Frozen provenance
- preregistration commit: `8902b56076f97ce202f35307a049ab0c64e98b2d`
- implementation commit: `a8aa8e71f5b1a3c942e18441c2b5043992110d62`
- guards commit: `6490a7f2a1b8109594ddb712cbc4506b3d4e2429`
- execution/workflow head: `d3cc8ec290a61610f05e3f9f3712987026595e13`
- run: `34580484191`
- job: `103202635694`
- artifact: `10191385866`
- provider artifact digest: `sha256:8487ba05b236063b370de76d4497d1af10d42fa69e56561b67de512f09c97cc1`
- independently downloaded ZIP SHA256: `8487ba05b236063b370de76d4497d1af10d42fa69e56561b67de512f09c97cc1`
- inner `result.json` SHA256: `3da29b55bfb460305d7aaa13a03f66a5431c841f294a50ee0c66e3027d69776f`

## Hosted result
The exact IceCube source bundle `https://export.arxiv.org/e-print/2304.12236` was acquired as `1532133` bytes with SHA256 `111c41e49dd50880bc6b00aca95a2479216622b47235fcb68e2a02e22456a149`.

The prospectively frozen text-member set contained:
- `main.tex`: 206990 bytes, SHA256 `2c25f03bfadc482a81a8f490efd15df3481988485630f92a255bb3f3c4c3708e`
- `MyBibFile.bib`: 46740 bytes, SHA256 `0055d6eb0585c44f2074b8f29712c38e1c645154d88830074fb7bff37b00e20c`

Against the unchanged complete 11-candidate R1g lineage, the frozen locator returned:
- `matched_candidates = []`
- `matches = []`

Therefore the IceCube publication source does not uniquely discriminate an MCEq release state under the preregistered rule. No candidate may be selected by output agreement or post-hoc source inspection.

## Prohibitions verified
- MCEq implementation inspected: false
- standard 3nu executed: false
- systematic Monte Carlo executed: false
- observed BSM residual inspected: false
- observed BSM residual permission: 0%
- systematic Monte Carlo execution permission: 0%

## Consequence
`BLOCKED_0105A5B_R1D_EXTERNAL_COMPUTATIONAL_AUTHORITY_INCOMPLETE` remains authoritative. R1h does not authorize MCEq implementation inspection or DeepCore 3nu reproduction. The exact MCEq-version-discriminator route is exhausted unless a separately provenance-qualified external provider explicitly names a release/tag/commit.
