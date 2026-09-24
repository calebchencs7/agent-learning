import re

# 匹配HTML标签

s = "<h1>编程语言</h1>啦啦啦啦啦啦啦<h1>Python代码</h1>"

p1 = r"<h1>.+</h1>"  # 贪婪模式
p2 = r"<h1>.+?</h1>"  # 非贪婪模式

r = re.match(p1, s)  # <h1>编程语言</h1>啦啦啦啦啦啦啦<h1>Python代码</h1>
print(r.group())
r = re.match(p2, s)  # <h1>编程语言</h1>
print(r.group())
