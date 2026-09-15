class Phone:
    def call(self):
        print("5G通话")


class NFCReader:
    def reader(self):
        print("第五代NFC读卡器")


class RemoteControl:
    def control(self):
        print("红外遥控器工作")


class RedMiPhone(Phone, NFCReader, RemoteControl):
    pass  # 此处没代码，规避语法报错


redmi = RedMiPhone()
redmi.call()
redmi.reader()
redmi.control()
