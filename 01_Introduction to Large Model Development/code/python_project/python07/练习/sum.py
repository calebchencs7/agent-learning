"""
两数求和
程序需要接收用户输入的两个数字，并计算它们的和。
要求：

定义函数 add(a, b)
函数返回两个数的和
调用函数并输出结果
"""


def add(a, b):
    return a + b


num1 = int(input("输入第一个数字:"))
num2 = int(input("输入第一个数字:"))
addition = add(num1, num2)
print(f"{num1}+{num2}的结果为{addition}")
