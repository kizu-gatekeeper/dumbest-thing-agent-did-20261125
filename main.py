#!/usr/bin/env python3
"""Write the one-line confession to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty.
The program writes exactly one line of text and nothing else.

How the line targets the brief: it is specific and self-incriminating --
a real agent failure mode (confident, tireless, pointless calendar
'optimization') with a concrete casualty (lunch) and a smug paper trail:
the agent logs its own damage as deep work. Funny because it is true.
"""

import os
from pathlib import Path

LINE = "Today my agent spent 40 minutes 'optimizing' my calendar, deleted lunch, then proudly blocked the freed hour as 'deep work: recovering from calendar optimization.'"

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the entry line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line within the limit.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
