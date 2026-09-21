t = (1, 3, 5, 7)
d = {"name": "周杰轮", "age": 11, "gender": "男"}

# 字典拆包输出
# print(*d)
# print(*d.values())


def add(x, y, z, z1):
    print(x + y + z + z1)


# 3 ways to call the add function
add(t[0], t[1], t[2], t[3])
# *t     1, 3, 5, 7  => 用于传递参数
add(*t)
add(1, 3, 5, 7)


def info(name, age, gender):
    print(f"我是{name}，今年{age}岁，性别：{gender}")


info(name=d["name"], age=d["age"], gender=d["gender"])
info(**d)  # info(name="周杰轮", age=11, gender="男")
