# 0105a6p — Ar content-addressed exact-byte reconstruction transport gate

Status: **PREREGISTERED / TRANSPORT ONLY / NONDISCOVERY**

## Purpose

Recover the exact official COHERENT Ar release bytes needed by the 0105a6o Tier-B numerical reproduction without relying on the currently unstable Zenodo transport.

The scientific authority remains the historical official 0105a3 direct Zenodo byte lock. The frozen GitHub mirror is an **untrusted carrier only**.

## Frozen carrier

- repository: `Newtrinos-org/Newtrinos.jl`
- exact commit: `fa87689ddedae1929e33d66ad1f0efa1b7cce206`
- base directory: `src/experiments/coherent/coherent_2020/lAr`

No branch tip or newer carrier content is allowed.

## Exact official identities

The following identities come from the successful 0105a3 official direct-byte lock. A carrier candidate is accepted only if a deterministic reconstruction yields all three exact properties: byte length, MD5 and SHA256.

| file | bytes | MD5 | SHA256 |
|---|---:|---|---|
| `datanobkgsub.txt` | 15537 | `4346ec521e91a7227b2e34ff8f3c269b` | `dabf3d80f13959f4b94b77c9b56f7347a645105801e8cc177424e7ffcf7c7f66` |
| `cevnspdf.txt` | 18857 | `5601234e03bc9bbd01066591629e72c0` | `3b1d5b25749e8d8e1cfdf5c32e48f026ce4aafec0a80632b3a63273e6e0e1f37` |
| `brnpdf.txt` | 17304 | `7ccf0fdc0d0010d2c6570d620816e4df` | `02664ce6a84eca8c6146b6502497bc5d8165df945da132193622334ff4ff826f` |
| `delbrnpdf.txt` | 16116 | `5d57e91a773f03368d149dc5739b6a01` | `ebccca6c1650b0ace71fdbaade7a80ea289a99ff3c120266ae6ecf0083df5c63` |
| `bkgpdf.txt` | 21190 | `ccc2df245a004a644cd04317d07b35df` | `36c89291dde3032a19ca7a8e64510d036d7b40c34b0805ce475a13ccfa739dd1` |
| `LArParametersAnlA.yaml` | 4906 | `cc9f2c60ce0c17809453e0caad9c4a38` | `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e` |
| `brnpdf+1sigBRNTimingMean.txt` | 17304 | `edf00a561d1f934d3e8bef2c401e8d91` | `7f06099e1bba0d2e328555c61cb255bb290607a44202327d29eb3ae3e05c1cd5` |
| `brnpdf-1sigBRNTimingMean.txt` | 17295 | `937c7c0f53aff94600ed7dfffb69de8b` | `b5c1c8d0cb8b2319d093d38418da5ac2ccda59108755fb23e7f4a559cfe154f8` |
| `brnpdf+1sigEnergy.txt` | 17333 | `2ad879a7302d8ca2e25ef1e192f88183` | `fb6fdaf99c9941653d33e1a909d8000b81c1ee9bb8e8ad3bf31839561faf6661` |
| `brnpdf-1sigEnergy.txt` | 17302 | `ea7dd87225a19fe75f28d3dec00e7441` | `20bcad29e716f3fb0f1e9eeb8ffb049b4b3d8b3b3a150800b9c8711e2b177be6` |
| `brnpdfBRNTimingWidthSyst.txt` | 17375 | `5050ef987d122fae43eeef27b86ec1b2` | `304dba1553989d7c0cd3f745df9731a5306ec07ecc1044c20efbe2952707b270` |
| `cevnspdf+1sigF90.txt` | 18837 | `0237a293b243b371459bcb19bc2fa116` | `308f78e19b7fb3e54399dc29c207bd2a89b91825df5309d48068a3495e1c92e2` |
| `cevnspdf-1sigF90.txt` | 18870 | `b9bd9500b0c84b851f0d38e4869cad0f` | `b4e8071f87aa22a562e0c00654a0989915251acf2c7e569068b9b78c3ae5ac35` |
| `cevnspdfCEvNSTimingMeanSyst.txt` | 18877 | `24455c1cd2acf4f359cf0942deb7b29b` | `3170dafd4cf44df35bde0795e1245606d8144c05f3e50f015648c57bcdba97f5` |

## Frozen reconstruction family

For each carrier file, and only for that same filename, test exactly these byte candidates in order:

1. `identity`: raw carrier bytes unchanged;
2. `append_LF`: raw carrier bytes followed by exactly one byte `0x0A`;
3. `append_CRLF`: raw carrier bytes followed by exactly two bytes `0x0D 0x0A`.

No other transformation is allowed. In particular:

- no whitespace normalization;
- no line-ending conversion inside the file;
- no numeric reserialization;
- no column repair/reordering;
- no removal of bytes;
- no tolerance-based semantic equivalence.

A reconstruction is `ACCEPTED_AS_EXACT_OFFICIAL_BYTES` iff one candidate matches **exact official size + MD5 + SHA256 simultaneously**. Thus an appended line terminator is accepted only when its resulting full file is cryptographically identical to the previously observed official Zenodo bytes.

If more than one candidate somehow matches, classify BLOCKED because reconstruction would not be unique.

## Output

The hosted artifact may include:

- `manifest.json` recording carrier byte identity, selected reconstruction and exact official checks;
- only the reconstructed files that pass all official identities.

Carrier scientific authority remains zero even after successful reconstruction; authority transfers solely from exact equality to the 0105a3 official byte identities.

## Classification

Central numerical-input gate:

- `central_ready = true` only if all six central files pass exact reconstruction.

Systematic-excursion input gate:

- `systematics_ready = true` only if all eight systematic files pass exact reconstruction.

Overall classifications:

- `PASS_0105A6P_ALL_REQUIRED_ARGON_BYTES_RECONSTRUCTED_NONDISCOVERY` if all 14 pass;
- `PASS_0105A6P_CENTRAL_BYTES_RECONSTRUCTED_SYSTEMATICS_INCOMPLETE_NONDISCOVERY` if all six central pass but one or more systematic files do not;
- otherwise `BLOCKED_0105A6P_CENTRAL_EXACT_BYTE_RECONSTRUCTION_INCOMPLETE`.

Only `central_ready=true` may satisfy 0105a6o Stage 0 for the central/null numerical child gate.

## Hard ceilings

- no likelihood evaluation or fit;
- no observed residual;
- no BSM/model comparison;
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0` regardless of outcome.
