import redis

r = redis.Redis(
    host="10.211.55.3",  # 数据库IP地址
    port=6379,  # Redis默认端口6379
    db=0,  # Redis默认有一个序号为0的数据库
    password=None,  # Redis默认没密码，需要密码自己设（豆包）
    decode_responses=True,  # 自动解码回复，也就是字符串会正常显示，而不是显示二进制字节
)

# redis结构是K+V
# K字符串
# V是各类类型，我们现在的V演示为字符串
# set存入  set(k, v)
r.set('name', 'caleb')
r.set('age', '23')

# 取出  get取出，  v = r.get(k)
name = r.get('name')
age = r.get('age')
age123 = r.get('age123')  # K不存在，结果为None
print(f"取出name：{name}，age：{age}, {age123}")

print("-----------------------------------------")
# mset multi set
# r.mset({k:v, k: v, K:v})
r.mset({"hobby": "唱跳RAP", "money": "123456", "gender": "男"})
# r.mget([k, k, k])   返回值 -> [v, v, v]
values = r.mget(['hobby', 'money', 'gender'])
print(f"一次型取出：{values}")
r.close()
