# Preregistration 0078 — external-authority refresh across blocked NMIR survivors

Date frozen: 2026-09-07
Parent: 0077 `BLOCKED_G9_TURNING_POINT_KERNEL` under frozen commit `71c21236b1da1817d122567286c938ca6efcce6c`; the 0077 decision tree requires returning to other funnel survivors rather than post-hoc repairing the G9 geometry method.

## Scientific question

Has genuinely new primary external evidence become available that supplies the exact missing authority for any currently blocked NMIR survivor and therefore makes a new quantitative gate executable?

This is an authority/materialization audit, not a positive-claim scan. Existing blockers remain valid unless the frozen missing ingredient is supplied directly.

## Frozen survivor requirements

### G2 — detector transfer / rejection × bulk-NR acceptance
Unlock only if a primary experimental publication or collaboration data release reports, in the same detector configuration and sub-keV regime relevant to the frozen G2 requirement, both (a) measured rejection of the relevant low-energy background topology and (b) measured acceptance/efficiency for bulk nuclear recoils, with enough numerical information to form the product without cross-detector multiplication or invented efficiency.

### G8 — Cu63 RIOEC normalization
Unlock only if a primary nuclear/neutrino source supplies an absolute normalization or a fully specified rate/cross-section formula for the exact `63Cu(g.s.,3/2-) + anti-nu_e + e_K -> 63Ni*(87.220 keV,5/2-)` entrance, sufficient to fold the already validated continuous thermal-solar anti-neutrino spectrum without importing an unrelated discrete-line normalization.

### BSM / B-L external envelope
Unlock only if a primary publication/release supplies reproducible numerical tables, source code, likelihood/data package, or a vector contour with unambiguous semantic identity and convention mapping sufficient to add a missing B-L constraint family to a common `(m_V,g_BL)` envelope. Raster/manual reading, proportional background splitting, Asimov substitution for required observed likelihoods, or cross-analysis response substitution are forbidden.

## Frozen search scope

Search primary literature/data releases available through 2026-09-07, prioritizing material newer than the authority already frozen in iterations 0063, 0068 and 0072-0074c. Reviews may be used only to locate primary sources and never to unlock a gate by themselves.

## Frozen classifications

- `PASS_NEW_EXECUTABLE_SURVIVOR_<class>`: at least one survivor's exact missing input is supplied by primary reproducible authority; record source/provenance and preregister the corresponding new quantitative gate before calculation.
- `NO_NEW_EXECUTABLE_AUTHORITY`: searches locate no primary source satisfying any frozen survivor requirement; all three remain blocked/open in their prior scopes.
- `PARTIAL_EXTERNAL_AUTHORITY`: a source materially improves provenance but still lacks at least one frozen mandatory input; no quantitative survivor gate is unlocked.
- `INFRASTRUCTURE_FAIL`: external source access fails before a substantive audit can be made.

## Decision rule

If multiple survivors unlock, choose the one with the most direct numerical authority and least additional modeling freedom; record the others as separately executable, not discarded. If none unlock, do not lower requirements. Readiness changes only for a reproducible scientific gate, not for the literature search itself.

## G9 guard

0078 must not add result-selected grid points, new derivative assumptions, or relaxed tolerances to 0077. Persistent-source G9 convolution remains closed unless a future prospectively distinct hypothesis changes the physical/numerical assumptions.
