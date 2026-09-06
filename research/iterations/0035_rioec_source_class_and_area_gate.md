# NMIR iteration 0035 — RIOEC source-class + integrated-area gate

Date: 2026-09-06
Classification: **RIOEC_B16_FLAVOR_NO_GO_PASS / RIOEC_AREA_PROFILE_PASS / G8_TARGET_SPECIFIC_OPEN**

## Funnel choice
`research/NMIR_FUNNEL.md` placed target-specific genuine resonance first among surviving passive-SM branches. This iteration therefore did not run another isotope scan. It tested the source/flavor and integrated-area prerequisites that apply to the whole resonant induced orbital electron-capture (RIOEC) class before any candidate can be ranked.

Prospective contract: `research/rioec_source_class_prereg.md`, commit `5decc89a2e19092ee362742ef42bc532f5321add`.

## External physics authority
Akhmedov, Lasserre & Maturi, arXiv:2608.25001 (submitted 2026-08-25), propose

`anti-nu_e + [e^- + (Z,A)] -> (Z-1,A)*`

as a one-body-final-state resonance. For continuous sources the useful effective response is governed by spectral intensity at the resonance times integrated entrance strength rather than an arbitrarily high peak cross section. This is consistent with the older recoilless-resonance discussion of Kells & Schiffer, Phys. Rev. C 28, 2162 (1983).

## F1/F3 source-flavor result
The ordinary pp-chain/CNO/B16 solar authority used throughout NMIR is a thermonuclear `nu_e` source. RIOEC as defined above requires incident `anti-nu_e`. Standard active-flavor oscillations change neutrino flavor but not neutrino into antineutrino.

Therefore the entire ordinary B16 thermonuclear solar source has exactly zero entrance factor for this RIOEC channel:

`B16 nu_e -> RIOEC factor = 0`.

This is a **source-class no-go**, not a statement that RIOEC is impossible. Thermal solar pair processes produce a distinct neutrino+antineutrino population at keV energies (Haxton & Lin, Phys. Lett. B 486, 263-271 (2000)); that separate source class remains eligible and must be folded with its own spectrum.

## F5/F6 integrated-area result
With

`sigma(E) = B0 * L(E;E_R,Gamma)`

and a unit-area Lorentzian `L`, narrowing `Gamma` raises the peak but does not increase `integral sigma dE = B0`.

Hosted numerical benchmark, using a transformed integration variable that resolves arbitrarily narrow widths:
- area/B0 at `Gamma=1e-3` (arbitrary energy units): `0.9999968169011043`;
- area/B0 at `Gamma=1e-9`: `0.9999968169011043`;
- identical within numerical precision despite a peak increase of 1e6.

For a Gaussian source profile much broader than the resonance:
- `Gamma/source_sigma = 1e-3` -> overlap / `[B0 phi(E_R)] = 0.9996011826863775`;
- `Gamma/source_sigma = 1e-5` -> `0.9999941797890092`.

Thus the prospective smooth-profile criterion passes, and the computation explicitly reproduces the source-density-times-area limit.

## Hosted validation
Workflow run `34043507541`, job `101514361978`, artifact `9992388766`.
Artifact ZIP SHA256 from raw log: `881167ee93b2d6963d8aa39e0dcd5a72e497bed0d31d7367fa048b69e2063941`.
Raw log inspected:
- `5 passed in 0.13s`;
- benchmark values listed above;
- no physics criterion was changed after the result.

## Scientific consequence
A spectacular narrow RIOEC peak cannot be multiplied by the ordinary B16 solar flux: the entrance particle is wrong. For the genuinely allowed thermal-solar antineutrino source class, linewidth narrowing still cannot manufacture integrated strength; the rate is controlled by `B0 * phi_anti-nu_e(E_R)` in the narrow-resonance limit.

This removes a major ambiguity in G8 and prevents accidental use of the ~1e10 cm^-2 s^-1 ordinary solar-neutrino flux in an antineutrino-only resonance calculation.

## What remains open
This is not yet the target-specific G8 W/kg closure. The next gate must select a real RIOEC candidate (the 2026 paper identifies candidates including 63Cu, 129Xe and 159Tb), freeze its evaluated Q value, daughter excitation, captured-shell binding/width and weak entrance strength, then convolve against a primary thermal-solar `anti-nu_e` spectral density. Only that matched result may enter F7 W/kg ranking.
