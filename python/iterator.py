#!/usr/bin/env python
# encoding: utf-8
"""
@version: ??
@author: muyeby
@license: Apache Licence 
@contact: bxf_hit@163.com
@site: http://muyeby.github.io
@software: PyCharm
@file: iterator.py
@time: 16-5-23 下午11:16
"""
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

    def __next__(self):
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
