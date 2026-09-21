"""
定义：
在嵌套函数中，内部函数引用了外部函数的局部变量，并且内部函数在外部函数执行结束后，
仍然能够保存和使用这些变量，这种结构叫闭包。

用途：
需要一个函数长期记住某些状态或配置，但又不想使用全局变量或专门创建一个类。

写法：
1. 函数有嵌套（外层函数内写内层函数）
2. 内层函数使用外层函数的局部变量（形参、定义的）
3. 外层函数要返回内层函数```本身```
"""

# Global，函数内部修改全局变量
# nonlocal，嵌套函数，内层函数修改外层函数局部变量


def outer():
    num = 100  # 外层函数的局部变量

    def inner():  # 1. 有嵌套函数
        nonlocal num  # 2. 内层函数使用外层局部变量,需要nonlocal声明
        num += 1
        print(num)

    return inner  # 3. 外层函数返回内层函数本身


# 概念上，outer() 执行结束后，它原本的普通局部调用帧会结束。
# 但是因为 inner 仍然引用 num，Python 会把 num 保存到一个闭包单元 cell 中。

f1 = outer()  # 将outer()函数的返回值赋值给f1，f1本身是inner函数
f2 = outer()  # 将outer()函数的返回值赋值给f2，f2本身是inner函数

# f1 f2本身是：inner函数
f1()  # 101
f1()  # 102
f1()  # 103

f2()  # 101
f2()  # 102

# f1.__closure__[0].cell_contents = 300
print(f1.__closure__[0].cell_contents)
print(f2.__closure__[0].cell_contents)
