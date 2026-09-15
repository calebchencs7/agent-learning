"""
将26个英文字母分为了三组。给你一个字符串数组word，判断字符串中的所有字母是否在同一组。只返回所有字母在同一组的字符串。
请注意，字符串中的字母 不区分大小写，相同字母的大小写形式都被视为在同一组。

26个英文字母分组如下：
第一组由字符 "qwertyuiop" 组成。
第二组由字符 "asdfghjkl" 组成。
第三组由字符 "zxcvbnm" 组成。

示例 1：
输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
解释：由于不区分大小写，"a" 和 "A" 都在第二组。

示例 2：
输入：words = ["omk"]
输出：[]

示例 3：
输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]

提示：
1 <= words.length <= 20
 1 <= words[i].length <= 100
words[i] 由英文字母（小写和大写字母）组成
"""


def detect_words_in_same_group(words):
    group1 = "qwertyuiop"
    group2 = "asdfghjkl"
    group3 = "zxcvbnm"
    result = []
    for word in words:
        lower_word = word.lower()
        if (all(char in group1 for char in lower_word)
                or all(char in group2 for char in lower_word)
                or all(
                    char in group3 for char in lower_word)):
            result.append(word)
    return result


words1 = ["Hello", "Alaska", "Dad", "Peace"]
words2 = ["omk"]
words3 = ["adsdf", "sfd"]

print(detect_words_in_same_group(words1))  # 输出: ["Alaska", "Dad"]
print(detect_words_in_same_group(words2))  # 输出: []
print(detect_words_in_same_group(words3))  # 输出: ["adsdf", "sfd"]
