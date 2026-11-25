#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — make.fun entry.

Writes one line, a single joke about a meeting that should have been
an email, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library, deterministic: the same line every run.
"""

import os

ENTRY = "The meeting's only outcome was a second meeting to discuss why the first meeting should have been an email."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    with open(path, "rb") as f:
        written = f.read()
    if written.decode("utf-8") != text:
        raise SystemExit("entry.txt bytes do not match the entry")


if __name__ == "__main__":
    main()
