# 可迭代的数据类型有： list   tuple  dict  set  str等
# 可迭代的数据结构有 generator （包括生成器和带yeild的generator function)
# 这些可以直接作用于for 循环的统称为可迭代对象， Iterable
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器，Iterator
# 生成器都是Iterator对象， 但list  dict  str 虽然是Iterable，但不是 Iterator
# 把list  dict  str等虽然是Iterable变成Iterator 可以使用iter()函数


# 常用方法
# 1. isinstance 判断是否是可迭代对象 Iterable
# 2. next 来判断是否为是Iterator

# from collections import Iterable, Iterator
import collections

print(isinstance([], collections.Iterable))
print(isinstance([], collections.Iterator))
print(isinstance(iter([]), collections.Iterable))
print(isinstance(iter([]), collections.Iterator))


def check_Iterator(obj_name):
    try:
        next(obj_name)
        print('是Iterator')
    except TypeError as e:
        print('不是Iterator,原因：' + str(e))

s1 = 'abcd'
s2 = (1, 3, 4)
s3 = iter(s2)
print(type(s1), type(s3))
check_Iterator(s1)
check_Iterator(s2)
check_Iterator(s3)