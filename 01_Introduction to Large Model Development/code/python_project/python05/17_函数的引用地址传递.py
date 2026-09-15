# 定义函数
def jia():  # jia = 地址
    print('jia方法执行了')


# 函数引用地址传递
def show(func):
    print(func)
    func()


# print(jia)  # 打印函数的地址
# f = jia
# print(f)

# 调用函数
# 注意: 传递函数名,本质就是传递函数地址,因为函数名引用对应的地址
show(jia)
# lambda表达式可以直接传递
show(lambda: print('lambda函数执行了'))
