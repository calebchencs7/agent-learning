# 可以认为创建非空容器的过程就是打包操作
my_str = '123'
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {'1': 'a', '2': 'b', '3': 'c'}

# 从容器中把元素一个个取出赋值给对应变量的过程就是拆包
a, b, c = my_str
print(a, b, c)

a, b, c = my_list
print(a, b, c)

a, b, c = my_tuple
print(a, b, c)

a, b, c = my_set
print(a, b, c)

a, b, c = my_dict
print(a, b, c)
