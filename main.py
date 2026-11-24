#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry -- one single-line safety warning label for every human
being, at most 160 characters -- to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs).

Deterministic: the same fixed text on every run. Standard library only;
no network, no randomness, no input.
"""

import os
from pathlib import Path

LABEL = "WARNING: This human has been 'about to reply' to your message since Tuesday. Do not hold your breath."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = LABEL.strip()
    assert 1 <= len(text) <= 160, f"label is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "label must be a single line"
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
