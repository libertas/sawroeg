#!/usr/bin/env python3

def iter_slice(iter, start=0, end=None):
    for i in range(start):
        next(iter)
    for i in range(start, end):
        yield (next(iter),)
    next(iter)
    yield None
