from pyecharts.globals import ThemeType

from pandasRead import readYearTransportCsv

from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline


def yearTransport():
    res = readYearTransportCsv()

    mode_2018 = res[0]
    order_2018 = res[1]
    avgProfit_2018 = res[2]

    mode_2019 = res[3]
    order_2019 = res[4]
    avgProfit_2019 = res[5]

    mode_2020 = res[6]
    order_2020 = res[7]
    avgProfit_2020 = res[8]

    mode_2021 = res[9]
    order_2021 = res[10]
    avgProfit_2021 = res[11]

    tl = Timeline(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))

    pie1 = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add(
            "销售量",
            [list(z) for z in zip(mode_2018, order_2018)],
            rosetype="radius",
            radius=["30%", "50%"],
            center=["27%", "50%"],
        )
            .add(
            "平均利润",
            [list(z) for z in zip(mode_2018, avgProfit_2018)],
            rosetype="radius",
            radius=["30%", "50%"],
            center=["72%", "50%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("不同运输方式2018年销售量和平均利润"),
                             legend_opts=opts.LegendOpts(pos_left='right', ))
    )
    tl.add(pie1, "2018年")

    pie2 = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
            .add(
            "销售量",
            [list(z) for z in zip(mode_2019, order_2019)],
            rosetype="radius",
            radius=["30%", "50%"],
            center=["27%", "50%"],
        )
            .add(
            "平均利润",
            [list(z) for z in zip(mode_2019, avgProfit_2019)],
            rosetype="radius",
            radius=["30%", "50%"],
            center=["72%", "50%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("不同运输方式2018年销售量和平均利润"),
                             legend_opts=opts.LegendOpts(pos_left='right', ))
    )
    tl.add(pie2, "2019年")

    pie3 = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add(
            "销售量",
            [list(z) for z in zip(mode_2020, order_2020)],
            rosetype="radius",
            radius=["30%", "50%"],
            center=["27%", "50%"],
        )
            .add(
            "平均利润",
            [list(z) for z in zip(mode_2020, avgProfit_2020)],
            rosetype="radius",
            radius=["30%", "50%"],
            center=["72%", "50%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("不同运输方式2018年销售量和平均利润"),
                             legend_opts=opts.LegendOpts(pos_left='right', ))
    )
    tl.add(pie3, "2020年")

    pie4 = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add(
            "销售量",
            [list(z) for z in zip(mode_2021, order_2021)],
            rosetype="radius",
            radius=["30%", "50%"],
            center=["27%", "50%"],
        )
            .add(
            "平均利润",
            [list(z) for z in zip(mode_2021, avgProfit_2021)],
            rosetype="radius",
            radius=["30%", "50%"],
            center=["72%", "50%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("不同运输方式2018年销售量和平均利润"),
                             legend_opts=opts.LegendOpts(pos_left='right', ))
    )
    tl.add(pie4, "2021年")

    return tl
