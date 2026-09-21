def outer():
    name = "周杰轮"

    def inner():  # 1. 双层嵌套函数
        print(f"我是{name}")  # 2. 内层用外层变量

    return inner


f = outer()
f()
f()
