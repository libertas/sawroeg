#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode

import bisect

try:
    from sawguq import sawguq
except ImportError:
    print("Cannot get sawguq.py")
try:
    from sawgeq import sawgeq
except ImportError:
    print("Cannot get sawgeq")

def searchWord(key, from_begin=False):
    try:
        str(key).encode('iso-8859-1')
    except UnicodeEncodeError:
        return searchWordByZh(key)
    return searchWordByZha(key, from_begin=from_begin)


def searchWordByZha(key, from_begin=False):
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
        # yield from (word for word in sawguq if not word[0].startswith(key)
        #             and key in word[0])
        #
        # Or, use the following:
        for i in searchWord(key, from_begin=True):
            yield i
        for i in (word for word in sawguq if not word[0].startswith(key) and
                  key in word[0]):
            yield i


def searchWordByZh(key, from_begin=False):
    assert from_begin is False
    key = str(key)
    for word, descs in sawguq:
        res_list = [desc for desc in descs if key in desc]
        if res_list:
            yield (word, res_list)


def searchExamples(key):
    result = ""
    for i in sawgeq:
        string = sawgeq[i]
        tlist = string.rsplit("\n")
        for j in tlist:
            for k in j.split(" "):
                if key == k:
                    result = "%s    --<<%s>>\n" % (j, i)
                    yield result
                    break
