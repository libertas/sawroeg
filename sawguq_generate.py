#!/usr/bin/env python3

sawguq_split = open('sawguq.txt', 'r').read().splitlines()
sawguq_dict = {}
for word in sawguq_split:
    word = word.replace('\u3000', '\x20').replace('(', '（').replace(
        ')', '）').strip()
    if not word:
        continue
    try:
        idx, content = word.split(' ', 1)
    except ValueError:
        raise ValueError('Misformed line: %s' % repr(word))
    idx = idx.strip('-').lower()
    if idx in sawguq_dict:
        sawguq_dict[idx].append(word)
    else:
        sawguq_dict[idx] = [word]
print('sawguq = {')
for word in sorted(sawguq_dict):
    sawguq_dict[word].sort()
    print('    %s: %s,' % (repr(word), repr(sawguq_dict[word])))
print('}')
