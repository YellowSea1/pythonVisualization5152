from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

from readCsv import readStateDistCsv


def stateDist():
    res = readStateDistCsv()
    state = res[0]
    order = res[1]
    sell = res[2]
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add("订单量", [list(z) for z in zip(state, order)], "美国")
            .add("销售量", [list(z) for z in zip(state, sell)], "美国")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(title_opts=opts.TitleOpts(title="州分布统计（订单量与销售量）"),
                             visualmap_opts=opts.VisualMapOpts(max_=10000),
                             )
    )
    return c
