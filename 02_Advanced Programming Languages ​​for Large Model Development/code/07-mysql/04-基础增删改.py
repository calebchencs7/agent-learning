import pymysql

# 连接数据库(TCP)
connection = pymysql.connect(
    host='10.211.55.3',
    user='root',
    password='5236980',
    charset='utf8mb4',
    database='jing_dong',
)

# 创建游标对象
cursor = connection.cursor()

# 执行SQL语句
numlines = cursor.execute("insert into user values(2, 'ch', '123456')")
print(f"受影响的行数：{numlines}")

# 提交事务
connection.commit()  # 确认

# 关闭游标对象
cursor.close()

# 关闭连接
connection.close()
