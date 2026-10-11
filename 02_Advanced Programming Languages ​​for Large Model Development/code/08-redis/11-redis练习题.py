import redis

r = redis.Redis(
    host="10.211.55.3", port=6379, db=0, password=None, decode_responses=True
)

r.lpush("lst1", 5, 4, 3, 2, 1)
r.rpush("lst2", "a", "b", "c", "d", "e")
print("lst1:", r.lrange("lst1", 0, -1))
print("lst2:", r.lrange("lst2", 0, -1))

r.lpush("lst1", 8, 7, 6)
r.rpush("lst2", "f", "g", "h")

print("lst2", r.lrange("lst2", 0, -1))

# -------
r.sadd("set3", "a", "b", "c", "a", "e", "a", "f")
r.spop("set3", 1)
print("set3: ", r.smembers("set3"))
r.srem("set3", "f")
print("set3: ", r.smembers("set3"))


r.close()
