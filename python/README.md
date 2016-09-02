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
#####Generator expressions
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
```
numbers = [1,2,3,4,5]
result = 1
for number in numbers:
    result *= number
# result is now 120
```
reduce函数
```
numbers = [1,2,3,4,5]
result = reduce(lambda a,b: a*b, numbers)
# result is now 120
```
#### 2.Iterating over a List: range, xrange and enumerate
xrange和range类似，但xrange比range效率高，因为xrange的列表不会一次全部加载到内存中；enumerate生成索引+内容对的序列
```
strings = ['a', 'b', 'c', 'd', 'e']
for index in xrange(len(strings)):
    print index,
# prints '0 1 2 3 4'
```
```
strings = ['a', 'b', 'c', 'd', 'e']
for index, string in enumerate(strings):
    print index, string,
# prints '0 a 1 b 2 c 3 d 4 e'
```
#### 3.all和any
1.判断存在
以前：
```
numbers = [1,10,100,1000,10000]
if [number for number in numbers if number < 10]:
	print 'At least one element is over 10'
```
2.5以后：
```
numbers = [1,10,100,1000,10000]
if any(number <10 for number in numbers):
	print 'balabalabala'
```
2.判断任意
2.5以前：
```
numbers = [1,2,3,4,5,6,7,8,9]
if len(numbers) == len([number for number in numbers if number < 10]):
    print 'Success!'
# Output: 'Success!'
```
2.5以后：
```
numbers = [1,2,3,4,5,6,7,8,9]
if all(number < 10 for number in numbers):
    print 'Success!'
```
#### 4. 合并多个列表
```
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
squares = [1, 4, 9]
zipped_list = zip(letters, numbers, squares)
# zipped_list contains [('a', 1, 1), ('b', 2, 4), ('c', 3, 9)]
```
#### 5.其他常用函数
`max() , min() , sum()`
#### 列表判重
```
numbers = [1,2,3,3,4,1]
if len(numbers) == len(set(numbers)):
    print 'List is unique!'
# In this case, doesn't print anything
```
## 字典
####简单字典构建
```
dict(a=1, b=2, c=3)
# returns {'a': 1, 'b': 2, 'c': 3}
```
####字典到列表
dict.items()
```
dictionary = {'a': 1, 'b': 2, 'c': 3}
dict_as_list = dictionary.items()
#dict_as_list now contains [('a', 1), ('b', 2), ('c', 3)]
```
####列表到字典
```
dict_as_list = [['a', 1], ['b', 2], ['c', 3]]
dict_as_list2 = [('a', 1), ('b', 2), ('c', 3)]
dictionary = dict(dict_as_list)
dictionary2 = dict(dict_as_list2)
# dictionary now contains {'a': 1, 'b': 2, 'c': 3}
```
混合使用
```
dict_as_list = [['a', 1], ['b', 2], ['c', 3]]
dictionary = dict(dict_as_list, d=4, e=5)
# dictionary now contains {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```
####字典生成
利用列表生成式和列表转字典函数完成，具体效率待考证
```
emails = {'Dick': 'bob@example.com', 'Jane': 'jane@example.com', 'Stou': 'stou@example.net'}
dict2 = dict( [name,'.com' in email] for name,email in emails.iteritems() )
# email_at_dotcom now is {'Dick': True, 'Jane': True, 'Stou': False}
```
## 条件表达式
#### 三目运算符
value1 if condition else value2
```
test = True
result = 'Test is True' if test else 'Test is False'
# result is now 'Test is True'
```
#### 嵌套
```
test1 = False
test2 = True
result = 'Test1 is True' if test1 else 'Test1 is False, test2 is True' if test2 else 'Test1 and Test2 are both False'
```
#### and-or tricks
and-or 被设计来模仿c语言的三目运算符
```
test = True
result = test and 'Test is True' or 'Test is False'
# result is now 'Test is True'
```
存在的问题：当bool and a or b 式中a的值为假时，它不会向三目运算符那样工作
安全的用法：
```
a = ""
b = "second"
res = (1 and [a] or [b])[0]
# res = ""
```
直接封装成函数：
```
def choose(bool,a,b):
    return (bool and [a] or [b])[0]
print  choose(1,'','second')    #''
```
#### True和False作为index
```
test = True
result = ['Test is False','Test is True'][test]
# result is now 'Test is True'
```
True相当于1，False相当于0，可以作为index
这个作法的问题就是要把两个结果/其他都装进数组，很浪费资源，尤其是包括关键IO计算时，会浪费很多时间
## Function
#### 函数的default值问题
我们写函数时常常这么写
```
def add_item(item, stuff = []):
    stuff.append(item)
    print stuff

add_item(1)
# prints '[1]'
add_item(2)
# prints '[1,2]' !!!
```
本意是向列表里加一个新元素，如果列表不存在就建一个列表
而当我们进行第二次调用时，会发现并不是我们想要的只含一个元素的列表，而是两个元素！！！python函数中的default变量是存在内存中的，只能初始化一次。而且当函数第二次调用时和第一次是公用该变量的。一个解决方案是这样的：
```
def function(item, stuff = None):
	if stuff is None:
    	stuff = []
    stuff.append(item)
    print stuff

function(1)
prints '[1]'
function(2)
# prints '[2]', as expected
```
总结起来就是function defaults不要用可变的对象
#### python函数参数数量
python允许你的函数传入任意多参数，只需在函数定义时的参数前加一个'*'
```
def do_something(a, b, c, *args):
    print a, b, c, args
do_something(1,2,3,4,5,6,7,8,9)
# prints '1, 2, 3, (4, 5, 6, 7, 8, 9)'
```
可以看出其它的参数被存到一个元组中
其实还可以这样：
```
def do_something_else(a, b, c, *args, **kwargs):
    print a, b, c, args, kwargs

do_something_else(1,2,3,4,5,6,7,8,9, timeout=1.5)
# prints '1, 2, 3, (4, 5, 6, 7, 8, 9), {"timeout": 1.5}'
```
如上，你可以加入任意多的赋值
#### 用list或dict的内容作为参数
```
arg = [5,2]
pow(*args)
# return pow(5,2) ,5^2 = 25
```
```
def do_something(actually_do_something=True, print_a_bunch_of_numbers=False):
    if actually_do_something:
        print 'Something has been done'
        if print_a_bunch_of_numbers:
            print range(10)
kwargs = {'actually_do_something': True, 'print_a_bunch_of_numbers': True}
do_something(**kwargs)
# prints 'Something has been done', then '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
```
#### 'Switch Statements' using Dictionaries of Functions
来看这样一种情况
```
def key_1_pressed():
    print 'Key 1 Pressed'

def key_2_pressed():
    print 'Key 2 Pressed'

def key_3_pressed():
    print 'Key 3 Pressed'
def unknown_key_pressed():
    print 'Unknown Key Pressed'
keycode = 2
if keycode == 1:
   key_1_pressed()
elif keycode == 2:
   key_2_pressed()
elif number == 3:
   key_3_pressed()
else:
   unknown_key_pressed()
# prints 'Key 2 Pressed'
```
当然你可以选择switch，但还是不够简单，来看一种更美丽的写法
```
keycode = 2
functions = {1: key_1_pressed, 2: key_2_pressed, 3: key_3_pressed}
functions.get(keycode, unknown_key_pressed)()
```
利用了字典的get(),如果没有对应的key，则运行unknown_key_pressed，是不是还不错？


- - -

目前就这么多，下次有机会再总结
英文原文：[http://www.siafoo.net/article/52](http://www.siafoo.net/article/52)
