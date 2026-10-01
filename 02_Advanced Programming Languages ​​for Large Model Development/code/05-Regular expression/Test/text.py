"""
12. 文本清洗
提取邮箱和编号
背景：
客服系统导出的留言中，经常同时包含邮箱和工单编号。运营同学希望程序能从一段文本中自动提取这些关键信息，减少人工复制。
问题：
给定文本：
text = "用户 zhangsan@example.com 提交了工单 NO1001，备用邮箱 service_01@test.cn，关联工单 NO1002。"

请使用正则表达式完成：

提取所有邮箱地址。(4分)
提取所有工单编号，编号格式为 NO 后跟 4 位数字。(4分)
分别打印两个列表。(2分)
【提交运行截图和代码】
"""

import re

text = "用户 zhangsan@example.com 提交了工单 NO1001，备用邮箱 service_01@test.cn，关联工单 NO1002。"


email_pattern = r'[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+'
ticket_pattern = r'NO\d{4}'

emails = re.findall(email_pattern, text)
tickets = re.findall(ticket_pattern, text)

print("提取的邮箱地址:", emails)
print("提取的工单编号:", tickets)
