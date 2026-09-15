# 1.先定义函数
def show1(*args):
    print(args, type(args))


def show2(**kwargs):
    print(kwargs, type(kwargs))


def show3(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


# 2.再调用函数
show1(1, 2)
print('========================================')
show2(a=1, b=2)
print('========================================')
show3(1, 2, 3, a=4, b=5, c=6)
print('========================================')
show3([1, 2, 3], {'a': 4, 'b': 5, 'c': 6})
print('========================================')
show3(*[1, 2, 3], **{'a': 4, 'b': 5, 'c': 6})
