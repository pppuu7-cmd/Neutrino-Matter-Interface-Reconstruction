# NMIR v2 0105a5b-R1i — official IceCube PISA repository metadata authority

Date frozen: 2026-09-11
Parent state: R1d remains `BLOCKED_0105A5B_R1D_EXTERNAL_COMPUTATIONAL_AUTHORITY_INCOMPLETE`; R1h is BLOCKED because the exact IceCube 2304.12236 source did not uniquely name an MCEq release.

## Purpose
Establish, without inspecting implementation content, whether the official IceCube-owned public repository `icecube/pisa` exposes immutable provider metadata and tag/release lineage that can support a later prospectively registered analysis-version discriminator.

This route is independently provenance-qualified by the GitHub provider identity `icecube/pisa`. It is not a repeat of the consumed MCEq route.

## Frozen provider endpoints
Only these GitHub REST metadata endpoints may be requested:
- `https://api.github.com/repos/icecube/pisa`
- `https://api.github.com/repos/icecube/pisa/tags?per_page=100`
- `https://api.github.com/repos/icecube/pisa/releases?per_page=100`

No README, source/blob/tree/archive, workflow, issue, pull request, package/container payload, documentation page, or scientific output may be fetched.

## Frozen acceptance
`PASS_0105A5B_R1I_ICECUBE_PISA_METADATA_PINNABLE_NONDISCOVERY` iff:
1. all three endpoints return HTTP 200 JSON;
2. repository `full_name` is exactly `icecube/pisa`, owner login exactly `icecube`, and repository is not private;
3. every returned tag has a nonempty name and a 40-hex commit SHA;
4. at least one immutable tag exists.

Otherwise classify `BLOCKED_0105A5B_R1I_ICECUBE_PISA_METADATA_NOT_PINNABLE`; transport/JSON failure is `INFRASTRUCTURE_FAIL_0105A5B_R1I`.

## Consequence
A PASS is provenance-only. It does not establish that `2304.12236` used PISA, does not choose a PISA version, does not authorize implementation/source inspection, does not close any Barr/CSMS direction, and does not authorize DeepCore standard-3nu reproduction. A subsequent analysis-source discriminator must be separately preregistered before searching the already byte-locked IceCube source for PISA/version references.

Hard prohibitions: no README/code/tree/blob/archive/container inspection; no output-based version selection; no standard-3nu; no systematics MC; no observed residual/BSM scan.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
