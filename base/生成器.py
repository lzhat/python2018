# 生成器 generator
# 1）生成器就是一函数
# 2）生成器具有next方法
# 3）生成器可以使用send 方法和外界交互。


# 迭代器
# 迭代器是访问集合元素的一种方式。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
# 迭代器只能往前不会后退，不过这也没什么，因为人们很少在迭代途中往后退。
# 另外，迭代器的一大优点是不要求事先准备好整个迭代过程中所有的元素。
# 迭代器仅仅在迭代到某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁。
# 这个特点使得它特别适合用于遍历一些巨大的或是无限的集合，比如几个G的文件
# 特点：
#   访问者不需要关心迭代器内部的结构，仅需通过next()方法不断去取下一个内容
#   不能随机访问集合中的某个值 ，只能从头到尾依次访问
#   访问到一半时不能往回退
#   便于循环比较大的数据集合，节省内存



# 1 创建生成器
# 1.1列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)]
print(L)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(10))
print(g)  # <generator object <genexpr> at 0x000000000113F9E8>

# 1.2.带yield 语句函数

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        k = (yield b)
        if k is not None:
            print("接收到的值：" + str(k))
        a, b = b, a + b
        n = n + 1


print(fib(10))  # <generator object fib at 0x000000000112FA40>

# 2 获取生成器中的内容，
# 2.1 用
f = fib(10)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

# 2.2 使用for循环
for n in fib(6):
    print(n)

# 3. 高级应用 通过send将值传入到生成器中
# next(), send()的返回值都是yield 后面的参数，
# send()跟next()的区别是send()是发送一个参数给(yield b)的表达式，作为其返回值给k,
# 而next()是发送一个None给(yield b)表达式，
# 这里需要区分的是，一个是调用next(),send()时候的返回值，一个是(yield n)的返回值，两者是不一样的.看输出结果可以区分。
f = fib(10)
print(f.__next__())
print(f.__next__())
f.send(4)
print(f.__next__())
print(f.__next__())

