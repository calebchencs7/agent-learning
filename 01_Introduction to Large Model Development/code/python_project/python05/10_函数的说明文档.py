# 1.先定义函数
def get_sum(a: int, b: int) -> int:
    """
    注意:python中不能限制变量的类型,只能警告
    :param a: 整数类型
    :param b: 整数类型
    :return: 整数类型
    """
    return a + b


# 2.再调用函数
result = get_sum(2, 1)
print(result)
