from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.globals import ThemeType
from readCsv import readMonthProfitCsv


def yearMktS():
    # res = readMonthProfitCsv()
    bar = (
        Bar(init_opts=opts.InitOpts(width="1300px", height="450px", theme=ThemeType.MACARONS), )
            .add_xaxis(['2018', '2019', '2020', '2021'])
            .add_yaxis(
            "Consumer销售量",
            [4006, 4244, 4855, 6121],
            yaxis_index=2,
            # color="#f4cccc",
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            "Home Office销售量",
            [1173, 1280, 1806, 2408],
            yaxis_index=2,
            # color="#e07070",
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            "Corporate销售量",
            [2312, 2396, 3064, 3708],
            yaxis_index=2,
            # color="#ea9e9e",
            label_opts=opts.LabelOpts(is_show=False),
        )

            .extend_axis(
            yaxis=opts.AxisOpts(
                is_show=False,
                name="销售量111（笔）",
                type_="value",
                min_=0,
                max_=7000,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
            )
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="销售量（笔）",
                min_=0,
                max_=10000,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    # linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
            )
        )
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="平均利润（元）",
                min_=0,
                max_=11,
                position="right",
                # offset=65,
                axisline_opts=opts.AxisLineOpts(
                    # linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                # axislabel_opts=opts.LabelOpts(formatter="{value}笔"),
            ),
            # datazoom_opts=opts.DataZoomOpts(is_show=True, ),
            title_opts=opts.TitleOpts(title="年细分市场统计", subtitle="统计不同类别"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_left="right"),
        )
    )

    line = (
        Line(init_opts=opts.InitOpts(width="1000px", height="400px", theme=ThemeType.MACARONS), )
            .add_xaxis(['2018', '2019', '2020', '2021'])
            .add_yaxis(
            "Consumer平均利润",
            [7.91, 7.57, 7.36, 7.35],
            yaxis_index=0,
            z=2,
            is_smooth=True,
            # color="#0093f3",
        )
            .add_yaxis(
            "Corporate平均利润",
            [5.84, 8.63, 10.1, 7.12],
            yaxis_index=0,
            z=2,
            is_smooth=True,
            # color="#d14a61",
        )
            .add_yaxis(
            "Home Office平均利润",
            [9.98, 10.22, 8.32, 8.73],
            yaxis_index=0,
            z=2,
            is_smooth=True,
            # color="#d55a61",
        )
    )
    overlap_1 = bar.overlap(line)
    return overlap_1
