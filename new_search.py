#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dictionary import *
from enviroment import *
import accurate_search

from platform import python_version
if python_version().startswith('2'):
    str = unicode
    FileNotFoundError = IOError


dbs = {}


def newSearch(key, group="Saw", levenshtein=True,  dbpath=DB_PATH):
    if not key:
        yield ""
    if not dbpath in dbs.keys():
        dbs[dbpath] = dictionary(dbpath)

    if group == "Laeh":
        result = searchExamples(key)
    else:
        result = dbs[dbpath].searchWord(key)
        if levenshtein:
            result = accurate_search.byLevenshtein(key, result)

    value = ""
    if group == "Laeh":
        for i in result:
            if i not in value:
                yield i
    else:
        for i in result:
            for j in i[1]:
                yield j
