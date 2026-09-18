class Worker:

    def __init__(self, name, work_id):
        self.name = name
        self.work_id = work_id

        self.__salary = 0

    def __increment_salary(self, num):
        # 做一堆验证
        # 做一堆验证
        # 做一堆验证
        # 做一堆验证
        # 做一堆验证
        self.__salary += num

    def __decrement_salary(self, num):
        self.__salary -= num

    def work_oneday(self):
        print("工作1天了")
        self.__increment_salary(1000)

    def work_late(self):
        print("工作迟到了")
        self.__decrement_salary(500)

    def get_salary(self):  # oa 查询入口
        return self.__salary


worker = Worker("牛马", "1")

print(f"我目前薪水：{worker.get_salary()}")
worker.work_oneday()
print(f"我目前薪水：{worker.get_salary()}")
print("............")
worker.__salary = 999999
print(f"我目前薪水：{worker.get_salary()}")
