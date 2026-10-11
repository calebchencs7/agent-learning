import redis

r = redis.Redis(
    host="10.211.55.3", port=6379, db=0, password=None, decode_responses=True
)

#
r.hdel("usercaleb", 'name')
print(r.hgetall('usercaleb'))  # {'age': '23', 'gender': '男'}

r.close()
