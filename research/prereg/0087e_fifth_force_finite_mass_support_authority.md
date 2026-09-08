# NMIR prereg 0087e — B-L fifth-force finite-mass support authority

Date: 2026-09-08

## Motivation
0087b leaves finite-mass fifth-force/EP as an unresolved mass-support threat to the robust low-mass topology target `6.845530367110015e-6 <= m_V <= 1.4057345497828417 eV`. 0079/0079a authorize a strict long-range/asymptotic MICROSCOPE/Fayet B-L anchor only; they explicitly do not authorize a finite-mass Yukawa continuation. 0087c and 0087d have now source-authority-blocked Cerdeño and COHERENT mass-support-only routes under the no-manual contract.

This gate asks only whether primary fifth-force/EP authority itself supplies a finite mediator-mass/range applicability interval that can be mapped to `m_V` without extrapolating the strict long-range result.

## Frozen primary scope
Primary-source family is restricted to the already accepted Fayet/MICROSCOPE authority chain used by 0079/0079a:
- P. Fayet, Phys. Rev. D 99, 055043, arXiv `1809.04991v2`;
- companion arXiv `1712.00856v2` only where it is explicitly part of the same normalization/range derivation.

Exact fetched source bytes and SHA256 values must be recorded before promotion. A later review or secondary fifth-force plot may not silently replace these sources.

## Scientific question
Do these primary sources themselves state a finite positive force range / mediator-mass domain, or a mass-dependent Yukawa suppression formula plus experimentally defined length-scale applicability, sufficient to certify a finite `m_V` support interval for the B-L EP constraint?

## Frozen allowed routes
### Route A — explicit finite mediator-mass interval
PASS_A only if primary text/equations explicitly give both finite positive mediator-mass endpoints with physical units for the relevant B-L EP/MICROSCOPE constraint.

### Route B — explicit finite force-range interval with exact conversion
PASS_B only if primary text/equations explicitly give both finite positive force-range endpoints `lambda_min, lambda_max` with physical length units for the relevant constraint. Convert endpointwise with

`m_V c^2 = ħ c / lambda`,

so the mass interval is `[ħ/(c lambda_max), ħ/(c lambda_min)]`. The numerical value of `ħ c` must come from a frozen CODATA/NIST authority and its provenance/version must be recorded before calculation.

### Route C — source-explicit mass-dependent Yukawa response
PASS_C only if the primary source gives an explicit Yukawa mass/range response for the actual experiment and an experimentally specified finite length/range domain sufficient to define both finite endpoints without selecting an arbitrary sensitivity threshold after seeing the curve.

Forbidden:
- taking Earth radius, Earth diameter, orbital altitude, instrument size or source-detector distance as an endpoint unless the primary source itself defines that endpoint for the published constraint;
- inventing a suppression threshold such as `e^-1`, 50%, 10%, or 1%;
- extending the strict `m_V -> 0` limit by dimensional intuition;
- importing a generic fifth-force review contour or secondary plot;
- visual/raster/manual digitization.

## Threat comparison
If and only if a finite interval `[a,b]` is certified, compare it to the frozen 0087b target `[t0,t1]`:
- `PROVABLY_MASS_DISJOINT` iff `b < t0` or `a > t1`;
- otherwise `MASS_OVERLAP_THREAT`, including endpoint contact.
Report log10 separation or overlap width/fraction.

## Classification
- `PASS_FIFTH_FORCE_FINITE_MASS_SUPPORT_AUTHORITY` if at least one allowed route uniquely certifies a finite positive interval and all passing routes agree within 0.03 decade per endpoint;
- `BLOCKED_FIFTH_FORCE_FINITE_MASS_SUPPORT_AUTHORITY` if no allowed route certifies both endpoints;
- `SCIENTIFIC_FAIL_FIFTH_FORCE_FINITE_MASS_SOURCE_INCONSISTENCY` only if independently authoritative passing routes disagree by >0.03 decade per endpoint;
- download/archive/parser failures before scientific evaluation are infrastructure failures.

## Guards
No finite-mass extrapolation of 0079/0079a. No change to the asymptotic `g_BL` bound. No coupling/y-axis contour reconstruction. No raster/OCR/manual reading. No arbitrary Yukawa sensitivity threshold. No global B-L allowed-region claim. No BSM response/enhancement scan.

## PASS/BLOCKED consequence
PASS permits only a later separately preregistered coupling-side/geometry question if the certified mass interval overlaps the 0087b target. MASS_DISJOINT clears only this specific target by mass. BLOCKED leaves fifth-force as an unresolved mass-support threat and moves the funnel to the localized BBN tail/actionability problem; it does not authorize an approximate finite-mass cutoff.
