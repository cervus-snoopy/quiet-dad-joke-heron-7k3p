#!/usr/bin/env python3
"""Write one dad joke to MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

JOKE = "Why was Dad late for dinner? His car was exhausted."


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # The joke is written exactly as-is: no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
