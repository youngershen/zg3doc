# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/14 10:05
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
# -*- coding: utf-8 -*-

# Copyright (c) 2023. All rights reserved.

"""
@author: wenjie
@file: day8.py
@time: 2023/3/1 10:27
@desc:

Supported platforms:

 - Linux
 - Windows

Works with Python versions 3.X.
"""

import pandas as pd

from pyecharts.charts import Pie, Bar, WordCloud, Line

# 读取附件中douban.json文件，存储到df中
# 1．获取所有行的数据
# 2．对豆瓣top250进行分析
df = pd.read_json('./douban.json')
# 3．分析 评分在9分以上所有电影的评论人数的占比情况，使用合适的组件可视化展示
df3 = df[df['电影评分'] > 9][['电影名称', '电影评论人数']]
pie = Pie()
pie.add('', list(zip(df3['电影名称'].tolist(), df3['电影评论人数'].tolist())))
# pie.render('./3.html')
# 4．分析 每个国家所有电影的评论人数的总和，使用合适的组件可视化展示
print(df.columns)
df4 = df.groupby(by='上映国家')['电影评论人数'].sum()
bar = Bar()
bar.add_xaxis(df4.index.tolist())
bar.add_yaxis('', df4.values.tolist())
# bar.render('./4.html')
# 5．分析 中国大陆上映的电影的每部电影的评论人数与评分的关系，使用合适的组件可视化展示
df5 = df[df['上映国家'].str.contains('中国大陆')][['电影名称', '电影评论人数', '电影评分']]
bar5 = Bar()
bar5.add_xaxis(df5['电影名称'].tolist())
bar5.add_yaxis('电影评论人数', df5['电影评论人数'].tolist())
bar5.add_yaxis('电影评分', df5['电影评分'].tolist())
# bar5.render('./5.html')
# 6．获取所有导演的资料，使用合适的组件可视化展示
df6 = df.groupby(by='电影导演')['电影名称'].count()
word = WordCloud()
word.add('', list(zip(df6.index.tolist(), df6.values.tolist())))
word.render('6.html')
# 7．分析 1994年以后上映的电影排名与评分的关系，使用合适的组件可视化展示
df7 = df[df['上映时间'] > 1994][['排名', '电影评分']]
line = Line()
line.add_xaxis(df7['排名'].tolist())
line.add_yaxis('', df7['电影评分'].tolist())
line.render('./7.html')
# 8．分析 每个导演导演电影的次数之间的关系，使用合适的组件可视化展示
pie1 = Pie()
pie1.add('', list(zip(df6.index.tolist(), df6.values.tolist())))
pie1.render('./8.html')
