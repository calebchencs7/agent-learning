# 1. 被修饰函数，接收3个参数传入，计算三个参数最大的数字，并return
#
# 2. 装饰器装饰函数，在函数执行前输出开始，执行后输出结束


def print_info(fn):

    def inner(x, y, z):
        print("开始")
        r = fn(x, y, z)
        print("结束")
        return r

    return inner


@print_info
def find_max(x, y, z):
    max_v = x

    if y > x:
        max_v = y

    if z > max_v:
        max_v = z

    return max_v


r = find_max(3, 1, 6)
print(r)
