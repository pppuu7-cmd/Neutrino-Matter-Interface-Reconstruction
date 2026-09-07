# NMIR Iteration 0079 — Fayet/MICROSCOPE B-L fifth-force authority

Date: 2026-09-07
Classification: **PASS_FIFTH_FORCE_B_L_ASYMPTOTIC_AUTHORITY**

## What was tested
The frozen 0079 gate asked whether the long-range fifth-force family in the global B-L constraint ledger has a primary, reproducible convention/range authority that maps into the NMIR interaction `g_BL V_mu J^mu_{B-L}` without raster reading or a post-result normalization choice.

The first hosted run was infrastructure-only failure because pytest was absent; no scientific step executed. The workflow dependency was corrected without changing the preregistration or audit code. The rerun completed 4/4 dedicated tests and the frozen primary-source audit.

Hosted rerun: run `34160053648`, job `101859746603`, artifact `10032282068`. Raw result SHA256 `d28969f005758558cf370d1dd90841652191c9c8cb531b03b8eb9fd2734c987d`; artifact ZIP SHA256 `24a0b8789afe0e32a5016f44b369517a490f4629a3390a16afcfac188df9ef55`.

## Primary authority result
Preferred source under the preregistered order is Fayet, Phys. Rev. D 99, 055043 (2019), arXiv:1809.04991v2, source SHA256 `ed233fa73a149ba9801d442339a2c5fd3b5051c1dc2caa1584a000760fcff29b`.

It defines the pure effective B-L coefficient as `epsilon_{B-L}(B-L)e` (eq. 19). Therefore for the NMIR convention `L_int = g_BL V_mu J^mu_{B-L}`, the current coefficient maps as

`g_BL = e |epsilon_{B-L}|`.

The paper's separate `g''` is a UV-normalized extra-U(1) coupling in a specific grand-unified construction; eq. 49 gives `epsilon_{B-L} e ~= -(5/4) g''`. It is not the NMIR `g_BL` and the factor must not be imported into the generic B-L current normalization.

The 2019 primary gives the 2-sigma long-range B-L limits `|bar alpha_g| < 2.2e-13` and `|epsilon_{B-L}| < 0.84e-24` (Table V / eqs. 33,43). It also makes clear that `bar alpha_g(B-L)=alpha_g(B-L)/4` for average nucleons.

The earlier Fayet Phys. Rev. D 97, 055039 (2018), arXiv:1712.00856v2, source SHA256 `e058c6338db1151bf631a2c2c5eb09102cb521327227ff5288570e51744cc03d`, explicitly writes the Yukawa potential and states that the quoted MICROSCOPE limits assume `lambda_U` infinite or somewhat larger than the Earth diameter. They weaken at shorter range and become nearly insensitive for ranges well below the ~710 km satellite altitude. That paper gives a slightly stronger direct 2-sigma value `|epsilon_{B-L}| < 0.73e-24`; the later 2019 source is retained as the preferred authority because the source order was frozen prospectively and it supplies the later published conservative normalization.

## Why this is not a finite-range PASS
Neither audited source supplies a machine-reproducible finite-range B-L exclusion contour/table or an exact extended-Earth Yukawa response suitable for converting the asymptotic MICROSCOPE result into a finite mediator-mass boundary. The qualitative damping statement is insufficient for a new numerical contour.

Therefore 0079 authorizes only a separately preregistered **asymptotic `m_V -> 0` materialization**. It does not authorize extending the bound to any chosen finite mass.

## Next gate
0079a: convert only the preferred 2019 asymptotic `|epsilon_{B-L}|` limit into NMIR `g_BL`, with the electromagnetic normalization frozen before execution. Then return to a separate finite-range/stellar/cosmology authority rather than drawing a Yukawa turn-off by hand.
