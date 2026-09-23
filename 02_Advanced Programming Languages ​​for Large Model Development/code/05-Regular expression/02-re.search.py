import re

"""
re.search 搜索，从整个字符串中找到符合规则的
"""


def print_result(result):
    """
    打印匹配结果
    :param result: 匹配结果对象
    :return:
    """
    if result:
        print("匹配成功")
        print("匹配结果：", result.group())  # result.group() 会返回匹配的结果
    else:
        print("匹配失败")


# 输入aaa111abc
def demo01():
    s = input("输入内容：")
    p = r"\d\d\d"
    result = re.match(p, s)  # 失败
    print(type(result))
    print_result(result)


def demo02():
    s = input("输入内容：")
    p = r"\d\d\d"
    result = re.search(p, s)  # 成功
    print(type(result))
    print_result(result)


demo01()
demo02()
