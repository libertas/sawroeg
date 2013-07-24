#!/usr/bin/env python3

def iter_slice(iter, start=0, end=None):
    try:
        for i in range(start):
            next(iter)
        for i in range(start, end):
            yield next(iter)
    except StopIteration:
        raise IndexError('iter_slice(iter, start=%s, end=%s) out of range' %
            (repr(start), repr(end)))
