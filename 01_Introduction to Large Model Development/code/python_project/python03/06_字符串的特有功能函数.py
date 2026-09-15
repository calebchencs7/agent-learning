# 字符串替换操作
s1 = '你TMD,TMD,TMD哦!'
new_s1 = s1.replace('TMD', '***', 2)
print(s1)
print(new_s1)

# 字符串的分割操作(字符串->列表)
s2 = '苹果,香蕉,橘子,榴莲'
new_s2_list = s2.split(',')
print(s2)
print(new_s2_list)

# 字符串的连接操作(容器->字符串)
l1 = ['苹果', '香蕉', '橘子', '榴莲']
new_l1_str = "-".join(l1)  # 将列表中的元素用'-'连接成一个字符串返回,苹果-香蕉-橘子-榴莲
print(l1)
print(new_l1_str)  # "苹果-香蕉-橘子-榴莲"

# 字符串规整操作
name = ' 张三 '
print(name == '张三')
print(name.strip() == '张三')
print(f"原始的name:{name}")
print(f"规整后的name:{name.strip()}")  # 去掉字符串两边的空格

# 字符串判断开头结尾操作
name = '张三丰'
print(f"{name}以{name[0]}开头为{name.startswith('张')}")
print(f"{name}以王开头为{name.startswith('王')}")
print(f"{name}以{name[-1]}结尾为{name.endswith('丰')}")

# 字符串的编码解码操作
name = '你好'
name1_encode = name.encode('utf8')
name2_encode = name.encode('gbk')
print(name1_encode)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(name1_encode.decode('utf8'))

print(name2_encode)  # b'\xc4\xe3\xba\xc3'
print(name2_encode.decode('gbk'))

print(name1_encode.decode('gbk'))  # 浣犲ソ 张冠李戴,编码和解码不一致,甚至报错

# 大小写转换
name = 'Andy'
print(name.upper())
print(name.lower())
