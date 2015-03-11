#!/usr/bin/env python3
import sqlite3

sawguq = {}
with open('sawguq.txt', 'r') as f:
    for word in f.read().splitlines():
        word = word.replace('\u3000', '\x20').replace('(', '（').replace(
            ')', '）').strip()
        if not word:
            continue
        try:
            idx, content = word.split(' ', 1)
        except ValueError:
            raise ValueError('Misformed line: %s' % repr(word))
        idx = idx.strip('-').lower()
        if idx in sawguq:
            sawguq[idx].append(word)
        else:
            sawguq[idx] = [word]
cx = sqlite3.connect("../sawguq.db")
cu = cx.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS sawguq (key, value)");
for word in sorted(sawguq):
    sawguq[word].sort()
    for i in sawguq[word]:
        cu.execute("INSERT INTO sawguq VALUES (?, ?)", (word, i))
cx.commit()
cu.close()
cx.close()
