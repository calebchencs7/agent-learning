import pandas as pd

# 创建示例数据
df = pd.DataFrame(
    {
        '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
        '年龄': [25, 30, 35, 28, 32],
        '部门': ['技术部', '销售部', '技术部', '人事部', '销售部'],
        '工资': [5000, 7000, 6000, 5500, 7500],
    }
)

print("原始数据：\n", df)
print("=" * 20)

# 条件筛选 df[筛选条件]    筛选条件 => df['列'] > 30  指定列大于30
# 示例  df[ df['列'] > 30  ]
# 年龄大于30
print("年龄大于30：\n", df[df['年龄'] > 30])

# 技术部
print("技术部内容：\n", df[df['部门'] == '技术部'])

# 类sql查询过滤   where 年龄 > 28 and 工资 < 700
print("年龄大于28且工资小于7000：\n", df.query('年龄 > 28 and 工资 < 7000'))

# 排序
print(
    "按工资降序排序：\n", df.sort_values('工资', ascending=False)
)  # ascending默认True（升序）

# 多列排序
print(
    "多列排序：\n",
    df.sort_values(
        ['部门', '工资'], ascending=False
    ),  # ascending:是否升序排列，默认True（升序），False（降序）
)
print("多列排序：\n", df.sort_values(['部门', '工资'], ascending=[True, False]))
