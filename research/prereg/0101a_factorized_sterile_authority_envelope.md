# 0101a — prospective factorized sterile-neutrino authority envelope

Date frozen: 2026-09-09
Parent benchmark: `NMIR-BENCHMARK-0101`
State: PREREGISTERED_AUTHORITY_ROUTE_NONTERMINAL

## Purpose

Close the external-parameter authority gap for the 3+1 sterile benchmark without manufacturing a joint global likelihood from statistically incompatible publications.

The preferred route remains a single reproducible joint 3+1 likelihood if one becomes publicly available before terminal execution. The present preregistration freezes the fallback route: a **factorized experimental authority envelope**. Each experimental authority axis is retained separately, with no multiplication of confidence levels and no claim that the Cartesian product is a global allowed region.

## Primary authority for `(Delta m^2_41, theta14, theta24)`

Primary accelerator authority:

- MicroBooNE Collaboration, *Search for light sterile neutrinos with two neutrino beams at MicroBooNE*, Nature 648 (2025) 64–69.
- Publication DOI: `10.1038/s41586-025-09757-7`.
- Public HEPData dataset DOI: `10.17182/hepdata.166435.v1`.

The publication states that measured data, predictions, systematic uncertainties, and `Delta chi^2` values over a three-dimensional 4-neutrino grid are publicly released. The fitted oscillation dimensions are equivalent to `(Delta m^2_41, sin^2 theta14, sin^2 theta24)` / the corresponding appearance-disappearance amplitudes, with the combined BNB+NuMI analysis used for the final result.

Frozen rules:

1. Only the **final combined BNB+NuMI** release may define the 0101 primary `(Delta m^2_41, theta14, theta24)` authority. The auxiliary NuMI-only Zenodo grid may be used as a reproducibility cross-check but must not silently replace the final combined result.
2. Before any NMIR terminal 0101 calculation, the exact HEPData table/file identities, their downloaded byte hashes, grid dimensions, parameter ordering, test-statistic convention, and any critical-value/CLs objects actually used must be frozen in a new immutable lock.
3. No contour may be digitized from a figure.
4. No Wilks threshold may be substituted for a Feldman–Cousins or CLs prescription used by the source analysis.
5. The tested NMIR grid must be a deterministic subset/interpolation of the frozen released grid. Grid boundaries may not be expanded after seeing the NMIR result.

## Tau / theta34 authority axis

Secondary authority:

- IceCube Collaboration, *Search for a light sterile neutrino with 7.5 years of IceCube DeepCore data*, Phys. Rev. D 110, 072007 (2024).
- Publication DOI: `10.1103/PhysRevD.110.072007`.
- Official IceCube data-release page points to Harvard Dataverse dataset DOI: `10.7910/DVN/QKL28Z`.

The published result reports, for `Delta m^2_41 >= 1 eV^2`, 90% CL constraints

- `|U_mu4|^2 < 0.0534`,
- `|U_tau4|^2 < 0.0574`.

This authority is **not** to be statistically multiplied with the MicroBooNE CLs result. It defines a separate consistency axis.

For the 0101 parameterization

`U4 = R34(theta34) R24(theta24) R14(theta14) diag(U_PMNS,1)`,

the standard real-angle relation is

`|U_tau4|^2 = cos^2(theta14) cos^2(theta24) sin^2(theta34)`.

However, that algebraic conversion may be used as a terminal theta34 bound only if the exact IceCube analysis convention and fixed/varied sterile parameters in the public release are shown to be compatible with the tested 0101 point. If compatibility cannot be established from the immutable data release and publication, the tau axis must remain separately reported as `BLOCKED_0101_THETA34_AUTHORITY_CONVENTION_MISMATCH` rather than forcing a converted bound.

## Mass-domain intersection rule

The factorized envelope is valid only where the authorities overlap in their published applicability. In particular, the IceCube averaged/eV-scale statement is explicitly for `Delta m^2_41 >= 1 eV^2`.

Therefore:

- no IceCube tau constraint may be extrapolated below `1 eV^2`;
- below that boundary, MicroBooNE may still define the `(Delta m^2_41, theta14, theta24)` authority, but theta34 remains separately BLOCKED unless another prospectively pinned public authority closes it;
- any terminal statement must report the authority coverage mask as a function of `Delta m^2_41`.

## Statistical semantics

The terminal benchmark must report at least these separate fields:

- `MICROBOONE_3D_AUTHORITY_STATUS`
- `ICECUBE_TAU_AXIS_STATUS`
- `AUTHORITY_DOMAIN_INTERSECTION_STATUS`
- `JOINT_GLOBAL_LIKELIHOOD_USED = false`

Forbidden phrases include `global 90% CL allowed region`, `combined 95% CL exclusion`, or equivalent wording unless a true prospectively frozen joint likelihood is later substituted through a new preregistration before execution.

## Exact-asset lock required before terminal execution

A later lock, provisionally `research/locks/0101b_sterile_parameter_terminal_lock.json`, must contain:

- MicroBooNE HEPData record/version and exact table/file names;
- cryptographic hashes of all consumed files;
- parameter-grid dimensions and ranges;
- test-statistic and confidence construction actually used;
- IceCube Dataverse persistent DOI, released version, exact consumed files and hashes;
- all assumptions needed to map released matrix-element limits to the 0101 angle convention;
- the final deterministic NMIR evaluation grid and interpolation rule;
- a Boolean guard `joint_global_likelihood_claim_allowed = false` unless a future preregistration explicitly replaces this route.

Until that lock exists, the existing overall ceiling remains

`BLOCKED_0101_STERILE_PARAMETER_AUTHORITY_UNPINNED`.

## Interpretation

A terminal PASS under this factorized envelope would mean only that the tested 3+1 model survives the prospectively frozen experimental authority axes within their valid domains. It would not establish that a sterile neutrino exists, and it would not convert separate experimental constraints into a statistically joint global fit.
