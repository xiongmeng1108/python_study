#!/usr/bin/env python
# -*- coding: utf-8 -*-

'example of using @property'

__author__ = 'xiongmeng'


class Student(object):
    # --------------------------------
    # 1.read and write property : birth
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('birth must be a int or float!')
        if value < 0 or value > 2016:
            raise ValueError('birth must be 0<=birth<=2016 !')
        self._birth = value

    # --------------------------------
    # 2.readonly property : age
    @property
    def age(self):
        return 2016 - self._birth


def test():
    s = Student()
    s.birth = 2011
    print 'birth=%d, age=%d' % (s.birth, s.age)


if __name__ == '__main__':
    test()
