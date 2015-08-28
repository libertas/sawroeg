#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from enviroment import *
import sqlite3

from platform import python_version
if python_version().startswith('2'):
    str = unicode

# delete database file from the filesystem online may cause problem
dbs = {}

def add(word, content, dbpath, email=None):
    if not dbpath in dbs.keys():
        dbs[dbpath] = sqlite3.connect(dbpath)
    cx = dbs[dbpath]
    cu = cx.cursor()
    if email:
        cu.execute("CREATE TABLE IF NOT EXISTS sawguq (key, value, email)")
        cu.execute("INSERT INTO sawguq VALUES (?, ?, ?)", (word, word + " " + content, email))
    else:
        cu.execute("CREATE TABLE IF NOT EXISTS sawguq (key, value)")
        cu.execute("INSERT INTO sawguq VALUES (?, ?)", (word, word + " " + content))
    cx.commit()

def delete(word, content, email, dbpath):
    if not dbpath in dbs.keys():
        dbs[dbpath] = sqlite3.connect(dbpath)
    cx = dbs[dbpath]
    cu = cx.cursor()
    cu.execute('DELETE FROM sawguq WHERE key="%s" AND value="%s" AND email="%s"' % (word, word + " " + content, email))
    cx.commit()
