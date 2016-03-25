#!/usr/bin/env python
# -*- coding: utf-8 -*-

'example of __slots__'

__author__ = 'xiongmeng'

class Student(object):
    #利用__slots__属性来限定Student类实例在动态运行过程中可动态添加的属性和方法
    __slots__ = ("name","score","fun1")
    

def test():
    def fun1(self):
        print "i am fun1!"
        
    import types
    s = Student()
    #由于name,score,fun1在__slots__中已声明，故下面代码正确
    s.name = 'xm'
    s.score = '100'
    s.fun1 = types.MethodType(s,fun1,Student)
    print s.name, s.score, s.fun1()
    
    #由于age没有包含在__slots__中，故下面代码报错
    try:
        s.age = 20 
    expect Error as e:
        print e
        
if __name__ = 'main':
    test()
