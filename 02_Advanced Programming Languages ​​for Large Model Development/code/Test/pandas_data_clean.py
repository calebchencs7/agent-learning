"""
Pandas 空值筛选错题
背景：
小张统计班级迟到数据，想要筛选出迟到次数不为空的所有学生全部信息，代码运行直接报错，请找出 bug、说明原因、给出完整修复代码。
题目：
请阅读下面代码，判断代码是否有问题。如果有问题，请说明问题原因并写出修复后的代码。

import pandas as pd

data = {
    "name": ["张三", "李四", "王五", "赵六"],
    "late_count": [2, None, 0, None]
}
df = pd.DataFrame(data)
# 筛选迟到次数不为空的数据
res = df[df["late_count"] != None]
print(res)
"""

import pandas as pd

data = {"name": ["张三", "李四", "王五", "赵六"], "late_count": [2, None, 0, None]}
df = pd.DataFrame(data)
# 筛选迟到次数不为空的数据
res = df[df["late_count"].notnull()]
print(res)
