import re

"""
re.match   从头匹配
re.search  全串搜索，返回第一个
re.findall 全串搜索，得到全部
"""


s = input("输入")
p = r"#..#"
# 输入：#xx##fc##
# 输出：['#xx#', '#fc#']
result: list = re.findall(p, s)
print(result)
