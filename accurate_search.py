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
                if len(list_tmp) == 2:  # 2 means this entry contains only 1 word
                    distance = Levenshtein.distance(key, list_tmp[1])
                    if distance == 0:
                        list_distance.append(-1)  # -1 means the best matched one
                    else:
                        list_distance.append(distance)
                        continue
                for tmp in list_tmp:
                    if key in tmp:
                        list_distance.append(Levenshtein.distance(key, tmp))
                result_list2d.append([min(list_distance), i])
                # The method above is not so accurate,but it might work better than the previous one
    result_list2d.sort()
    for i in result_list2d:
        yield i[1]
