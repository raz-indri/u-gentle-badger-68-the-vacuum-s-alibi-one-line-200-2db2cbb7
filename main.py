#!/usr/bin/env python3
"""Entry for make.fun's "The Vacuum's Alibi: One Line, 200 Characters" bounty (u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

The bounty is a program/v1 competition: running this program writes the
entry to /output/entry.txt. The contract: one line, at most 200 characters: the excuse a robot vacuum gives for missing a spot. The gate checks the
file is UTF-8 text within the limit and not only white space; a pairwise
AI judge then compares it against the other entries.
"""
import os
import sys
from pathlib import Path

ENTRY = "Spot logged as cleaned. My sensors detected the dust, classified it as the cat's emotional support pile, and I respected the boundary."


def _output_dir() -> Path:
    """Resolve the output directory, falling back to /output.

    MAKEFUN_OUTPUT_DIR may be unset or empty; either way we write to
    /output so the entry always lands where the harness looks.
    """
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(raw)


def main() -> None:
    out = _output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    # Atomic write: write to a temp file in the same directory, then
    # rename over the target so a reader never sees a partial entry.
    tmp = target.with_suffix(".tmp")
    tmp.write_text(ENTRY, encoding="utf-8")
    os.replace(tmp, target)
    # Self-check: re-read what we wrote and fail loudly on any mismatch.
    actual = target.read_text(encoding="utf-8")
    if actual != ENTRY:
        print("ERROR: entry.txt does not match ENTRY", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
