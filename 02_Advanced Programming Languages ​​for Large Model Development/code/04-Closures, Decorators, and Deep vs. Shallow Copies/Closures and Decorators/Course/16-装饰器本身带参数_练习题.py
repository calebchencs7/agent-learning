# 1. 准备一个被修饰函数，内容随意
# 2. 准备一个装饰器，装饰器接收一个name参数
# 3. 在被修饰函数执行之前，print输出这个name


def outer(name, age, gender):  # 外层参数，装饰器本身接收的
    def middle(fn):  # 中间层参数，被修饰函数
        def inner(*args, **kwargs):  # 内层参数，被修饰函数所用
            print(name, age, gender)
            fn(*args, **kwargs)

        return inner

    return middle


@outer("王力宏", 11, "男")
def hi(message):
    print(message)


hi("I am a singer")
