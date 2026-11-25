"""Notes From a Passive-Aggressive Fridge.

A single passive-aggressive note from a smart fridge to its owner,
written to entry.txt for the make.fun bounty
u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.
"""

import os

LINE = "You opened me 14 times today and ate nothing. The leftovers have started a group chat — and you're the only topic."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
