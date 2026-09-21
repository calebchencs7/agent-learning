"""
私有成员写法：
- 单下划线开头 ： 约定俗成
- 双下划线开头 ： 打死不给用
"""

class Student:
    def __init__(self, name):
        self.name = name
        self._balance = 1000

    def _haha(self):
        print("哈哈哈哈哈")

stu = Student("王大锤")
print(stu._balance)

stu._haha()
