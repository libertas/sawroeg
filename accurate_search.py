#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import jpype

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


jvmPath = jpype.getDefaultJVMPath()
ext_class_dir = "jars/"
jvmArg = '-Djava.ext.dirs=' + ext_class_dir
jpype.startJVM(jvmPath, jvmArg)

Dict = jpype.JPackage('org.roeg.sawroeg').Dict
cuengh_tokenizer = jpype.JPackage('org.roeg.cytokenizer').CuenghTokenizer()
bouyei_tokenizer = jpype.JPackage('org.roeg.cytokenizer').BouyeiTokenizer()
wordsSimilarity = Dict.wordsSimilarity
isStringChinese = Dict.isStringChinese
languageFilter = Dict.languageFilter

WORD_TIMES = 1000
Max_Ch_Word_Length = 7


def byWordsAndLevenshtein(key, result_yield, tokenizer):
    issc = isStringChinese(key)
    result_list2d = []

    if issc:
        for i in result_yield:
            parts = re.split("[ ，；。]+", languageFilter(i[1][0], issc))
            l_distances = []
            for part in parts:
                if part == "" or\
                        (len(key) < Max_Ch_Word_Length and len(part) > Max_Ch_Word_Length) :
                    continue
                l_distance = Levenshtein.distance(part, key)
                if l_distance == 0:
                    l_distances = [l_distance,]
                    break
                l_distances.append(l_distance)
            result_list2d.append([sum(l_distances) / len(l_distances), i])
    else:
        for i in result_yield:
            w_distance = wordsSimilarity(tokenizer.tokenize(key), tokenizer.tokenize(i[0]))
            l_distance = Levenshtein.distance(key, i[0])
            result_list2d.append([w_distance * WORD_TIMES + l_distance, i])

    result_list2d.sort()
    for i in result_list2d:
        yield i[1]
