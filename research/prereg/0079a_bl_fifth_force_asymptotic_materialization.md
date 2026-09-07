# Preregistration 0079a — asymptotic MICROSCOPE B-L materialization

Date frozen: 2026-09-07
Parent: 0079 `PASS_FIFTH_FORCE_B_L_ASYMPTOTIC_AUTHORITY`, classification commit `cbc2586097d18bfd2126010cdc7aa8d7c4129796`.

## Question
What is the NMIR coupling upper bound in the strict long-range/asymptotic `m_V -> 0` limit implied by the preferred Fayet 2019 primary authority, under the already-resolved pure-current mapping `g_BL = e |epsilon_{B-L}|`?

## Frozen inputs
- Preferred primary: arXiv:1809.04991v2 / Phys. Rev. D 99, 055043 (2019), source SHA256 `ed233fa73a149ba9801d442339a2c5fd3b5051c1dc2caa1584a000760fcff29b`.
- 2 sigma asymptotic bound: `|epsilon_{B-L}| < 0.84e-24` from Table V / eq. 43.
- NMIR current convention: `L_int = g_BL V_mu J^mu_{B-L}`.
- Exact convention map authorized by 0079: `g_BL = e |epsilon_{B-L}|`.
- Electromagnetic normalization for this conversion: `alpha_EM(0)^-1 = 137.035999177`, `e = sqrt(4*pi*alpha_EM(0))` in Heaviside-Lorentz natural units. This value is frozen before execution; the published bound has only two significant digits, so scientific reporting must also provide the appropriately rounded result.

## Calculation
Compute
`g_BL_2sigma = sqrt(4*pi/137.035999177) * 0.84e-24`.

Also calculate the corresponding Compton mass scale for one Earth diameter only as a **diagnostic reference**,
`m_ref = hbar*c / D_Earth`, with `D_Earth = 12742 km`, but do not convert the qualitative source phrase “somewhat larger than Earth diameter” into a hard finite-mass validity edge. The materialized scientific constraint remains an asymptotic `m_V -> 0` datum.

## Frozen checks
1. direct double-precision and Decimal implementations of `e` and `g_BL` agree to relative `1e-12`;
2. algebraic roundtrip `g_BL/e` returns the frozen epsilon bound to relative `1e-12`;
3. result lies in `[2.4e-25, 2.7e-25]` as a gross convention guard;
4. no finite-mass polygon, interpolation or Yukawa turn-off is emitted;
5. output explicitly distinguishes NMIR `g_BL` from Fayet UV `g''`.

## Classification
- `PASS_FIFTH_FORCE_B_L_ASYMPTOTIC_MATERIALIZATION` if all checks pass.
- `SCIENTIFIC_FAIL_FIFTH_FORCE_B_L_ASYMPTOTIC_MATERIALIZATION` if a frozen algebra/convention check fails.
- `INFRASTRUCTURE_FAIL` if code cannot execute.

PASS closes only the asymptotic fifth-force datum. The next research gate must seek a separate finite-range low-mass constraint family (or move to the next required 0071 family, stellar/SN or cosmology); it must not extrapolate this datum.
