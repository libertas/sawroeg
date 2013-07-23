#!/usr/bin/env python3

import bisect

from sawguq import sawguq
from sawgeq import sawgeq


def searchWord(key, from_begin=False):
    key = str(key).lower()
    if from_begin:
        for i in range(bisect.bisect_left(sawguq, (key,)), len(sawguq)):
            word = sawguq[i]
            if not word[0].startswith(key):
                break
            yield word
    else:
        # Require Python 3.3:
        # yield from searchWord(key, from_begin=True)
        # yield from (word for word in sawguq if key in word[0][1:])
        #
        # Or, use the following:
        for i in searchWord(key, from_begin=True):
            yield i
        for i in (word for word in sawguq if key in word[0][1:]):
            yield i


def searchExamples(key):
    result = ""
    for i in sawgeq:
        string = sawgeq[i]
        tlist = string.rsplit("\n")
        for j in tlist:
            if key in j:
                result += "%s    --<<%s>>\n" % (j, i)
                yield result


def newSearch(key, group):
    if group == "Gyaeuj":
        result = searchWord(key, True)
    elif group == "Gyang":
        result = searchWord(key, False)
    elif group == "Laeh":
        result = searchExamples(key)
    value = ""
    n = 0
    for i in result:
        n += 1
        value += "%d.%s\n" % (n, i)
    return value
