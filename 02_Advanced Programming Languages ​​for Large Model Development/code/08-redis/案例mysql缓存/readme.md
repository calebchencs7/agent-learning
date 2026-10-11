# 需求
mysql：可以存的数据多，查询效率不高（相对redis）

redis：可以存的少，但是查询效率极高（相对MySQL）

## 设计
- 用户要求查询信息，先看看redis有没有
- redis有，则从redis直接返回
- redis没有，从mysql现查，查完后放入redis

## 思考
- 基于上面的设计，redis的内容会越来越多
- 每一个从mysql查出来的内容放入redis设置ttl
- 每一次从redis命中，重置ttl
- 如果长时间这个Redis的数据没有命中，自动就消失了

# 代码
- 以面向对象设计，有几个实体？
- 被操作的：MySQL和Redis 2个数据库
- 实体：MySQL
- 实体：Redis
- 2个class，一个服务MySQL一个服务Redis

## class MySQL
- __init__(host, port, user, pswd, db, charset)
- __del__()，自动销毁，关闭TCP连接
- def get_user_info(username) -> 信息

## class Redis
- __init__(host, port, pswd, db)
- __del__() close()
- def get_user_info(username) -> 信息
- def save_user_info(info)
- def ttl_reset()

