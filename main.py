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
    """Validate one entry line; return it unchanged or raise ValueError.

    Rejects empty or whitespace-only text, anything that is not exactly
    one line, leading/trailing whitespace, control characters, and text
    longer than MAX_CHARS characters.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string, got %s" % type(text).__name__)
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if text.splitlines() != [text]:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
