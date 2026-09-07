# NMIR Iteration 0079a — Fayet/MICROSCOPE asymptotic B-L materialization

Date: 2026-09-07
Classification: **PASS_FIFTH_FORCE_B_L_ASYMPTOTIC_MATERIALIZATION**

## Frozen question
Convert only the preferred Fayet 2019 long-range 2-sigma bound `|epsilon_{B-L}| < 0.84e-24` into the NMIR pure-current convention `L_int = g_BL V_mu J^mu_{B-L}`, using the 0079-authorized map `g_BL = e |epsilon_{B-L}|`. No finite-mass contour or Yukawa turn-off was permitted.

## Hosted result
Run `34160325335`, job `101860584123`; 4 dedicated tests passed in 0.01 s. Artifact `10032369690`. Raw JSON SHA256 `1f8af81dd4150366aefc7821c35285af766bfe2801f6b6dc9d57a1ba3af17511`; artifact ZIP SHA256 `bdc7c75c13bc8c10a0698c58953072aa0f5d2540463ca3db9088272496b7cb2e`.

Frozen electromagnetic normalization: `alpha_EM(0)^-1 = 137.035999177`, hence `e = 0.30282212076899695`. Double precision and independent Decimal implementations agree to the recorded precision, and the algebraic epsilon round-trip is exact at the reported numerical precision.

The materialized limit is

`g_BL < 2.5437058144595744e-25` at 2 sigma,

reported at the precision of the primary input as

**`g_BL < 2.5e-25` (2 sigma, strict long-range / m_V -> 0 limit).**

The one-Earth-diameter Compton mass `1.5486342834719824e-14 eV` is retained only as a diagnostic reference. It is explicitly not a hard validity edge because the primary source states a range infinite or somewhat larger than the Earth diameter and does not supply a reproducible finite-range contour.

## CI note
The dedicated 0079a scientific gate passed. Baseline CI on the same head failed during collection of the older 0079 test because `scripts/` was not importable as a package (`ModuleNotFoundError: scripts`). This is an infrastructure/repository-test issue, not a scientific failure. A package marker `scripts/__init__.py` was added in commit `912079347279e691275f375655c0612f0efed74f`; the baseline rerun must be checked independently.

## Scientific consequence
The partial global B-L ledger now has a reproducible asymptotic fifth-force anchor in addition to the 0078c machine-readable solar-CEvNS excluded region. These are not connected by an invented interpolation. The global envelope remains incomplete until finite-range/stellar/SN/cosmology families are materialized under their own primary authority.

## Next allowed move
After repository CI reconciliation and auto-research race check, select the next independently executable low-mass B-L family. Do not extend the MICROSCOPE asymptotic datum to finite mediator mass without a separately frozen primary finite-range authority.
