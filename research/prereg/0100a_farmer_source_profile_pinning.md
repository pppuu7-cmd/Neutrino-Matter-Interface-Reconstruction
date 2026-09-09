# 0100a — authoritative source-profile pinning for benchmark 0100

Date frozen: 2026-09-09
Benchmark ID: NMIR-BENCHMARK-0100A
Parent: `research/prereg/0100_known_model_benchmark_standard_3flavor_msw.md`
State: ACTIVE_AUTHORITY_PINNING

## Purpose

Close the external `rho(r), Ye(r)` authority gate for the standard three-flavor + MSW control without changing any 0100 physics criterion.

This step is provenance only. It must not be interpreted as a physics PASS and it must not tune a stellar profile to obtain a desired flavor result.

## Frozen authority

Primary dataset record:

- Farmer et al., *On Variations of Pre-Supernova Model Properties*.
- Zenodo immutable record: `https://zenodo.org/records/2641723`
- DOI: `10.5281/zenodo.2641723`
- MESA version reported by the dataset: `7624`.
- Frozen archive: `25_final_profiles.tar.gz`.
- Frozen archive MD5 published by Zenodo: `762af1b62365fbe15c102fbf6f2f9142`.

Frozen model identity inside that archive:

- `25_79_0p005_ml`
- ZAMS mass: `25 Msun`
- reaction network family: `mesa_79.net`
- maximum cell mass: `0.005 Msun`
- mass loss: enabled (`ml`)
- evolutionary snapshot: final/pre-supernova profile at onset of core collapse as represented by the Farmer final-profile archive.

The model identity is also independently used in published pre-supernova neutrino calculations as a realistic MESA profile containing density and electron-fraction structure. This independent use is an authority cross-check only; the numerical terminal input must come from the frozen Zenodo archive above.

## Two-stage provenance rule

The top-level archive hash is known before execution, but the exact internal member path and member SHA-256 must be discovered without manual selection. Therefore 0100a is deliberately a one-use pinning stage:

1. download exactly the frozen archive URL;
2. verify the published archive MD5 before extraction;
3. enumerate the archive and select candidates containing the exact token `25_79_0p005_ml`;
4. reject the run if no candidate or an ambiguous set survives deterministic MESA-profile validation;
5. extract only the selected member;
6. compute its SHA-256;
7. parse the MESA header and require usable radial coordinate, density and electron-fraction columns from the same member;
8. emit a normalized profile plus a JSON provenance record containing archive identity, member path, member SHA-256, column mapping, row count and monotonicity checks;
9. upload both as immutable workflow artifacts.

The resulting internal-member identity/hash is **not terminal merely because the workflow succeeds**. It must be copied into a prospective amendment/lock commit before the 0100 terminal MSW workflow is enabled.

## Frozen deterministic selection rules

A candidate member must:

- contain the exact case-sensitive model token `25_79_0p005_ml` in its archive path;
- be a regular file, not a directory;
- parse as a MESA-style whitespace table with a named column header;
- contain a radial coordinate column (`radius`, `logR`, or an explicitly documented equivalent);
- contain density (`rho` or `logRho`);
- contain electron fraction (`ye`, `Ye`, `electron_fraction`, or a documented MESA equivalent);
- contain at least 32 finite zones;
- yield non-negative radius after unit conversion and a strictly monotonic radial sequence after canonical ordering;
- satisfy `rho > 0` and `0 < Ye <= 1` in all retained zones.

If more than one candidate satisfies all of these rules, the result is `BLOCKED_0100A_AMBIGUOUS_ARCHIVE_MEMBER`; no manual tie-break is allowed after inspection of the physical output.

## Frozen output contract

The pinning artifact must contain:

- `artifacts/0100a/source_profile.csv`
- `artifacts/0100a/source_profile_lock.json`

The normalized CSV columns are exactly:

`radius_km,rho_g_cm3,ye`

The lock JSON must include at least:

- dataset DOI and record URL;
- archive name, URL, expected MD5 and observed MD5;
- exact member path;
- member SHA-256;
- parser version / git SHA;
- source column names and transformations;
- number of zones;
- minimum/maximum radius, density and Ye;
- all validation gates;
- `terminal_physics_execution_allowed: false`.

Allowed 0100a states:

- `PASS_0100A_PROFILE_MEMBER_PINNED_NONTERMINAL`
- `BLOCKED_0100A_ARCHIVE_HASH_MISMATCH`
- `BLOCKED_0100A_PROFILE_MEMBER_NOT_FOUND`
- `BLOCKED_0100A_AMBIGUOUS_ARCHIVE_MEMBER`
- `BLOCKED_0100A_REQUIRED_COLUMNS_MISSING`
- `BLOCKED_0100A_PROFILE_VALIDATION_FAILED`

## Interpretation guard

This 25 Msun profile is a **control benchmark environment**, not a claim that Betelgeuse has exactly a 25 Msun ZAMS progenitor or exactly this internal structure. A Betelgeuse-specific astrophysical prediction requires a separately preregistered progenitor/profile uncertainty treatment.
