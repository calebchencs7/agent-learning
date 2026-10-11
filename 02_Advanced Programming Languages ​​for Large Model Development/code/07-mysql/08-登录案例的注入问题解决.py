import pymysql

username = input("请输入账户")
password = input("请输入密码")

# 1. 创建连接，代码（客户端）到服务器MySQL的TCP连接，获得连接类的类对象
conn = pymysql.connect(
    host="10.211.55.3",
    port=3306,
    user="root",
    password="123456",
    database="jing_dong",
    charset="utf8",
)

# 2. cursor
cursor = conn.cursor()

# 3. 执行SQL
# 使用%站位，等同字符串格式化，%s
sql = "SELECT * FROM user WHERE user=%s and pwd=%s"
print(sql)
cursor.execute(sql, [username, password])
# ((), ())
all_result = cursor.fetchall()
if len(all_result) > 0:
    print("认证通过")
else:
    print("认证失败")

# 4. close
cursor.close()
conn.close()
