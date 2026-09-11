# 0105a6q5a3 — Argon historical byte-lock ↔ live Zenodo metadata crosswalk preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5A3`
Scope: checksum/name provenance crosswalk only; NONDISCOVERY. This gate is independent of q5a2 and may run in parallel.

## Frozen historical authority

Historical byte-lock run/job/artifact: `34418207408 / 102834981270 / 10147580844`.
Historical artifact ZIP SHA256: `b4d93c5e121ddbf503f9dd837fff1c356fd704342d48c5d243213ac599e26da4`.
Historical manifest SHA256: `5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091`.
Argon DOI/record: `10.5281/zenodo.3903810` / `3903810`.
Expected Argon inventory: exactly 24 files.

Frozen filename → provider-MD5 pairs:
- `bkgpdf.txt` — `ccc2df245a004a644cd04317d07b35df`
- `brnpdf+1sigBRNTimingMean.txt` — `edf00a561d1f934d3e8bef2c401e8d91`
- `brnpdf+1sigEnergy.txt` — `2ad879a7302d8ca2e25ef1e192f88183`
- `brnpdf-1sigBRNTimingMean.txt` — `937c7c0f53aff94600ed7dfffb69de8b`
- `brnpdf-1sigEnergy.txt` — `ea7dd87225a19fe75f28d3dec00e7441`
- `brnpdf.txt` — `7ccf0fdc0d0010d2c6570d620816e4df`
- `brnpdfBRNTimingWidthSyst.txt` — `5050ef987d122fae43eeef27b86ec1b2`
- `CENNS10AnlAEfficiency.txt` — `77139f1bb79dcf972a3a0ecc28a4a8f5`
- `CENNS10DataReleaseCompanion.pdf` — `f0f67a11113f5d60c84421bb76e37728`
- `cevnspdf+1sigF90.txt` — `0237a293b243b371459bcb19bc2fa116`
- `cevnspdf-1sigF90.txt` — `b9bd9500b0c84b851f0d38e4869cad0f`
- `cevnspdf.txt` — `5601234e03bc9bbd01066591629e72c0`
- `cevnspdfCEvNSTimingMeanSyst.txt` — `24455c1cd2acf4f359cf0942deb7b29b`
- `datanobkgsub.txt` — `4346ec521e91a7227b2e34ff8f3c269b`
- `delbrnpdf.txt` — `5d57e91a773f03368d149dc5739b6a01`
- `energydata1d.txt` — `fb4122f9309e16df39de4d3f3224af56`
- `f90data1d.txt` — `4fa866380574a7d70f719ffcbab11806`
- `LArParametersAnlA.yaml` — `cc9f2c60ce0c17809453e0caad9c4a38`
- `PlotExtractedData.C` — `1161762465460efdda35d4494a0d8547`
- `readYAMLParameters.py` — `708becd2d56cec1c2e672038581b8c7c`
- `systerrors1denergy.txt` — `d933e52f2c0dd8987e3535640194065f`
- `systerrors1dpsd.txt` — `2d0cb7ca23e3b0a3edfd2f0cb0e9d5dd`
- `systerrors1dtime.txt` — `98c920d71497cfa8b35bbd18fc8975c3`
- `timingdata1d.txt` — `a467365800489d105f7305a38751c9e5`

## Prospective question

Does the current Zenodo metadata endpoint for record 3903810 expose exactly the same 24 filename/checksum pairs as the frozen 0105a3 byte-lock authority, without downloading any release-file payload?

## Frozen transport and extraction

Only Zenodo record metadata endpoint `https://zenodo.org/api/records/3903810` may be requested, with same-provider redirects only.
Parse record id, DOI, version, file count, and for each file only the filename/key and checksum string.
Normalize a checksum only by stripping an optional `md5:` prefix and lowercasing hexadecimal characters.
Do not request any file link. Do not inspect descriptions, scientific text, PDFs, code, tables, plots, or file contents.

## Frozen predicates

- record id is exactly `3903810`;
- DOI is exactly `10.5281/zenodo.3903810`;
- file count is exactly 24;
- every current file has an MD5 checksum;
- the set of 24 `(filename, md5)` pairs is exactly equal to the frozen historical set above;
- no duplicate filename is permitted.

## Frozen terminal classes

- `PASS_0105A6Q5A3_ARGON_ZENODO_METADATA_EXACTLY_MATCHES_FROZEN_BYTE_LOCK_NONDISCOVERY` iff every predicate passes.
- `BLOCKED_0105A6Q5A3_ZENODO_METADATA_TRANSPORT_FAILURE`.
- `BLOCKED_0105A6Q5A3_ZENODO_RECORD_IDENTITY_FAILURE`.
- `BLOCKED_0105A6Q5A3_ZENODO_INVENTORY_DRIFT`.
- `BLOCKED_0105A6Q5A3_ZENODO_FILENAME_MD5_CROSSWALK_DRIFT`.

PASS is provenance-only. It does not authorize q5b scientific-content inspection, pseudo-data generation, likelihood evaluation, nuisance profiling, systematic MC, observed residual analysis, or BSM fitting.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`
