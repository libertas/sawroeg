#!/usr/bin/env python3

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
with open('sawguq.py', 'w') as f:
    f.write('''# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode

\n
sawguq = [\n''')
    for word in sorted(sawguq):
        sawguq[word].sort()
        f.write('    %s,\n' % repr((word, sawguq[word])))
    f.write(']\n')
