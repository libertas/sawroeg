#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode
    FileNotFoundError=IOError

from re import split

try:
    import Levenshtein
except:
    import levenshtein as Levenshtein

def byLevenshtein(key,result_yield):
    lang="zha"
    try:
        str(key).encode('iso-8859-1')
    except UnicodeEncodeError:
        lang = "zh"
    result_list2d = []
    if lang == "zha":
        for i in result_yield:
            tmp=i.split(" ")[0]
            result_list2d.append([Levenshtein.distance(key, tmp), i])
    else:
        for i in result_yield:
            list_tmp=split("[\[\]\（\）\ \；\，\。\,\．]",i)
            list_distance=[]
            for tmp in list_tmp:
                if key in tmp:
                    list_distance.append(Levenshtein.distance(key,tmp))
            result_list2d.append([min(list_distance), i])
    result_list2d.sort()
    result = ""
    for i in result_list2d:
        yield i[1]
