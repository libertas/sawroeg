#!/usr/bin/env python3

from sawguq_old import sawguq


sawguq_split = '\n'.join((sawguq[i] for i in sawguq)).splitlines()
sawguq_dict = {}
for word in sawguq_split:
    word = word.replace('\u3000', '\x20').strip()
    if not word:
        continue
    try:
        idx, content = word.split(' ', 1)
    except ValueError:
        raise ValueError('Misformed line: %s' % repr(word))
    if idx in sawguq_dict:
        sawguq_dict[idx].append(content)
    else:
        sawguq_dict[idx] = [content]
print('sawguq = {')
for word in sorted(sawguq_dict):
    print('    %s: %s,' % (repr(word), repr(sawguq_dict[word])))
print('}')
