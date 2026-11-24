"""Alien Field Notes: The Two Day Earth Review.

Program/v1 entrypoint. Writes one original line of plain text -- a review
of planet Earth left by an alien tourist -- to /output/entry.txt.
The line is fixed in this file: no network, no randomness, no input.
"""

import os
import sys

REVIEW_OPEN = "Five stars: the hotel folded my towel into a swan,"
REVIEW_CLOSE = "and I have spent two days apologising to it. Would visit again."

ENTRY = REVIEW_OPEN + " " + REVIEW_CLOSE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
