# 五个容器中支持推导式的只能是可变类型

# TODO 需求1: 快速生成一个存储1-100的列表
# 一.原始方式
# 1.先定义空列表
my_list1 = []
# 2.利用for循环快速生成1-100
for i in range(1, 101):
    # 3.边生成边添加到空列表中
    my_list1.append(i)
# 4.循环外使用最终的列表
print(my_list1)

# 二.推导式
my_list1 = [i for i in range(1, 101)]

# TODO 需求2: 快速生成一个存储1-100中偶数的列表
# 一.原始方式
# 1.先定义空列表
my_list1 = []
# 2.利用for循环快速生成1-100
for i in range(1, 101):
    # 3.边生成边添加到空列表中
    if i % 2 == 0:
        my_list1.append(i)
# 4.循环外使用最终的列表
print(my_list1)
# 二.推导式
my_list1 = [i for i in range(1, 101) if i % 2 == 0]
print(my_list1)
