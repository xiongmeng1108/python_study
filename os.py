#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""module os"""

__author__ = 'xiongmeng'

import os

if os.name == 'posix':
    print 'Linux or Unix or Mac OS x'
    # windows do not support os.uname()
    os.uname()
if os.name == 'nt':
    print 'Windows'

    # ----操作文件和目录---

    # 查看当前目录的绝对路径
    print os.path.abspath('.')

    # 合成路径：不要直接拼字符串，而是利用os.path.join(),可以自动处理不同os的分隔符
    print "合成路径："
    print os.path.join('\Users\michael', 'testdir')

    # 拆分路径：不要直接去拆字符串，而是利用os.path.split(),可以自动根据os的分隔符拆分成2部分
    print "拆分路径：\users\\xm\testdir\\file.txt"
    print os.path.split("\users\\xm\testdir\\file.txt")

    # 直接得到文件扩展名
    print os.path.splitext('/usr/xm.txt')

    # 对文件重命名
    with open('./test.txt', 'w') as f:
        f.write("hello world")
    print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt']
    os.rename('test.txt', 'test11.py')
    print [x for x in os.listdir('.') if os.path.isfile(x)]

    # 删除文件
    os.remove('test11.py')

    # 在某个目录下创建一个新目录
    print [x for x in os.listdir('.') if os.path.isdir(x)]
    path = os.path.join('.', 'testdir')  # 可以不要此步
    print path
    os.mkdir(path)
    print [x for x in os.listdir('.') if os.path.isdir(x)]

    # 删掉一个目录
    os.rmdir(path)
    print [x for x in os.listdir('.') if os.path.isdir(x)]

    print [x for x in os.listdir('.')]
    print [x for x in os.listdir('.') if os.path.isdir(x)]
    print [x for x in os.listdir('.') if os.path.isfile(x)]
    print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']




