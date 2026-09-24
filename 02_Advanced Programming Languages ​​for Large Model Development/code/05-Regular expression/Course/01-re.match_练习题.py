# input输入内容，内容随意
# 要求匹配是否是heima开头
# 是的话输出匹配成功，并输出匹配结果
# 否则输出匹配失败

import re

s = input("输入内容：")

result = re.match("heima", s)

if result:  # 对象有有意义的内容就是True，None就是False
    print("匹配成功")
    # 结果通过 result.group()提取
    print("结果：", result.group())
else:
    print("匹配失败")
