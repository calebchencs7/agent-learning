import redis

r = redis.Redis(
    host="10.211.55.3", port=6379, db=0, password=None, decode_responses=True
)

r.set('num', '0')

# incr -> increment
r.incr('num')  # num的值+1
print('自增+1后', r.get('num'))

# incrby -> increment by
r.incrby('num', 5)
print('增长+5后', r.get('num'))

# decr -> decrement
r.decr('num')
print('自减-1后', r.get('num'))
# decrby -> decrement by
r.decrby('num', 3)
print('自减-3后', r.get('num'))

# 如果是复杂计算，就取出来，自己算，算完存回去
# num = int(r.get('num'))
# num = num * 10 + 2
# r.set('num', num)
# print('计算后：', r.get('num'))

r.close()
