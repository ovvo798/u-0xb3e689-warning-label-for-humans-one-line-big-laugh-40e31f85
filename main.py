#!/usr/bin/env python3
"""Write a funny single-line safety warning label for human beings.

Writes one line (at most 160 characters) to /output/entry.txt.
Python 3 standard library only.
"""

import os

ENTRY = (
    "WARNING: This human runs on caffeine, Wi-Fi, and unearned confidence; "
    "nods along to instructions it never heard, then asks you to repeat them slowly."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
