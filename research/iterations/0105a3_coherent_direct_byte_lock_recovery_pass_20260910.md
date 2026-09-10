# 0105a3 — COHERENT direct byte-lock recovery PASS

Date: 2026-09-10
Gate: `NMIR-V2-0105A3`
Classification: `PASS_0105A3_COHERENT_ZENODO_DIRECT_BYTE_LOCK_NONTERMINAL`

## Purpose

Record the authority-preserving recovery of the prospectively frozen COHERENT direct-byte lock after the earlier hosted transport-only block. This record supersedes the *current classification* of the transport block, but does not erase the historical blocked run.

## Frozen scientific implementation

- implementation/execution SHA: `6ab2b940be4431c6fd7cad8048e10764a88eb086`
- preregistration: `research/prereg/0105a3_coherent_zenodo_direct_byte_lock_preflight.md`
- CsI Zenodo record: `1228631`, DOI `10.5281/zenodo.1228631`, frozen version `1.0`, 13 files
- Ar Zenodo record: `3903810`, DOI `10.5281/zenodo.3903810`, frozen version `1.0`, 24 files
- total frozen file count: 37

No provider, record identity, filename inventory, provider-MD5 predicate, discovery rule, or scientific acceptance criterion was changed for the successful retry.

A repository comparison from execution SHA `6ab2b940...` to the then-current branch tip `806fde758e175e62f0fee8666372c18f45cae1c8` showed 61 subsequent commits but no modifications to the 0105a3 preregistration, workflow, script, or tests. The successful rerun therefore evaluates the same frozen 0105a3 contract.

## Successful hosted execution

- workflow run: `34418207408`
- successful run attempt: `3`
- job: `102834981270` (`byte-lock`)
- deterministic tests: `5 passed`
- workflow conclusion: `success`
- uploaded artifact: `10147580844`, `nmir-v2-0105a3-coherent-byte-lock`
- artifact ZIP SHA256 reported by GitHub Actions: `b4d93c5e121ddbf503f9dd837fff1c356fd704342d48c5d243213ac599e26da4`
- normalized byte-manifest SHA256: `5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091`

## Frozen validation result

All required 0105a3 gates passed:

- `frozen_inventory_valid = true`
- `exact_total_file_count_37 = true`
- `all_provider_md5_match = true`
- `all_sha256_recorded = true`
- `observed_residual_execution_remains_locked = true`
- `coherent_event_byte_lock_complete = true`

Release split:

- CsI: 13/13 files successfully retrieved from the frozen Zenodo record and provider-MD5 verified;
- Ar: 24/24 files successfully retrieved from the frozen Zenodo record and provider-MD5 verified.

The successful manifest records independent SHA256 values and byte sizes for every frozen file.

## Relation to the historical block

The earlier hosted execution failed on the first CsI byte with repeated `HTTP 504 Gateway Time-out` responses. Its correct historical classification remains `BLOCKED_0105A3_TRANSPORT`; that record is retained as provenance.

Because the exact same frozen job later completed without any scientific-contract change, the previous 504 is resolved as a transient transport/provider failure rather than evidence of a missing/changed COHERENT release or a physics failure.

## Discovery guard

This PASS closes **only** the COHERENT event-release byte-authority subgate.

It does not authorize:

- inspection for a BSM residual;
- residual-basis selection from observed data;
- a model-family fit;
- cross-experiment significance combination;
- a discovery claim.

`observed_residual_execution_allowed = false`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

The parent 0105 authority/null/nuisance ladder remains controlling.

## Next authority-preserving front

With the COHERENT transport block removed, the next work must remain pre-discovery. Two admissible fronts remain:

1. determine whether the now byte-locked COHERENT releases contain sufficient exact likelihood/response/nuisance semantics to prospectively preregister and independently reproduce the Standard-Model CEvNS null without inspecting a BSM residual; and
2. for DeepCore, create a new prospective external-authority acquisition gate if attempting to recover the exact seven released nuisance-direction transformations left unresolved by terminal-blocked R1d.

No observed residual execution is authorized until the relevant parent gates independently PASS.
