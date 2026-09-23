import re

s = "ItHeiMA"
p = r"itheima"

r = re.match(p, s, re.I)        # re.I 忽略大小写
print(r.group())

#
s = "it\nheima"
p = r"it.heima"
r = re.match(p, s, re.S)        # re.S .可以匹配换行
print(r.group())

