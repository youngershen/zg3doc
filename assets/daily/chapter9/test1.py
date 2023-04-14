# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/14 10:07
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

# -*- coding: utf-8 -*-

# Copyright (c) 2023. All rights reserved.

"""
@author: wenjie
@file: day9.py
@time: 2023/3/2 10:25
@desc:

Supported platforms:

 - Linux
 - Windows

Works with Python versions 3.X.
"""
import pandas as pd
from pyecharts.charts import Bar, Line, Pie, WordCloud

# 1．读取附件，train.csv文件，pd查看数据集情况
# 2．pd查看数据值的分布
df = pd.read_csv('./train.csv')
# 3．根据Ticket列进行分组，获取年龄的平均数
print(df.columns)
df3 = df.groupby(by='Ticket')['Age'].mean()
# 4．根据Embarked列进行分组，获取SibSp列的总数
df4 = df.groupby(by='Embarked')['SibSp'].sum()
# 5．对数据中的Ticket列数据使用pyecharts生成词云图
word = WordCloud()
word.add('', [(i, 1) for i in df['Ticket'].tolist()])
# word.render('./5.html')
# 6．根据Embarked列进行分组，获取性别的占比，可视化生成饼图
df6 = df.groupby(by='Embarked')['Sex'].count()
pie = Pie()
pie.add('', list(zip(df6.index.tolist(), df6.values.tolist())))
# pie.render('./6.html')
# 7．统计性别列，可视化生成柱状图
df7 = df.groupby(by='Sex')['PassengerId'].count()
bar = Bar()
bar.add_xaxis(df7.index.tolist())
bar.add_yaxis('', df7.values.tolist())
# bar.render('./7.html')
# 8．根据Ticket列进行分组，获取该数据中年龄的最大值，可视化生成折线图
df8 = df.groupby(by='Ticket')['Age'].max()
line = Line()
line.add_xaxis(df8.index.tolist())
line.add_yaxis('', df8.values.tolist())
# line.render('./8.html')
# 9．根据SibSp以及Parch，可视化生成多柱状图
df9 = df[['SibSp', 'Parch']]
bar9 = Bar()
bar9.add_xaxis(df9.index.tolist())
bar9.add_yaxis('', df9['SibSp'].tolist())
bar9.add_yaxis('', df9['Parch'].tolist())
# bar9.render('./9.html')
# 10．根据Fare，SibSp，可视化生成多条折线图
df10 = df[['Fare', 'SibSp']]
line10 = Line()
line10.add_xaxis(df10.index.tolist())
line10.add_yaxis('', df10['Fare'].tolist())
line10.add_yaxis('', df10['SibSp'].tolist())
# line10.render('./10.html')

# [1, 2, 3, ...., 100000000] -> [2, 4, 6, 8]


