import re

"""
在正则表达式中：
\d:匹配一个数字,通常表示 0-9
\D:匹配一个非数字字符,相当于 \d 的取反
\s 匹配空白
\S 匹配非空白
\w 匹配字母或数字或下划线    a-z A-Z 0-9 _ 汉字
\W 匹配非字母或数字或下划线。
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


# 匹配任意字符
def demo01():
    """
    匹配字符串是否是：
    - 开头有3个字符，内容随意
    - 结尾有3个字符，内容随意
    - 中间必须是itheima
    aaaitheimaaaa合格
    bbbitheimabbb合格
    aitheimab 不合格
    """
    # 正则中  . 代表字符数量1， 内容随意(\n除外)
    s = input("输入内容：")
    result = re.match("...itheima...", s)  # 规则

    print_result(result)


# 匹配大小写与数字
def demo02():
    """
    字符串必须符合规则：
    - 从头开始，第一个字符是小写字母，第二个是大写字母，第三个是数字，其余随意
    [ab]        表示1个字符， 内容非a即b
    [abcde]     表示1个字符， 内容a或b或c或d或e
    第一个字符是小写字母: [abcdefghijklmnopqrstuvwxyz]        表示1个字符，内容是或a或b或c...或z
    第二个字符是大写：[ABCDEFGHIJKLMNOPQRSTUVWXYZ]       表示1个字符，内容是或A或B或C...或Z
    第三个字符是数字：[0123456789]       表示1个字符，内容是或0或1或2...或9
    """
    s = input("输入内容：")
    result = re.match(
        "[abcdefghijklmnopqrstuvwxyz][ABCDEFGHIJKLMNOPQRSTUVWXYZ][0123456789]",  # 规则
        s,
    )

    print_result(result)


# demo03是 demo02的简化版，使用了范围表示法
def demo03():
    """
    字符串必须符合规则：
    - 从头开始，第一个字符是小写字母，第二个是大写字母，第三个是数字，其余随意
    [ab]        表示1个字符， 内容非a即b
    [abcde]     表示1个字符， 内容a或b或c或d或e
    第一个字符是小写字母: [abcdefghijklmnopqrstuvwxyz]        表示1个字符，内容是或a或b或c...或z
    第二个字符是大写：[ABCDEFGHIJKLMNOPQRSTUVWXYZ]       表示1个字符，内容是或A或B或C...或Z
    第三个字符是数字：[0123456789]       表示1个字符，内容是或0或1或2...或9

    [abcdefghijklmnopqrstuvwxyz]  简化为：[a-z]     范围是按照ASCII
    [ABCDEFGHIJKLMNOPQRSTUVWXYZ]  简化为：[A-Z]
    [0123456789]    简化为[0-9]        -本身不算
    """
    s = input("输入内容：")
    result = re.match("[a-z][A-Z][0-9]", s)  # 规则

    print_result(result)


def demo04():
    """
    第一个字符是字母（大小写都行），第二个是数字，后面随意
    [a-zA-Z]   字符数量1个，内容小写或大写
    [a-zA-Z]   等同于[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]
    """
    s = input("输入内容：")
    p = "[a-zA-Z][0-9]"
    result = re.match(p, s)

    print_result(result)


def demo05():
    """
    第一个字符不能是字母和数字
    [a-zA-Z0-9]  等于 [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]
    不是字母和数字
    [^a-zA-Z0-9] 不是这些
    [^]表示取反
    """
    s = input("输入内容：")
    p = "[^a-zA-Z0-9]"
    result = re.match(p, s)

    print_result(result)


"""
在正则表达式中：
\d:匹配一个数字,通常表示 0-9
\D:匹配一个非数字字符,相当于 \d 的取反
"""


def demo06():
    # \d匹配数字，0-9任意
    r"""
    前三个字符必须是数字，后面随意
    \d 表示字符数量为1，内容，必须是数字
    """
    s = input("输入内容：")
    p = r"\d\d\d"
    result = re.match(p, s)

    print_result(result)


def demo07():
    r"""
    前三个字符必须不是数字，后面随意
    \D 表示字符数量为1，内容，必须不是数字
    """
    s = input("输入内容：")
    p = r"\D\D\D"
    result = re.match(p, s)

    print_result(result)


def demo08():
    r"""
    匹配字符串开头的是如下的IPv4地址
    xxx.xxx.xxx.xxx

    .表示任意字符，数量1
    \. 表示 . 本身
    """
    s = input("输入内容：")
    p = r"\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"  # 在正则表达式中， \d:匹配一个数字,通常表示 0-9; \.匹配任意一个字符
    result = re.match(p, s)

    print_result(result)


"""
    \s 匹配空白
    \S 匹配非空白
"""


def demo09():
    r"""
    找 字母 字母 字母的串
    要求字符串中有即可，找到出现的第一个
    """
    s = input("输入内容：")
    p = r"[a-zA-Z]\s[a-zA-Z]\s[a-zA-Z]"

    result = re.search(p, s)
    print_result(result)


"""
    \w 匹配字母或数字或下划线    a-z A-Z 0-9 _ 汉字
    \W 匹配非字母或数字或下划线。
"""


def demo10():
    r"""
    要求字符串必须是 找到 2连字母+1个字符+2连字母   [a-zA-Z][a-zA-Z]\S[a-zA-Z][a-zA-Z]
    中间的一个字符不能是空白
    """
    s = input("输入内容：")
    p = r"[a-zA-Z][a-zA-Z]\S[a-zA-Z][a-zA-Z]"

    result = re.search(p, s)
    print_result(result)


def demo11():
    """
    匹配 xxxx xxxx
    x表示正常字符（有内容的），且不可以是符号

    """
    s = input("输入")
    p = r"\w\w\w\w\s\w\w\w\w"

    print_result(re.search(p, s))


def demo12():
    """
    用户设置密码，最少有1个特殊字符（!#!@*这些符号）
    """
    s = input("设置密码：")
    p = r"\W"

    result = re.search(p, s)
    if result:
        print("符合规则")
    else:
        print("必须有1个特殊字符")


if __name__ == '__main__':
    demo10()
