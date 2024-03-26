from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

from readCsv import readStateDistCsv

list_name = ['anhui2', 'anhui', 'Macao', 'beijing', 'fujian', 'gansu', 'guangdong', 'guangxi', 'guizhou', 'hainan',
             'hebei', 'henan', 'heilongjiang', 'hubei', 'hunan', 'jilin', 'jiangsu', 'jiangxi', 'liaoning', 'neimenggu',
             'ningxia', 'qinghai', 'shandong', 'shanxi', 'shanxi', 'shanghai', 'sichuan', 'Taiwan', 'tianjin', 'xizang',
             'Hong Kong', 'xinjiang', 'yunnan', 'zhejiang', 'chongqing', 'nanhai', 'bb']



def stateDist():
    res = readStateDistCsv()
    state = res[0]
    order = res[1]
    sell = res[2]

    ###将原省份名称与新名字打包成字典
    name_translate = dict(zip(state, list_name))

    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add("start", [list(z) for z in zip(list_name, order)],"china",name_map=name_translate )
            # .add("末尾", [list(z) for z in zip(state, sell)])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(title_opts=opts.TitleOpts(title="each province confirmed count"),
                             visualmap_opts=opts.VisualMapOpts(max_=10000),
                             )
    )
    return c

def stateEnd():
    res = readStateDistCsv()
    state = res[0]
    sell = res[2]

    ###将原省份名称与新名字打包成字典
    name_translate = dict(zip(state, list_name))

    ###将原省份名称与新名字打包成字典
    name_translate = dict(zip(state, list_name))

    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
            .add("end", [list(z) for z in zip(list_name, sell)],"china",name_map=name_translate )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(title_opts=opts.TitleOpts(title="each province confirmed count"),
                             visualmap_opts=opts.VisualMapOpts(max_=10000),
                             )
    )
    return c