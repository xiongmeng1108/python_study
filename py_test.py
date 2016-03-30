#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""test for python study"""

__author__ = 'xiongmeng'


# from collections import Iterable


class IterTest(object):
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    # def __next__(self):
    #     self.a = 1
    #     self.a += 1
    #     if self.a > 10:
    #         raise StopIteration()
    #     return self.a

    def next(self):
        self.a += 1
        if self.a > 10:
            raise StopIteration()
        return self.a

if __name__ == "__main__":
    for n in IterTest():
        print n

    d = dict(id=1, name='xm', age=30)
    print d
    for key in d:
        print key

    for value in d.values():
        print value

    for k,v in d.items():
        print k, '=', v
