#!/usr/bin/env python3
# This script should run in the app root
import sqlite3
import sys

help_msg = "Usage: python3 sawguq_generate.py (-f)[input.txt] [output.db]"

if len(sys.argv) == 3:
    force = False
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
elif len(sys.argv) == 4 and sys.argv[1] == "-f":
    force = True
    inputFile = sys.argv[2]
    outputFile = sys.argv[3]
else:
    print(help_msg)
    exit(-1)


sawguq = {}
with open(inputFile, 'r') as f:
    for word in f.read().splitlines():
        word = word.replace('\u3000', '\x20').replace('(', '（').replace(
            ')', '）').strip()
        if not word:
            continue
        try:
            idx, content = word.split(' ', 1)
        except ValueError:
            if force:
                continue
            else:
                raise ValueError('Misformed line: %s' % repr(word))
        idx = idx.strip('-').lower()
        if idx in sawguq:
            sawguq[idx].append(word)
        else:
            sawguq[idx] = [word]
cx = sqlite3.connect(outputFile)
cu = cx.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS sawguq (key, value)");
cu.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_value ON sawguq (value)")
for word in sorted(sawguq):
    sawguq[word].sort()
    for i in sawguq[word]:
        cu.execute("INSERT OR IGNORE INTO sawguq VALUES (?, ?)", (word, i))
cx.commit()
cu.close()
cx.close()

print("Success")
