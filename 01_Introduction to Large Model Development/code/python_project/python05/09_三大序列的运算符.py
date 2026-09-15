# 准备数据
my_str = '12315'
my_list = [1, 2, 3, 1, 5]
my_tuple = (1, 2, 3, 1, 5)
# my_set = {1, 2, 3, 1, 5}
# my_dict = {1: 'a', 2: 'a', 3: 'a', 1: 'a', 5: 'a'}
# 序列只有: 字符串,列表,元组
# + 拼接返回新的序列
print(my_str + '6')
print(my_list + [6])
print(my_list)  # [1, 2, 3, 1, 5] 原先的不会改变
print(my_tuple + (6,))

# * 本质也是拼接返回新序列
print("========================")
print(my_str * 2)
print(my_str + my_str)
print(my_list * 2)
print(my_list + my_list)
print(my_tuple * 2)
print(my_tuple + my_tuple)
