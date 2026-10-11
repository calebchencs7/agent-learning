import pymysql
import random

# 1. conn
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
# 可能异常的放在try中，异常处理放在except中
try:
    for i in range(1, 10001):
        name = f"王大锤{i}"
        gender = random.choice(["男", "女"])
        height = random.randint(160, 186)
        age = random.choice([22, 11, 33, 21, 25, 26, 28, 20])

        if i == 5001:
            sql = f"INSERT INTO student VALUES({i}, '{name}', '{gender}', {height}, {age}, 12345)"  # 第5001条数据插入错误，字段数不匹配
        else:
            sql = f"INSERT INTO student VALUES({i}, '{name}', '{gender}', {height}, {age})"

        # sql = f"INSERT INTO student VALUES({i}, '{name}', '{gender}', {height}, {age})"
        cursor.execute(sql)

        if i % 1000 == 0:
            print(f"插入了{i}条数据")

    conn.commit()  # 确认这些操作生效
except Exception as e:
    print(f"插入数据库中途出现问题，前面全部操作撤回: {e}")
    conn.rollback()  # 撤回

# 4. close
cursor.close()
conn.close()
