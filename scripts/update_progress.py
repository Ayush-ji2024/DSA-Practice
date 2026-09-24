"""
Auto-update the Progress Tracker in README.md.

Counts the .cpp files inside every Step-XX-* folder and rewrites:
  - the "Solved" number and status emoji of each step row
  - the Total row
  - the "Solved-X / 455" badge at the top

Run by the GitHub Action on every push; can also be run locally:
    python scripts/update_progress.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# | 01 | [Learn the Basics](./Step-01-Basics) | 0 | 31 | 🟡 |
ROW = re.compile(
    r"^\|\s*(\d{2})\s*\|\s*(\[[^\]]+\]\(\./([^)]+)\))\s*\|\s*\d+\s*\|\s*(\d+)\s*\|\s*[^|]*\|\s*$"
)
# | | **Total** | **0** | **455** | |
TOTAL = re.compile(r"^\|\s*\|\s*\*\*Total\*\*\s*\|.*$")
# Solved-0%20%2F%20455
BADGE = re.compile(r"Solved-\d+%20%2F%20\d+")


def count_solutions(folder: str) -> int:
    path = ROOT / folder
    if not path.is_dir():
        return 0
    return sum(1 for f in path.rglob("*.cpp") if f.is_file())


def status(solved: int, total: int) -> str:
    if solved == 0:
        return "⚪"
    if solved >= total:
        return "🟢"
    return "🟡"


def main() -> None:
    lines = README.read_text(encoding="utf-8").splitlines()
    solved_sum, total_sum = 0, 0
    out = []

    for line in lines:
        m = ROW.match(line)
        if m:
            step, link, folder, total = m.group(1), m.group(2), m.group(3), int(m.group(4))
            solved = count_solutions(folder)
            solved_sum += solved
            total_sum += total
            out.append(f"| {step} | {link} | {solved} | {total} | {status(solved, total)} |")
        elif TOTAL.match(line):
            out.append("__TOTAL__")
        else:
            out.append(line)

    text = "\n".join(out) + "\n"
    text = text.replace("__TOTAL__", f"| | **Total** | **{solved_sum}** | **{total_sum}** | |")
    text = BADGE.sub(f"Solved-{solved_sum}%20%2F%20{total_sum}", text)

    README.write_text(text, encoding="utf-8")
    print(f"Progress updated: {solved_sum} / {total_sum} solved")


if __name__ == "__main__":
    main()