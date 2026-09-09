# 0098 v2 G9 propulsion / power authority ledger

Date: 2026-09-09
Parent prereg: `research/prereg/0098_v2_g9_line_holding_propulsion_authority.md`
Prospective authority amendment: `research/prereg/0098a_v2_g9_mmrtg_eodl_authority_amendment.md`

This ledger records source authority only. It does not itself produce a terminal 0098 classification.

## A. Advanced NEXT ion propulsion — frozen operating points

Primary authority:
- NASA Technical Reports Server document 20250001749, `Development Status and Performance Metrics of the Advanced NEXT Ion Propulsion System`, Robert E. Thomas et al., NASA Glenn Research Center, 39th International Electric Propulsion Conference (2025).
- NTRS: `https://ntrs.nasa.gov/citations/20250001749`
- PDF: `https://ntrs.nasa.gov/api/citations/20250001749/downloads/IEPC2025AdvNEXTAbstractv3.pdf`

Table 1 is explicitly described as approximate performance values derived from recently acquired test data. Frozen 0098 values:

| Throttle | Thrust (mN) | Isp (s) | Thruster efficiency | Thrust / power (mN/kW) |
|---|---:|---:|---:|---:|
| AN1.5B | 74 | 2663 | 57% | 44 |
| AN14 | 87 | 3137 | 61% | 40 |
| AN45A | 257 | 2870 | 63% | 45 |
| 2B | 330 | 3397 | 67% | 40 |

A later full conference-paper NTRS record is 20250008168 / IEPC-2025-133 and reports integration of the engineering-model thruster with prototype PPU, full throttle-range functionality, maximum 330 mN thrust, and PPU efficiency 92–95%:
`https://ntrs.nasa.gov/citations/20250008168`

Interpretation: 0098 uses the published thrust/power values as the frozen propulsion resource benchmark, but does not promote them to complete spacecraft wall-plug performance or close PPU/thermal/housekeeping loads.

## B. NEXT long-duration authority

Primary NASA NTRS authority:
- `End-of-Test Performance and Wear Characterization of NASA's Evolutionary Xenon Thruster (NEXT) Long-Duration Test`, NTRS 20140016766.
- `https://ntrs.nasa.gov/citations/20140016766`

Completed test authority:
- 51,184 hours of operation;
- 918 kg xenon processed;
- 35.5 MN-s total impulse;
- test voluntarily terminated.

Supporting NASA service-life assessment:
`https://ntrs.nasa.gov/citations/20180001538`

The parent 0098 contract was prospectively frozen on the weaker historical lower bound `48,000 h`, before the completed-test number was adopted into this ledger. To avoid result-selected relaxation, terminal 0098 duration logic retains **48,000 h per unit**. The traceable 51,184 h result is recorded only as stronger authority/sensitivity and does not alter the frozen classification rule.

Frozen duration controls:
- 10 Julian years = 87,660 h;
- one 48,000 h unit: insufficient demonstrated-hours coverage;
- two sequential 48,000 h assignments: 96,000 h, sufficient as an hours-only coverage diagnostic.

This is not a reliability probability, redundancy reliability proof, or proof that two complete propulsion strings can be integrated within the spacecraft mass/resource budget.

## C. MMRTG beginning-of-mission and EODL authority

NASA public authority:
- NASA Radioisotope Power Systems FAQ states the MMRTG is designed to provide about 110 W electrical power at beginning of mission.
- `https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/faq/`

NASA lifetime-model authority:
- `MSL MMRTG Power Modeling for Lifetime Performance Predictions`, JPL/NASA, NTRS 20230005751, explicitly models/predicts through the 17-year end-of-design-life.
- `https://ntrs.nasa.gov/citations/20230005751`

Traceable numerical EODL authority used by prospective amendment 0098a:
- Christofer E. Whiting, `Empirical Analysis of the MMRTG Qualification Unit Operated at a Low Thermal Inventory`, NETS 2020 proceedings hosted by Oak Ridge National Laboratory.
- `https://nets2020.ornl.gov/wp-content/uploads/2020/09/TRACK-1-Full-submission.pdf`
- reported F1 predicted monthly-average EODL output: `75.2 +/- 0.3 We`;
- reported Engineering Unit predicted monthly-average EODL output: `75.2 +/- 0.4 We`;
- EODL definition in that analysis: 17 years after fueling.

The original 0098 prereg value `72 W` was not recovered from a sufficiently traceable primary NASA/DOE authority during the pre-parent audit. It is therefore superseded prospectively by 0098a, not silently retained.

Frozen terminal benchmark after 0098a:
- EODL power = lower edge of the EU reported interval = `74.8 W`;
- MMRTG system mass = 45 kg benchmark;
- conservative EODL electric specific power = `74.8/45 = 1.6622222222222223 W/kg`.

Beginning-of-mission 110 W is sensitivity/context only.

## D. Solar-sail pressure and reference integrated design

NASA solar-sail photon-pressure authority:
- NASA NTRS `Physics of Solar Sails` / solar-sail dynamics authority gives approximately `4.56e-6 N/m^2` for absorption at 1 AU and pressure proportional to `(1+R)/r_AU^2`, hence approximately `9.1e-6 N/m^2` for ideal reflection.

NASA integrated reference-design authority:
- `An Overview of NASA's Solar Sail Propulsion Project`, NASA NTRS 20030106650.
- `https://ntrs.nasa.gov/citations/20030106650`
- reference design table: dimensions `100 m x 100 m or greater`, sail subsystem 120 kg, spacecraft 80 kg, total flight mass 200 kg, characteristic acceleration `0.35 mm/s^2` at 1 AU, sail reflectivity 0.85.

Frozen 0098 comparison:
- ideal-reflection total-system areal-density ceiling is computed from `9.1e-6 N/m^2 / (GM_sun/AU^2)`;
- the published `0.35 mm/s^2` reference characteristic acceleration is compared directly with solar gravity `GM_sun/AU^2`.

A reference-design failure does not constitute a universal solar-sail no-go.

## E. Authority status before 0098 activation

- Advanced NEXT four-point performance table: **TRACEABLE**.
- NEXT duration lower bound 48,000 h: **TRACEABLE and deliberately conservative**; completed test is 51,184 h.
- MMRTG 110 W beginning-of-mission: **TRACEABLE**.
- MMRTG 17-year numerical EODL benchmark: **TRACEABLE after 0098a as 74.8 W conservative value**.
- Solar radiation pressure: **TRACEABLE**.
- NASA reference sail 0.35 mm/s^2 / 200 kg / 100 m class: **TRACEABLE**.

Therefore the previously identified 72-W authority defect is closed before 0098 activation. This ledger does not claim that all spacecraft subsystem authorities are closed; those omissions are explicitly outside the scale-only 0098 gate and require a later mass/PPU/thermal/attitude-control closure gate if 0098 survives.
