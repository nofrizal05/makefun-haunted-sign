#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door — make.fun entry.

Writes one funny sign line to /output/entry.txt (created if needed).
Standard library only; the line is a plain string in this file.
"""

import os

LINE = "DO NOT ENTER. This room is haunted by a process that will not die. We tried kill -9. It sent back a thank-you note."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
