# Grocery List — Builds a case-insensitive grocery list and prints sorted item counts in uppercase.

import sys

grocery = {}
while True:
    try:
        item = input().lower()
        grocery[item] = grocery.setdefault(item, 0) + 1
    except EOFError:
        for key, value in sorted(grocery.items()):
            print(f"{value} {key.upper()}")
        sys.exit()