# 如果推导式语法不足以描述规则，可以用函数搭配yield来实现生成器
#  yield关键字需要搭配函数使用，替代函数的return
# 函数的return一次性返回全部结果
# yield是返回一个数据，在函数中，yield可以重复使用


# 得到1个1~10奇数的生成器，要求写def和yield
def num_gen():  # yield，就别写return
    print("拉拉拉")
    yield 1  # yield 对外生成1条数据，生成后代码暂停，直到对方需要下一个数据代码继续向下
    print("咔咔咔")
    yield 3
    print("呱呱呱")
    yield 5
    print("嘎嘎嘎")
    yield 7
    print("擦擦擦")
    yield 9


# yield执行几次，这就是生成几个数据

# gen = num_gen()  # gen 生成器对象

# print(next(gen))  # next()方法，获取生成器的下一个数据

# for num in gen:  # for循环会自动调用next()方法，直到生成器没有数据
#     print(num)


def num_gen2(max_num, flag):
    if flag == 1:
        # 生成1~maxnum在（包含）之间的奇数
        for i in range(1, max_num + 1):
            if i % 2 == 1:
                yield i
    else:
        # 生成1~maxnum在（包含）之间的偶数
        for i in range(1, max_num + 1):
            if i % 2 == 0:
                yield i


gen = num_gen2(100, 0)  # gen 生成器对象

for num in gen:
    print("yy", num)
