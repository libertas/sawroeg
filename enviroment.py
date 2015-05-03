#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str = unicode

DB_PATH = "sawguq.db"
DOWNLOAD_PATH = "./downloads/"
DOWNLOADPAGENAME = "Banj Lizsienq"
USER_DB_PATH = "userdb.db"
USER_PREFIX = "(Vunz-raiz)"
