# 要求用户输入一个字符串，遍历当前字符串并打印，如果遇见“q”,则终止循环
str = input("请输入一个字符串：")
for ch in str:
    if ch == 'q':
        break
    print(ch)
