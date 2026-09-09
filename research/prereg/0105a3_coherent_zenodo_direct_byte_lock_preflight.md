# 0105a3 — direct Zenodo event-release byte-lock preflight

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105A3
State: ACTIVE_PREREGISTRATION_ONLY
Parent: `research/prereg/0105_v2_model_agnostic_bsm_residual_reconstruction.md`
Dependencies: 0105a2 official collaboration->Zenodo route PASS; 0105a1 REST metadata transport remains blocked.

## Purpose

Recover file-level immutability for the two preregistered COHERENT CEvNS event releases without changing authority provider. The official COHERENT/ORNL release page points to Zenodo records `1228631` and `3903810`; their Zenodo landing pages publish the release version, file inventory, and provider MD5 checksums.

0105a3 freezes that landing-page inventory before any direct file-byte fetch. It then downloads the exact named files from the **same Zenodo records**, verifies every provider MD5, and computes independent SHA256 values over the retrieved bytes.

No file content may be parsed as event data in this gate. Bytes are opaque hashing inputs only.

## Frozen record identities

### CsI CEvNS event release

- record: `1228631`
- DOI: `10.5281/zenodo.1228631`
- landing-page version: `1.0`
- expected files: 13

Provider-MD5 inventory frozen from the Zenodo landing page:

- `arrivalTimePDF_delayedNeutrinos.txt` — `fd5d053696ba30164cd3711b38b8eaa5`
- `arrivalTimePDF_promptNeutrinos.txt` — `d5009119454ec8ed3b5a31bf8d1e82e5`
- `arrivalTimePDF_promptNeutrons.txt` — `400d86635b180b52e51b429ec5fe5965`
- `coherent_parameters.yaml` — `66b907201dcd7cccfb9af0a1b35893a7`
- `coherentCollaboration_dataReleaseCompanion_april2018.pdf` — `0cb94c4e8fa3c03a1d4bb0cd8599d318`
- `data_anticoincidence_beamOff.txt` — `c6371164b444b9357e004299c591546a`
- `data_anticoincidence_beamOn.txt` — `4067e588ff44d0a210655eacb987e2d7`
- `data_coincidence_beamOff.txt` — `529e822eb3a144170cd03d9d9628b4fa`
- `data_coincidence_beamOn.txt` — `23f399e605e94401a611c23c37090a31`
- `promptPDF.txt` — `faf1a4b6b27cd9fa685e17ddd38a00cf`
- `qfData_chicago.txt` — `b9dec892fb9d6c7502ed03446ddd0305`
- `qfData_tunl.txt` — `93b016293c04c741c3088bced0a5c015`
- `README` — `40cbf0bcdb370530526b7e293480ab9d`

### Ar CEvNS event release

- record: `3903810`
- DOI: `10.5281/zenodo.3903810`
- landing-page version: `1.0`
- expected files: 24

Provider-MD5 inventory frozen from the Zenodo landing page:

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

## Frozen transport route

For each file, use the current Zenodo record file endpoint under

`https://zenodo.org/records/{record_id}/files/{urlencoded_filename}?download=1`

Redirects within Zenodo/CERN object delivery are allowed as transport only. No third-party mirror is allowed.

Transient retry is allowed only for 429, 5xx, timeout, or temporary network errors. Provider MD5 mismatch, missing file, 403/404, wrong record identity, or an unexpected frozen filename is fail-closed.

## Frozen validation

For every one of the 37 files:

1. download opaque bytes;
2. record exact byte size;
3. calculate MD5 and require exact equality with the frozen Zenodo landing-page MD5;
4. calculate SHA256 over the same bytes;
5. record resolved final URL host for transport audit;
6. do **not** parse, summarize, histogram, fit, or inspect file contents.

The normalized manifest must also include a deterministic SHA256 over the sorted manifest representation.

## Discovery guard

Even a complete PASS here does not authorize an observed residual scan by itself. It closes only the COHERENT event-release **byte authority** sub-gate. DeepCore authority, likelihood semantics, nuisance implementation, SM null reproduction, and the parent 0105 execution lock remain independent requirements.

Set:

- `coherent_event_byte_lock_complete=true` only if all 37 provider MD5 checks pass and all SHA256 values are recorded;
- `observed_residual_execution_allowed=false` unconditionally in 0105a3.

## Allowed result

PASS:

`PASS_0105A3_COHERENT_ZENODO_DIRECT_BYTE_LOCK_NONTERMINAL`

Otherwise:

`BLOCKED_0105A3_COHERENT_ZENODO_BYTE_LOCK_INCOMPLETE`.
