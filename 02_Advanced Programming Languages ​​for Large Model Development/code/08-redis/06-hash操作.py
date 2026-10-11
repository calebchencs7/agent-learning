import redis

r = redis.Redis(
    host="10.211.55.3", port=6379, db=0, password=None, decode_responses=True
)

# hset(k1, k2, v)
# redis记录的k-v
# k就是k1   v(k2->v)

r.hset('usercaleb', 'age', '23')
r.hset('usercaleb', 'hobby', 'coding')
r.hset('usercaleb', 'height', '181')

# 取出
# r.hget(k1, k2)
hobby = r.hget('usercaleb', 'hobby')
print(hobby)

# 取出全部的字段
userinfo: dict = r.hgetall('usercaleb')
print(userinfo)

print("--------------------")

# 一次性设置hash里面的k-v
r.hset('userviola', mapping={'name': 'viola', 'age': 34, 'gender': '女'})

print("---------------------------")
keys = r.hkeys('userviola')
print("viola的keys：", keys)
values = r.hvals('userviola')
print("viola的values：", values)
r.close()
