"""
统计字符串中，各个字符的个数，
"hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
使用程序实现。
"""

text = "hello world"

char_count = {}

for char in text:
    if char == " ":
        continue

    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

for key, value in char_count.items():
    print(f"{key}:{value}", end=" ")
