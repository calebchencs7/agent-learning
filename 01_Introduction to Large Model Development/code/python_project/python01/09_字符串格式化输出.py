x = 11.345
# 旧版
print("x = %.2f" % x)  # x = 11.35
# 新版
print(f"x = {x:.2f}")  # x = 11.35

# 需求: 定义三个变量,分别存储你的姓名,年龄,体重,
# 要求格式化输出: '姓名:xx,年龄:xx岁,体重:xxkg'
name = "斌子"
age = 18
weight = 66.6

# 注意: 按住ctrl+鼠标左键print进入源码
# 方式1: print(多个内容)  不推荐,太麻烦
print("姓名:", name, ",年龄:", age, "岁,体重:", weight, " kg", sep="")

# 方式2: + 拼接字符串   不推荐,太麻烦
print("姓名:" + name + ",年龄:" + str(age) + "岁,体重:" + str(weight) + " kg")

# 方式3: %s占位   %s自动把整数,浮点数都转换为字符串放到对应位置
print("姓名:%s,年龄:%s岁,体重:%s kg" % (name, age, weight))

# 方式4: %s给字符串占位  %d给整数占位  %f给浮点数占位
print("姓名:%s,年龄:%d岁,体重:%.1f kg" % (name, age, weight))

# TODO 方式5(推荐): format格式方式-> f"{变量}"
print(f"姓名:{name},年龄:{age}岁,体重:{weight} kg")  # python3.x推荐
print("姓名:{},年龄:{}岁,体重:{} kg".format(name, age, weight))  # python2.x推荐

cr7 = "Cristiano Ronaldo"
print(
    f"The best football player in the world is {cr7}."
)  # The best football player in the world is Cristiano.
