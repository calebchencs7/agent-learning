# 定义空列表,存储名字
names = []
print(names)

# TODO 列表的添加操作
# append()
# 需求:张三,李四依次排到列表末尾
names.append('张三')  # add the element to the end of the list
names.append('李四')
print(names)

# extend()
# 需求: 把王五,赵六,田七作为一批依次放到列表末尾
names.extend(['王五', '赵六', '田七'])  # add multiple elements to the end of the list
print(names)

# insert()
# 需求1:熊大插入到列表首位
names.insert(0, '熊大')
print(names)

# 需求2:熊二插入到列表的第二个位置
names.insert(1, '熊二')
print(names)

# TODO 列表的修改操作 list[index] = new value
# 需求: 要求把列表末尾的元素修改为周八
names[-1] = '周八'
print(names)
# 需求: 要求把张三修改为张三丰
names[names.index('张三')] = '张三丰'
print(names)

# TODO 列表的删除操作
# 需求: 删除第一个元素
# del names[0]  # 效果和pop一致,了解下
names.pop(0)  # 删除指定索引位置的元素,如果不指定索引,默认删除最后一个元素
print(names)

# 需求: 删除熊二元素
names.remove('熊二')  # remove()方法删除指定元素,如果有多个相同元素,只删除第一个
print(names)
# 需求: 清空所有元素
names.clear()
print(names)

# 拓展: 删除容器
del names
print(names)  # NameError: name 'names' is not defined
