# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:06
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com


import pandas as pd
from pyecharts.charts import Bar, Line, Pie, WordCloud
# 读取附件中stock.json文件，存储到df中
# 1．获取所有行的数据
# 2．对上市公司的数据进行分析
df = pd.read_json('./stock.json')
print(df.columns)
# 3．分析 上海市所有公司员工人数的情况，使用合适的组件可视化展示
df3 = df[df['市'] == '上海市'].groupby('公司全称')['员工人数'].sum()
bar = Bar()
bar.add_xaxis(df3.index.tolist())
bar.add_yaxis('', df3.values.tolist())
# bar.render('./3.html')
# 4．分析 每个省的注册资金最多的公司详情，使用合适的组件可视化展示
df['注册资金(万元)'] = df.apply(lambda x: float(x['注册资金(万元)'].replace(',', '')),
                          axis=1)
df4 = df.groupby(by=['省', '公司全称'])['注册资金(万元)'].max()
bar4 = Bar()
bar4.add_xaxis(df4.index.tolist())
bar4.add_yaxis('', df4.values.tolist())
# bar4.render('./4.html')
# 5．分析 随着上市日期的递进，注册资金与之的关系，使用合适的组件可视化展示
df5 = df.sort_values(by='上市日期')
bar5 = Bar()
bar5.add_xaxis(df5['上市日期'].tolist())
bar5.add_yaxis('', df5['注册资金(万元)'].tolist())
# bar5.render('./5.html')
# 6．分析 各个省份以及各个市级，注册资金与员工人数的关系，使用合适的组件可视化展示
df['员工人数'] = df['员工人数'].astype('int64')
df6 = df.groupby(by=['省', '市']).agg({'注册资金(万元)': 'max', '员工人数': 'sum'})
bar6 = Bar()
bar6.add_xaxis(df6.index.tolist())
bar6.add_yaxis('注册资金(万元)最大值', df6['注册资金(万元)'].tolist())
bar6.add_yaxis('员工人数总和', df6['员工人数'].tolist())
# bar6.render('./6.html')
# 7．分析 北京市，上海市，深圳市的上市公司的注册资金的占比情况，使用合适的组件可视化展示
df7 = df[df['市'].isin(['北京市', '上海市', '深圳市'])].\
    groupby(by='市')['注册资金(万元)'].sum()
bar7 = Bar()
bar7.add_xaxis(df7.index.tolist())
bar7.add_yaxis('', df7.values.tolist())
# bar7.render('./7.html')
# 8．分析 随着成立日期的递进，员工人数与之的关系，使用合适的组件可视化展示
df8 = df.sort_values(by='成立日期')[['员工人数', '成立日期']]
line = Line()
line.add_xaxis(df8['成立日期'].tolist())
line.add_yaxis('', df8['员工人数'].tolist())
line.render('./8.html')
