# 0105a3 — COHERENT direct byte-lock transport block

Status: `BLOCKED_0105A3_TRANSPORT`

This record preserves the first hosted byte-lock failure. It is an infrastructure/transport block, not a scientific FAIL and not evidence about any neutrino model.

## Hosted execution

- Frozen implementation SHA: `6ab2b940be4431c6fd7cad8048e10764a88eb086`
- Workflow run: `34418207408`
- Job: `102687701257` (`byte-lock`)
- Deterministic byte-lock tests: `5 passed`
- Ordinary regression check on the same commit: success

The hosted job then attempted to fetch the prospectively frozen Zenodo release bytes. After four allowed attempts it terminated with:

`BLOCKED_0105A3_TRANSPORT attempts=4 url=https://zenodo.org/records/1228631/files/arrivalTimePDF_delayedNeutrinos.txt?download=1`

The failure was HTTP 504 Gateway Time-out from the Zenodo file endpoint.

## Classification

- frozen file inventory changed: **no**
- provider MD5 values changed: **no**
- scientific acceptance criteria changed: **no**
- observed event content parsed: **no**
- observed BSM residual executed: **no**

Therefore 0105a3 remains blocked rather than failed scientifically. The complete 37-file byte lock is not established by this run.

A later transport-only retry may reuse the exact frozen inventory/criteria. Any change of provider, record identity, file set, checksum predicate, or scientific criterion requires a new prospective amendment before execution.

Observed BSM residual permission remains `0%`.
