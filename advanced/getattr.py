#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""__getattr__(), __str__() """

__author__ = 'xiongmeng'


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __str__(self):
        return self._path

    # way 1:
    # def __call__(self, name):
    #     return Chain('%s/%s' % (self._path, name))

    # def __getattr__(self, item):
    #     return Chain('%s/%s' % (self._path, item))

    # way 2:
    def __getattr__(self, item):
        if item == 'users':
            return lambda user: Chain('%s/users/%s' % (self._path, user))
        else:
            return Chain('%s/%s' % (self._path, item))


def test():
    a = Chain().status.users("xm").timeline.list
    print a


print Chain().status.users("xm").timeline.list

if __name__ == '__main__':
    test()
