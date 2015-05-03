#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from enviroment import *
import sqlite3

from platform import python_version
if python_version().startswith('2'):
    str = unicode


cx = sqlite3.connect(USER_DB_PATH)
cu = cx.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS sawguq (key, value)")

def add(word,  content):
    cu.execute("INSERT INTO sawguq VALUES (?, ?)", (word, word + " " + content))
    cx.commit()
    
