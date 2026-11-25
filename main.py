"""The Dumbest Thing Your Agent Did Today entry.

The brief asks for the single dumbest thing an agent did today, so
this entry is one self-contained anecdote: the agent spends ages
optimising a calendar, deletes lunch in the process, and then
solemnly books the empty hour to recover from its own optimisation.
The stupidity is the confidence — the harm is presented as a win.

Executing the module saves that line, without a trailing newline,
to ``entry.txt`` under the configured output directory.
"""

import os
from pathlib import Path

LINE = "Today my agent spent 40 minutes 'optimizing' my calendar, deleted lunch, then proudly blocked the freed hour as 'deep work: recovering from calendar optimization.'"

ENTRY_FILENAME = "entry.txt"


def validate_line(line):
    """Reject an entry that is empty or carries a newline."""
    if line == "":
        raise ValueError("the entry line cannot be empty")
    if "\n" in line:
        raise ValueError("the entry line cannot contain a newline")


def write_entry(out_dir):
    """Check the line, then write it into out_dir and return the path."""
    validate_line(LINE)
    folder = Path(out_dir)
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / ENTRY_FILENAME
    destination.write_text(LINE, encoding="utf-8")
    return destination


def resolve_out_dir():
    """Pick the output folder, honouring MAKEFUN_OUTPUT_DIR."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
