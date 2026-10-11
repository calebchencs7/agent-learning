# 1. 导入模块
import pymysql

# 2. 创建连接类的类对象
# Connection对象，负责整个网络的连接通畅,TCP/IP协议，网络连接
conn = pymysql.connect(
    host="10.211.55.3",  # 指定MySQL服务器的IP地址
    port=3306,  # 默认在3306端口
    user="root",  # 指定用户名
    password="5236980",  # 指定密码
    charset="utf8mb4",  # 指定编码集
    database="jing_dong",  # 指定数据库
)

# 3. 创建游标(cursor)
# 干活的是游标对象
# conn负责的是整个网络的连接通畅
# 游标对象，是干活的小弟
# conn是老大，保持住网络，游标cursor是小弟，干活
cursor = conn.cursor()

# 4. 执行sql查询, execute执行
cursor.execute("SELECT name,brand_name,price from goods where price>5000;")

# 4.1 小弟执行完SQL后，结果小弟cursor保存了，可以取出
# fetchone抓取一行结果，格式是元组：(列, 列, 列...)
# r1 = cursor.fetchone()
# print(r1)
# r2 = cursor.fetchone()
# print(r2)

# 4.2 抓取全部
all_result = cursor.fetchall()
# 返回结果： (  (列, 列, ...), (), (), ...)
print(all_result)


for row in all_result:
    name = row[0]
    brand_name = row[1]
    price = row[2]
    print(f"商品名称：{name}，品牌：{brand_name}，价格：{price}")


# 5. 关闭游标
cursor.close()
# 6. 关闭连接
conn.close()
