#!/usr/bin/env python3
# pip install bibtexparser

import bibtexparser
from bibtexparser.bwriter import BibTexWriter

import os
cwd = os.getcwd()
print("cwd: ", cwd)

PREFIX = "./bibliography/"
INPUT_FILE = PREFIX + "all_papers.bib"
OUTPUT_FILE = PREFIX + "main.bib"

# Keep only normal LaTeX/BibTeX fields.
# Custom fields such as code_url, blog_url, abstract, tldr will be removed.
KEEP_FIELDS = {
    "ENTRYTYPE", "ID",
    "title", "author", "editor",
    "booktitle", "journal",
    "year", "month",
    "volume", "number", "pages",
    "publisher", "organization", "institution", "school",
    "address", "series", "edition", "chapter",
    "type", "note",
    "doi", "url", "isbn", "issn",
    "howpublished",
}

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    bib_db = bibtexparser.load(f)

clean_entries = []
for entry in bib_db.entries:
    clean_entry = {
        key: value
        for key, value in entry.items()
        if key in KEEP_FIELDS
    }
    clean_entries.append(clean_entry)

bib_db.entries = clean_entries

writer = BibTexWriter()
writer.indent = "  "
writer.order_entries_by = None

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(writer.write(bib_db))

print(f"Wrote standard bibliography to {OUTPUT_FILE}")