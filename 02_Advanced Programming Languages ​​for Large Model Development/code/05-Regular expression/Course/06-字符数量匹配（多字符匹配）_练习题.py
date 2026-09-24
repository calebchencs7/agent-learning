# 1. 字符串必须包含test（用match）
# 2. 匹配IP格式 xxx.xxx.xxx.xxx   xxx是纯数字数量1-3
# 3. 匹配网址  http://www.itheima.com或https://www.itheima.com
# 4. 匹配手机号，必须是1开头，其余纯数字数量11位
import re


def demo01():
    """字符串必须包含test（用match）"""
    s = input("输入：")
    p = r".*test.*"

    r = re.match(p, s)
    if r:
        print(r.group())
    else:
        print("匹配失败")


def demo02():
    """匹配IP格式 xxx.xxx.xxx.xxx   xxx是纯数字数量1-3"""
    s = input("输入：")
    p = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    r = re.match(p, s)
    if r:
        print(r.group())
    else:
        print("匹配失败")


def demo03():
    """匹配网址  http://www.itheima.com或https://www.itheima.com"""
    s = input("输入：")
    p = r"https?://www.itheima.com"

    r = re.match(p, s)
    if r:
        print(r.group())
    else:
        print("匹配失败")


def demo04():
    """匹配手机号，必须是1开头，其余纯数字数量11位"""
    s = input("输入：")
    p = r"1\d{10}"

    r = re.match(p, s)
    if r:
        print(r.group())
    else:
        print("匹配失败")


demo04()
