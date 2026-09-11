# NMIR v2 0105a5b-R1f — MCEq official repository metadata preflight

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Parent evidence: validated R1e repository inventory plus frozen R1d Stage-1/Stage-2 records.

## Motivation and scope

R1e established that the committed NMIR repository contains no still-unconsumed external URL beyond the already consumed B4RITM, IceCube `2304.12236`, Barr 2006, MCEq/Sibyll 2019 and CSMS 2011 routes. R1d therefore remains BLOCKED.

R1d Stage-1/Stage-2 already records MCEq as an upstream computational authority explicitly used/cited by the IceCube publication. R1f opens a genuinely new prospective **metadata-only** route to the official MCEq software repository. It does not inspect implementation source code and cannot itself satisfy any of the seven nuisance contracts.

## Frozen endpoints

Only these exact GitHub REST metadata endpoints may be requested:

1. `https://api.github.com/repos/mceq-project/MCEq`
2. `https://api.github.com/repos/mceq-project/MCEq/releases?per_page=100`
3. `https://api.github.com/repos/mceq-project/MCEq/tags?per_page=100`

No redirect-derived contents URL, README, blob, tree, archive, tarball, zipball, raw file, commit diff, issue, pull request, workflow, package index or documentation page may be fetched.

## Frozen extracted fields

From repository metadata record only: `full_name`, `owner.login`, `html_url`, `homepage`, `description`, `archived`, `default_branch`, `created_at`, `updated_at`, `pushed_at`.

From each release record only: `tag_name`, `target_commitish`, `draft`, `prerelease`, `published_at`, `html_url`.

From each tag record only: `name` and `commit.sha`.

Raw response byte counts and SHA256 digests are recorded for all three endpoints. No source payload is downloaded.

## Frozen classification

`PASS_0105A5B_R1F_MCEQ_REPOSITORY_METADATA_PINNABLE_NONDISCOVERY` iff:

- all three exact endpoints return HTTP 200 JSON;
- repository `full_name == "mceq-project/MCEq"` and `owner.login == "mceq-project"`;
- releases and tags responses are JSON arrays;
- at least one tag exists and every recorded tag commit SHA is a 40-hex immutable Git object id;
- no prohibited content/source endpoint was requested.

This PASS establishes only that the already-authorized MCEq upstream software authority has a machine-readable official repository with pin-able immutable software states. It does **not** select a scientifically correct version and does not close BarrWP/BarrWM/BarrYP/BarrYM/BarrZP/BarrZM or DIS-CSMS.

`BLOCKED_0105A5B_R1F_MCEQ_REPOSITORY_METADATA_NOT_PINNABLE` iff the endpoints are reachable but the frozen repository identity or immutable-tag metadata criterion is not met.

`INFRASTRUCTURE_FAIL_0105A5B_R1F_MCEQ_METADATA_TRANSPORT` iff an exact endpoint cannot be evaluated because of transport/runtime/rate-limit/non-JSON failure. A repair may change transport/runtime only, not endpoint identities or scientific criteria.

## Hard prohibitions

No source-code inspection. No README inspection. No archive/source download. No selection of MCEq version based on nuisance-output behavior. No Barr W/Y/Z or P/M mnemonic inference. No nuisance transformation implementation. No standard-3nu expectation or likelihood. No systematic Monte Carlo. No observed residual or BSM scan. QKL28Z remains a separate sterile-control authority and is not a substitute for B4RITM.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
