# Iteration 0091 — G9 named-source realizability BLOCKED by external source authority

Date: 2026-09-08
Classification: `BLOCKED_G9_REAL_SOURCE_AUTHORITY`

## Frozen contract
Preregistration: `research/prereg/0091_g9_named_source_realizability_authority.md`.
Prereg commit: `4bf6979684c287e65a2f37b5ef0e092a787698a0`.
Parent numerical authority: 0090f `PASS_G9_FULL_GRID_FINITE_NONZERO_SURVIVORS`.

0091 is an external-authority / realizability gate. It does not alter the 0090f lens map, source-size grid, offset grid, survivor threshold or magnification values. It does not authorize multiplying 0090f magnification into detector event rates, material response, interaction probability or neutrino-supplied power.

## Frozen parent geometry
0090f support used here only for overlap/actionability:
- observer distance family: approximately `23.97–24.26 AU`;
- angular source-radius support: `1e-18 <= theta <= 1e-6 rad`;
- nonzero source-plane offsets: `d={0.01,0.1,1,10,100} m`;
- all 1125 nonzero-offset rows had `mu>=2` under the frozen numerical experiment.

For centre misalignment `beta`, preregistered mapping is `d=z*AU*beta`.
At the maximum frozen nonzero offset `d=100 m`, the corresponding angular scale is:
- `5.752175 microarcsec` at `23.97 AU`;
- `5.727378 microarcsec` at the earlier CCSN Model-S benchmark `24.073780819657056 AU`;
- `5.683415 microarcsec` at `24.26 AU`.

These are geometry-only scales, not a practical station-keeping/duty-cycle result.

## Candidate 1 — steady high-energy source selected prospectively: NGC 1068

### Selection authority
The frozen rule selects the individually named source with the strongest steady-source evidence in the latest primary IceCube point-source/source-catalog result available by the 2026-09-08 cutoff.

Latest authority found: IceCube `IceTracks-DR2`, arXiv:2605.19040, submitted 2026-05-18, explicitly described as IceCube's latest and most comprehensive public all-sky muon-track dataset for source searches:
- https://arxiv.org/abs/2605.19040

In its 110-source catalog benchmark, NGC 1068 is the highest-significance source; reported catalog values are pre-trial `p=2.07e-6` (4.6 sigma) and global `p=2.28e-4` (3.5 sigma). Therefore NGC 1068, not a result-selected alternative, is candidate 1.

Supporting primary source evidence:
- IceCube, `Evidence for neutrino emission from the nearby active galaxy NGC 1068`, Science 378 (2022), arXiv:2211.09972: https://arxiv.org/abs/2211.09972
- source distance used by IceCube communication is about 47 million light-years (~14.4 Mpc).
- the 2022 analysis constrains the principal contribution to the measured excess to roughly `1.5–15 TeV`, with a soft best-fit spectrum.

### Morphology/centroid authority
The IceCube analyses are point-source likelihood analyses; their directional likelihood/localization is detector inference and cannot be promoted to a physical neutrino-emitting radius under the frozen 0091 guards.

No primary observational authority recovered in the 0091 search determines a physical angular radius of the neutrino-emitting region, or a sufficiently tight source-specific upper bound that identifies the neutrino production zone without adopting one of several theoretical EM/AGN scenarios. A current review explicitly states that present IceCube angular resolution does not identify the neutrino-emitting region of NGC 1068 and discusses multiple possible production sites:
- `Active Galactic Nuclei as high-energy neutrino sources`, Astronomy and Astrophysics Review (2026): https://link.springer.com/article/10.1007/s00159-026-00168-9

Theoretical corona/torus/jet/starburst models are scientifically useful, but selecting one after seeing 0090f would violate the frozen requirement unless its link to the observed neutrino morphology were independently authoritative. Electromagnetic source sizes are not accepted as neutrino sizes.

### Spectrum compatibility note
The relevant signal is TeV-scale. Solar-matter attenuation for TeV neutrinos is known to become non-negligible/important in high-energy solar-neutrino propagation literature, so transparent-Sun compatibility at the specific G9 core-grazing ray family cannot be assumed. This is an additional open physics compatibility question, not used to manufacture the 0091 classification because the morphology/centroid authority already blocks the candidate.

Candidate classification:
`BLOCKED_G9_NAMED_SOURCE_NEUTRINO_MORPHOLOGY_AUTHORITY`.

## Candidate 2 — time-dependent benchmark: TXS 0506+056

Primary IceCube authority:
- IceCube, `Neutrino emission from the direction of the blazar TXS 0506+056 prior to the IceCube-170922A alert`, Science 361 (2018), arXiv:1807.08794: https://arxiv.org/abs/1807.08794
- the archival analysis found a time-dependent excess between September 2014 and March 2015, with 3.5 sigma evidence after the time-variable search construction.

Distance/redshift authority:
- Paiano et al., ApJL 854 L32 (2018), arXiv:1802.01939, measured `z=0.3365 +/- 0.0010`: https://arxiv.org/abs/1802.01939

The IceCube time-dependent likelihood localizes events/direction statistically but does not directly measure a physical neutrino-emitting radius. Published one-zone/two-zone and VLBI-informed models constrain possible plasma/emission regions, but the mapping of those EM/radio structures to the physical neutrino-emitting region is model-dependent. The frozen 0091 rule forbids silently promoting those sizes to neutrino morphology.

The source is also episodic rather than an unambiguously persistent steady beacon for this gate. Its high-energy neutrinos raise the same separate solar-transmission compatibility issue as NGC 1068.

Candidate classification:
`BLOCKED_G9_NAMED_SOURCE_NEUTRINO_MORPHOLOGY_AUTHORITY`.

## Candidate 3 — generic Galactic CCSN at 10 kpc

Frozen prior source authority from NMIR iteration 0061 is retained; this is not a post-result source substitution.

Source morphology authority:
- benchmark distance: `10 kpc`;
- fiducial neutrino-emission radius used by the existing NMIR authority: `21 km`;
- primary simulation authority cited by NMIR: Delfan Azari et al., arXiv:1910.06176, with neutrinosphere scale approximately `16–21 km`;
- conservative NMIR sensitivity size: `100 km`.

At 10 kpc these radii correspond to angular radii:
- `16 km -> 5.18525e-17 rad`;
- `21 km -> 6.80564e-17 rad`;
- `100 km -> 3.24078e-16 rad`.

All are strictly inside the frozen 0090f support `[1e-18,1e-6] rad` (and far from its upper edge). Thus the CCSN morphology itself is compatible with the frozen numerical source-size range.

The same NMIR CCSN authority uses a burst-scale integration of about `20 s`, so this candidate is transient.

Alignment authority is the blocker. The frozen candidate is a **generic** Galactic CCSN class, not a prospectively named progenitor. It therefore has no specific pre-event sky direction that can be tied prospectively to the `<=100 m` source-plane support at ~24 AU. Selecting a favorable known star after this result would violate the frozen candidate rule. Neutrino-detector pointing after the burst begins is not equivalent to prospective microarcsecond-class line placement.

Candidate classification:
`BLOCKED_G9_NAMED_SOURCE_ALIGNMENT_AUTHORITY` (class-level semantic use per preregistration).

## Gate-level result
The three frozen candidates therefore classify as:

| Candidate | Frozen 0091 result | Main reason |
|---|---|---|
| NGC 1068 | `BLOCKED_G9_NAMED_SOURCE_NEUTRINO_MORPHOLOGY_AUTHORITY` | observed neutrino excess exists, but physical neutrino-emission region/centroid is not directly identified tightly enough for the 0090f map without a model-dependent EM proxy |
| TXS 0506+056 | `BLOCKED_G9_NAMED_SOURCE_NEUTRINO_MORPHOLOGY_AUTHORITY` | time-dependent neutrino association exists, but physical neutrino production morphology/centroid remains model-dependent |
| generic Galactic CCSN, 10 kpc | `BLOCKED_G9_NAMED_SOURCE_ALIGNMENT_AUTHORITY` | neutrinosphere angular size is inside support, but a generic future burst has no prospectively fixed source direction tied to the <=100 m focal-plane offset support |

No frozen candidate reaches `PASS_G9_NAMED_SOURCE_MORPHOLOGY_OVERLAP` with all morphology + centroid/alignment + spectrum authority simultaneously.

Therefore the gate classification is:

**`BLOCKED_G9_REAL_SOURCE_AUTHORITY`**.

This is not `SCIENTIFIC_FAIL_G9_REAL_SOURCE_FROZEN_SET`: the numerical G9 survivor region remains valid, CCSN morphology directly overlaps it, and the high-energy cases are blocked primarily by missing neutrino-morphology/centroid authority rather than an established physical exclusion.

## New independent issue exposed by 0091
High-energy solar transmission must be treated as a dedicated follow-on authority problem. Literature on neutrinos produced/propagating through the Sun explicitly includes charged-current absorption and neutral-current energy loss, and work on solar atmospheric neutrinos notes that higher-energy neutrinos are absorbed in the Sun. Example authority:
- Ng, Beacom, Peter & Rott, `Solar Atmospheric Neutrinos: A New Neutrino Floor for Dark Matter Searches`, arXiv:1703.10280: https://arxiv.org/abs/1703.10280

0091 does **not** quantify the optical depth on the exact Model-S G9 ray family. A new prospective gate may do so using a frozen solar density/composition profile and an external neutrino-nucleon cross-section authority. Until then no TeV-source transparent-Sun claim is authorized.

## Consequence / next admissible step
G9 is now:
- numerically surviving under the full frozen finite-source grid (0090f);
- externally non-actionable under the three prospectively selected real-source candidates (0091);
- not physically disproven.

Do not search post hoc for a fourth source under 0091. A new source census requires a new prospective selection rule. The highest-value next physics gate is an independently preregistered solar-transmission compatibility calculation for the exact G9 ray family and the frozen MeV/TeV source-energy regimes, followed only if warranted by source-morphology/centroid authority repair.

No detector/material gain, BSM gain, practical duty cycle or neutrino-supplied power is authorized by 0091.
