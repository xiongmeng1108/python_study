#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""print / assert / logging"""

__author__ = 'xiongmeng'


# err.py
def foo(s):
    print 'ssddss'
    n = int(s)
    pass   # pass 预研占位，后面有代码会继续执行
    print 'sss'
    assert n != 0, 'n is zero!'   # 断言： 表达式n!=0应该是True,否则,后面的代码就会出错
    return 10 / n


def main():
    foo('0')


def log():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    s = '0'
    n = int(s)
    logging.debug(' n = %d' % n)
    print 10/n

if __name__ == '__main__':
    #main()
    log()
