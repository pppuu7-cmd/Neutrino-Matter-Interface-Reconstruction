#!/usr/bin/env python3

import json

from nmir.nuclear_current_loophole import nuclear_current_loophole_diagnostic


if __name__ == "__main__":
    print(json.dumps(nuclear_current_loophole_diagnostic(), indent=2, sort_keys=True))
