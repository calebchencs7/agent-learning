import redis

r = redis.Redis(
    host="10.211.55.3", port=6379, db=0, password=None, decode_responses=True
)

# 存入集合（去重）
r.sadd("set1", 'python', 'itheima', 'itcast', 'python')
# 获取全部
all_tags: set = r.smembers('set1')
print(all_tags)

# 判断元素是否有
is_member = r.sismember('set1', 'python')
print('是否有python结果：', is_member)  # 结果1 True 0为False

# 弹出元素（集合没下标,随机弹出元素）
ele = r.spop('set1')
print('弹出：', ele)

# 指定弹出（删除）元素
r.srem('set1', 'itheima')  # srem:Remove values from set name
print("删除后：", r.smembers('set1'))

r.sadd('seta', 'a', 'b', 'c')
r.sadd('setb', 'd', 'b', 'c')

# 交集
intersection = r.sinter('seta', 'setb')
print("交集", intersection)

# 并集
union = r.sunion('seta', 'setb')
print("并集", union)

# 差集
difference = r.sdiff('setb', 'seta')
print(f"差集：", difference)
r.close()
