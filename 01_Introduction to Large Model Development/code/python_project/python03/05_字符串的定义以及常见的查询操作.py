# 1.定义空字符串
s1 = ''
s2 = ""
s3 = ''''''
s4 = """"""
s5 = str()  # 用类型来定义空字符串
print(s1, s2, s3, s4, s5)
print(type(s1), type(s2), type(s3), type(s4), type(s5))

# 2.定义非空字符串
s = "你好,我现在正在读一本书:'钢铁是怎么练成的',也建议你看"
print(s)
s6 = '黑马程序员是传智教育旗下线下教育品牌'

# 需求1: 查询总长度  s6 = "黑马程序员是传智教育旗下线下教育品牌"
print(len(s6))
# 需求2: 查询'育'出现的个数
print(f"s6中'育'出现的个数为:{s6.count('育')}")
print(f"s6中'中'出现的个数为:{s6.count('中')}")  # 注意:如果子串没有找到,默认返回0

# 需求3: 查询'育'出现的位置索引
print(f"s6中'育'出现的位置索引为:{s6.index('育')}")
print(f"s6中'育'出现的最后一个位置索引为:{s6.rindex('育')}")
# print(s6.index('中'))  # 注意:index如果子串没有找到,直接报错
# print(s6.rindex('中'))  # 注意:rindex如果子串没有找到,直接报错

print(s6.find('育'))  # 字符串特有
print(s6.rfind('育'))  # 字符串特有
print(s6.find('中'))  # 注意:find如果子串没有找到,返回-1
print(s6.rfind('中'))  # 注意:find如果子串没有找到,返回-1

# 需求4: 查询索引为0,3,-1对应位置的字符
print(s6[0])
print(s6[3])
print(s6[-1])

# 拓展: 删除容器
del s6
print(s6)  # NameError: name 's6' is not defined. Did you mean: 's1'?
