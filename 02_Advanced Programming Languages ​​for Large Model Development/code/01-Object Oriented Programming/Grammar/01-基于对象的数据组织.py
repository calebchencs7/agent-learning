"""
生活中：
1. 在excel中设计一个表
2. 打印机打印多个表
3. 把表的纸给用户，让用户填写
"""


class Student:
    name = None
    age = None
    addr = None


# 2. 打印具体的表格（创建类的对象）
stu1 = Student()
stu2 = Student()

# 3. 让用户填数据（记录数据）
stu1.name = "周杰轮"
stu1.age = 18
stu1.addr = "合肥"

stu2.name = "王力宏"
stu2.age = 22
stu2.addr = "杭州"

# 验证是否可以使用stu1 stu2这2个变量 得到用户填写的信息
print(f"stu1 name 是： {stu1.name}")
print(f"stu1 age 是： {stu1.age}")
print(f"stu1 addr 是： {stu1.addr}")

print(f"stu2 name 是： {stu2.name}")
print(f"stu2 age 是： {stu2.age}")
print(f"stu2 addr 是： {stu2.addr}")
