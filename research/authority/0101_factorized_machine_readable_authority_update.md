# 0101 factorized machine-readable authority update

Date: 2026-09-10
Status: RESEARCH NOTE — TERMINAL LOCK DELIBERATELY NOT CREATED YET
Benchmark: `NMIR-BENCHMARK-0101`

## Question

Can the outstanding 0101 sterile-parameter authority block be converted from an open literature-search problem into a finite, reproducible pinning task without fabricating a four-dimensional global likelihood?

## Result

Yes. Two official machine-readable/public-data authorities now provide a concrete factorized route:

1. an electron-disappearance axis from the Daya Bay full-dataset sterile-neutrino search; and
2. independent muon/tau sterile-mixing authority from the IceCube DeepCore 7.5-year sterile-neutrino data release.

This is sufficient to define the architecture of a prospectively frozen **factorized experimental-envelope benchmark**. It is not sufficient yet to create `research/locks/0101_sterile_parameter_terminal_lock.json`, because the individual payload files still need byte-level pinning, field/parameter verification, and a frozen extraction rule.

## Authority A — Daya Bay full-dataset chi-square map

Publication:
- Daya Bay Collaboration, *Search for a Sub-eV Sterile Neutrino Using Daya Bay's Full Dataset*, Phys. Rev. Lett. 133, 051801 (2024).
- DOI: `10.1103/PhysRevLett.133.051801`.

Official supplemental-material landing page:
- `https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.133.051801`

The APS supplemental record explicitly exposes:
- `chiSquareMap_DayaBay_3158days.dat`;
- `readme.pdf` explaining use of the chi-square map;
- comparison/shape-rate figures.

Scientific role:
- machine-readable authority for the electron-disappearance plane involving `sin^2(2 theta14)` and `Delta m^2_41`;
- preferable to plot digitization;
- published with the final 3158-day Daya Bay sample.

Important interpretation guard:
- this object constrains the electron-disappearance sector only;
- it must not be relabeled as authority for `theta24` or `theta34`;
- a contour or Delta-chi-square threshold extracted from this map must follow the accompanying README/publication convention exactly.

## Authority B — IceCube DeepCore muon/tau sterile data release

Publication:
- IceCube Collaboration, *Search for a light sterile neutrino with 7.5 years of IceCube DeepCore data*, Phys. Rev. D 110, 072007 (2024).
- DOI: `10.1103/PhysRevD.110.072007`.

Official IceCube data-release page:
- `https://icecube.wisc.edu/data-releases/2025/07/a-search-for-a-light-sterile-neutrino-with-7-5-years-of-icecube-deepcore-data/`

Persistent data-release DOI:
- `10.7910/DVN/QKL28Z` (Harvard Dataverse).

Published constraint regime relevant to 0101:
- analysis is reported for `Delta m^2_41 >= 1 eV^2`;
- the publication reports 90% CL bounds `|U_mu4|^2 < 0.0534` and `|U_tau4|^2 < 0.0574` under that regime.

Scientific role:
- independent authority for the muon/tau sterile-mixing directions that the electron-disappearance map cannot supply.

Important interpretation guard:
- IceCube and Daya Bay likelihoods/confidence constructions are not to be multiplied or assigned a synthetic joint confidence level unless a prospectively defined statistically justified joint likelihood is constructed from compatible released likelihood objects;
- until then, the benchmark is an **axis-wise factorized envelope**, not a global fit.

## Candidate terminal architecture

A scientifically conservative terminal 0101 run can be defined on a finite common mass-splitting fixture at or above `Delta m^2_41 = 1 eV^2`, subject to verification that the Daya Bay released chi-square map contains the chosen mass-splitting coordinate.

Prospective parameter semantics:

- `Delta m^2_41`: fixed terminal fixture chosen before execution from the intersection of released-authority domains;
- `theta14`: chosen/extracted only from the pinned Daya Bay map under its published statistical convention;
- `theta24`, `theta34`: bounded/selected only under the pinned IceCube release convention;
- sterile CP phases: retain the already-preregistered zero-phase 0101 preflight convention unless a separate terminal preregistration expands them;
- no combined CL statement;
- no claim that the Cartesian product is a community global allowed region.

The purpose is not to find a sterile-neutrino best fit. The purpose is to test whether an experimentally admissible 3+1 extension occupies an NMIR design region while preserving the funnel's authority semantics.

## Pinning gates before terminal lock

`0101_sterile_parameter_terminal_lock.json` may be created only after all of the following are complete:

1. Retrieve the Daya Bay `chiSquareMap_DayaBay_3158days.dat` payload from the official APS supplemental record.
2. Record its byte size and SHA-256 hash.
3. Retrieve and pin the corresponding `readme.pdf`; record byte size and SHA-256.
4. Verify column definitions, parameter units, map bounds and the exact statistic stored in the map.
5. Confirm that the prospectively chosen `Delta m^2_41` fixture lies inside the released map domain rather than being an extrapolation.
6. Retrieve the IceCube Harvard Dataverse release by persistent DOI `10.7910/DVN/QKL28Z`.
7. Record the exact dataset version, relevant file names, byte sizes and SHA-256 hashes.
8. Verify whether the released IceCube object provides a likelihood/grid/contour suitable for selecting `theta24` and `theta34`, or only sufficient material to reproduce the published bounds.
9. Freeze a deterministic parameter-selection rule before running the terminal 0101 calculation.
10. Run the existing 0101 mathematical/known-limit gates unchanged.

## Current decision

`BLOCKED_0101_STERILE_PARAMETER_AUTHORITY_UNPINNED` remains the correct terminal status **for now**, but the nature of the block has changed materially:

- before this note: the required machine-readable electron-disappearance authority had not been identified;
- after this note: official candidate payloads and persistent identities are identified, and the remaining work is a finite retrieval/hash/schema-verification task.

Therefore no physics FAIL has occurred and no gate is weakened.

## Next deterministic task

Pin the Daya Bay `.dat` + README and the IceCube Dataverse payloads byte-for-byte, then preregister the common `Delta m^2_41` fixture and axis-wise parameter-selection rule. Only after that step may the terminal 0101 lock be created and the authority readiness counter legitimately move from 1/5 to 2/5.
