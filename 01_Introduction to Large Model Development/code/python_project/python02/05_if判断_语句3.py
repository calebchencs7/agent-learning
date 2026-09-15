# 需求: 录入学生的分数(0-100),查询对应的等级: 90-100优 70-89良 60-69中  0-59差
# 获取用户录入的分数
score = int(input("请您输入分数(0-100):"))
# 再判断
if 90 <= score <= 100:
    print("等级: 优")
elif 70 <= score <= 89:
    print("等级: 良")
elif 60 <= score <= 69:
    print("等级: 中")
elif 0 <= score <= 59:
    print("等级: 差")

else:
    print("成绩无效,重新输入")
