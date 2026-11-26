"""Lost sock status update: print the one-line entry.

Reads entry.txt next to this script, strips it, prints it. When
MAKEFUN_OUTPUT_DIR is set, writes a copy of entry.txt there instead
of writing next to the script (the grader mounts the repo read-only).
"""

import os
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8").strip()
    if not text:
        print("entry.txt is empty", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        Path(out_dir).mkdir(parents=True, exist_ok=True)
        (Path(out_dir) / "entry.txt").write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
