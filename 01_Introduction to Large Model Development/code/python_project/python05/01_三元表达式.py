# 需求: 判断年龄,如果成年了:就可以进入网吧,否则回家写作业去
age = 16
# 原始方式:if else
if age >= 18:
    print('可以进入网吧了！')
else:
    print('回家写作业吧!')

# 三元表达式: if else
result = '可以进入网吧了！' if age >= 18 else '回家写作业吧!'
print(result)
