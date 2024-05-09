"""
数据定义
"""


class Record:  # 记录数据的类

    def __init__(self, date, order_id, money, province):  # 构造方法来声明成员变量
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):  # 魔术方法 把返回的地址转变为字符串
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"
