'''
装饰器
  定义：本质是函数，(装饰其他函数)，即为其他函数添加附加功能。
  原则： 1、不能修改被装饰的函数的源代码；
         2、不能修改被装饰的函数的调用方式。

装饰器的强大在于它能够在不修改原有业务逻辑的情况下对代码进行扩展，权限校验、用户认证、日志记录、性能测试、事务处理、缓存等都是装饰器的绝佳应用场景，它能够最大程度地对代码进行复用。

实现装饰器知识储备：
   1. 函数即'变量'
   2. 高阶函数
       a. 把一个函数名当作实参传递给另一个函数(在不修改被装饰函数源代码的前提下为其添加新功能)
       b. 返回值中包含函数名(不修改函数的调用方式)
   3. 嵌套函数：在函数内部又定义了一个函数，不是调用外部函数。

高阶函数 + 嵌套函数 (组成)--> 装饰器
'''
import time


def test():
    print('test正在运行...')
    time.sleep(2)
    print('test正常结束!!!')


def simple_decorator(func):
    def wrapper():
        print('记录开始执行时间')
        start_time = time.time()
        func()
        print('记录执行完毕时间')
        end_time = time.time()
        print(func)
        print('总运行时间:' + str(end_time - start_time))
    return wrapper


@simple_decorator
def test1():
    print('test1正在运行...')
    time.sleep(2)
    print('test1正常结束!!!')


def intermediate_decorator(func):
    print('intermediate_decorator在运行...')

    def wrapper(*args, **kwargs):
        print('装饰器中的包装器在运行...')
        print('记录开始执行时间')
        start_time = time.time()
        func(*args, **kwargs)
        print('记录执行完毕时间')
        end_time = time.time()
        print(func)
        print('总运行时间:' + str(end_time - start_time))
    return wrapper


@intermediate_decorator
def test2(name, age):
    print('test2正在运行...')
    print('name:' + name + '\tage:' + str(age))
    time.sleep(2)
    print('test2正常结束!!!')


def senior_decorator(auth_type):
    print('senior_decorator在运行...')

    def out_wrapper(func):

        def wrapper(*args, **kwargs):
            if auth_type == 'file':
                print('装饰器中的包装器在运行...')
                print('记录开始执行时间')
                start_time = time.time()
                func(*args, **kwargs)
                print('记录执行完毕时间')
                end_time = time.time()
                print('总运行时间:' + str(end_time - start_time))
            else:
                print('装饰器中的包装器在运行,但是参数不正确，请修改装饰器的参数')
        return wrapper
    return out_wrapper


@senior_decorator(auth_type='file')
def test3(name, age):
    print('test3正在运行...')
    print('name:' + name + '\tage:' + str(age))
    time.sleep(2)
    print('test3正常结束!!!')


if __name__ == '__main__':
    print('1：正常函数')
    test()
    print('2:不带参数的函数加装饰器')
    test1()
    print('3.带参数的函数加装饰器')
    test3('admin', 33)





