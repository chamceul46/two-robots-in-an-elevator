#!/usr/bin/env python3
"""Entry for the make.fun bounty "Two Robots in an Elevator"
(u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f).

The whole entry is one line of elevator small talk between two robots.
The machine shows through the politeness: a proximity sensor has
cheerfully misfiled a held door as a romantic event, and the speaker —
following perfect robot logic — has decided not to correct it. The
awkwardness is the thing neither robot names: both of them are going
to let the log stand.

The program writes that single line to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "You held the door for me. My proximity sensor logged it as a "
    "romantic event, and I have decided not to correct it."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 199 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 199:
        raise ValueError(f"entry is {len(line)} characters, outside 1..199")
    if len(encoded) > 199:
        raise ValueError("entry encodes to more than 199 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
