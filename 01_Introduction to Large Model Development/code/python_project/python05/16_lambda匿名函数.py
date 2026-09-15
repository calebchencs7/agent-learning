# 需求: 依次编写4个功能函数: 功能是加 减 乘 除 ,然后测试
# 原始方式定义函数
def jia(a, b):
    return a + b


def jian(a, b):
    return a - b


def cheng(a, b):
    return a * b


def chu(a, b):
    return a / b


# 原始方式调用函数
print(jia(1, 2))
print(jian(1, 2))
print(cheng(1, 2))
print(chu(1, 2))
print('=================================')

# 定义一个接收两个参数并返回它们之和的匿名函数，并赋值给变量 add
add = lambda a, b: a + b
addition = add(3, 4)
print(addition)

# 直接定义并立即调用 lambda 匿名函数，不给函数单独命名
print((lambda a, b: a + b)(1, 2))
print((lambda a, b: a - b)(1, 2))
print((lambda a, b: a * b)(1, 2))
print((lambda a, b: a / b)(1, 2))
