

def print_info(fn):

    def inner(x, y):
        print("开始修饰")
        fn(x, y)
        print("结束修饰")

    return inner


@print_info
def add(x, y):
    print(f"x + y = {x + y}")


add(3, 5)

