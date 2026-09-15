# 需求: 录入学生的分数(0-100),查询对应的等级: 90-100优 70-89良 60-69中  0-59差
# 1.获取用户录入的分数
score = int(input("请您输入分数(0-100):"))
# 2.判断(利用if嵌套，先判断成绩范围,再判断对应等级)
if 0 <= score <= 100:
    if score >= 90:
        print("等级: 优")
    elif score >= 70:
        print("等级: 良")
    elif score >= 60:
        print("等级: 中")
    else:
        print("等级: 差")
else:
    print("成绩无效,重新输入")
