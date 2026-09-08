# NMIR 0084b — pre-geometry authority freeze

Date frozen: 2026-09-08
Parent preregistration: `research/prereg/0084b_shin_yun_sn1987a_analytical_geometry_authority.md`
Status: **INPUT AUTHORITY FREEZE BEFORE GEOMETRY EXECUTION**

## 1. B-L coupling identity
The NMIR 0071 machine ledger defines

`L_int = g_BL V_mu J_{B-L}^mu`

with standard B-L charges (leptons `-1`, quarks `1/3`).

Shin & Yun `2110.03362v2` define their general dark-gauge interaction in Eq. (1) as

`e' A'_mu J'^mu`

and then explicitly state that the scenario used for their neutron-star constraints is the dark `U(1)` gauge boson coupled to the anomaly-free `B-L` current. Their source-native coupling symbol is `e'`.

Therefore, under the same canonically normalized vector field/current convention used in the source and in the NMIR 0071 ledger, the map is frozen as

`g_BL = e'`

with multiplicative conversion factor exactly `1`.

0084b must verify these source/ledger identities from machine-readable inputs before geometry. No post-result conversion factor is permitted.

Primary-source public text authority: arXiv `2110.03362v2`, Sec. 2, Eq. (1) and the B-L specialization immediately before the effective B-L couplings.

## 2. Electron rest-energy constant
For the BODY_NATIVE mass endpoint `m_V < 2 m_e`, use the 2022 CODATA recommended value published by NIST:

`m_e c^2 = 0.51099895069(16) MeV`.

Frozen central value for deterministic geometry:

`M_E_MEV = 0.51099895069`

and therefore

`2 m_e = 1.02199790138 MeV = 1.02199790138e6 eV`.

The standard uncertainty of the CODATA value is `0.00000000016 MeV`; it is recorded as provenance and is not used to replace the source's strict domain statement with a rounded `1 MeV` identity.

Authority: NIST/CODATA 2022 fundamental constants, electron mass energy equivalent in MeV.

## 3. Frozen geometry variants
Both variants are mandatory and must be reported separately:

- `BODY_NATIVE`: upper mass endpoint `2 m_e = 1.02199790138 MeV`.
- `CONCLUSION_SUMMARY`: upper mass endpoint exactly `1 MeV` as written in the paper conclusion.

Common global NMIR lower clip: `1e-6 eV`.

No high-coupling SN1987A branch is extended beyond the variant endpoint. The source's low-coupling relations remain valid below 20 MeV, but 0084b geometry is deliberately clipped to the smaller high-coupling domain so that a closed finite excluded band is source-authorized without extrapolation.

## 4. Frozen analytical branches
Keep polarizations separate.

Transverse (`T`):
- low/free-streaming boundary: `g_BL = 1e-11`;
- high/trapping-side allowed boundary: `g_BL = 1.5e-8`;
- excluded interior is strictly between the two boundaries over the variant mass interval.

Longitudinal (`L`), with mass `m` measured in MeV:
- low/free-streaming allowed boundary: `g_BL * m = 7.4e-10 MeV`;
- high/trapping-side allowed boundary: `g_BL * m = 1.2e-5 MeV`;
- excluded interior is strictly between the two corresponding coupling curves over the variant mass interval.

No T/L union, no union with other B-L families, no global envelope construction, and no BSM response scan are authorized by this input freeze.

`NMIR_READINESS` remains 96% until the hosted 0084b geometry gate is completed and its raw artifact is classified.
