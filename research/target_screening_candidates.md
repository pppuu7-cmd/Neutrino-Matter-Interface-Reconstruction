# NMIR cross-target Standard-Model capture screening

Status: active quantitative screening ledger. `71Ga`, `37Cl`, and now `82Se` have matched B16+MSW power entries; other targets remain candidates until their response is independently validated.

## Historically motivated pool
John N. Bahcall, *Solar neutrino experiments*, Rev. Mod. Phys. 50, 881 (1978), calculated solar-neutrino absorption cross sections for nine proposed targets:

- 7Li
- 37Cl
- 51V
- 55Mn
- 71Ga
- 81Br
- 87Rb
- 115In
- 205Tl

Ga and Cl are quantitatively validated in NMIR. This historical list remains useful but is not exclusive: modern charge-exchange data can identify better-screened targets outside it.

## Newly validated modern target: 82Se
Frekers et al., Phys. Rev. C 94, 014614 (2016), measured the `82Se(3He,t)82Br` GT distribution at high resolution. The dominant `75-keV 1+` state has `B(GT)=0.338(31)` and a capture threshold near `171.6 keV` after the `~96.6-keV` ground-state mass difference. The paper reports a nonoscillation total solar-capture rate `668 ± 12(stat) ± 60(sys) SNU`, with roughly 97% of captures feeding the 75-keV state.

NMIR validation sequence:
1. point-Coulomb allowed-GT pp normalization: **FAIL**, `-32.6%` vs published source average;
2. relativistic finite-size Fermi-function pp normalization: **PASS**, `-0.453%`;
3. full measured/binned GT response vs nine source-average controls: **PASS all prospective component gates**;
4. matched frozen B16+MSW fold: **PASS** after one infrastructure-only zero-endpoint repair.

Current pure-82Se GS98+MSW neutrino-only ceiling: `2.94006655e-22 W/kg`, the largest validated value in the present ledger. Natural selenium gives only `2.66241785e-23 W/kg` because the natural 82Se isotopic fraction is about `0.0873`.

## 115In status: useful provisional negative screen
R. S. Raghavan, Phys. Rev. Lett. 37, 259 (1976), proposed the low-threshold 115In inverse-beta channel and historical full-response rates of order `~750 SNU`.

NMIR's deliberately provisional single-state model (`threshold≈0.114 MeV`, `B(GT)=0.17`, point-Coulomb) produced only `~371.7 SNU` without oscillations and therefore **fails as a complete 115In response model**. It is not in the G3 authority ledger. Its GS98+MSW pure-isotope screening ceiling `~8.32e-23 W/kg` was also below validated 71Ga.

115In remains eligible for a later precision reconstruction with a fuller primary response, but it is no longer the highest-priority immediate candidate.

## Screening requirements before ranking
For each candidate, NMIR must freeze a matched primary nuclear response or measured-ft authority; reconstruct threshold and allowed/excited-state branches; fold the same B16 spectra and component-specific MSW survival probabilities used for validated targets; normalize to pure isotope and natural abundance where useful; compute event rate and the strict neutrino-only bound `E_dep,nu <= E_nu`; and propagate nuclear-response uncertainty.

Any resonant/narrow-line candidate must additionally pass G8 integrated-strength, linewidth, and solar-spectrum-overlap bounds before peak cross section enters a ranking.

## Priority order for the next pass
1. **7Li** — classic target with simple/light nuclear structure; seek a modern response or robust matrix-element authority and compare high-threshold/high-energy weighting to 82Se.
2. **115In precision rebuild** — only if a complete primary GT/weak response can be frozen; do not reuse the failed one-state screen as authority.
3. **51V, 55Mn, 81Br, 87Rb, 205Tl** — provenance/reaction-threshold audit; retain only candidates with sufficient solar-spectrum overlap and defensible response data.
4. Search beyond the historical Bahcall pool for modern charge-exchange targets with measured low-threshold GT strength comparable to the successful 82Se case.

Negative screening outcomes are retained as scientific results; targets are not silently dropped for small rates.
