# 向user表插入10000条数据
import pymysql
import random

names = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 1. 连接（TCP）
conn = pymysql.connect(
    host="10.211.55.3",
    port=3306,
    user="root",
    password="5236980",
    charset="utf8",
    database="jing_dong",
)

# 2. cursor
cursor = conn.cursor()

# 3. 执行sql
for data_id in range(4, 10004):
    user = random.choice(names) + random.choice(names) + random.choice(names)
    password = "123456"

    sql = f"INSERT INTO user VALUES({data_id}, '{user}', '{password}')"
    cursor.execute(sql)

# 4. 确认
conn.commit()

# 5. 关闭
cursor.close()
conn.close()
