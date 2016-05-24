#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: muyeby
@contact: bxf_hit@163.com
@site: http://muyeby.github.io
@software: PyCharm
@file: iterator.py
@time: 16-5-23 下午11:16
"""
"""================================python iterator========================"""
ita = iter([1,2,3]) #将可迭代对象转换成迭代器
print type(ita)
print next(ita)
print next(ita)
print next(ita)

class Container(object):
    def __init__(self,start=0,end=0):
        self.start = start
        self.end = end
    def __iter__(self):
        print "[LOG] I made this iterator!"
        return self

    def next(self):                            #python 3中将此函数改为__next__()
        print("[LOG] Calling __next__ method!")
        if self.start<self.end:
            i = self.start
            self.start+=1
            return i
        else:
            raise StopIteration
c = Container(0,5)
for i in c:
    print i

"""python迭代器做一个斐波那契数列"""
class Fibs(object):

    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        if self.a <10:
            self.a,self.b = self.b,self.a+ self.b
            return self.a
        else:
            return StopIteration
    def __iter__(self):
        return self

c2 = Fibs()
for i in c2:
    if i<10:
        print i
    else:
        break
print("what are you fucking to say?")