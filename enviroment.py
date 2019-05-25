#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str = unicode

DB_BASE_PATH = "dbs/"
DB_PATH = DB_BASE_PATH + "sawguq.db"
BOUYEI_DB_PATH = DB_BASE_PATH + "selgus.db"
DOWNLOAD_PATH = "./downloads/"
DOWNLOADPAGENAME = "Banj Lizsienq"
USER_DB_PATH = DB_BASE_PATH + "userdb.db"
NEW_PREFIX = "(Vunz-raiz)"
NEW_DB_PATH = DB_BASE_PATH + "newdb.db"
SEARCHING_LIMIT = 30

groupList = ["Cuengh-Gun", "Qyaix-Has", "Laeh"]
groupDB = {groupList[0]: DB_PATH, groupList[1]: BOUYEI_DB_PATH, groupList[2]: DB_PATH}
