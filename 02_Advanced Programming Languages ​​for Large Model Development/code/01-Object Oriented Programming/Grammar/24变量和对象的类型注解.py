# 1 基础类型的注解
var_1: int = 10
var_2: float = 12.33
var_3: bool = True
var_4: str = "asd"

var_5: list = 10  # 注意，注解就是注释，不会影像变量本身的类型
print(var_5)
print(type(var_5))  # 输出int


# 2 类类型
class Student:
    pass


stu: Student = Student()

# 3 容器类型
my_list: list = [1, True, "a"]
my_tuple: tuple = (1, True, "a")
my_set: set = {1, True, "a"}
my_dict: dict = {"a": 1, "b": 2}

# 4 同元素类型容器注解
my_list2: list[int] = [1, 2, 3]  # 列表里面都是int
my_tuple2: tuple[str] = ("a", "b", "c")  # tuple里面都是str
my_set2: set[float] = {1.1, 2.2, 3.3}  # set内都是float
my_dict2: dict[str:int] = {"a": 1, "b": 2}  # 字典内的键值对，key都是str，value都是int


# 5. 在注释中写类型描述
num1 = 10  # 这是int类型（这种写法out啦）
num2 = 10  # type: int    # 这是标准写法
num3 = 12.33  # type: float
