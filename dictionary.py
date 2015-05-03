#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sqlite3

try:
    from sawgeq import sawgeq
except ImportError:
    print("Cannot get sawgeq")

from platform import python_version
if python_version().startswith('2'):
    str = unicode



class dictionary:
    def __init__(self,  dbpath, item_prefix=""):
        self.prefix = item_prefix
        self.cx = sqlite3.connect(dbpath, check_same_thread = False)
        self.cu = self.cx.cursor()


    def searchWord(self,  key, from_begin=False):
        try:
            str(key).encode('iso-8859-1')
        except UnicodeEncodeError:
            return self.searchWordByZh(key)
        return self.searchWordByZha(key, from_begin=from_begin)


    def searchWordByZha(self,  key, from_begin=False):
        key = str(key).lower()
        self.cu.execute("""SELECT * FROM sawguq WHERE key like "%%%s%%" """ % key)
        for i in self.cu.fetchall():
            yield (i[0], (i[1],))


    def searchWordByZh(self,  key, from_begin=False):
        assert from_begin is False
        self.cu.execute("""SELECT * FROM sawguq WHERE value like "%%%s%%" """ % key)
        for i in self.cu.fetchall():
            yield (i[0], (i[1],))


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
