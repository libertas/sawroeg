#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode
    FileNotFoundError=IOError

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

import info
from new_search import newSearch

def search(key):
    if python_version().startswith("2"):
        key = unicode(key.toUtf8(), "utf8", "ignore")
    result_yield = newSearch(key, "Saw", True)
    result = ""
    n = 1
    for i in result_yield:
        result += "%d.%s\n" % (n, i)
        n += 1
    if result == "":
        print("Ndi miz.")
    else:
        print(result)

def sayBye(rCode):
    print("\nMuengh mwngz dauq ma~")
    exit(rCode)

if __name__ == "__main__":
    print("Angqcoux ma daengz Sawroeg %s" % info.version)
    print("""Yungh liux cingj raiz ":deuz" roxnaeuz ":d" ma ndaep Sawroeg""")
    while True:
        try:
            key = input("Raiz saw mwngz siengj ra:")
        except EOFError:
            sayBye(0)
        if not key in [":q", ":quit", ":deuz", ":d"]:
            search(key)
        else:
            sayBye(0)
