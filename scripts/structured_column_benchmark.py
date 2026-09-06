#!/usr/bin/env python3

import json

from nmir.structured_column import structured_column_gate


if __name__ == "__main__":
    print(json.dumps(structured_column_gate(), indent=2, sort_keys=True))
