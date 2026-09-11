# 0105a5b R1m3 amendment 01 — fail-closed hosted classifier correction

Date: 2026-09-11
Parent preregistration: `research/prereg_0105a5b_r1m3_csms_b4ritm_mapping.md`.

## Trigger

Hosted execution `34617899333/103324284516`, artifact `10270512595`, produced a machine self-label PASS, but independent artifact validation against the already-frozen semantic contract showed that the lexical bucket implementation can count **negative/absence statements** as positive evidence. The authoritative scientific classification is therefore recorded separately as `BLOCKED_0105A5B_R1M3_CSMS_B4RITM_EXPERIMENTAL_MAPPING_INCOMPLETE` in `research/iterations/0105a5b_r1m3_csms_b4ritm_mapping_blocked_20260911.md`.

## Frozen correction before code changes

This amendment does not change, weaken, or add any scientific PASS criterion. It only makes the hosted implementation fail closed with respect to the original preregistration.

The corrected hosted script must:

1. continue to emit the complete mechanically selected frozen corpus inventory with SHA256;
2. continue to emit bounded semantic contexts needed for independent validation;
3. **not** promote lexical keyword/bucket presence to a scientific PASS;
4. emit only `EVIDENCE_BUNDLE_ONLY_0105A5B_R1M3_UNCLASSIFIED` for a complete successful hosted execution;
5. retain `INFRASTRUCTURE_FAIL_0105A5B_R1M3` only for genuine read/execution failure;
6. retain hard booleans showing no standard-3nu, no systematic MC, no observed residual and no network request.

Scientific PASS/BLOCKED classification remains an artifact-consumption step against the original five-element frozen contract. Existing run `34617899333` is not rerun to seek a different scientific outcome; any workflow execution caused by this correction is reproducibility/integrity evidence only.

The original R1m3 BLOCKED scientific result remains authoritative unless genuinely new independently provenance-qualified external authority is prospectively frozen in a new gate.
