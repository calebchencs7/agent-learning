# 遍历字符串'黑马程序员'
name = '黑马程序员'
# for循环方式    todo for循环又叫遍历循环,直接拿到元素
for e in name:
    print(e)  # 此处e代表每个元素

print('=========================')

# while循环方式  todo 核心思想是: 变量充当索引使用
# 1.初始变量
index = 0
# 2.条件判断
while index < len(name):
    # 3.循环体
    e = name[index]  # 此处e代表每个元素
    print(e)
    # 4.条件控制
    index += 1
