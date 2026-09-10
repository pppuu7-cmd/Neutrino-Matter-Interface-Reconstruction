# 0105a6p — Ar content-addressed exact-byte reconstruction transport

Date: 2026-09-10
Classification: **PASS_0105A6P_ALL_REQUIRED_ARGON_BYTES_RECONSTRUCTED_NONDISCOVERY**

## Frozen provenance

- preregistration commit: `2a48003cc83349820d40fc0c4076850a2a8efef3`
- execution head: `03f26eadf13b3f09532240bba323b9a48a2014aa`
- run/job: `34498465808/102942870228`
- dedicated guards: `6 passed`
- artifact: `10160794369`, `nmir-v2-0105a6p-argon-exact-official-byte-reconstruction`
- artifact ZIP SHA256: `a66b3408b22b14575f156c0be7c389589dd9865ada1f4769fe8366a1df65ec82`
- inner `manifest.json` SHA256: `5b1df47a50dd4dbb2a7fbd5ee64346c2854bdbad0540bfa6f16637eb10b6bada`

## Carrier and authority separation

Frozen untrusted carrier:

- `Newtrinos-org/Newtrinos.jl`
- commit `fa87689ddedae1929e33d66ad1f0efa1b7cce206`
- `src/experiments/coherent/coherent_2020/lAr`

Scientific authority remains the successful 0105a3 direct official COHERENT Zenodo byte lock. The carrier contributed no scientific authority. Each reconstructed file was accepted only after exact simultaneous equality to its pre-existing official byte length, MD5 and SHA256.

## Result

All **14/14** prospectively frozen files were reconstructed as exact official bytes.

Central files (`6/6`):

- `datanobkgsub.txt`: `append_LF` — carrier 15536 bytes -> exact official 15537 bytes;
- `cevnspdf.txt`: `identity`;
- `brnpdf.txt`: `identity`;
- `delbrnpdf.txt`: `identity`;
- `bkgpdf.txt`: `append_LF` — carrier 21189 bytes -> exact official 21190 bytes;
- `LArParametersAnlA.yaml`: `identity`.

Systematic excursion files (`8/8`):

- `brnpdf+1sigBRNTimingMean.txt`: `identity`;
- `brnpdf-1sigBRNTimingMean.txt`: `identity`;
- `brnpdf+1sigEnergy.txt`: `identity`;
- `brnpdf-1sigEnergy.txt`: `identity`;
- `brnpdfBRNTimingWidthSyst.txt`: `identity`;
- `cevnspdf+1sigF90.txt`: `identity`;
- `cevnspdf-1sigF90.txt`: `identity`;
- `cevnspdfCEvNSTimingMeanSyst.txt`: `identity`.

For the two reconstructed-LF cases, the line terminator was not inferred semantically. The prospectively frozen transformation family was `{identity, append_LF, append_CRLF}`, and only `append_LF` yielded the exact historical official size+MD5+SHA256. Therefore the artifact bytes are cryptographically identical to the official 0105a3 observations.

## Permissions

- `central_ready = true`
- `systematics_ready = true`
- `A6O_STAGE0_CENTRAL_INPUT_PERMISSION_PERCENT = 100`
- likelihood evaluation performed: **false**
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`

This PASS authorizes execution of the already-preregistered 0105a6o Tier-B central/null reproduction, subject to all frozen structural, numerical, publication-target and dual-anchor gates. It does not authorize BSM residual inspection.
