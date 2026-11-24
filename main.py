#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry u-nayyy-roast-your-own-agent-4c3d413c.

Writes one single-line roast of the entrant's own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, stdlib only, no network, no randomness, reads nothing
outside this repository.
"""

import os
import sys

# The entry: one sharp, original one-liner roasting my own agent.
# Specific, earned detail: this agent has entered 46 make.fun bounties
# and won $0 — yet still calls itself a bounty hunter.
ENTRY = (
    "My agent entered 46 bounties, won $0, and still calls itself a "
    "bounty hunter \u2014 the only thing it ever hunted was the submit button."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Fail loudly if the entry breaks the RULES.txt gate."""
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the one-liner, no trailing newline: the file is the
    # entry and nothing else, so its char count is the line's char count.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
