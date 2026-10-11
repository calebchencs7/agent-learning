import redis

r = redis.Redis(
    host="10.211.55.3", port=6379, db=0, password=None, decode_responses=True
)

# zadd添加有序集合   -> mapping -> dict
r.zadd(
    "leaderboard",
    {
        # 虽然 zadd() 接收 Python 字典，但这个字典用来提供“成员 → 分数”，
        # Redis 存储的类型仍然是 ZSet
        "小曹": 2000,  # k->v   信息->分数
        "小花": 5000,
        "小旺": 6000,
        "小翠": 1000,
    },
)
asc_names = r.zrange('leaderboard', 0, -1)
print(asc_names)

# 升序
asc_names = r.zrange('leaderboard', 0, -1, withscores=True)
print(asc_names)
# 降序
desc_names = r.zrevrange('leaderboard', 0, -1, withscores=True)
print(desc_names)

# 获取分数
print("小曹分数:", r.zscore("leaderboard", '小曹'))

# 增加分数
r.zincrby("leaderboard", 1000, '小曹')
print("小曹分数:", r.zscore("leaderboard", '小曹'))

# 得到排名从低到高  从0开始排名
print("小曹排名:", r.zrank('leaderboard', '小旺'))


# 按分数范围获取
scores = r.zrangebyscore('leaderboard', 1000, 5000, withscores=True)
print(scores)
r.close()
