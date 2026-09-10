# 0105a6g — Ar direct-provider semantic recovery: transport BLOCKED

Date: 2026-09-10
Gate: `NMIR-V2-0105A6G`
Classification: `BLOCKED_0105A6G_ARGON_DIRECT_PROVIDER_TRANSPORT_OR_BYTE_MISMATCH`
Scope: authority-preserving transport recovery only; NONDISCOVERY.

## Frozen gate

Execution head: `86b29f01e6e9589aa886e04231f87fac99c866b4`
Preregistration: `research/prereg/0105a6g_argon_direct_file_semantic_recovery.md`

## Hosted evidence

- workflow run/job: `34488843078 / 102909985110`
- deterministic guards: `5 passed`
- infrastructure workflow conclusion: `success`
- artifact: `10156914601`, `nmir-v2-0105a6g-argon-direct-semantic-recovery`
- artifact ZIP SHA256: `51e6dfae1cccbaac9f77489ea7889fb61da8615e4ecc06aa491032b076878ab4`
- result JSON SHA256: `a9086dd1d5688016bcd908a3524b6b26ea9eb630882d5dd2ffa6bd6f57ac1c8d`

## Parent authority verification PASS

The gate first recovered the exact historical 0105a3 artifact and verified:

- artifact ZIP SHA256 `b4d93c5e121ddbf503f9dd837fff1c356fd704342d48c5d243213ac599e26da4`;
- normalized manifest SHA256 `5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091`;
- frozen Ar record `3903810`, 24 official files.

Both checksum checks passed before any provider fetch.

## Direct-provider transport result

The next step requested only the exact official per-file Zenodo URLs already recorded in the verified 0105a3 manifest. The fetch returned:

`HTTPError: HTTP Error 504: Gateway Time-out`

The script therefore emitted:

`BLOCKED_0105A6G_ARGON_DIRECT_PROVIDER_TRANSPORT_OR_BYTE_MISMATCH`

Because the failure occurred before a complete 24-file audit, no partial subset is promoted to semantic authority and no F1-F7 field is upgraded by this run.

This establishes that the contemporaneous Zenodo incident affects both the record metadata API used in 0105a6f and at least the direct file-delivery path used in 0105a6g. The provider-byte authority itself remains historically established by the successful 0105a3 lock; the current blocker is reacquisition transport.

## Scientific meaning

This is not a Standard-Model failure, not a likelihood failure, and not evidence for a BSM residual. It is a reproducibility/transport block under the frozen reacquisition predicate.

## Authorization

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Next authority-preserving option

A later prospective recovery gate may treat a non-authoritative transport mirror only as a byte carrier **if and only if** every recovered file exactly matches the already frozen official 0105a3 SHA256, provider MD5 and byte size. In such a gate, authority remains the 0105a3 official Zenodo lock; the mirror contributes no scientific semantics and a single hash mismatch is a hard BLOCK.

Alternatively, reacquisition can be retried from Zenodo after transport recovery. Neither option changes the frozen F1-F7 semantic criteria of 0105a6f.
