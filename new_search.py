#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode
    FileNotFoundError=IOError

from dictionary import *
import accurate_search

def newSearch(key, group, levenshtein):
    if not key:
        yield ""

    if group == "Saw":
        result = searchWord(key, False)
        if levenshtein:
            result = accurate_search.byLevenshtein(key, result)
    elif group == "Laeh":
        result = searchExamples(key)
    value = ""
    n = 0
    if group != "Laeh":
        for i in result:
            for j in i[1]:
                yield j
    else:
        for i in result:
            if not i in value:
                yield i
