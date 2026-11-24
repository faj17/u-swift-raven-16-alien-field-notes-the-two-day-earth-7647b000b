"""Alien field notes: a two-day Earth hotel review.

A single fixed review line, emitted verbatim to a file and to stdout.
The text is fixed at authoring time; nothing is fetched, randomised, or read from input at run time.
"""

import os

ENTRY = "Five stars: the hotel folded my towel into a swan, and I have spent two days apologising to it. Would visit again."

OUTPUT_PATH = "/output/entry.txt"


def emit(text):
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text, end="")


def main():
    emit(ENTRY)


if __name__ == "__main__":
    main()
