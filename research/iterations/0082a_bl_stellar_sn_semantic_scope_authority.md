# NMIR iteration 0082a — B-L stellar/SN semantic and scope authority

Date: 2026-09-08
Classification: **PASS_B_L_STELLAR_SN_SEMANTIC_SCOPE_AUTHORITY**
Prospective contract: `research/prereg/0082a_bl_stellar_sn_semantic_scope_authority.md`, frozen commit `3c978de292d259e8beacbe0cfed6c0dd474e498b`.

## Result
Exact TeX/source semantics from the three 0082-authorized archives deterministically identify the source-native B-L constraint-summary figures and native parameter conventions needed for the next vector-only audit. No PDF path/color geometry was inspected.

### Hong–Shin–Yun 2021
- Exact source: `2012.05427v3`, archive SHA256 `6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc`.
- Controlling B-L constraint summary: `B-LConstraints.pdf`, label `fig:B-LConstraints`.
- Caption/source semantics explicitly include Cas A rapid-cooling exclusion, NS1987A context, earlier SN1987A cooling constraints and other external constraints.
- Native B-L gauge-coupling notation is `e'` in this source; native gauge-boson mass notation is `m_{gamma'}`/equivalent TeX form. No conversion to another paper's coupling convention is performed here.
- Cooling-curve/hint assets are not constraint-geometry authority merely because they are B-L related.

### Cerdeño et al. 2021
- Exact source: `2106.11660v3`, archive SHA256 `f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d`.
- Controlling B-L constraint summary: `Figures/BL_constraints.pdf`, label `fig:vector_constraints`.
- Source explicitly states a `U(1)_{B-L}` vector mediator with one independent coupling `g_{B-L}`; quarks carry `g_{B-L}/3` and charged/neutral leptons `-g_{B-L}`. Vector mediator is `Z'` with mass `m_{Z'}`.
- `Figures/medium_effects_BL.pdf` is preserved as a medium-effect diagnostic, not the final excluded-geometry control asset.

### Shin–Yun 2022
- Exact source: `2110.03362v2`, archive SHA256 `7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd`.
- Controlling B-L constraint summary: `B-L_Constraints.pdf`, label `fig:bound`.
- Caption/source semantics explicitly identify:
  - revisited SN1987A transverse exclusion;
  - a newly excluded longitudinal region;
  - a separately derived stringent NS1987A constraint;
  - Cas A as a current external constraint, not as a result explicitly replaced by this paper.
- Native B-L gauge-coupling notation is `e'`; native gauge-boson mass notation is `m_{gamma'}`/equivalent TeX form.
- Under the frozen revision parser, source text supports revisiting the SN1987A and NS1987A constraint branches, but does not authorize generic replacement of Cas A or all young-neutron-star cooling authority.

## Hosted provenance
- Scientific run/job: `34167424919 / 101881140465`
- Head SHA: `ff111f4f09ace38cd9cae83309a8726e97b938c2`
- Artifact: `10034602959`
- Dedicated tests: `5 passed in 0.06s`
- Raw JSON SHA256: `333c79aaa14170777ac68b8754c8f9b03e8929cef803c5989d95b19ed0862e9c`
- Artifact ZIP SHA256: `f11ef6a5138b0766cabe94b5a8bf55c60859acf355f48b84d75ded19e55eb0ef`
- Artifact ZIP and inner JSON hashes were independently verified after download.
- Baseline CI on the same head: run `34167424840`, `success` (`pytest` and `nmir.baseline`).

## Interpretation
0082a closes the semantic/source-scope ambiguity needed to choose the correct final constraint-summary assets prospectively. It also prevents a physically incorrect blanket supersession: Shin–Yun 2022 updates the explicitly revisited SN1987A/NS1987A branches but does not, from the audited wording, automatically erase Hong's Cas-A/other young-NS authority.

This is still not a numerical excluded-region materialization. Coupling equivalence across papers remains to be audited explicitly if needed.

## Guards preserved
- No PDF drawing/path/color inspection.
- No axis calibration or point extraction.
- No manual/raster digitization.
- No cross-paper union/intersection.
- No generic Cas-A/young-NS supersession.
- No cross-paper coupling conversion without explicit source identity.
- No global B-L envelope or BSM response scan.

## Next gate
0082b must inspect **only** the three prospectively selected final constraint-summary assets:
1. Hong `B-LConstraints.pdf`;
2. Cerdeño `Figures/BL_constraints.pdf`;
3. Shin–Yun `B-L_Constraints.pdf`.

0082b is limited to vector integrity, text extraction, native axis identity and tick-anchor sufficiency. It must not select source-own curves by color/path or construct excluded polygons. Those require a separate subsequent gate.

`NMIR_READINESS: 94%` — unchanged until a new stellar/SN excluded region is reproducibly materialized.
