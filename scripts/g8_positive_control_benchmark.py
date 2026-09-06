#!/usr/bin/env python3

import json

from nmir.g8_positive_control import g8_positive_control


if __name__ == "__main__":
    result = g8_positive_control()
    print(json.dumps(result, indent=2, sort_keys=True))
