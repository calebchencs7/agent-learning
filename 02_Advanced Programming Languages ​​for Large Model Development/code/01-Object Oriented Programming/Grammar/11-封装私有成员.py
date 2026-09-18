class Phone:
    producer = "apple"

    # 私有成员变量，变量名以__开头
    __running_voltage = 1.12  # 标准电压

    def __init__(self, name):
        self.name = name
        self.__current_voltage = 1.15  # 当前电压

    def __cpu_boost(self):
        self.__current_voltage = 1.5
        print("CPU超频")

    def power_mode(self, mode):
        if mode == "high":
            self.__cpu_boost()
        else:
            print("默认模式")

    def camera(self):
        print("拍照了")

    def call(self):
        print("通话了")


phone = Phone("小曹的Iphone")
print(phone.name)
phone.camera()
phone.call()

phone.power_mode("high")
