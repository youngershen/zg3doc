# Project: ZG3Doc
# File : test3.py
# Date : 2023/4/14 10:06
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com


import pandas as pd
from pyecharts.charts import Bar, Line, Pie, WordCloud
# 读取附件中job.csv文件，存储到df中
# 1．获取所有行的数据
# 2．对python相关的岗位情况进行分析
df = pd.read_csv('./job.csv')
def func(x):
    x_list = x['薪资范围'].replace('k', '').split('-')
    return (int(x_list[0]) + int(x_list[1])) / 2
df['平均薪资'] = df.apply(func, axis=1)
# 3．分析 各个学历与薪资的关系，使用合适的组件可视化展示
df3 = df.groupby(by=['学历要求'])['平均薪资'].mean()
bar = Bar()
bar.add_xaxis(df3.index.tolist())
bar.add_yaxis('', [round(i, 2) for i in df3.values.tolist()])
# bar.render('./3.html')
# 4．分析 各种阶段的经验与薪资的关系，使用合适的组件可视化展示
df4 = df.groupby(by='经验范围')['平均薪资'].mean()
line = Line()
line.add_xaxis(df4.index.tolist())
line.add_yaxis('', [round(i, 2) for i in df4.values.tolist()])
# line.render('./4.html')
# 5．分析 各个城市中薪资的平均值如何分布，使用合适的组件可视化展示
df5 = df.groupby(by='城市名称')['平均薪资'].mean()
line1 = Line()
line1.add_xaxis(df5.index.tolist())
line1.add_yaxis('', [round(i, 2) for i in df5.values.tolist()])
# line1.render('./5.html')
# 6．分析 北京市相同经验下本科学历与大专学历的薪资的占比情况，使用合适的组件可视化展示
df6 = df[(df['城市名称'] == '北京') & (df['学历要求'].isin(['本科', '大专']))]
df66 = df6.groupby(by='经验范围')['平均薪资'].mean()
pie = Pie()
pie.add('', list(zip(df66.index.tolist(), df66.values.tolist())))
# pie.render('./6.html')
# 7．分析 每个城市的薪资的最大值与最小值的趋势变化，使用合适的组件可视化展示
df7 = df.groupby(by='城市名称').agg({'平均薪资': ['max', 'min']})
line2 = Line()
line2.add_xaxis(df7.index.tolist())
line2.add_yaxis('max', df7['平均薪资']['max'].tolist())
line2.add_yaxis('min', df7['平均薪资']['min'].tolist())
# line2.render('./7.html')
# 8．获取北京市所有公司的全称，使用合适的组件可视化展示
df8 = df[df['城市名称'] == '北京'].groupby(by='公司名称')['发布时间'].count()
word = WordCloud()
word.add('', list(zip(df8.index.tolist(), df8.values.tolist())))
word.render('./8.html')
