import redis

r = redis.Redis(
    host="10.211.55.3", port=6379, db=0, password=None, decode_responses=True
)

r.set('name', "viola")
v = r.get('name')
print(f"取出name：{v}")

#
r.mset({'age': '34', 'gender': '女'})
vs = r.mget(['age', 'gender'])
print(vs)

r.close()
