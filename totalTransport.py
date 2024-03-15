from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Pie
from readCsv import readTotalTransportCsv


def totalTransport():
    res = readTotalTransportCsv()
    mode = res[0]
    order = res[1]
    avgProfit = res[2]

    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width="1200px", height="400px", ))
            .add(
            "", [list(z) for z in zip(mode, order)],
            radius=["30%", "60%"],  # 内圈和外圈的比例
            center=["27%", "50%"],  # 饼图的位置：左边距和上边距
            rosetype="radius",  # 扇区圆心角展现数据的百分比，半径展现数据的大小
        )
            .add(
            "", [list(z) for z in zip(mode, avgProfit)],
            radius=["30%", "60%"],
            center=["72%", "50%"],
            rosetype="radius",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="总运输方式统计（订单量与平均利润）", subtitle="扇区圆心角展现数据百分比，半径展现数据大小"),
                             legend_opts=opts.LegendOpts(pos_left='right', ))
    )
    return c