"""
给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。
记录中只含下面三种字符：
 'A'：Absent，缺勤
 'L'：Late ， 迟到
 'P'：Present，到场

如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
条件一：按 总出勤 计，学生缺勤（'A'）严格 少于两天。
条件二：学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。

如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。

示例 1：
输入：s = "PPALLP"
输出：true
解释：学生缺勤次数少于 2 次，且不存在 3 天或以上的连续迟到记录。

示例 2：
输入：s = "PPALLL"
输出：false
解释：学生最后三天连续迟到，所以不满足出勤奖励的条件。

提示：
1 <= s.length <= 1000
 s[i] 为 'A'、'L' 或 'P'
"""


def detectPresence(str):
    # 统计缺勤次数
    absent_count = str.count('A')

    # 检查是否有连续三天或以上的迟到记录
    if 'LLL' in str:
        return False

    # 检查缺勤次数是否少于两天
    if absent_count < 2:
        return True
    else:
        return False


demo1 = "PPALLP"
demo2 = "PPALLL"
print(detectPresence(demo1))
print(detectPresence(demo2))
