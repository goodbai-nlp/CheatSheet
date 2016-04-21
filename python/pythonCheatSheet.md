# Python CheatSheet
## 常用Tricks
#### 1.字符串判空：
```
if my_object:
    print 'my_object is not empty'
```
空字符串等同于False，如果只对字符串是否为空感兴趣，没必要用len
#### 2.字串判断
不要用find函数，用python的in操作
```
string = 'Hi there'
if 'Hi' in string:
	print 'Success'
```
#### 3.list 打印
不要用for循环，join函数一方面不会再最后一个元素后增加符号，另一方面它可以在线性时间内解决连接，更加优雅和高效
```
recent_presidents = ['George Bush', 'Bill Clinton', 'George W. Bush']
print 'The three most recent presidents were: %s.' % ', '.join(recent_presidents)
#prints 'The three most recent presidents were: George Bush, Bill Clinton, George W. Bush'.
```
#### 4.整数除法
默认是整除，想得到小数结果可能要这样
```
5.0/2      # Returns 2.5
float(5)/2 # Returns 2.5
5//2       # Returns 2
```
还可以这样
```
from __future__ import division
5/2        # Returns 2.5
float(5)/2 # Returns 2.5
5//2       # Returns 2
```
#### 5.lambda 表达式
Lambda 就是一个单行的匿名函数，你可以把它转换成一个正常的函数，但活用 Lambda 可以让代码更加优雅
```
def add(a,b) return a+b
add2 = lambda a,b: a+b
print add2(1,2)
squares = map(lambda a:a*a,[1,2,3,4,5])
# squares is now [1,4,9,16,25]
```
## 列表
#### 1.列表表达式
##### 一个栗子：
```
numbers = [1,2,3,4,5]
squares = []
for number in numbers:
    squares.append(number*number)
# Now, squares should have [1,4,9,16,25]
```
使用map
```
numbers = [1,2,3,4,5]
squares = map(lambda a:a*a,numbers)
# Now, squares should have [1,4,9,16,25]
```
使用列表表达式
```
numbers = [1,2,3,4,5]
squares = [x*x for x in numbers]
# Now, squares should have [1,4,9,16,25]
```
##### 列表过滤
```
numbers = [1,2,3,4,5]
numbers_under_4 = []
for number in numbers:
    if number < 4:
        numbers_under_4.append(number)
# Now, numbers_under_4 contains [1,4,9]
```
filter版本
```
numbers = [1,2,3,4,5]
numbers_under_4 = filter(lambda x:x<4,numbers)
```
列表生成式
```
numbers = [1,2,3,4,5]
numbers_under_4 = [x for x in numbers if x<4 ]
```
##### 更加复杂的例子
```
numbers = [1,2,3,4,5]
squares = []
for number in numbers:
    if number < 4:
        squares.append(number*number)
# squares is now [1,4,9]
```
map + filter 版本
```
numbers = [1,2,3,4,5]
squares = map(lambda x:x*x,filter(lambda t:t<4,numbers))
```
列表生成式
```
numbers = [1,2,3,4,5]
numbers_under_4 = [x*x for x in numbers if x<4]
```
#####生成表达式
列表生成式要求数据必须一次加载到内存当中，而对于生成表达式，可以不必如此，它每次生成一个generator object，每次加载一个对象
生成表达式和列表生成式的语法基本相同，区别是生成表达式用的是'()'而不是'[]'
```
numbers = [1,2,3,4,5]
squares_under_10 = (number*number for number in numbers if number*number < 10)
for square in squares_under_10:
    print square,
```
此时的squares_under_10是一个generator object对象，不能直接打印，需要遍历
#####多重嵌套
```
for x in (0,1,2,3):
    for y in (0,1,2,3):
        if x < y:
            print (x, y, x*y),
# prints (0, 1, 0) (0, 2, 0) (0, 3, 0) (1, 2, 2) (1, 3, 3) (2, 3, 6)
```
```
print [(x, y, x * y) for x in (0,1,2,3) for y in (0,1,2,3) if x < y]
```
#### 2.reduce函数
