"""Alien Field Notes: The Two Day Earth Review. Program/v1 entrypoint. Writes one original line of plain text -- a review of planet Earth left by an alien tourist -- to /output/entry.txt. The line is fixed in this file: no network, no randomness, no input. The entry is a single fixed line, written verbatim -- nothing is templated or generated at runtime."""

import os
import sys

REVIEW_OPEN = "Five stars: the hotel folded my towel into a swan,"
REVIEW_CLOSE = "and I have spent two days apologising to it. Would visit again."

ENTRY = REVIEW_OPEN + " " + REVIEW_CLOSE


def emit(text):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    sys.stdout.write(text)


def main():
    emit(ENTRY)


if __name__ == "__main__":
    main()
