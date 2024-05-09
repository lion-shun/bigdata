"""
销售数据分析，业务逻辑
1. 数据的封装 设计一个类，记录成员变量
2. 设计一个抽象类，重写子类，实现对不同的数据格式进行读取
3. 读取文件，生产数据对象
3. 按需求对数据进行计算
4. 用pyecharts绘图
"""
from pyecharts.globals import ThemeType
from pymysql import Connection
from file_def import FileRead, TextFileRead, JsonFileRead
from data_def import Record
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts, TitleOpts, InitOpts

text_file_read = TextFileRead("D:/Study/2011年1月销售数据.txt")  # 实例化对象
json_file_read = JsonFileRead("D:/Study/2011年2月销售数据JSON.txt")
data_1: list[Record] = text_file_read.read_data()  # 使用该对象的方法  类型说明
data_2: list[Record] = json_file_read.read_data()

# 图形化展示
# 合并2个月的数据
data_all: list[Record] = data_1 + data_2

"""
# 数据计算
# record = Record()
data_dict = {}
for record in data_all:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money  # 已有数据直接累加
    else:
        data_dict[record.date] = record.money   # 初始数据则赋值
# print(data_dict)
sale_bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
sale_bar.add_xaxis(list(data_dict.keys()))
sale_bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
sale_bar.set_global_opts(title_opts=TitleOpts(title="每日销售额"))
sale_bar.render("每日销售额.html")
"""
conn = Connection(
    host="39.107.78.20",
    port=3306,
    user="root",
    password="1234",
    database="test",
    autocommit=True
)
cur = conn.cursor()
conn.select_db("test")
for record in data_all:
    insert_sql = f"insert into orders " \
                  f"(order_date, order_id, money, province) " \
                  f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    # print(insert_sql)
    cur.execute(insert_sql)
print("数据写入完成")
conn.close()