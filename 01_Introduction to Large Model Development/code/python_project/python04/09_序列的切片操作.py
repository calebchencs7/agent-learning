# 序列: 字符串  列表  元组
# 定义序列,并使用切片
# 1.定义字符串'abcde' 完成对应需求
s = 'abcde'
print(s[::])
print(s)  # abcde
# 需求: 获取 abc
print(s[0:3:1])
print(s[:3])
# 需求: 获取 ace
print(s[0::2])
print(s[::2])
# 需求: 获取 cd
print(s[2:4:1])
print(s[2:4])
# 需求: 获取 edcba
print(s[-1::-1])
print(s[::-1])
# 需求: 获取 eca
print(s[-1::-2])
print(s[::-2])
# 需求: 获取 cba
print(s[2::-1])
print(s[-3::-1])
print('=============================================')
# ctrl+R  替换快捷键   ctrl+F 查找快捷
# 2.定义列表['a','b','c','d','e'] 完成对应需求
l = ['a', 'b', 'c', 'd', 'e']
# 需求: 获取 abc
print(l[0:3:1])
print(l[:3])
# 需求: 获取 ace
print(l[0::2])
print(l[::2])
# 需求: 获取 cd
print(l[2:4:1])
print(l[2:4])
# 需求: 获取 edcba
print(l[-1::-1])
print(l[::-1])
# 需求: 获取 eca
print(l[-1::-2])
print(l[::-2])
# 需求: 获取 cba
print(l[2::-1])
print(l[-3::-1])
print('==============================================')

# 2.定义元组('a','b','c','d','e') 完成对应需求
t = ('a', 'b', 'c', 'd', 'e')
# 需求: 获取 abc
print(t[0:3:1])
print(t[:3])
# 需求: 获取 ace
print(t[0::2])
print(t[::2])
# 需求: 获取 cd
print(t[2:4:1])
print(t[2:4])
# 需求: 获取 edcba
print(t[-1::-1])
print(t[::-1])
# 需求: 获取 eca
print(t[-1::-2])
print(t[::-2])
# 需求: 获取 cba
print(t[2::-1])
print(t[-3::-1])
