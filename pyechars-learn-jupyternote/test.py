from pyecharts.charts import Bar
from pyecharts import options as opts


firm_names = []
firm_value_part = []
firm_num_data = (
    Bar()
        .add_xaxis(firm_names)
        .add_yaxis('', [firm[1] for firm in firm_value_part])  # 事务所出具审计报告数量
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(
        title_opts=opts.TitleOpts(title="事务所出具审计报告数量"),
        yaxis_opts=opts.AxisOpts(name="事务所名称", is_inverse=True),
        xaxis_opts=opts.AxisOpts(name="出具报告数量"),
        sigle_opts=opts.SingleAxisOpts(pos_left='left'),
    )
)