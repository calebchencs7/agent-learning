# 定义空字典
names = {}
print(names)

# TODO 增    注意:key必须是之前没有的
# 需求: 依次存储张三:18,李四:28,王五:38
names['张三'] = 18
names['李四'] = 28
names['王五'] = 38
print(names)

# TODO 改    注意:key必须是之前已有的
# 需求: 修改张三的年龄为19
names['张三'] = 19
print(names)

# TODO 删
# pop()需求: 删除李四的信息
names.pop('李四')
print(names)

# del 需求: 删除王五信息
del names['王五']
print(names)
# clear()需求: 清空学生信息
names.clear()
print(names)

# 拓展:删除容器
del names
# print(names) # NameError: name 'names' is not defined
