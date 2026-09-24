import re


def print_result(result):
    if result:
        print("匹配成功，结果：", result.group())
    else:
        print("匹配失败")


def demo01():
    """
    字符串中间必须是ITHEIMA
    ITHEIMA之前有3个字符内容随意
    之后有2个内容随意
    """
    s = input("输入内容：")
    p = r".{3}ITHEIMA.{2}"
    # .{3} .任意字符{3}3次 .{3}任意字符3次

    result = re.match(p, s)
    print_result(result)


def demo02():
    """
    匹配网址，格式是 xxx.xxx.xxx
    xxx内容要求必须是字母，数量要求2~5位
    合规  www.qq.com   www.itaaa.cn
    """
    s = input("输入内容：")
    p = r"[a-zA-Z]{2,5}\.[a-zA-Z]{2,5}\.[a-zA-Z]{2,5}"

    result = re.match(p, s)
    print_result(result)


def demo03():
    """
    必须包含itheima
    必须用match
    """
    s = input("输入内容：")
    p = r".*itheima.*"

    result = re.match(p, s)
    print_result(result)


def demo04():
    """
    网址判断 https
    xxx.xxx.xxx
    xxx内容 字母数字 数量最少1个最多不限
    """
    s = input("输入内容：")
    p = r"[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+"

    result = re.match(p, s)
    print_result(result)


def demo05():
    """
    网址判断：
    http[s]://xxx.xxx.xxx
    [s] s可有可无
    xxx字母数字数量最少1个最多10个
    """
    s = input("输入内容：")
    p = r"https?://[a-zA-Z0-9]{1,10}\.[a-zA-Z0-9]{1,10}\.[a-zA-Z0-9]{1,10}"
    # https?   ?只作用于s本身

    result = re.match(p, s)
    print_result(result)
