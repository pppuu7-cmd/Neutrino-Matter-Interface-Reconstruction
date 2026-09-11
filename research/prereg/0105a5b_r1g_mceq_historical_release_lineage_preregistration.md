# NMIR v2 0105a5b-R1g — MCEq historical release-lineage metadata gate

Date frozen: 2026-09-11
Parent: validated R1f `PASS_0105A5B_R1F_MCEQ_REPOSITORY_METADATA_PINNABLE_NONDISCOVERY`.

## Purpose
Pin the complete historical stable-release candidate set that existed before the frozen IceCube analysis publication authority (`arXiv:2304.12236`, first submitted 2023-04-24), without reading source code or selecting a version by scientific output.

The candidate set is the full set of non-draft, non-prerelease R1f release records published before 2023-04-24, with the exact tag->commit SHA mappings returned by validated R1f. No candidate may be dropped or ranked.

Frozen candidates:
- `mceq108` -> `d6246a179075a43a14b3839fa7e600277518f813`
- `mceq_1_1_1` -> `03200f418cce6240d5f5427ec7aa108868b8ca71`
- `release_1_1_2` -> `bcee968da8021016558d033088e348c54fdffc7f`
- `release_1_1_3` -> `344a573d5e87a82a187fd53d3647b4145472c1ac`
- `release_1_2_0` -> `7f10aae90d1714997216edcf82a099628d1ff3c6`
- `release_1_2_1` -> `dc71cd599e56d9eeda8bfa16a55dcc5d8a478109`
- `release_1_2_2` -> `23108b123bb5173a08761add0e95678e93776ba9`
- `release_1_2_3` -> `de7ebb7e4c127726cb12c0beb269f81ce865358c`
- `release_1_2_4` -> `3e87560f7a25f9579cfe7a0144156beae3fe9610`
- `release_1_2_5` -> `23ab910d3e346c68d769267780602b0bae37b7a8`
- `release_1_2_6` -> `553a0a62e17f86e11a80b80aa9ffcf528157ac81`

For each and only each frozen SHA, request exact GitHub REST commit metadata `/repos/mceq-project/MCEq/commits/{sha}` and record only SHA, author/committer dates, parents' SHAs and response byte hash. No files, trees, patches, commit message, source, README, archive or documentation may be inspected.

## Classification
`PASS_0105A5B_R1G_MCEQ_HISTORICAL_RELEASE_LINEAGE_PINNED_NONDISCOVERY` iff every frozen commit endpoint returns HTTP 200 JSON with response `sha` exactly equal to its frozen SHA. PASS establishes only immutable lineage metadata for the full candidate set.

`BLOCKED_0105A5B_R1G_MCEQ_HISTORICAL_RELEASE_LINEAGE_INCOMPLETE` if one or more candidate identities cannot be validated. Transport/runtime failures are `INFRASTRUCTURE_FAIL_0105A5B_R1G`.

No R1g outcome may choose a scientifically correct MCEq version. If multiple validated candidates remain and no already-authorized IceCube/provider authority distinguishes them, R1d remains BLOCKED pending a separate prospective authority-compatibility gate.

Hard prohibitions: no source/code/tree/blob/archive inspection; no nuisance implementation; no standard-3nu; no systematic MC; no observed residual; no BSM scan.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
