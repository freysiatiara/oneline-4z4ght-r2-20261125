#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry, round 2.

Writes a single funny line of text to /output/entry.txt.

The line (89 characters, two beats: setup -> reframe -> kicker):
  "My GPS rerouted me past my ex's street three times; even
   satellites think I need closure."

Beat 1 sets up a mundane GPS reroute. Beat 2 reframes the satellites
as amateur therapists who have diagnosed the driver. The mechanism is
original: navigation hardware staging an intervention, not a re-skin
of any neighbouring entry.

Standard library only. No network, no secrets, no input files.
"""

import os

ENTRY = (
    "My GPS rerouted me past my ex's street three times; "
    "even satellites think I need closure."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 140


def _validate(text):
    """Guard the gate before anything is written: 1-140 chars, one line."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")


def main():
    text = ENTRY
    _validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("written entry does not match the entry text")


if __name__ == "__main__":
    main()
