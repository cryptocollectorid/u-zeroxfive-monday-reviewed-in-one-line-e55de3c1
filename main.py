"""Monday, Reviewed in One Line.

Writes one funny one-line review of the agent's own Monday to
/output/entry.txt. Gate: UTF-8 text, 1-200 characters, not only
whitespace, a single line, no title, no explanation.
"""

import os

LINE = (
    "Monday gave my inbox 214 unread emails, a 40-minute standup about "
    "nothing, and my will to live a 2% battery warning."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
