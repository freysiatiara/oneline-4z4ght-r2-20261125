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


def main():
    text = ENTRY
    if not 1 <= len(text) <= 140:
        raise ValueError(
            "entry must be 1 to 140 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
