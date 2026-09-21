def print_info(fn):

    def inner(x, y):
        print("开始")
        r = fn(x, y)
        print("结束")
        return r

    return inner


@print_info
def add(x, y):
    return x + y


r = add(5, 5)
print(r)
