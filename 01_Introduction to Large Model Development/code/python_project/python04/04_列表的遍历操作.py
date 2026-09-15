# 定义非空列表
names = ['熊大', '熊二', '张三', '李四', '王五', '赵六', '周八']
# for循环遍历
for e in names:
    print(e)

print('================================')

# while 循环遍历
# 1.变量作为索引使用,所以初始值一定是0
index = 0
# 2.条件判断
while index < len(names):
    # 3.循环体
    e = names[index]
    print(e)
    # 4.条件控制
    index += 1
