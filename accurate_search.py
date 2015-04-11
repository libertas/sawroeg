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
    lang = "zha"
    try:
        str(key).encode('iso-8859-1')
    except UnicodeEncodeError:
        lang = "zh"
    result_list2d = []
    if lang == "zha":
        for i in result_yield:
            result_list2d.append([Levenshtein.distance(key, i[0]), i])
    else:
        for i in result_yield:
            for j in i[1]:
                list_tmp = split("[\[\]\（\）\ \；\，\。\,\．]", j)
                list_distance = []
                for tmp in list_tmp:
                    if key in tmp:
                        list_distance.append(Levenshtein.distance(key, tmp))
                result_list2d.append([sum(list_distance) / len(list_distance), i])  # The method above is not perfect,it will not be good at all time.It's left unsolved.
    result_list2d.sort()
    for i in result_list2d:
        yield i[1]
