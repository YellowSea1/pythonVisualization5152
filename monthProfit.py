from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.globals import ThemeType
from readCsv import readMonthProfitCsv


def monthProfit():
    res = readMonthProfitCsv()
    bar = (
        Bar(init_opts=opts.InitOpts(width="1300px", height="450px"), )
            .add_xaxis(res[0])
            .add_yaxis(
            "利润",
            res[3],
            yaxis_index=2,
            color="#f4cccc",
            label_opts=opts.LabelOpts(is_show=False),
        )

            .extend_axis(
            yaxis=opts.AxisOpts(
                name="订单量（笔）",
                type_="value",
                min_=0,
                max_=2000,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
            )
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="利润（元）",
                min_=0,
                max_=18000,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
            )
        )
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="销售量（笔）",
                min_=0,
                max_=2500,
                position="right",
                offset=65,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                # axislabel_opts=opts.LabelOpts(formatter="{value}笔"),
            ),
            datazoom_opts=opts.DataZoomOpts(is_show=True, ),

            title_opts=opts.TitleOpts(title="月销售利润统计", subtitle="按年月统计"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_left="center"),
        )
    )

    line = (
        Line(init_opts=opts.InitOpts(width="1000px", height="400px"), )
            .add_xaxis(res[0])
            .add_yaxis(
            "订单量",
            res[1],
            yaxis_index=1,
            z=2,
            is_smooth=True,
            # color="#0093f3",
        )
            .add_yaxis(
            "销售量",
            res[2],
            yaxis_index=0,
            z=2,
            is_smooth=True,
            color="#d14a61",
        )
    )
    overlap_1 = bar.overlap(line)
    return overlap_1
# # 1.条形图
# def bar_datazoom_slider():
#     res = readMonthProfitCsv()
#     c = (
#         Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width="700px", height='400px', ))
#             .add_xaxis(res[0])
#             .add_yaxis("利润", res[1])
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="月销售利润", subtitle="按年月统计"),
#             datazoom_opts=[opts.DataZoomOpts()],
#         )
#     )
#     # c.set_global_opts(
#     #     # 标题配置
#     #     title_opts=opts.TitleOpts(
#     #         title="主标题", subtitle='副标题',
#     #     )
#     # )
#     return c
