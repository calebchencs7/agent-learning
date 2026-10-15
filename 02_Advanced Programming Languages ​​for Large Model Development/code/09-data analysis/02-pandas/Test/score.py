"""
Pandas 筛选高分学生
背景：
班主任想快速找出成绩优秀的学生。现在有一份简单的学生成绩数据，需要筛选出分数大于 80 的学生。
问题：
使用 Pandas 创建学生成绩数据，包含 name 和 score 两列，输出分数大于 80 的学生。
"""

import pandas as pd

# 创建学生成绩数据
df = pd.DataFrame(
    {'name': ['张三', '李四', '王五', '赵六', '钱七'], 'score': [85, 72, 90, 65, 95]}
)

# 筛选分数大于80的学生
result = df[df['score'] > 80]

# 输出结果
print(result)
