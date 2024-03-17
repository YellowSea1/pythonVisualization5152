from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.globals import ThemeType
from readCsv import readMonthProfitCsv


def yearArea():
    # res = readMonthProfitCsv()
    bar = (
        Bar(init_opts=opts.InitOpts(width="1300px", height="450px", theme=ThemeType.MACARONS), )
            .add_xaxis(['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.'])
            .add_yaxis(
            "美国各月份感染人数",
            [0.845, 1.380, 4.643, 4.643,6.255,6.421,6.632 ],
            yaxis_index=2,
            # color="#f4cccc",
            label_opts=opts.LabelOpts(is_show=False),
        )
        #     .add_yaxis(
        #     "East销售量",
        #     [1976, 2344, 2782, 3359],
        #     yaxis_index=2,
        #     # color="#e07070",
        #     label_opts=opts.LabelOpts(is_show=False),
        # )
        #     .add_yaxis(
        #     "South销售量",
        #     [1302, 1338, 1607, 1879],
        #     yaxis_index=2,
        #     # color="#ea9e9e",
        #     label_opts=opts.LabelOpts(is_show=False),
        # )
        #
        #     .add_yaxis(
        #     "West销售量",
        #     [2517, 2425, 3004, 4186],
        #     yaxis_index=2,
        #     # color="#ea9e9e",
        #     label_opts=opts.LabelOpts(is_show=False),
        # )

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
                max_=7,
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
            title_opts=opts.TitleOpts(title="年地区统计", subtitle="按年份统计"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_left="right"),
        )
    )

    line = (
        Line(init_opts=opts.InitOpts(width="1000px", height="400px", theme=ThemeType.MACARONS), )
            .add_xaxis(['2018', '2019', '2020', '2021'])
            .add_yaxis(
            "Central平均利润",
            [4.67, 6.8, 8.53, 2.66],
            yaxis_index=0,
            z=2,
            is_smooth=True,
            # color="#0093f3",
        )
            .add_yaxis(
            "East平均利润",
            [8.63, 8.98, 7.21, 9.86],
            yaxis_index=0,
            z=2,
            is_smooth=True,
            # color="#d14a61",
        )
            .add_yaxis(
            "South平均利润",
            [9.12, 9, 11.02, 4.44],
            yaxis_index=0,
            z=2,
            is_smooth=True,
            # color="#d55a61",
        )

            .add_yaxis(
            "West平均利润",
            [7.97, 8.45, 8, 10.38],
            yaxis_index=0,
            z=2,
            is_smooth=True,
            # color="#d55a61",
        )
    )
    overlap_1 = bar.overlap(line)
    return overlap_1
