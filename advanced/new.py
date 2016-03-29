#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""one way example using of  __new__() : Singleton
__new__特殊方法的一种用法是实现python中的单例模式"""

__author__ = 'xiongmeng'


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

        return cls.instance


obj1 = Singleton()
obj2 = Singleton()
obj1.attr1 = 'value1'

print obj1.attr1, obj2.attr1
print obj1 is obj2
