import pymysql

connection = pymysql.connect(
    host='10.211.55.3',
    port=3306,
    user='root',
    password='5236980',
    charset='utf8mb4',
)
print(connection.get_server_info())
connection.close()
