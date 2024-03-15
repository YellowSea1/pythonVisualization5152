from pyecharts.globals import ThemeType

from pandasRead import readYearProductCategoryCsv

from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline


def yearProductCategory():
    res = readYearProductCategoryCsv()

    category_2018 = res[0]
    sell_2018 = res[1]
    avgProfit_2018 = res[2]

    category_2019 = res[3]
    sell_2019 = res[4]
    avgProfit_2019 = res[5]

    category_2020 = res[6]
    sell_2020 = res[7]
    avgProfit_2020 = res[8]

    category_2021 = res[9]
    sell_2021 = res[10]
    avgProfit_2021 = res[11]

    tl = Timeline(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))

    pie1 = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add(
            "销售量",
            [list(z) for z in zip(category_2018, sell_2018)],
            rosetype="radius",
            radius=["30%", "55%"],
            center=["27%", "48%"],
        )
            .add(
            "平均利润",
            [list(z) for z in zip(category_2018, avgProfit_2018)],
            rosetype="radius",
            radius=["30%", "55%"],
            center=["72%", "52%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("不同产品类别2018年销售量和平均利润"),
                             legend_opts=opts.LegendOpts(pos_left='right', ))
    )
    tl.add(pie1, "2018年")

    pie2 = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
            .add(
            "销售量",
            [list(z) for z in zip(category_2019, sell_2019)],
            rosetype="radius",
            radius=["30%", "55%"],
            center=["27%", "48%"],
        )
            .add(
            "平均利润",
            [list(z) for z in zip(category_2019, avgProfit_2019)],
            rosetype="radius",
            radius=["30%", "55%"],
            center=["72%", "52%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("不同产品类别2019年销售量和平均利润"),
                             legend_opts=opts.LegendOpts(pos_left='right', ))
    )
    tl.add(pie2, "2019年")

    pie3 = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add(
            "销售量",
            [list(z) for z in zip(category_2020, sell_2020)],
            rosetype="radius",
            radius=["30%", "55%"],
            center=["27%", "48%"],
        )
            .add(
            "平均利润",
            [list(z) for z in zip(category_2020, avgProfit_2020)],
            rosetype="radius",
            radius=["30%", "55%"],
            center=["72%", "52%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("不同产品类别2020年销售量和平均利润"),
                             legend_opts=opts.LegendOpts(pos_left='right', ))
    )
    tl.add(pie3, "2020年")

    pie4 = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add(
            "销售量",
            [list(z) for z in zip(category_2021, sell_2021)],
            rosetype="radius",
            radius=["30%", "55%"],
            center=["27%", "48%"],
        )
            .add(
            "平均利润",
            [list(z) for z in zip(category_2021, avgProfit_2021)],
            rosetype="radius",
            radius=["30%", "55%"],
            center=["72%", "52%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("不同产品类别2021年销售量和平均利润"),
                             legend_opts=opts.LegendOpts(pos_left='right', ))
    )
    tl.add(pie4, "2021年")

    return tl
# def yearProductCategory(opts=None):
#     res = readYearProductCategoryCsv()
#     c = (
#         Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width="700px", height='400px', ))
#             .add_xaxis(res[0])
#             .add_yaxis("利润", res[1])
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="月销售利润", subtitle="按年月统计"),
#             datazoom_opts=[opts.DataZoomOpts()],
#         )
#     )
# c.set_global_opts(
#     # 标题配置
#     title_opts=opts.TitleOpts(
#         title="主标题", subtitle='副标题',
#     )
# )
# return c
