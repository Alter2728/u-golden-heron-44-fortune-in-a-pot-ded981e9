#!/usr/bin/env python3
"""Fortune in a Pot.

Writes one kind, funny fortune for a houseplant to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3 standard library only, deterministic. The line is
self-checked against the bounty's 120-character cap.
"""

import os

FORTUNE = "Your newest leaf will unfurl toward the morning sun, and your keeper will take full credit — let them. You knew first."

assert 0 < len(FORTUNE) <= 120, "fortune must be 1-120 characters"
assert FORTUNE.count("\n") == 0, "fortune must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
