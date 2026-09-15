# 1.先定义函数
def show():
    return 1, 2, 3


# 2.再调用函数
result = show()
print(result, type(result))  # 默认返回元组类型
a, b, c = result
print(a, b, c)
