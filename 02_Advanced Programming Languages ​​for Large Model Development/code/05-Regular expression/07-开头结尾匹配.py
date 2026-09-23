import re
r"""
^表示字符串开头
$表示字符串结尾含义
r"^1\d{10}$"表示，从头到尾，整体符合1\d{10}
"""
"""
[^]在[]内部是区反
单独用是开头
"""


def demo01():
    """匹配手机号，必须是1开头，其余纯数字数量11位"""
    s = input("输入：")
    p = r"^1\d{10}$"

    r = re.match(p, s)
    if r:
        print(r.group())
    else:
        print("匹配失败")


def demo02():
    """匹配密码，必须6位纯数字"""
    s = input("输入：")
    p = r"^\d{6}$"

    r = re.match(p, s)
    if r:
        print(r.group())
    else:
        print("匹配失败")

demo02()