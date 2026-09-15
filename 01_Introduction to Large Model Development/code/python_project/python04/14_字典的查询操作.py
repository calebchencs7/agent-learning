# 定义字典
grade_dict = {
    '张三': {'语文': 99, '数学': 88},
    '李四': {'语文': 89, '数学': 79},
    '王五': {'语文': 100, '数学': 59},
}
# 查看grade_dict字典元素个数
print(len(grade_dict))

# 查看李四的所有成绩
print(grade_dict['李四'])
print(grade_dict.get('李四'))

# 查看李四的数学成绩
print(grade_dict['李四']['数学'])
print(grade_dict.get('李四').get('数学'))
print('=============================================')

grade = {'语文': 99, '数学': 88, '英语': 80}
# 获取grade所有的key
print(grade.keys())
# 获取grade所有的value
print(grade.values())
# 获取grade所有的键值对
print(grade.items())
