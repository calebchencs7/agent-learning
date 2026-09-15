from typing import Union


def add(x: Union[int, float], y: Union[int, float]) -> int | float:
    return x + y


print(add(1, 2))

# 如果类型是多个类型，需要或关系
# 快捷写法： int | float   不是int就是float
# Union写法： Union[int, float]   Union需要import导包
