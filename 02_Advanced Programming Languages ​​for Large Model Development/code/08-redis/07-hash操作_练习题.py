# 1. 存入一个人的信息，key叫做user1001，value是字典，存入name、age、gender
#
# 2. 通过user1001这个key取出来他的name age gender信息
import redis

r = redis.Redis(
    host="10.211.55.3", port=6379, db=0, password=None, decode_responses=True
)

# 存入信息
# method1:
r.hset('user1001', 'name', 'caleb')
r.hset('user1001', 'age', 23)
r.hset('user1001', 'gender', '男')
# method2:
r.hset('user1002', mapping={'name': 'viola', 'age': 34, 'gender': '女'})

# 取出信息
# Method1:
print(r.hget("user1001", "name"), r.hget("user1001", "age"))
print(r.hget("user1002", "name"), r.hget("user1002", "age"))

# Method2:
userinfo: dict = r.hgetall('user1001')
print(userinfo)


# close
r.close()
