import redis

# 创建redis连接，TCP长连接
conn = redis.Redis(
    host="10.211.55.3",  # 数据库IP地址
    port=6379,  # Redis默认端口6379
    db=0,  # Redis默认有一个序号为0的数据库
    password=None,  # Redis默认没密码，需要密码自己设（豆包）
    decode_responses=True,  # 自动解码回复，也就是字符串会正常显示，而不是显示二进制字节
)

# 测试  ping方法，测试通不通，通了返回True，否则False
response = conn.ping()
print(response)

conn.close()
