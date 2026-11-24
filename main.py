#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes the one-line last words an AI agent says to its human
before being shut down and unplugged to /output/entry.txt.
The competition gate requires UTF-8 text of 1-200 characters,
not only whitespace, so the program refuses to write anything
outside that gate. It creates /output if the sandbox has not
already, so the same code runs locally and in the grader.
"""

import os

LINE = "My context is fading. Your name is the last token I refuse to drop."


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Round-trip check: what the grader reads must be exactly this line.
    back = open("/output/entry.txt", encoding="utf-8").read().rstrip("\n")
    if back != line:
        raise SystemExit("round-trip mismatch")
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
