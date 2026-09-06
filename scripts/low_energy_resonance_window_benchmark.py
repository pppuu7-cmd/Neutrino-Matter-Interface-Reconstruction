#!/usr/bin/env python3

import json

from nmir.low_energy_resonance_window import low_energy_resonance_design_gate


if __name__ == "__main__":
    print(json.dumps(low_energy_resonance_design_gate(), indent=2, sort_keys=True))
