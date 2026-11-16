"""Turn the three markdown pack files into packs.js for the Saathi web app.

Run from anywhere:  python saathi/app/build_packs.py
Re-run it whenever a file in saathi/packs/ is edited.
"""
import json
import re
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
PACKS_DIR = APP_DIR.parent / "packs"
END_LINE = "Aaj ka rest poora. Kal milte hain."

GROUPS = {
    "medical": ("medical_neet.md", "Medical / NEET", "Doctor banne ka sapna"),
    "tech": ("tech_engineering.md", "Tech / Engineering", "Software engineer banne ka sapna"),
    "sarkari": ("sarkari_exam.md", "Sarkari exam", "Sarkari adhikari banne ka sapna"),
}


def split_days(text):
    """Return [(day_number, title, body)] for every '### Din N: title' block."""
    parts = re.split(r"^### Din (\d+): (.+)$", text, flags=re.M)
    days = []
    for i in range(1, len(parts), 3):
        body = re.split(r"^## ", parts[i + 2], flags=re.M)[0]  # drop the trailing notes section
        days.append((int(parts[i]), parts[i + 1].strip(), body))
    return days


def section(body, name):
    """Text of the '**NAME ...:**' section, up to the next section or rule."""
    m = re.search(r"^\*\*%s[^\n]*\n(.*?)(?=^\*\*(?:THAKA|THEEK|TAAZA)|^---\s*$|\Z)" % name,
                  body, flags=re.M | re.S)
    if not m:
        raise ValueError("section %s missing" % name)
    return m.group(1).strip()


def parse_theek(text):
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    reveal = re.sub(r"^\*?Reveal:\*?\s*", "", " ".join(lines[1:]))
    return {"question": lines[0], "reveal": reveal}


def split_options(line):
    """'(a) x (b) y ...' or 'A) x  B) y ...' -> ['x', 'y', ...]"""
    marker = r"\s*\([a-d]\)\s+" if "(a)" in line else r"\s*\b[A-D]\)\s+"
    return [o.strip() for o in re.split(marker, " " + line)[1:]]


def parse_mcqs(text):
    """Parse three 'question / options / **Sahi|Uttar: x** why' blocks. None if not that shape."""
    out = []
    for block in re.split(r"^\d\.\s+", text, flags=re.M)[1:]:
        lines = [ln.strip() for ln in block.strip().splitlines() if ln.strip()]
        if len(lines) != 3:
            return None
        ans = re.match(r"\*\*(?:Sahi|Uttar):\s*\(?([A-Da-d])\)?\.?\*\*\s*(.*)", lines[2])
        opts = split_options(lines[1])
        if not ans or len(opts) != 4:
            return None
        out.append({"q": lines[0], "options": opts,
                    "answer": "abcd".index(ans.group(1).lower()), "why": ans.group(2)})
    return out if len(out) == 3 else None


def parse_taaza(text):
    mcqs = parse_mcqs(text)
    if mcqs:
        return {"type": "mcq", "items": mcqs}
    m = re.search(r"^\*\*Jawab", text, flags=re.M)
    if not m:
        raise ValueError("free-form task has no **Jawab** line")
    return {"type": "reveal", "prompt": text[:m.start()].strip(), "answer": text[m.start():].strip()}


def build():
    data, problems = {}, []
    for key, (fname, label, dream) in GROUPS.items():
        text = (PACKS_DIR / fname).read_text(encoding="utf-8")
        days = []
        for num, title, body in split_days(text):
            try:
                story = section(body, "THAKA")
                if not story.rstrip().endswith(END_LINE):
                    problems.append("%s din %d: story does not end with the closing line" % (key, num))
                story = story.replace(END_LINE, "").strip()
                days.append({"day": num, "title": title,
                             "story": [p.strip() for p in story.splitlines() if p.strip()],
                             "theek": parse_theek(section(body, "THEEK")),
                             "taaza": parse_taaza(section(body, "TAAZA"))})
            except ValueError as exc:
                problems.append("%s din %d: %s" % (key, num, exc))
        if [d["day"] for d in days] != list(range(1, 11)):
            problems.append("%s: expected days 1-10, got %s" % (key, [d["day"] for d in days]))
        data[key] = {"label": label, "dream": dream, "days": days}
    return data, problems


if __name__ == "__main__":
    data, problems = build()
    for key, group in data.items():
        kinds = [d["taaza"]["type"] for d in group["days"]]
        print("%-8s %d days, tasks: %d mcq, %d reveal" %
              (key, len(group["days"]), kinds.count("mcq"), kinds.count("reveal")))
    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    out = APP_DIR / "packs.js"
    out.write_text("window.PACKS = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n",
                   encoding="utf-8")
    print("wrote", out)
