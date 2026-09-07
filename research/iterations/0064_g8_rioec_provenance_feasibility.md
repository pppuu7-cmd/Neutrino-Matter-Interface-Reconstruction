# NMIR iteration 0064 — G8 thermal-solar anti-nu_e RIOEC provenance feasibility

Date: 2026-09-07
Classification: **BLOCKED_ENTRANCE_STRENGTH**

## Funnel target
G8 / F2-F4. Determine prospectively whether NMIR can freeze both a physical thermal-solar electron-antineutrino source spectrum and an independently evaluated target-specific RIOEC entrance-strength/width package before any rate or W/kg ranking.

## Prospective contract
Frozen before the result-dependent audit:
- `research/prereg/0064_g8_rioec_provenance_feasibility.md`
- prereg commit `5e2e183e92dd4c23dab9c3d0d17ca16f6e456b3f`.

No ordinary solar `nu_e` flux, guessed resonance area, linewidth-as-strength substitution, or post-hoc target matrix element was allowed.

## Frozen evidence ledger
- `data/g8_rioec_provenance_authority_0064.json`
- ledger commit `f464f7baa796c515105cbf93e99aa351b26f2c10`.

## Source-side result: physical SM thermal anti-nu source exists
Haxton & Lin (Phys. Lett. B 486, 263-271 (2000), DOI `10.1016/S0370-2693(00)00764-4`, arXiv `nucl-th/0006055`) explicitly calculate the very-low-energy solar flux of **neutrinos and antineutrinos of all flavors** from thermal pair processes. Their primary abstract reports per-flavor spectral flux densities of order `1e8-1e9 cm^-2 s^-1 MeV^-1` below about 5 keV. The production inventory includes Compton/plasmon-pole processes, neutral-current decay of thermally populated nuclear states, plasmon decay and free-to-bound electron transitions.

A modern independent primary study, Arguelles et al. (arXiv `2606.15904`, 2026), treats the Standard-Model keV thermal solar neutrino component in low-threshold direct detection. Thus the source **class and particle identity are physically grounded**; NMIR does not need to invent a solar anti-nu component.

However, an exact target-specific numerical RIOEC fold must still prospectively materialize the differential `anti-nu_e` spectrum locally (table/data/recomputed model with provenance) rather than read values from plots or chat. That materialization requirement remains for the later numerical gate, but it is not the principal scientific blocker discovered here.

## RIOEC F4 requirement
The primary RIOEC formalism of Oldeman, Meloni & Saitta (Eur. Phys. J. C 65, 81-87, DOI `10.1140/epjc/s10052-009-1209-6`, arXiv `0905.1029`) writes the resonant cross section with the factor

`Gamma_beta_b / Gamma`,

where `Gamma_beta_b` is the reverse bound-beta partial width and `Gamma` is the total excited-atom width. Therefore the physical linewidth does **not** by itself determine the entrance strength. A target-specific weak partial width/matrix element is mandatory.

The 2026 Akhmedov-Lasserre-Maturi RIOEC proposal (`arXiv:2608.25001`) supplies the correct channel identity

`anti-nu_e + [e^- + (Z,A)] -> (Z-1,A)*`

and kinematic relation

`E_R = -Q_epsilon + E_x + E_b`,

and identifies candidate nuclides, but candidate/kinematic identification alone is not sufficient for NMIR F4.

## Target-side audit
### 63Cu
The 2026 LiquidO geoneutrino primary study (Communications Physics 9, 95; DOI `10.1038/s42005-026-02518-6`) independently confirms favorable allowed charged-current transitions involving `63Cu -> 63Ni/63Ni*`, but explicitly notes strong sensitivity to `Log(ft)`: a 10% change changes the cross section by roughly a factor three, and the authors call for refined nuclear input and/or direct reactor calibration. This is strong evidence that a convenient candidate label is not yet an independently precision-closed RIOEC entrance strength. The ordinary IBD transition also cannot automatically be substituted for the exact excited-state reverse width required by a thermal-window resonance.

### 159Tb
NNDC/ENSDF contains evaluated `159Gd beta-` and `159Dy EC` datasets feeding `159Tb`, so the isobaric system is data-rich. But the audit did not identify an evaluated reverse weak width for the **exact daughter excited state plus captured shell** required to place `E_R` in the thermal eV-keV window. Ground-state/isobar decay data cannot be substituted for that exact-state quantity.

### 129Xe
`129I beta- -> 129Xe` is well established, but the audited authority set likewise did not supply a complete exact-state thermal-RIOEC package tying `Q`, daughter excitation, shell binding/width and the reverse weak partial width together.

The point is not that these nuclides are impossible. The point is that NMIR's required F4 input is not yet independently closed for a thermal-window target.

## F10 classification
**`BLOCKED_ENTRANCE_STRENGTH`**.

The physical Standard-Model thermal-solar antineutrino source class survives F1-F3 provenance. The branch fails closed at F4 because no audited thermal-window candidate has a complete independently evaluated exact-state reverse weak entrance-strength/width package. Therefore no events/kg/s or W/kg number is calculated in 0064.

This is a scientific provenance blocker, not a negative statement about RIOEC as a detection method and not a claim that no suitable target can ever be measured.

## Guards preserved
- ordinary solar `nu_e` was not substituted for `anti-nu_e`;
- standard flavor oscillations were not used as particle-antiparticle conversion;
- linewidth was not promoted to integrated entrance strength;
- kinematic candidate matching was not promoted to F4 strength;
- no cross-transition or cross-target gain multiplication was used.

## Next funnel action
Do **not** continue a blind isotope scan. Reopen G8 only if an independently evaluated target paper/database package explicitly fixes the exact-state reverse weak width for a thermal-window RIOEC resonance; then freeze that package and the differential thermal `anti-nu_e` spectrum under a new preregistration before folding.

Per the funnel ordering, return now to the next independent highest-value OPEN class-level residual: **G3 absolute short-range/contact-current coefficient residual**. Iterations 0059 and 0062 prohibit treating EFT naturalness, fitted LEC ranges or a hard `l_max≈kR` as a theorem, so the next G3 contract must use a genuinely different coefficient-independent or observable-driven route.

`NMIR_READINESS` remains **87%**: 0064 is a reproducible blocker that prevents overclaim but does not close the physical target-strength residual.
