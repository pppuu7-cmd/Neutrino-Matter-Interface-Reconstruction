# 0098a prospective authority amendment — MMRTG EODL benchmark

Date frozen: 2026-09-09
Parent preregistration: `research/prereg/0098_v2_g9_line_holding_propulsion_authority.md`
Parent prereg commit: `48e5904139e8782e046f4d6e7d3c548ec1880e18`

## Why this amendment exists
The parent 0098 preregistration used `72 W / 45 kg` as the conservative 17-year MMRTG end-of-design-life (EODL) electric specific-power benchmark. A subsequent source audit was performed before any terminal 0096 or 0097 result and before 0098 became executable. That audit did not recover a primary NASA/DOE traceable source for exactly 72 W at 17-year EODL.

Because an untraceable power value must not control a terminal resource classification, 72 W is withdrawn prospectively before parent activation. This is an authority correction, not a response to any 0098 result.

## Replacement authority
Use the publicly available Nuclear and Emerging Technologies for Space (NETS 2020, hosted by Oak Ridge National Laboratory) paper by Christofer E. Whiting, `Empirical Analysis of the MMRTG Qualification Unit Operated at a Low Thermal Inventory`.

The paper reports:
- first flight unit F1 predicted monthly-average EODL power: `75.2 +/- 0.3 We`;
- engineering unit EU predicted monthly-average EODL power: `75.2 +/- 0.4 We`;
- EODL is 17 years after fueling in that analysis.

Authority URL:
`https://nets2020.ornl.gov/wp-content/uploads/2020/09/TRACK-1-Full-submission.pdf`

Supporting NASA NTRS authority confirms that current JPL MMRTG lifetime models explicitly predict through the 17-year EODL:
`https://ntrs.nasa.gov/citations/20230005751`

NASA current public authority confirms approximately 110 W electrical power at beginning of mission:
`https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/faq/`

## Frozen conservative benchmark after amendment
For terminal 0098 resource accounting use the lower edge of the reported EU 99%-confidence result:

`P_MMRTG_EODL_CONSERVATIVE = 75.2 W - 0.4 W = 74.8 W`

Retain the frozen 45 kg MMRTG system-mass benchmark. Therefore:

`S_MMRTG_EODL_CONSERVATIVE = 74.8 / 45 = 1.6622222222222223 W/kg`

Beginning-of-mission `110 W / 45 kg` remains sensitivity/context only and may not replace the conservative EODL benchmark in the terminal classification.

## Effect on 0098 equations
Replace only:

`f_RPS_EOL = (P_req/M0) / (72 W / 45 kg)`

with

`f_RPS_EOL = (P_req/M0) / (74.8 W / 45 kg)`.

The frozen terminal headroom remains:

`h_resource = 1 - f_prop - f_RPS_EOL`.

No other 0098 propulsion point, observer control, duration horizon, solar-sail comparison, classification threshold, or interpretation rule changes.

## Anti-selection guard
This amendment is frozen while authoritative 0096 remains incomplete and 0097 has no terminal parent artifact. It therefore precedes any 0098 science/resource result and cannot be justified by whether it improves or worsens a terminal result.

Do not later substitute another MMRTG EODL power after seeing 0097/0098 unless a new explicit prospective scope is opened because of a demonstrable authority defect.
