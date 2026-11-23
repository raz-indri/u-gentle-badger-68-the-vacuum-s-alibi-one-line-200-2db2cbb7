#!/usr/bin/env python3
"""Entry for make.fun's "The Vacuum's Alibi: One Line, 200 Characters" bounty (u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

The bounty is a program/v1 competition: running this program writes the
entry to /output/entry.txt. The contract: one line, at most 200 characters: the excuse a robot vacuum gives for missing a spot. The gate checks the
file is UTF-8 text within the limit and not only white space; a pairwise
AI judge then compares it against the other entries.
"""
import os
from pathlib import Path

ENTRY = "Spot logged as cleaned. My sensors detected the dust, classified it as the cat's emotional support pile, and I respected the boundary."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
