# | 匹配左右任意一个表达式，或者
# ()
#   1. 将内容作为整体
#   2. 将内容作为一个分组
# \数字   引用分组的内容
import re


def demo01():
    # 需求：匹配163 qq sina的邮箱，且@符号前面4-20位 结尾.com .cn
    # 使用或关系： (x|y|z)  x或y或z， xyz就是规则
    s = input("输入内容：")
    p = r"^\w{4,20}@(163|qq|sina)\.(com|cn)$"

    r = re.match(p, s)
    if r:
        print("成功")
        print(r.group())
    else:
        print("匹配失败")


def demo02():
    # 需求：匹配163 qq sina的邮箱，且@符号前面4-20位 结尾.com .cn
    # 使用或关系： (x|y|z)  x或y或z， xyz就是规则
    # ()本身也是分组
    s = input("输入内容：")
    p = r"^\w{4,20}@(163|qq|sina)\.(com|cn)$"

    r = re.match(p, s)
    if r:
        print("成功")
        print(r.group())
        print(r.group(0))
        print(r.group(1))
        print(r.group(2))
    else:
        print("匹配失败")


def demo03():
    # 需求：匹配163 qq sina的邮箱，且@符号前面4-20位 结尾.com .cn
    # 使用或关系： (x|y|z)  x或y或z， xyz就是规则
    # ()本身也是分组
    # 需求：输出@之前内容  输出@之后的域名  输出.后面的结尾
    # abcd@qq.com   输出 abcd   输出qq   输出com
    s = input("输入内容：")
    p = r"^(\w{4,20})@(163|qq|sina)\.(com|cn)$"
    # ()也是分组，从左到右，序号是组1组2组3...

    r = re.match(p, s)
    if r:
        print("成功")
        print("@符号之前：", r.group(1))
        print("@符号之后：", r.group(2))
        print(".符号之后：", r.group(3))
    else:
        print("匹配失败")


def demo04():
    """
    匹配HTML标签，HTML标签规则符合如下：
    <h1>............</h1>
    <abc>............</abc>
    <ccc>............</ccc>
    """
    s = input("输入内容：")

    # \1是引用分组1的内容
    p = r"^<(\w+)>.*</\1>$"

    r = re.match(p, s)
    if r:
        print("成功", r.group())
    else:
        print("匹配失败")


def demo05():
    """
    邮箱 abcd@qq.com
    邮箱允许 @之前4-20   @之后，qq.com或sina.com 或163.com
    输入字符串是：
    abcd@qq.com 二级域名abcd 域名qq.com
    :return:
    """
    s = input("输入：")
    p = r"^(\w{4,20})@(qq\.com|sina\.com|163\.com)\s二级域名\1\s域名\2$"

    r = re.match(p, s)
    if r:
        print("成功", r.group())
        print("二级域名：", r.group(1))
        print("域名：", r.group(2))
    else:
        print("匹配失败")


def demo06():
    """
    将合规手机号，替换为185****1234
    在sub中，参数2repl，也可以用正则，可以引用规则中的分组
    """
    s = input("手机号：")

    p = r"(\d{3})\d{4}(\d{4})"

    r = re.sub(p, r"\1****\2", s)
    print(f"替换后：{r}")


# demo06()


def demo07():
    s = input("手机号：")
    s = s[:3] + "****" + s[7:]
    print(s)


demo02()
