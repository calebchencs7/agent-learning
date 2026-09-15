"""
定义一个参数为不定长（可变）类型的函数fun，同时传入一个列表和字典，求列表里的数字元素和字典里的value值它们的累积结果。
示例：
​ 输入：列表[1,2,3]，字典{'a': 4,'b': 5, 'c': 6},定义一个函数fun，
​ 输出：21
​ 解释：它们（1+2+3+4+5+6）的累积结果=21
"""

list = [1, 2, 3]
dict = {'a': 4, 'b': 5, 'c': 6}


def fun(*args, **kwargs):
    total = 0
    for arg in args:
        total += sum(arg)
    for value in kwargs.values():
        total += value
    return total


print(fun(list, **dict))
