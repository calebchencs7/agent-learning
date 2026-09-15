# 定义空集合
names = set()
print(names)
# add()需求:添加内容
names.add('王五')
names.add('李四')
names.add('张三')
names.add(10)
names.add(3.14)
names.add(True)
print(names)

# remove()需求: 删除王五
names.remove('王五')
print(names)
# pop()需求:随机一个元素
names.pop()
print(names)
# clear()需求:清空集合
names.clear()
print(names)

# 拓展:删除容器
del names
print(names)  # NameError: name 'names' is not defined
