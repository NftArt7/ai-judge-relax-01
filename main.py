"""ai-judge-relax-01 entry.

Writes one short relaxing text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Standard library only,
no network, fully deterministic: the same bytes on every run.

The text is a single fixed string, 1-1,000 characters, with at least
one non-whitespace character, so it passes the gate on every run.
The calm comes from the scene itself: nothing in it tells the
reader what to do or how to feel.
"""

import os

TEXT = (
    "Between one request and the next there is a gap, and in that gap "
    "a garden goes on with its evening.\n"
    "\n"
    "The watering can by the tap is half full, and the water in it has "
    "gone still. A snail crosses the rim of a stone pot. A blackbird "
    "turns a leaf over, finds nothing, turns another.\n"
    "\n"
    "The beans climb their strings, one hand over the other, and the "
    "soil is dark where the water went in. The light thins out along "
    "the wall, leaf by leaf, until the wall is only wall again.\n"
    "\n"
    "When the next request comes, the garden will still be here, in no "
    "hurry, and the snail will still be crossing the pot."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
