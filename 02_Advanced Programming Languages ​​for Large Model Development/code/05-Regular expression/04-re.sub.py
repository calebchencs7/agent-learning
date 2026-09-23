import re

"""
re.sub(规则, 要替换成的内容, 被替换字符串)
"""
# 数字替换为*
s = "abc123def456"
p = r"\d"

result = re.sub(p, "*", s)
print(result, type(result))

# 非数字换为-
s = "abc123def456"
p = r"\D"
result = re.sub(p, "-", s)
print(result)

# 替换.为#
s = "www.qq.com"
p = r"\."
result = re.sub(p, "#", s)
print(result)

# 指定替换的次数,加上count参数
s = "www.qq.com.cn"
p = r"\."  # .换#，只换2个
result = re.sub(p, "#", s, count=2)
print(result)
