# 需求: 已知以下字典,要求遍历打印为: 语文成绩为xx,数学成绩为xx,英语成绩为xx;
grade = {'语文': 99, '数学': 88, '英语': 80}

# 直接遍历字典，默认的遍历的就是key
print('字典里面的key为:')
for key in grade:
    print(key, end=' ')
print('\n========================================')

# 第一种：直接遍历字典
for key in grade:
    # 根据key找值
    value = grade[key]
    print(f'{key}的成绩为:{value}', end=' ')
print('\n========================================')

# 第二种：先手动获取所有key,然后遍历
for key in grade.keys():
    # 根据key找值
    value = grade[key]
    print(f'{key}的成绩为:{value}', end=' ')
print('\n========================================')

# 第三种：先手动获取所有键值对元组,然后遍历
for item in grade.items():  # item是一个元组,第一个元素是key,第二个元素是value
    print(f'{item[0]}的成绩为:{item[1]}', end=' ')
print('\n========================================')

# 补充: 拆包方式(推荐)
for k, v in grade.items():
    print(f'{k}的成绩为:{v}', end=' ')
print('\n========================================')
