# 1. 函数1 收2个数字，print2数的和
#  通过  *元组的方式传入参数
#
# 2. 函数2，收name，age。打印信息
# 通过**字典方式传入参数

def add(x, y):
    print(x + y)


def info(name, age):
    print(f"我{name}, {age}岁")


t = (3, 5)
d = {"name": "王大锤", "age": 11}

add(*t)         # 拆，作为位置参数传入  ，等于传入了 3, 5

info(**d)       # 拆，作为关键字参数传入，等于传入了 name="王大锤", age=11
