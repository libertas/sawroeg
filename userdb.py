#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from enviroment import *
import sqlite3

from platform import python_version
if python_version().startswith('2'):
    str = unicode


dbs = {}

def add(word,  content,  dbpath):
    if not dbpath in dbs.keys():
        dbs[dbpath] = sqlite3.connect(dbpath)
    cx = dbs[dbpath]
    cu = cx.cursor()
    cu.execute("CREATE TABLE IF NOT EXISTS sawguq (key, value)")
    cu.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_item ON sawguq (key, value)")
    cu.execute("INSERT INTO sawguq VALUES (?, ?)", (word, word + " " + content))
    cx.commit()

def delete(word,  dbpath):
    if not dbpath in dbs.keys():
        dbs[dbpath] = sqlite3.connect(dbpath)
    cx = dbs[dbpath]
    cu = cx.cursor()
    cu.execute('DELETE FROM sawguq WHERE value="%s"' % word)
    cx.commit()
