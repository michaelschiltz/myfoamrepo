#!/usr/bin/env python3
"""
Scaffold a new atomic note (or MOC) with schema-correct frontmatter.

Examples:
  python3 scripts/new_note.py "The bill of exchange unbundles the loan" \\
      --session ron-harris-tradeoffs --tags bill-of-exchange,risk-pricing \\
      --moc "MOC - Risk-sharing vs risk-pricing"

  python3 scripts/new_note.py "MOC - Bimetallism" --type moc

Writes into notes/ (default) or mocs/ (type=moc). Refuses to overwrite.
Pure standard library.
"""

import os, sys, argparse, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

p = argparse.ArgumentParser()
p.add_argument("title")
p.add_argument("--type", default="permanent",
               choices=["permanent", "moc", "source", "reference"])
p.add_argument("--project", default="clearing-settling-realm")
p.add_argument("--session", default="")
p.add_argument("--tags", default="")
p.add_argument("--status", default="seed",
               choices=["stub", "seed", "developed"])
p.add_argument("--moc", action="append", default=[],
               help="MOC hub(s) to link (repeatable)")
a = p.parse_args()

folder = "mocs" if a.type == "moc" else "notes"
path = os.path.join(ROOT, folder, a.title + ".md")
if os.path.exists(path):
    sys.exit(f"refusing to overwrite existing note: {os.path.relpath(path, ROOT)}")

tags = [t.strip() for t in a.tags.split(",") if t.strip()] or (["moc"] if a.type == "moc" else [])
today = datetime.date.today().isoformat()

fm = [
    "---",
    f"title: {a.title}",
    f"type: {a.type}",
    f"tags: [{', '.join(tags)}]",
    f"project: {a.project}",
]
if a.session:
    fm.append(f"source-session: {a.session}")
fm += [f"created: {today}", f"status: {a.status}", "---", ""]

body = [f"# {a.title}", "", "<!-- one claim, argued forensically -->", "", "## Links", ""]
for m in a.moc:
    body.append(f"- [[{m}]]")
if not a.moc:
    body.append("- [[MOC - HistorEE]]")
body += ["", "## Source", ""]
if a.session:
    body.append(f"{a.session} session.")
else:
    body.append("<!-- provenance -->")
body.append("")

os.makedirs(os.path.dirname(path), exist_ok=True)
open(path, "w", encoding="utf-8").write("\n".join(fm + body))
print(f"created {os.path.relpath(path, ROOT)}")
print("remember: also add this note under the relevant MOC's ## Notes list")
