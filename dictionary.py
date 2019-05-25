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
    def __init__(self,  dbpath):
        self.cx = sqlite3.connect(dbpath, check_same_thread = False)
        self.cu = self.cx.cursor()


    def searchWord(self,  key):
        sql = "SELECT * FROM sawguq WHERE key LIKE ? OR value LIKE ?;"
        key = "%" + key + "%"
        self.cu.execute(sql, (key, key))
        for i in self.cu.fetchall():
            yield (i[0], (i[1],))


def searchExamples(key):
    MAXLEN = 200  # Magic number
    result = ""
    for i in sawgeq:
        string = sawgeq[i]
        tlist = string.rsplit("\n")
        for j in tlist:
            for k in j.split(" "):
                if key == k and len(j) < MAXLEN:
                    result = "%s    --<<%s>>\n" % (j, i)
                    yield result
                    break
