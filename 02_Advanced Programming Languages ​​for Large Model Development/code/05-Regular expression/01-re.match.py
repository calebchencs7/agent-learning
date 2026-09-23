import re

# 调用re的基础方法 match search findall

"""
re.match 从被匹配的字符串头部开始做匹配
如果匹配成功，得到匹配结果
"""

s = input("输入内容：")

# match 被匹配的字符串的头部是否符合匹配规则，匹配成功返回一个对象，匹配失败返回None
result = re.match(
    pattern="caleb",  # 匹配规则
    string=s,  # 被匹配的字符串
)

# 获取结果
if result:
    print("匹配成功")
    print("匹配结果：", result.group())  # result.group() 会返回匹配的结果
else:
    print("匹配失败")
