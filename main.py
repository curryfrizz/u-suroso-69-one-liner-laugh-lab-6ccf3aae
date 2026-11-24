"""One-Liner Laugh Lab -- make.fun entry, draft one.

A program/v1 entry: running this file writes exactly one funny line
to /output/entry.txt. The line answers the competition prompt, the
excuse a robot vacuum gives after eating a sock, in at most 200
characters. It uses only the Python standard library, touches no
network, and writes the same bytes on every run.

Why this excuse should score: the vacuum pleads its case in court,
deadpan, inventing a duel that makes the sock the aggressor, then
hides behind an ancient Roomba code that made eating the evidence a
legal duty rather than a malfunction. Three escalations, one line.
"""

from pathlib import Path

JOKE = "Your Honor, the sock challenged me to a duel, lost, and \u2014 per the ancient Roomba code \u2014 I was legally required to eat the evidence."


def main() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(JOKE, encoding="utf-8")
    target.chmod(0o644)


if __name__ == "__main__":
    main()
