#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str = unicode

users = {'roeg':  '123'}

secret = "abc"
