# Amendment 0092b-a1 — exact Model-S GONG composition authority

Date frozen: 2026-09-08
Parent preregistration: `research/prereg/0092b_g9_ccsn_mev_solar_transmission_authority.md`.
Parent prereg commit: `66341d7eb7322e958a52dc30fb24d4e2b3e44647`.

This amendment is frozen before inspecting any 0092b chord-composition result. It narrows the composition-authority choice permitted by the parent prereg; it does not change the frozen ray, 5–50 MeV source interval, tau thresholds, channel requirements, or PASS/BLOCKED/FAIL taxonomy.

## Exact authority
Use the official Christensen-Dalsgaard Model-S archive only:

Archive landing page:
`https://users-phys.au.dk/jcd/solar_models/`

Extensive GONG-format Model-S file:
`https://users-phys.au.dk/jcd/solar_models/fgong.l5bi.d.15c`

Official GONG format documentation:
`https://users-phys.au.dk/jcd/solar_models/file-format.pdf`

The hosted authority run must fetch both exact files and report SHA256 of each. No mirrored/reformatted composition table may replace them in the terminal authority result.

## Frozen format interpretation
The GONG file header reports `nn=2482`, `iconst=15`, `ivar=25`, `ivers=210`.

Under the official format documentation:
- `var(1,n) = r`, radius in cm;
- `var(5,n) = rho`, density in g cm^-3;
- `var(6,n) = X`, hydrogen abundance by mass;
- for version `ivers=210`, `var(17,n) = Z`, heavy-element abundance by mass;
- helium mass fraction for the bulk H/He/Z ledger is defined deterministically as `Y = 1 - X - Z`.

Reject the file as `BLOCKED_G9_0092B_SOLAR_COMPOSITION_AUTHORITY` if header/version do not match these frozen expectations or if any accepted physical mesh point has non-finite `X,Z,Y`, `X<0`, `Z<0`, `Y<0`, or `X+Y+Z` inconsistent with unity beyond `5e-10`.

## Frozen coupling to the already validated density chord
The 0092 density authority remains the official limited Model-S file `cptrho.l5bi.d.15c` with validated SHA256
`65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc`.

0092b-a1 must **not** replace the validated 0092 density chord by the GONG density. Instead:
1. parse the GONG `r`, `X`, `Z` profiles;
2. normalize GONG radius by its own frozen global photospheric radius `glob(2)` to obtain `r/R`;
3. interpolate `X(r/R)` and `Z(r/R)` linearly onto the exact chord quadrature radii used with the 0092 limited-file density interpolation;
4. set `Y=1-X-Z` pointwise;
5. integrate component mass columns using the same `Rsun=6.957e10 cm`, `b/Rsun=0.024` and chord geometry as 0092.

This preserves the already validated density authority while using the extensive file only for local composition fractions.

## Frozen component columns
Compute

`Sigma_H = 2*Rsun * integral rho(r) X(r) dx`,

`Sigma_He = 2*Rsun * integral rho(r) Y(r) dx`,

`Sigma_Z = 2*Rsun * integral rho(r) Z(r) dx`.

Require the closure

`Sigma_H + Sigma_He + Sigma_Z = Sigma_total`

against the independently validated 0092 `Sigma_total = 2.9324883602905845e12 g cm^-2` with relative error `<=1e-8`.

Use two deterministic composite-Simpson chord resolutions `N=131072` and `N=262144`; require relative coarse/fine agreement `<=1e-4` for each of H, He and Z component columns.

Report at minimum:
- exact GONG/file-format SHA256 hashes;
- parsed header and global radius;
- `X,Y,Z` at the `b/Rsun=0.024` closest-approach radius;
- `Sigma_H`, `Sigma_He`, `Sigma_Z` at both resolutions;
- corresponding H-nucleus and He-nucleus columns using `m_u` and mass numbers 1 and 4;
- total metal mass column but **do not** choose a representative metal nucleus after seeing the result.

## Frozen classification of this amendment subgate
- `PASS_G9_0092B_MODEL_S_COMPOSITION_AUTHORITY` if provenance, version semantics, physical-fraction checks, component refinement and column closure all pass.
- `BLOCKED_G9_0092B_SOLAR_COMPOSITION_AUTHORITY` for authority/format/physical-fraction failure.
- `BLOCKED_G9_0092B_COMPOSITION_NUMERICS` for failure of the frozen numerical closure/refinement thresholds.
- `INFRASTRUCTURE_FAIL_G9_0092B_A1` only for download/execution/tool failures.

A PASS closes only the H/He/Z chord-composition authority. It does not by itself establish `tau_total<=0.1`, because the low-energy interaction channel/cross-section ledger remains separately required by the parent 0092b preregistration.

## Guards
No photospheric abundance substitution. No GONG-density replacement of the validated 0092 density result. No post-result representative metal nucleus. No MeV cross-section calculation inside this subgate. No detector/material/BSM gain fold.
