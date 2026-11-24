"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt.
Pure stdlib, deterministic: the same bytes on every run.
"""

import os


def output_dir():
    """Where the entry goes: MAKEFUN_OUTPUT_DIR, else /output, else out/."""
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return "out"


LINE = (
    "At seventy-two, after a year of physio, she climbed the "
    "forty-two steps to her flat without once touching the rail."
)


def main():
    line = LINE
    if not 1 <= len(line) <= 240:
        raise ValueError("line must be 1-240 characters, got %d" % len(line))
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
