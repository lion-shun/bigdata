"""
文件相关
"""
import json

from data_def import Record


class FileRead:
    def read_data(self) -> list[Record]:
        # 读取文件数据，定义为Record对象，封装到list返回
        pass


class TextFileRead(FileRead):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:  # 复写父类的read_data方法
        f = open(self.path, 'r', encoding="utf-8")
        record_list = []  # record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()  # 消除读取到的\n
            data_list = line.split(",")
            # print(line)
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        f.close()
        return record_list


class JsonFileRead(FileRead):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding="utf-8")
        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], data_dict["money"], data_dict["province"])
            record_list.append(record)
            f.close()
            return record_list


if __name__ == '__main__':  # 内部测试使用，外部调用需重新
    text_file_read = TextFileRead("D:/Study/2011年1月销售数据.txt")  # 实例化对象
    json_file_read = JsonFileRead("D:/Study/2011年2月销售数据JSON.txt")
    list_text = text_file_read.read_data()  # 使用该对象的方法
    list_json = json_file_read.read_data()

    for data in list_text:
        print(data)

    for data in list_json:
        print(data)

