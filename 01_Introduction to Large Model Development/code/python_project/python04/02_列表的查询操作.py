# 需求:定义列表嵌套列表
info = [['张三', '李四', '王五'], [18, 18, 18, 38]]
print(info)
# 获取所有的姓名所在的列表
print(info[0])

# 获取所有的年龄所在的列表
print(info[1])

# 获取第一个姓名张三
print(info[0][0])

# 需求: 查询info列表元素个数
print(len(info))

# 需求: 查询年龄列表中18出现的次数
print(info[1].count(18))

# 新列表,再次查询
ages = [18, 18, 18, 38]
print(ages.count(38))  # 查询年龄列表中38出现的次数

# 需求: 定义数字列表[10,20,30,20,40,50]
numbers = [10, 20, 30, 20, 40, 50]
# 查看20出现的索引位置
print(numbers.index(20))
# 注意: index查询不存在的就会报错
# print(numbers.index(60)) # 报错
