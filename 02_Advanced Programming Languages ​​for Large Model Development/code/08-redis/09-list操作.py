# list操作，  redis  ：k -> v   ，  k字符串， v是list
import redis

r = redis.Redis(
    host="10.211.55.3", port=6379, db=0, password=None, decode_responses=True
)

# 存入列表
# 从列表左侧插入
r.lpush("lst1", 't1', 't2', 't3')  # t3, t2, t1
# 从列表右侧插入
r.rpush('lst1', 't4', 't5', 't6')  # t3, t2, t1, t4, t5, t6

# 长度
length = r.llen('lst1')
print(f"列表长度：", length)

# 获取下标范围的元素
all_element = r.lrange('lst1', 0, -1)
print(f"全部列表内容：", all_element)
# 获取前3      # 包头包尾
all_element = r.lrange('lst1', 0, 2)
print(f"全部列表内容：", all_element)

# 取出第一个元素，弹出数量不管是1还是多，都是结果为[x,...]
first_e = r.lpop('lst1', 1)
print("左弹出：", first_e)
right_e = r.rpop('lst1', 2)
print("右弹出：", right_e)

r.close()
