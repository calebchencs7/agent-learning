# 准备数据
my_str = '12315'
my_list = [1, 2, 3, 1, 5]
my_tuple = (1, 2, 3, 1, 5)
my_set = {1, 2, 3, 1, 5}
my_dict = {1: 'a', 2: 'a', 3: 'a', 1: 'a', 5: 'a'}
# len() 获取container容器的元素个数
print(len(my_str))
print(len(my_list))
print(len(my_tuple))
print(len(my_set))
print(len(my_dict))
print('========================')
# max() 获取最大值
print(max(my_str))
print(max(my_list))
print(max(my_tuple))
print(max(my_set))
print(max(my_dict))
print('========================')
# min() 获取最小值
print(min(my_str))
print(min(my_list))
print(min(my_tuple))
print(min(my_set))
print(min(my_dict))
print('========================')

# 注意: 列表本身有sort()函数,但是其他容器调用不了
# 所以封装了一个sorted(),五大容器都可以使用列表的sort()函数
print(sorted(my_str))
print(sorted(my_list))
print(sorted(my_tuple))
print(sorted(my_set))
print(sorted(my_dict))
print('-------------------')
print(sorted(my_str, reverse=True))
print(sorted(my_list, reverse=True))
print(sorted(my_tuple, reverse=True))
print(sorted(my_set, reverse=True))
print(sorted(my_dict, reverse=True))
print('========================')
print('1' in my_str)
print(1 in my_list)
print(1 in my_tuple)
print(1 in my_set)
print(1 in my_dict)
print('------------')
print('11' in my_str)
print(11 in my_list)
print(11 in my_tuple)
print(11 in my_set)
print(11 in my_dict)
