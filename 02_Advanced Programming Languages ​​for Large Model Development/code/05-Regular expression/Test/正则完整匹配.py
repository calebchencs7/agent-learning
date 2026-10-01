"""
背景：
小王正在写邮箱格式校验功能，希望只有完整邮箱格式才算通过。但下面代码把一段包含邮箱的普通文本也判断成了通过，需要找出问题并修复。
题目：
请阅读下面代码，判断代码是否有问题。如果有问题，请说明问题原因，并写出修复后的代码。


import re

text = "我的邮箱是 test@example.com"
result = re.search(r"\w+@\w+\.\w+", text)

if result:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")
"""

import re

text = "我的邮箱是 test@example.com"
result = re.search(r"^\w+@\w+\.\w+$", text)

if result:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")
