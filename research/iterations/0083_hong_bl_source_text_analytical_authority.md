# NMIR iteration 0083 — Hong–Shin–Yun B-L source-text analytical authority

Date: 2026-09-08
Prospective contract: `research/prereg/0083_hong_bl_source_text_analytical_authority.md`, frozen commit `d03a50e0ae2c1f83b5327b5c47d71fc3106fe525`.
Final classification: **PASS_HONG_B_L_SOURCE_TEXT_ANALYTICAL_ANCHOR / BLOCKED_HONG_B_L_EXACT_FINITE_MASS_TEXT_AUTHORITY**
`NMIR_READINESS: 94%`.

## Question
After the 0082c vector-geometry route closed as BLOCKED, can the exact Hong–Shin–Yun `2012.05427v3` source TeX provide primary-source numerical B-L cooling bounds without raster/manual contour reading, and does the same text provide an exact finite mass endpoint suitable for geometric materialization?

Frozen source archive SHA256: `6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc`.

## Hosted provenance
Authoritative successful run:
- run `34169172908`
- job `101886047546`
- head `cada605f9528b27d69fd720a5f034c5920e3971f`
- artifact `10035135738`
- GitHub artifact ZIP digest `sha256:d735c27d144a0b1474a42ea7aa924f44074f15eac02dedf9c597c762e0e636e2`
- independently downloaded ZIP SHA256: `d735c27d144a0b1474a42ea7aa924f44074f15eac02dedf9c597c762e0e636e2`
- raw JSON SHA256: `6cb7e42b867d4263fef15c8b36c89f97d3e6093826f6c41b33a8eac9226a0574`
- exact TeX inventory: one file, `draft.tex`.

Dedicated regression tests and the frozen audit both passed. The workflow enforcement step also passed.

## Historical infrastructure failures retained
1. run/job `34169010025/101885588842`: regression-test failure before the scientific audit because an exact-mass synthetic fixture used a LaTeX unit wrapper not normalized by the implementation. No scientific result.
2. run/job `34169076021/101885774865`, artifact `10035107467`: tests and audit executed, but JSON serialization failed because a Python `re.Match` escaped into the result structure. This is infrastructure failure, not scientific authority. Its partial diagnostic output also exposed that the parser had incorrectly been hard-coded around one public-abstract value, so the implementation was corrected to extract arbitrary explicit source-native numeric upper bounds without changing the preregistered scientific contract.

## Authoritative source-text findings
The exact source archive contains at least two explicit B-L numerical upper-bound levels, and they are not safe to collapse into one unconditional number:

### 1. General/abstract low-mass cooling statement
The source TeX abstract states that, for dark gauge-boson mass below `O(0.1 MeV)`, the `U(1)_{B-L}` coupling to nucleons/electrons is bounded at

`e' < 5e-13`.

The same abstract separately mentions a possible Cas A hint around eV-scale mass and `e' ~ 1e-13`.

### 2. Explicit Cas A equation-level branch
The body gives the source-labelled Cas A result

`e' < 1e-13`

(`eq:B-L_keyresult`) when the mediator mass is below the neutron-triplet critical-temperature scale `T_c(n^3 P_2)=O(0.1 MeV)` **and** `eta = 1e-13`. The source further states that within that low-mass branch the bound has no mass dependence because the B-L gauge boson couples to neutrons without the dark-photon plasma-screening suppression.

### 3. Envelope/composition-dependent Cas A branch
Later source text states that `e' < 5e-13` causes little alteration of the standard cooling curve in the cited low-mass regime, and that the interval

`1e-13 < e' < 5e-13`

can be further excluded by Cas A if `eta < 1e-11`. Conversely, for larger `eta` in the source-stated range, the same rapid-cooling observation can be discussed as a possible B-L hint rather than as the same exclusion branch.

The machine audit therefore reports distinct source-native upper-bound values `[1e-13, 5e-13]`.

## Scientific interpretation
✅ **Analytical source-text authority passes.** There is primary-source, machine-readable authority for B-L low-mass cooling constraints without using figure geometry.

🟡 **A single unqualified Hong global bound is NOT yet authorized.** The `1e-13` and `5e-13` statements have different local assumptions/roles. They must first be separated into source-defined observational/`eta`/constraint-vs-hint branches.

🟡 **Exact finite-mass materialization is BLOCKED.** The controlling B-L mass applicability is expressed through `T_c(...)=O(0.1 MeV)`, not as a source-authorized exact numerical endpoint. The frozen contract forbids replacing `O(0.1 MeV)` by the exact coordinate `0.1 MeV`. Therefore no text-derived finite-area polygon is authorized by 0083.

This means 0083 improves the external-constraint ledger qualitatively but does not yet add a new geometric excluded area and does not unlock BSM response calculations.

## Exact next gate
Prospectively preregister 0083a as a **Hong source-text branch/scope identity gate**. It must associate each distinct numerical B-L statement with its source-native tuple:
- observation/source: Cas A / NS1987A / general young-NS statement;
- `eta` condition or interval if explicit;
- role: robust constraint, conditional additional exclusion, standard-cooling compatibility ceiling, or possible hint;
- approximate mass-domain text;
- source equation/section label when present.

Only source text may be used. PASS may authorize scenario-qualified analytical anchors; it still may not create exact finite-mass area. After Hong branch identity, the later Shin–Yun `2110.03362v2` source text should be audited for exactly which SN1987A/NS1987A branches it revises, while Cas A remains separately scoped unless primary authority states otherwise.

## Guards
No raster/OCR/manual contour reading. No conversion of `O(0.1 MeV)` to an exact endpoint. No selection of the stronger `1e-13` value as a universal bound merely because it is numerically tighter. No union/supersession across Hong/Cerdeño/Shin–Yun without dedicated primary-source authority. No finite-mass continuation of the 0079a fifth-force asymptote. No BSM response/enhancement scan before the external envelope is separately unlocked.
