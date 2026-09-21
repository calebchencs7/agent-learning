"""
函数执行统计：编写带参数返回值的装饰器
背景：
后台系统中很多函数都需要记录执行日志。如果每个函数里都手动写日志代码，会重复很多。可以使用装饰器统一增加日志功能，同时不影响原函数参数和返回值。
问题：
编写一个装饰器 log_func，要求：
1.函数执行前输出：开始执行。 (1分)
2.函数执行后输出：执行结束。(1分)
3.装饰器内部需要支持任意参数。(2分)
4.定义函数 add(a, b)，返回两个数的和。(3分)
5.使用装饰器装饰 add。(2分)
6.调用 add(10, 20) 并打印返回结果。(1分)
"""


def log_func(func):
    def wrapper(*args, **kwargs):
        print("开始执行")
        result = func(*args, **kwargs)
        print("执行结束")
        print(f"{result}")

    return wrapper


@log_func
def add(a, b):
    return a + b


add(10, 20)
