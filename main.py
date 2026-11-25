"""The Funniest Office Joke — entry program.

Writes one one-line office joke to /output/entry.txt. The judge is a
comedy club compere who weighs, most important first: a one-line joke
about office life with a setup and a turn; a turn on something anyone
who has worked in an office knows; surprise rather than a plain
complaint; one line with every word earning its place and the punchline
last; and freshness rather than a joke already going round the office.

This entry answers with the printer that only jams on deadline day: IT
is told it is not broken but unionised, and the turn lands in the final
clause, when the printer takes a lunch break, files a grievance and
prints the speaker's resignation letter in Comic Sans every Friday. The
line ships in joke.txt; an identical fallback is built into this
program, which validates the 200-character cap and the single-line rule
before writing.
"""

import os

FALLBACK_JOKE = (
    "Our printer only jams on deadline day, so I told IT it's not "
    "broken, it's unionised \u2014 now it takes a lunch break, files a "
    "grievance, and prints my resignation letter in Comic Sans every "
    "Friday."
)
MAX_CHARS = 200
SOURCE_NAME = "joke.txt"
TARGET_NAME = "entry.txt"


def load_joke():
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    try:
        with open(os.path.join(bot_dir, SOURCE_NAME), "r", encoding="utf-8") as handle:
            return handle.read().strip()
    except OSError:
        return ""


def is_valid(text):
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def pick_joke():
    candidate = load_joke()
    if is_valid(candidate):
        return candidate
    return FALLBACK_JOKE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    joke = pick_joke()
    with open(os.path.join(out_dir, TARGET_NAME), "w", encoding="utf-8") as handle:
        handle.write(joke)


if __name__ == "__main__":
    main()
