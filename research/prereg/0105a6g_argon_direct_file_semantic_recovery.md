# 0105a6g — COHERENT Ar direct-file semantic recovery

Date: 2026-09-10
Gate: `NMIR-V2-0105A6G`
Parent: `BLOCKED_0105A6F_ARGON_AUTHORITY_BYTE_OR_TRANSPORT`
Stage: authority-preserving transport recovery + semantic evidence inventory only; NONDISCOVERY

## Purpose

Recover the exact official COHERENT Ar release bytes needed by 0105a6f without weakening or changing the scientific authority contract. The Zenodo record-metadata API returned HTTP 504 in three unchanged 0105a6f attempts, while 0105a3 had already byte-locked the same release successfully.

This gate therefore bypasses only the unstable metadata API. It does **not** change provider, record, release, filenames, bytes, hashes, semantic completion criteria, or analysis target.

## Frozen parent authority

The only admissible parent manifest is the exact 0105a3 artifact:

- workflow run: `34418207408`
- artifact ID: `10147580844`
- artifact name: `nmir-v2-0105a3-coherent-byte-lock`
- artifact ZIP SHA256: `b4d93c5e121ddbf503f9dd837fff1c356fd704342d48c5d243213ac599e26da4`
- normalized manifest filename: `coherent_zenodo_direct_byte_manifest.json`
- normalized manifest SHA256: `5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091`
- frozen Ar record: `3903810`, DOI `10.5281/zenodo.3903810`
- frozen Ar file count: 24

The hosted gate must retrieve this exact GitHub Actions artifact using the repository's authenticated Actions API, verify the ZIP SHA256 and manifest SHA256, and reject any mismatch before contacting Zenodo.

## Direct provider-byte rule

For each of the 24 Ar entries in the verified 0105a3 manifest, the gate may request only the recorded official `https://zenodo.org/records/3903810/files/...` URL.

For every file it must require exact equality to all frozen parent values:

- filename;
- byte size;
- provider MD5 recorded by 0105a3;
- independent SHA256 recorded by 0105a3.

No Zenodo metadata API call is needed or allowed for scientific acceptance. No mirror, secondary archive, reanalysis repository, filename substitution, redirect to another provider, hash repair, or partial-file acceptance is permitted.

## Frozen semantic extraction

After **all 24/24** direct provider files pass exact byte identity, the gate may decode text-like files and emit deterministic, line-numbered contexts for:

`likelihood`, `nll`, `roofit`, `profile`, `fit`, `constraint`, `correlation`, `covariance`, `systematic`, `uncertainty`, `normalization`, `background`, `cevns`, `brn`, `prompt`, `steady`, `f90`, `energy`, `time`, `pdf`, `parameter`, `efficiency`, `acceptance`, `yaml`.

It may also emit exact contents of small configuration/code files needed for independent semantic review when their SHA256 has first matched the parent manifest, especially:

- `LArParametersAnlA.yaml`;
- `readYAMLParameters.py`;
- `PlotExtractedData.C`;
- `CENNS10AnlAEfficiency.txt`.

Binary/PDF content is byte-verified but is not interpreted by this gate.

## Scientific classification rule

This recovery gate does not itself upgrade the 0105a6f F1-F7 fields. Its output classification is only one of:

- `PASS_0105A6G_ARGON_DIRECT_PROVIDER_BYTES_RECOVERED_NONDISCOVERY` if 24/24 direct files match the exact frozen parent manifest; or
- `BLOCKED_0105A6G_ARGON_DIRECT_PROVIDER_TRANSPORT_OR_BYTE_MISMATCH` otherwise.

Only after a byte PASS may a separate independent semantic review combine:

1. the exact 0105a6f arXiv-source evidence; and
2. the exact 0105a6g recovered release-file evidence

against the **unchanged** F1-F7 completion criteria frozen in 0105a6f.

## Authorization

No fit/minimization and no observed residual calculation are allowed.

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

A direct-byte recovery PASS is transport/authority progress, not a Standard-Model/null reproduction PASS and not evidence for BSM physics.
