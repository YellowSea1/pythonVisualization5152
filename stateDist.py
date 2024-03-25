from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

from readCsv import readStateDistCsv
from readCsv import readStateDistCsvUS


def stateDistStart():
    res = readStateDistCsv()
    state = res[0]
    order = res[1]
    sell = res[2]
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add("start", [list(z) for z in zip(state, order)])
            # .add("末尾", [list(z) for z in zip(state, sell)])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(title_opts=opts.TitleOpts(title="Province distribution statistics"),
                             visualmap_opts=opts.VisualMapOpts(max_=10000),
            )
    )
    return c


def stateEnd():
    res = readStateDistCsv()
    state = res[0]
    sell = res[2]
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add("end", [list(z) for z in zip(state, sell)])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(title_opts=opts.TitleOpts(title="Province distribution statistics"),
                             visualmap_opts=opts.VisualMapOpts(max_=10000),
                             )
    )
    return c

def stateDistStartUS():
    res = readStateDistCsvUS()
    state = res[0]
    start = res[1]
    end = res[2]
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add("start", [list(z) for z in zip(state, start)], "美国")
        # .add("末尾", [list(z) for z in zip(state, end)], "美国")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(title_opts=opts.TitleOpts(title="State distribution statistics"),
                         visualmap_opts=opts.VisualMapOpts(max_=10000),
                         )
    )
    return c

def stateDistEndUS():
    res = readStateDistCsvUS()
    state = res[0]
    start = res[1]
    end = res[2]
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add("end", [list(z) for z in zip(state, end)], "美国")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(title_opts=opts.TitleOpts(title="State distribution statistics"),
                         visualmap_opts=opts.VisualMapOpts(max_=10000),
                         )
    )
    return c

