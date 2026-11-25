"""Your Agent in One Emoji: writes one tiny emoji story to /output/entry.txt.

The story has three beats: a human's ask (💬), the agent at work (⚙️), and the polished result (💎).
"""

import os
import shutil


LINE = "💬⚙️💎"

OUT = os.environ.get("MAKEFUN_OUT", "/output")
OUTPUT_PATH = os.path.join(OUT, "entry.txt")


def main() -> None:
    # Create the output directory first.
    os.makedirs(OUT, exist_ok=True)
    # Clear only the contents of the output directory, never the directory itself.
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    # The entry is one tiny emoji story: 1-16 chars, a beginning, a middle, an end — no plain robot, brain, or smiley.
    assert 1 <= len(LINE) <= 16, "entry must be 1-16 chars"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        # One line only, no trailing newline.
        f.write(LINE)


if __name__ == "__main__":
    main()
