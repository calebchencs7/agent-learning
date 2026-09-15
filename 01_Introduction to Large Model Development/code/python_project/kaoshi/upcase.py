"""
我们定义，在以下情况时，单词的大写用法是正确的：
​ 第一种情况：全部字母都是大写，比如 "USA" 。
​ 第二种情况：单词中所有字母都不是大写，比如 "leetcode" 。
​ 第三种情况：如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。

​ 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。

​ 示例 1：
​ 输入：word = "USA"
​ 输出：true

​ 示例 2：
​ 输入：word = "FlaG"
​ 输出：false

​ 提示：
​ 1 <= word.length <= 100
​ word由小写和大写英文字母组成
"""


def detectCapitalUse(word):
    if word.isupper() or word.islower():
        return True
    elif word[0].isupper() and word[1:].islower():
        return True
    else:
        return False


result1 = detectCapitalUse("USA")
print(result1)  # 输出: True
result2 = detectCapitalUse("FlaG")
print(result2)  # 输出: False
