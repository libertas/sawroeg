#!/usr/bin/env python3

sawguq = {}
for word in open('sawguq.txt', 'r').read().splitlines():
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
sawguq_py = open('sawguq.py', 'w')
sawguq_py.write('sawguq = [\n')
for word in sorted(sawguq):
    sawguq[word].sort()
    sawguq_py.write('    %s,\n' % repr((word, sawguq[word])))
sawguq_py.write(']\n')
sawguq_py.close()
