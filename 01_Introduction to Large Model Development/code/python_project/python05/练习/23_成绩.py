"""
考试成绩的问题：提示用户输入成绩，判断是属于哪个水平，将结果打印到控制台。
60以下不及格，60分以上为及格，70分至80分为合格，80分至90分为良好，90分以上为优秀。
例如：请输入考试成绩：85，打印“你的成绩是良好”
"""

score = int(input('输入你的成绩:'))

if score < 0 or score > 100:
    print('成绩输入错误')
elif score >= 90:
    print('你的成绩是优秀')
elif score >= 80:
    print('你的成绩是良好')
elif score >= 70:
    print('你的成绩是合格')
elif score >= 60:
    print('你的成绩是及格')
else:
    print('你的成绩不及格')
