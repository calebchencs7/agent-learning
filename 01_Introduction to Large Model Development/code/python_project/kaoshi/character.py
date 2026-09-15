"""
定义一个字符串，如str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。
编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。
"""
import random

str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_random_string(str, length):
    """
    生成指定长度的随机字符串
    :str: 待抽取的字符串
    :param length: 随机字符串的长度
    :return: 随机字符串
    """
    return ''.join(random.sample(str, length))


print(generate_random_string(str1, 4))
