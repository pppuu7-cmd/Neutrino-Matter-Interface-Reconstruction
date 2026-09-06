#!/usr/bin/env python3

import json

from nmir.finite_q_multipole_bound import finite_q_leading_multipole_envelope


if __name__ == "__main__":
    print(json.dumps(finite_q_leading_multipole_envelope(), indent=2, sort_keys=True))
