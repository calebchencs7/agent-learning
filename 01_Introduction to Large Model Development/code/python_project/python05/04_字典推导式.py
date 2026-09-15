# TODO 需求1: 快速生成一个存储1-100的字典   k=v
# 一.原始方式
# 1.先定义空字典
my_dict1 = dict()
# 2.利用for循环快速生成1-100
for i in range(1, 101):
    # 3.边生成边添加到空字典中
    my_dict1[i] = i
# 4.循环外使用最终的字典
print(type(my_dict1), my_dict1)

# 二.推导式
my_dict1 = {i: i for i in range(1, 101)}
print(type(my_dict1), my_dict1)

# TODO 需求2: 快速生成一个存储1-100中偶数的字典  k=v
# 一.原始方式
# 1.先定义空字典
my_dict1 = dict()
# 2.利用for循环快速生成1-100
for i in range(1, 101):
    # 3.边生成边添加到空字典中
    if i % 2 == 0:
        my_dict1[i] = i
# 4.循环外使用最终的字典
print(type(my_dict1), my_dict1)

# 二.推导式
my_dict1 = {i: i for i in range(1, 101) if i % 2 == 0}
print(type(my_dict1), my_dict1)
