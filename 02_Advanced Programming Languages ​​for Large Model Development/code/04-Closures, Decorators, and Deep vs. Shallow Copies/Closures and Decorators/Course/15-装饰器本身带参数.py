"""
outer("+")       # 第一层：接收装饰器参数 operator
    ↓
middle(add)      # 第二层：接收被装饰的函数 fn
    ↓
inner(1, 2)      # 第三层：接收函数调用时的参数 args
"""


def outer(operator):

    def middle(fn):

        def inner(*args, **kwargs):
            if operator == "+":
                print("正在做加法运算")
            else:
                print("正在做减法运算")

            r = fn(*args, **kwargs)
            return r

        return inner

    return middle


@outer("+")
def add(a, b):
    print(f"a + b = {a + b}")


add(1, 2)


@outer("-")
def sub(a, b):
    print(f"a - b = {a - b}")


add(1, 2)
sub(1, 2)


# 不用语法糖的方式实现装饰器
# def outer(operator):

#     def middle(fn):

#         def inner(*args, **kwargs):
#             if operator == "+":
#                 print("正在做加法运算")
#             else:
#                 print("正在做减法运算")

#             r = fn(*args, **kwargs)
#             return r

#         return inner

#     return middle


# def add(a, b):
#     print(f"a + b = {a + b}")


# def sub(a, b):
#     print(f"a - b = {a - b}")


# # outer("+") 返回 middle；
# # middle(add) 返回 inner
# add_decorator = outer("+")
# add = add_decorator(add)


# # outer("-") 返回 middle；middle(sub) 返回 inner
# sub_decorator = outer("-")
# sub = sub_decorator(sub)

# add(1, 2)
# sub(1, 2)
