#!/usr/bin/env python3
import json
from pathlib import Path

from nmir.se82_validation import validate_pp_source_average

# Prospective screening gate set before running hosted validation.
# The measured B(GT)=0.338(31) alone carries ~9% relative uncertainty; allow
# 15% total for the first point-Coulomb/allowed-GT reproduction. A larger
# residual blocks promotion and requires a response-convention audit.
MAX_ABS_RELATIVE_RESIDUAL = 0.15

result = validate_pp_source_average(Path('.cache/se82_pp'))
result['max_allowed_absolute_relative_residual'] = MAX_ABS_RELATIVE_RESIDUAL
result['pass'] = result['absolute_relative_residual'] <= MAX_ABS_RELATIVE_RESIDUAL
Path('artifacts/se82_pp_validation').mkdir(parents=True, exist_ok=True)
Path('artifacts/se82_pp_validation/results.json').write_text(
    json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8'
)
print(json.dumps(result, indent=2, sort_keys=True))
if not result['pass']:
    raise SystemExit('Se-82 pp source-average validation gate failed')
