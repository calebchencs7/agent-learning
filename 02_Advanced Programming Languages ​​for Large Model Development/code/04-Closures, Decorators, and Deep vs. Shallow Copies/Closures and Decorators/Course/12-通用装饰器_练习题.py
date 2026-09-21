# 要求实现通用装饰器，被修饰函数执行前和执行后输出开始和结束

def buff(fn):

    def inner(*args, **kwargs):
        print("开始")
        r = fn(*args, **kwargs)
        print("结束")
        return r

    return inner


@buff
def say_hello(name, age, gender):
    print(f"我是{name}，今年{age}岁，性别：{gender}")


@buff
def loop_print(num):
    for i in range(1, num+1):
        print(i)


say_hello("aaa", 11, "nan")
loop_print(10)