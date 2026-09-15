class Phone:

    def __init__(self):
        self.__is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G打开")
        else:
            print("5G关闭，使用4G")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()

# 私有成员，无法外部修改
# phone.__is_5g_enable = True

phone = Phone()
phone.call_by_5g()
