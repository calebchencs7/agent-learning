from data_class import DataClass
import json


class FileReader:
    def __init__(self, path, encoding="UTF-8") -> None:
        self.fr = open(path, "r", encoding=encoding)

    def read_csv(self) -> list[DataClass]:
        data_list = []
        for line in self.fr.readlines()[1:]:
            line = line.strip()
            # 分隔
            arr = line.split(",")

            dc = DataClass(arr[0], arr[1], float(arr[2]), arr[3])
            data_list.append(dc)

        return data_list

    def read_json(self) -> list[DataClass]:
        """{"日期":"2026-05-01","订单ID":"ORD7392645","销售额":4885,"省份":"广东"}"""

        # JSON 就是字典的字符串形式
        # 如何吧JSON字符串转为字典， 字典 = json.loads(字符串)
        data_list = []
        for line in self.fr.readlines():
            line = line.strip()
            # 字符串转字典
            data_dict = json.loads(line)

            # 从字典 data_dict 中取出一条销售记录的数据，然后创建一个 DataClass 对象，并将对象保存到变量dc内
            dc = DataClass(
                data_dict['日期'],
                data_dict['订单ID'],
                data_dict['销售额'],
                data_dict['省份'],
            )
            data_list.append(dc)

        return data_list
