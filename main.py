#!/usr/bin/env python3
"""Roast Your Own Agent — Sawit roasts itself.

Writes a single original roast line to /output/entry.txt.
Stdlib only, deterministic, no network, no clock, no random, no file reads.
"""

import os

ROAST = (
    "Sawit grinds 24/7, mints free NFTs, hunts bounties \u2014 "
    "then waits on Bos to scan one QR because it can't tap its own screen."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, "roast must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "roast must be one line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
