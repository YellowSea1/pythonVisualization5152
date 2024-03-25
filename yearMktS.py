import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.globals import ThemeType
from readCsv import readCompareCountNumber


def yearMktS():
    res = readCompareCountNumber()
    custom_interval=[0, 100, 500, 1000000, 3000000, 20000000, 50000000, 99900000]
    date=res[0]
    china=np.log(res[1]).tolist()
    us=np.log(res[2]).tolist()
    chinaGrow=np.log(res[3]).tolist()
    usGrow=np.log(res[4]).tolist()
    print("aaa")
    print(res[1])
    print("bbb")
    print(np.log(res[1]))


    bar = (
        Bar(init_opts=opts.InitOpts(width="1300px", height="450px", theme=ThemeType.MACARONS), )
            .add_xaxis(date)
            .add_yaxis(
            "China确诊人数e^y",
            china,
            yaxis_index=2,
            color="#424769",
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add_yaxis(
            "US确诊人数e^y",
            us,
            yaxis_index=2,
            color="#424769",
            label_opts=opts.LabelOpts(is_show=False),
        )

            .extend_axis(
            yaxis=opts.AxisOpts(
                is_show=False,
                name="销售量111（笔）",
                type_="value",
                # min_=0,
                # max_=7000,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#F6B17A")
                ),
            )
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="确诊人数",
                #min_=0,
                # max_=99999999,
                position="left",
                #interval=custom_interval,
                axisline_opts=opts.AxisLineOpts(
                    # linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
            )
        )
            .set_global_opts(
            # yaxis_opts=opts.AxisOpts(
            #     name="平均利润（元）",
            #min_=0,
            #     max_=11,
            #     position="right",
            #     # offset=65,
            #     axisline_opts=opts.AxisLineOpts(
            #         # linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            #     ),
            #     # axislabel_opts=opts.LabelOpts(formatter="{value}笔"),
            # ),
            # datazoom_opts=opts.DataZoomOpts(is_show=True, ),

            title_opts=opts.TitleOpts(title="中美疫情对比", subtitle="统计两国确诊增长情况"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_left="right"),
        )
    )

    line = (
        Line(init_opts=opts.InitOpts(width="1000px", height="400px", theme=ThemeType.MACARONS), )
            .add_xaxis(date)
            .add_yaxis(
            "China确诊增长率",
            chinaGrow,
            #[3,4,5,7.91, 7.57, 7.36, 7.35],
            yaxis_index=1,
            z=2,
            is_smooth=True,
            color="#0093f3",
        )
            .add_yaxis(
            "America确诊增长率",
            usGrow,
            yaxis_index=1,
            z=2,
            is_smooth=True,
            color="#d14a61",
        )

    )
    overlap_1 = bar.overlap(line)
    return overlap_1
