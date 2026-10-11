# 查询商品名称、品牌、价格，要求是大于5000的价格
# 输出格式是： 每一个商品输出为： 商品名称：xxx，商品品牌：xxx，商品价格：xxx
import pymysql

# conn连接（TCP 三次握手）
conn = pymysql.connect(
    host="10.211.55.3",
    port=3306,
    user="root",
    password="123456",
    charset="utf8",
    database="jing_dong",
)

# 创建游标对象
cursor = conn.cursor()

# 查询
cursor.execute("select name, brand_name, price from goods where price > 5000")

# 抓取结果      all_result ==> ((name, brand_name, price), (), (), ...)
all_result = cursor.fetchall()

# 循环输出
for row in all_result:
    name = row[0]
    brand_name = row[1]
    price = row[2]

    print(f"商品名称：{name}，商品品牌：{brand_name}，商品价格：{price}")

# 关闭小弟
cursor.close()

# 关闭连接（断网，四次挥手）
conn.close()
