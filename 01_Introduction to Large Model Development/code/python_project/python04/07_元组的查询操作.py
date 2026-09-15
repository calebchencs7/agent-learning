# 定义元组
info = (('张三', '李四', '王五'), (18, 18, 38), (66.6, 77.7, 88.8))
print(info)

# 查询info的元素个数
print(len(info))

# 查询info第二个元素中18出现的个数
ages = info[1]
print(ages.count(18))
print(info[1].count(18))

# 查询ages中38的索引
print(ages.index(38))
# 注意: 如果元素不存在就报错
# print(ages.index(68))

# 拓展: 删除容器
del info
print(info)  # NameError: name 'info' is not defined
