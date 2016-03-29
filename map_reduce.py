#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ## 1、将一个数值形式的字符串转换成相应整数


def char2num(s):
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[s]


def fn(x, y):
    return x * 10 + y


reduce(fn, map(char2num, '13579'))


# 整理上述代码为一个函数str2int：
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))


# 进一步用lambda优化得：
def str2int(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


###====================================================================================================

###2、 将一个整数转换成对应的字符串
def num2char(n):
    L1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    L = []
    while n != 0:
        a = n % 10
        n = n / 10
        L.append(L1[a])
    return L


def fn(x, y):
    return y + x


reduce(fn, num2char(13579))
