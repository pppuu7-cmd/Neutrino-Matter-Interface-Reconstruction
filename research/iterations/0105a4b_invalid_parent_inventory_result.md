# 0105a4b — invalid parent-inventory result

Status: `BLOCKED_0105A4B_INVALID_PARENT_INVENTORY_TRANSCRIPTION`

0105a4b was prospectively frozen and executed using a four-file `.pckl` inventory that was later found not to be the authoritative 0105a4 B4RITM artifact inventory. The original 0105a4 raw artifact contains 11 `.tab`/`.ipynb`/`.md` files with IDs in the `116468xx/116746xx` range.

## Hosted failure evidence

- workflow run: `34426972296`
- job: `102714173003`
- head SHA: `4b0ba83e51a8abbbbd006e1872856f2c47ec372f`
- deterministic tests: `5 passed`
- full repository regression on same SHA: success
- authority byte-lock: failure

All four frozen numeric IDs resolved through Harvard Dataverse to unrelated `.vec` payloads under `doi:10.7910/DVN/HDBMHV`, with sizes and MD5 values inconsistent with the 0105a4b preregistration. The workflow therefore correctly failed closed with:

`BLOCKED_0105A4B_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE`.

This is not a DeepCore physics failure and not a failure of B4RITM itself. It is a downstream provenance-construction error caused by an incorrect transcription of the parent 0105a4 artifact.

## Immutable disposition

- do not edit the executed 0105a4b preregistration to replace its file list;
- do not reuse any of its four file IDs, hashes or downloaded SHA256 values;
- do not treat the unrelated downloaded `.vec` bytes as IceCube data;
- preserve 0105a4b as a negative provenance/audit result;
- build any corrected byte lock as a new prospective gate from the exact 11-file raw 0105a4 artifact.

No binary DeepCore payload belonging to the correct B4RITM inventory was parsed by 0105a4b. Observed BSM residual permission remains `0%`.
