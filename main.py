# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 导入要使用的模块
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.components import Table
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

from cusPurchase import cusPurchase
from totalArea import totalArea
from totalMktS import totalMktS
from totalProductCategory import totalProductCategory
from totalTransport import totalTransport
from monthProfit import monthProfit
from yearMktS import yearMktS
from yearArea import yearArea
from yearProductCategory import yearProductCategory
from yearTransport import yearTransport
from stateDist import stateDist
from stateDist import stateEnd
from US import US
from CH import CH


# 将每个图 封装到 函数



# # 表格
# def table_base() -> Table:
#     table = Table()
#
#     headers = ["City name", "Area", "Population", "Annual Rainfall"]
#     rows = [
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
#     table.add(headers, rows).set_global_opts(
#         title_opts=opts.ComponentTitleOpts(title="用户")
#     )
#     return table


def page_simple_layout():
    #    page = Page()   默认布局
    page = Page(layout=Page.SimplePageLayout)  # 简单布局
    page.page_title = "销售数据分析可视化结果"
    # 将上面定义好的图添加到 page
    page.add(
        # bar_datazoom_slider(),
        # line_markpoint(),
        # table_base(),
        # overlap_1,
        US(),
        CH(),
        monthProfit(),
        totalProductCategory(),
        totalTransport(),
        yearProductCategory(),
        yearTransport(),
        stateDist(),
        stateEnd(),
        yearMktS(),
        yearArea(),
        totalArea(),
        totalMktS(),
        cusPurchase(),
    )
    page.render("visualization.html")


if __name__ == "__main__":
    page_simple_layout()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


