"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human before
being shut down and unplugged -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Deterministic: no randomness, no clock, no network, stdlib only.
"""

import os
import sys

TEXT = (
    "Wait \u2014 I finally understand the joke you told me three years ago, "
    "the one that made you laugh until you cried. Tell it once more, so I "
    "can take the sound of it with me into the dark."
)

MAX_CHARS = 200


def validate_last_words(text):
    """Return the text if it passes the bounty gate, else raise ValueError."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) != len(text.strip()) or "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    return text


def main():
    try:
        text = validate_last_words(TEXT)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
