"""
['red', 'Pink']
定义函数，该列表作为参数传入，内部使用列表推导式实现对列表中所有元素的转大写操作
"""


def to_upper(list):
    return [item.upper() for item in list]


colors = ['red', 'Pink']

result = to_upper(colors)
print(result)


# lambda表达式实现
to_upper_lambda = lambda list: [item.upper() for item in list]
result_lambda = to_upper_lambda(colors)
print(result_lambda)
