#!/usr/bin/env python3
import json
from pathlib import Path

from nmir.se82_full_validation import validate_source_averages

# Prospective tolerances frozen before hosted execution.
# Mono/low-energy branches are stricter; high-energy continuum branches allow
# extra room for spectrum-convention and 0.5-MeV GT-bin representation.
LIMITS = {
    "pp": 0.05,
    "pep": 0.10,
    "Be7_862": 0.10,
    "Be7_384": 0.10,
    "N13": 0.15,
    "O15": 0.15,
    "F17": 0.15,
    "B8": 0.20,
    "hep": 0.20,
}

rows = validate_source_averages(Path('.cache/se82_full_validation'))
passed = True
for key, row in rows.items():
    row['max_allowed_absolute_relative_residual'] = LIMITS[key]
    row['pass'] = row['absolute_relative_residual'] <= LIMITS[key]
    passed = passed and row['pass']
result = {'components': rows, 'pass': passed, 'limits_frozen_prospectively': True}
Path('artifacts/se82_full_validation').mkdir(parents=True, exist_ok=True)
Path('artifacts/se82_full_validation/results.json').write_text(
    json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8'
)
print(json.dumps(result, indent=2, sort_keys=True))
if not passed:
    raise SystemExit('Full Se-82 source-average validation matrix failed')
