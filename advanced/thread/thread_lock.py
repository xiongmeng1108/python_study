#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""线程锁使用举例"""

__author__ = 'xiongmeng'

import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)


def run_thread_with_lock(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


def thread_fun(fun):
    t1 = threading.Thread(target=fun, args=(5,))
    t2 = threading.Thread(target=fun, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print 'fun %s: balance=%s' % (fun.__name__, balance)

if __name__ == '__main__':
    thread_fun(run_thread_with_lock)
    thread_fun(run_thread)