#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""多线程"""

__author__ = 'xiongmeng'

import threading
import time


def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n += 1
        print 'thread %s >>> %s' % (threading.currentThread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.currentThread().name

if __name__ == '__main__':
    print 'thread %s is running...' % threading.currentThread().name
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print 'thread %s ended.' % threading.currentThread().name
