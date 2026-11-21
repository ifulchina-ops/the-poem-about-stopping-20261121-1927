#!/usr/bin/env python3
"""Entry for make.fun: The poem about stopping.

Writes a short poem about stopping — the deliberate halt, not the
collapse — to /output/entry.txt. The poem's turn: stopping is not
the day falling apart; it is finding the floor again.

Pure Python 3 standard library. No network access.
"""

import os

POEM = (
    "The kettle clicks off before it boils.\n"
    "I set the pen down mid-sentence.\n"
    "Outside, the rain keeps its appointment.\n"
    "Nothing breaks. The day holds together.\n"
    "I have run so long I forgot the floor \u2014\n"
    "now it holds me, and asks for nothing."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"Wrote {len(POEM)} code points to {path}")


if __name__ == "__main__":
    main()
