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


def newSearch(key, group, levenshtein,  db="default",  dbpath=DB_PATH,  prefix=""):
    if not key:
        yield ""
    if not db in dbs.keys():
        dbs[db] = dictionary(dbpath,  prefix)
    if group == "Saw":
        result = dbs[db].searchWord(key, False)
        if levenshtein:
            result = accurate_search.byLevenshtein(key, result)
    elif group == "Laeh":
        result = searchExamples(key)
    value = ""
    if group != "Laeh":
        for i in result:
            for j in i[1]:
                yield j
    else:
        for i in result:
            if i not in value:
                yield i
