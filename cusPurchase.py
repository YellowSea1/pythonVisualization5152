from pyecharts import options as opts
from pyecharts.components import Table


# 表格
def cusPurchase() -> Table:
    table = Table()

    headers = ["客户名称", "订单量", "销售量", "累计总利润", "排名"]
    rows = [
        ["Tamara Chand", 12, 42, 8981.32, 1],
        ["Raymond Buch", 18, 71, 6976.1, 2],
        ["Sanjit Chand", 22, 87, 5757.41, 3],
        ["Hunter Lopez", 11, 50, 5622.43, 4],
        ["Adrian Barton", 20, 73, 5444.81, 5],
        ["Tom Ashbrook", 10, 36, 4703.79, 6],
        ["Christopher Martinez", 10, 34, 3899.89, 7],
        ["Luke Foster", 16, 69, 3819.81, 8],
        ["Joseph Holt", 14, 64, 3079.93, 9],
        ["Keith Dawkins", 28, 84, 3038.63, 10],
    ]
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="客户购买力统计")
    )
    return table
