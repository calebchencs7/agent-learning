# TODO 需求1: 快速生成一个存储1-100的集合
# 一.原始方式
# 1.先定义空集合
my_set1 = set()
# 2.利用for循环快速生成1-100
for i in range(1, 101):
    # 3.边生成边添加到空集合中
    my_set1.add(i)
# 4.循环外使用最终的集合
print(type(my_set1), my_set1)
# 二.推导式
my_set1 = {i for i in range(1, 101)}
print(type(my_set1), my_set1)

# TODO 需求2: 快速生成一个存储1-100中偶数的集合
# 一.原始方式
# 1.先定义空集合
my_set1 = set()
# 2.利用for循环快速生成1-100
for i in range(1, 101):
    # 3.边生成边添加到空集合中
    if i % 2 == 0:
        my_set1.add(i)
# 4.循环外使用最终的集合
print(type(my_set1), my_set1)
# 二.推导式
my_set1 = {i for i in range(1, 101) if i % 2 == 0}
print(type(my_set1), my_set1)
