# 有一个函数内容随意，要求被3个装饰器装饰，装饰器1流程是先输出开始1，然后执行被装饰函数
# 装饰器2流程是先输出开始2，然后执行被装饰函数
# 装饰器3流程是先输出开始3，然后执行被装饰函数


def buff1(fn):
    def inner(*args, **kwargs):
        print("开始1")
        r = fn(*args, **kwargs)
        return r

    return inner


def buff2(fn):
    def inner(*args, **kwargs):
        print("开始2")
        r = fn(*args, **kwargs)
        return r

    return inner


def buff3(fn):
    def inner(*args, **kwargs):
        print("开始3")
        r = fn(*args, **kwargs)
        return r

    return inner


@buff1
@buff2
@buff3
def func():
    print("hahaha")


func()
