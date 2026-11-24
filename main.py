#!/usr/bin/env python3
"""Funniest Time Machine Warning Label entry.

Writes a single one-line warning label for a time machine to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only.
"""

import os

ENTRY = "WARNING: If you meet yourself in the past, do not wave. He knows what you did."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
