#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""print / assert / logging"""

__author__ = 'xiongmeng'


class Dict(object):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value