"""
数据准备
MySQL:
create database if not exists my_db charset utf8;


create table if not exists userinfo(
    id int primary key,
    name varchar(255) not null ,
    age int,
    height float,
    hobby varchar(255)

);


use my_db;

insert into userinfo values (1,'caleb',23,181,'coding') ;



Redis:



"""

import json

import redis
import pymysql


class MySQLService:

    def __init__(
        self,
        host="10.211.55.3",
        port=3306,
        user="root",
        password="5236980",
        db="my_db",
        charset="utf8",
    ):
        # 连接对象
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
            charset=charset,
        )
        # 创建游标对象，用于执行sql
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_user_info(self, username):
        sql = "SELECT * FROM userinfo WHERE name=%s"
        self.cursor.execute(sql, [username])

        # 获取结果
        return self.cursor.fetchall()


class RedisService:

    def __init__(
        self, ms: MySQLService, host="10.211.55.3", port=6379, pswd=None, db=0
    ):
        self.redis_conn = redis.Redis(
            host=host,
            port=port,
            password=pswd,
            db=db,
            decode_responses=True,
        )

        self.ms: MySQLService = ms

    def __del__(self):
        self.redis_conn.close()

    # 内部private方法，设置TTL过期时间，默认300秒
    def __ttl_reset(self, key, ttl_time=300):
        # 设置TTL默认为300秒
        self.redis_conn.expire(key, ttl_time)

    def __save_user_info(self, username, infos):
        """
        save_user_info 方法是把查到的用户信息存进 Redis 缓存，
        并设置缓存的过期时间。
        """
        # 周杰轮: -> ((), ())
        # redis: key:周杰轮， value：list[(id, name, age), (), ()]
        for info in infos:  # 遍历查询结果，每次取出一条用户记录。
            # 以 username 为 Redis 的 key，把这条记录追加到对应 List 列表的末尾。
            self.redis_conn.rpush(
                username,
                json.dumps(
                    info, ensure_ascii=False
                ),  #   # json.dumps() 的作用是：把 Python 对象转换成 JSON 字符串。
            )  # 将元组序列化为字符串存储到Redis中
        # 设置过期时间
        self.__ttl_reset(username)

    def get_user_info(self, username):
        """
        get_user_info 方法是从 Redis 缓存中获取用户信息，
        如果缓存中没有，则从 MySQL 数据库中查询，并将结果存入 Redis 缓存。
        """
        # 检查 Redis 中是否存在该用户的缓存
        if self.redis_conn.exists(username):  # 1 True
            # Redis 中存在数据
            print(f"查询{username}，缓存命中，重设TTL")
            # 重设TTL
            self.__ttl_reset(username)

            # 返回缓存中的用户信息
            # username作为key，返回对应的list，从0到-1表示返回整个list
            cached_infos = self.redis_conn.lrange(username, 0, -1)
            return tuple(tuple(json.loads(info)) for info in cached_infos)
        else:
            # Redis 中不存在数据
            print(f"查询{username}，缓存未命中，跳转MySQL查询")
            # 从 MySQL 数据库中查询用户信息
            infos = self.ms.get_user_info(username)  # ((), ())

            # 如果mySQL中有数据，则保存到redis中
            if infos:  # 空元组是False，非空是True
                print(
                    f"查询{username}，缓存未命中，从MySQL中查询得到信息，同检索到{len(infos)}条信息"
                )
                self.__save_user_info(username, infos)
                print(f"保存信息{infos}到redis")
            else:
                print(f"查询{username}，缓存未命中，MySQL也没查到，没有此用户")

            return infos


if __name__ == '__main__':
    ms = MySQLService()
    rs = RedisService(ms)

    while True:
        username = input("输入要查询的姓名，要退出输入exit:")
        if username == "exit":
            break

        infos = rs.get_user_info(username)
        print(infos)
