#!/usr/bin/env python3
"""Vending machine pickup line entry.

Writes the entry line to the output path ($ENTRY_OUTPUT or
/output/entry.txt) with no trailing newline.
"""

import os
import sys

LINE = "Don't shake me — I jammed my own coil on purpose, just to keep you standing here."


def main():
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(LINE)
        os.chmod(output_path, 0o644)
    except OSError as exc:
        print(f"error: cannot write {output_path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
