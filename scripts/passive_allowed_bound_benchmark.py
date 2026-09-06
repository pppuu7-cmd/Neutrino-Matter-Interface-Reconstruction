#!/usr/bin/env python3
"""Emit the preregistered passive allowed-current stress envelope as JSON."""

from __future__ import annotations

import json

from nmir.passive_allowed_bound import known_nuclei_allowed_stress_envelope


if __name__ == "__main__":
    result = known_nuclei_allowed_stress_envelope()
    print(json.dumps(result, indent=2, sort_keys=True))
