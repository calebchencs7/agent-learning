# 元组的遍历
names = ('熊大', '熊二', '张三', '李四', '王五', '赵六', '周八')
# for循环方式
for e in names:
    print(e)

print('===============================')
# while循环方式   变量充当索引
# 初始变量
index = 0
# 条件判断
while index < len(names):
    # 循环体
    e = names[index]
    print(e)
    # 条件控制
    index += 1
