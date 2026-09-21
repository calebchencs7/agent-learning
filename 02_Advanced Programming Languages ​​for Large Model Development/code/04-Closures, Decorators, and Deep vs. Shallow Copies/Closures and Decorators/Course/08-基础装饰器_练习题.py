# 装饰其它函数，其它函数内容随意
# 装饰的功能是，
# 执行先输出“我来了”再执行被装饰函数，
# 最后在输出“结束了”


def buff(fn):

    def inner():
        print("我来了")
        fn()
        print("结束了")

    return inner


@buff
def hello():
    print("我来自黑马，帅得很")


@buff
def say_hi():
    print("大家好")


hello()

say_hi()
