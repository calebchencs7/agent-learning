from file_reader import FileReader
from data_class import DataClass
from pyecharts import options as opts
from pyecharts.charts import Bar


def read_all_data(csv_path: str, json_path: str) -> list[DataClass]:
    fr_csv = FileReader(csv_path)
    fr_json = FileReader(json_path)

    lst1 = fr_csv.read_csv()
    lst2 = fr_json.read_json()

    return lst1 + lst2


# 得到每日的销售额
# list1: [2026-04-01, 2026-04-02, ...]
# list2: [1111, 2233, ...]
def data_process(data: list[DataClass]):
    data_dict = {}
    for dc in data:
        if dc.date in data_dict:
            # 日期在字典内，已经记录过值了，取出来+新值，放回去
            # old_value = data_dict[dc.date]
            # data_dict[dc.date] = old_value + dc.sale_amount
            data_dict[dc.date] += dc.sale_amount
        else:
            # 日期不在字典内
            data_dict[dc.date] = dc.sale_amount

    # 数据抽取工作
    # data_dict 字典转列表
    data = [(k, v) for k, v in data_dict.items()]
    # 方便排序，list内是元组，默认按元组第一个元素作为排序依据
    data.sort()
    # 提取日期列表
    date_list = [t[0] for t in data]
    # 提取销售额列表
    amount_list = [t[1] for t in data]

    return date_list, amount_list


def create_sales_bar_chart(date_list, amount_list):
    """
    生成销售额柱状图（优化数值显示，不拥挤重叠）
    :param date_list: 日期列表，格式如 ["2026-04-01", ...]
    :param amount_list: 销售额列表，格式如 [1234.56, ...]
    :return: Bar 图表对象
    """
    bar = (
        Bar(
            # 扩大图表宽度，从根源避免拥挤（核心优化）
            init_opts=opts.InitOpts(width="1300px", height="600px")
        )
        .add_xaxis(date_list)
        .add_yaxis(
            series_name="销售额",
            y_axis=amount_list,
            itemstyle_opts=opts.ItemStyleOpts(color="blue"),
            # 核心优化：显示数值标签 + 不重叠配置
            label_opts=opts.LabelOpts(
                is_show=True,  # 显示数值
                position="top",  # 放在柱子顶部
                font_size=11,  # 字体大小适中
                rotate=0,  # 文字不旋转
                formatter="{c}",  # 只显示纯数值
                distance=3,  # 距离柱子距离
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="黑马程序员数据分析案例",
                title_textstyle_opts=opts.TextStyleOpts(font_size=18),
            ),
            # X轴日期倾斜 防止重叠
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(rotate=-30, font_size=10)
            ),
            # Y轴优化
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=10)),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            # 数据缩放滑块（数据很多时也能看清）
            datazoom_opts=[
                opts.DataZoomOpts(type_="inside"),  # 鼠标滚轮缩放
                opts.DataZoomOpts(type_="slider"),  # 底部滑动条
            ],
        )
    )

    # 生成图表文件
    bar.render("销售额柱状图.html")
    return bar


lst = read_all_data("2026年4月销售数据.csv", "2026年5月销售数据.txt")
date_list, amount_list = data_process(lst)
print(date_list, end="\n")
print(amount_list)

create_sales_bar_chart(date_list, amount_list)
