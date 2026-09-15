"""
写一个 lambda 表达式，用于将字符串列表中的字符串都转换为大写
"""

ch_list = ['c', 'h', 'i', 'n', 'a']

upcase = (lambda ch: [i.upper() for i in ch])(ch_list)

print(upcase(ch_list))
