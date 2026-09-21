# 1. 被修饰函数，接收3个参数传入，计算三个参数的和并print输出
#
# 2. 装饰器装饰函数，在函数执行前输出开始，执行后输出结束


def print_info(fn):

    def inner(x, y, z):
        print("开始")
        fn(x, y, z)
        print("结束")

    return inner


@print_info
def add3(x, y, z):
    print(f"x + y + z = {x + y + z}")


add3(1, 3, 5)
