#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from re import split

try:
    import Levenshtein
except:
    import levenshtein as Levenshtein

from platform import python_version
if python_version().startswith('2'):
    str = unicode
    FileNotFoundError = IOError


def byLevenshtein(key, result_yield):
    result_list2d = []

    for i in result_yield:
        result_list2d.append([Levenshtein.distance(key, i[0]), i])

    result_list2d.sort()
    for i in result_list2d:
        yield i[1]
