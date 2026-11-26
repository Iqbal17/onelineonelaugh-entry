"""One Line, One Laugh — entry program.

Writes a single funny line (max 140 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Printing alone would be invalid,
so the file write is the entry.

Decision record — candidates weighed on humour first, freshness second
(judge criteria: a real joke, the laugh from a turn/surprise word,
one breath, fresh wording, lands on a single read):

1. "I tried to meditate, but my brain treated silence like an open mic
   night." (73 chars) — CHOSEN. The laugh is one exact turn: silence,
   the thing meditation promises, becomes a stage where the brain
   performs. "Open mic night" is the surprise word that reframes the
   whole sentence on the last beat. Fresh pairing (meditation x open
   mic), plain words, needs no context, lands in one read.

2. "I finally got eight hours of sleep — in three separate naps, over
   two days, none of them at night." (105 chars) — Strong runner-up.
   The arithmetic subversion is funny and relatable, but the
   "I never sleep properly" gag is a well-worn template; a deadpan
   judge who has heard every joke twice has likely heard this shape
   before. Loses to (1) on freshness.

3. "My horoscope said avoid financial decisions today, so I bought a
   lottery ticket to celebrate my discipline." (112 chars) — Clean
   irony, single read, no shared knowledge. But "horoscope told me X
   so I did the opposite" is a familiar joke skeleton, and the laugh
   leans on the setup rather than one surprising word. Loses to (1)
   on both freshness and punch-per-word.

4. "I told my GPS I wanted the scenic route; it took me past my ex's
   house and three of my bad decisions." (104 chars) — Vivid and
   funny, but ex jokes are the most crowded lane in one-line comedy
   and the punchline needs a beat of unpacking ("three of my bad
   decisions" = the exes?). Loses to (1) on freshness and immediacy.

Why (1) wins: shortest, sharpest turn, freshest image, and the joke
lives in a single surprising phrase rather than a template. At 73
characters it is also well inside the 140 cap, and brevity is a
practical edge too: an exact tie on judge win rate goes to the
smaller text, so a short line costs nothing and can only help.
Note on counts: the 73 above was verified by running the program and
measuring entry.txt (73 chars + trailing newline = 74 bytes); the
runner-up counts are estimates from drafting and do not affect the
gate, since only the chosen line is ever written.
"""

import os

LINE = "I tried to meditate, but my brain treated silence like an open mic night."


def validate_line(line):
    """Gate the entry exactly as the sealed scorer does: 1-140 chars,
    not only whitespace, and a single line."""
    assert isinstance(line, str)
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 140, "line must be 1-140 characters"


def main():
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
