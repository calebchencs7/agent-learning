# 定义两个集合,存储任意内容
s1 = {10, 20, 60, '张三'}
s2 = {10, 20, 80, True}
print(s1)
print(s2)

print('======================')
# 修改s1的内容为 它和s2的差集
s1.difference_update(s2)
print(s1)  # {'张三', 60}
print(s2)

print('======================')
# 修改s1的内容为 它和s2的并集
s1.update(s2)
print(s1)
print(s2)
