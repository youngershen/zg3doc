# Project: ZG3Doc
# File : test5.py
# Date : 2023/4/14 11:38
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
09-18-3-00005

1.   读取数据文件sample.csv，形成数据集，对日期相关字段不同格式进行统一处理为类似“2020-01-31”形式
2.   对数据集进行空值处理、异常值处理、去除重复数据
3.   总体业绩概况，计算每年度1-12个月每月总的销售收入
4.   业绩发展趋势1，计算年度销售额以及增长率，使用折线图和柱状图进行可视化。对数据进行适当的评述
5.   业绩发展趋势2，计算年度利润额以及增长率，使用折线图和柱状图进行可视化。对数据进行适当的评述
6.   市场分析，计算利润贡献前10的国家，并以饼图进行可视化
7.   分别计算每年的商品促销活动的销售额、利润额和非促销活动销售额、利润额，基于促销对公司的销售额以及利润额影响进行评述，其中促销活动订单是指价格折扣大于0的订单。
8.   使用RFM模型对用户价值进行分类，以所有订单的最新的日期为基准，计算R、F、M的均值，根据R、F、M实际值与均值大小比较定义客户类型，统计不同客户类型的数量，并进行分析
9.   计算月复购率， 即用户当月内购买超过1次，认为该用户进行了复购活动；计算回购率，用户在当月有购买活动，下个月也有购买活动，认为该用户进行了回购活动。
10.  以月为单位，计算每月新用户、活跃用户、不活跃用户和回归用户数量，对结果进行可视化
"""

# -*- coding: utf-8 -*-

# Copyright (c) 2023. All rights reserved.

"""
@author: wenjie
@file: m5.py
@time: 2023/4/7 10:28
@desc:

Supported platforms:

 - Linux
 - Windows

Works with Python versions 3.X.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pyecharts.charts import Bar, Line, Pie

# 1.   读取数据文件sample.csv，形成数据集，对日期相关字段不同格式进行统一处理为类似“2020-01-31”形式
df = pd.read_csv('sample.csv')
df['订单日期'] = pd.to_datetime(df['订单日期'])
df['配送日期'] = pd.to_datetime(df['配送日期'])
# 2.   对数据集进行空值处理、异常值处理、去除重复数据
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
# 3.   总体业绩概况，计算每年度1-12个月每月总的销售收入
df['月'] = df['订单日期'].dt.month
print(df.columns)
df3 = df.groupby('月').agg({'销售额': 'sum'})
# 4.   业绩发展趋势1，计算年度销售额以及增长率，使用折线图和柱状图进行可视化。对数据进行适当的评述
df['年'] = df['订单日期'].dt.year
df4 = df.groupby('年').agg({'销售额': 'sum'})
sale_dic = df4.to_dict()['销售额']
add_lv = dict()
sale_list = list(sale_dic.values())
year_list = list(sale_dic.keys())
for i in range(len(sale_dic)):
    if i < len(sale_dic) - 1:
        add_lv[year_list[0]] = 0
        add_lv[year_list[i + 1]] = (sale_list[i + 1] - sale_list[i]) / \
                                   sale_list[i]
bar = Bar()
bar.add_xaxis(df4.index.tolist())
bar.add_yaxis('', df4.values.tolist())
bar.render('./销售额.html')
line = Line()
line.add_xaxis([str(i) for i in add_lv.keys()])
line.add_yaxis('', list(add_lv.values()))
line.render('./增长率1.html')
# 5.   业绩发展趋势2，计算年度利润额以及增长率，使用折线图和柱状图进行可视化。对数据进行适当的评述
df5 = df.groupby('年').agg({'利润': 'sum'})
sale_dic = df5.to_dict()['利润']
add_lv = dict()
sale_list = list(sale_dic.values())
year_list = list(sale_dic.keys())
for i in range(len(sale_dic)):
    if i < len(sale_dic) - 1:
        add_lv[year_list[0]] = 0
        add_lv[year_list[i + 1]] = (sale_list[i + 1] - sale_list[i]) / \
                                   sale_list[i]
bar = Bar()
bar.add_xaxis(df5.index.tolist())
bar.add_yaxis('', df5.values.tolist())
bar.render('./利润.html')
line = Line()
line.add_xaxis(list(add_lv.keys()))
line.add_yaxis('', list(add_lv.values()))
line.render('./增长率2.html')
# 6.   市场分析，计算利润贡献前10的国家，并以饼图进行可视化
df6 = df.groupby('国家').agg({'利润': 'sum'}).sort_values(by='利润', ascending=False)
pie = Pie()
pie.add('', list(zip(df6.index.tolist(), df6.values.tolist())))
pie.render('./6.html')
# 7.   分别计算每年的商品促销活动的销售额、利润额和非促销活动销售额、利润额，
# 基于促销对公司的销售额以及利润额影响进行评述，其中促销活动订单是指价格折扣大于0的订单。
sales_df = df[df['折扣'] > 0]
no_sales_df = df[df['折扣'] <= 0]
sales_df = sales_df.groupby('年').agg({'利润': 'sum', '销售额': 'sum'})
no_sales_df = no_sales_df.groupby('年').agg({'利润': 'sum', '销售额': 'sum'})
# 8.   使用RFM模型对用户价值进行分类，以所有订单的最新的日期为基准，计算R、F、M的均值，
# 根据R、F、M实际值与均值大小比较定义客户类型，统计不同客户类型的数量，并进行分析
R = df.groupby(by='客户ID').agg({'产品ID': 'count'}).reset_index()
f = df.groupby(by='客户ID').agg({'订单日期': 'max'}).reset_index()
M = df.groupby(by='客户ID').agg({'销售额': 'count'}).reset_index()
f['F'] = (pd.to_datetime(datetime.now()) - f['订单日期']).dt.days
F = f[['客户ID', 'F']]
RF = pd.merge(R, F, left_on='客户ID', right_on='客户ID', how='inner')
RFM = pd.merge(RF, M, left_on='客户ID', right_on='客户ID', how='inner')
RFM['mean_r'], RFM['mean_f'], RFM['mean_m'] = RFM['产品ID'].mean(), RFM[
    'F'].mean(), RFM['销售额'].mean()
# 9.   计算月复购率， 即用户当月内购买超过1次，认为该用户进行了复购活动；
# 计算回购率，用户在当月有购买活动，下个月也有购买活动，认为该用户进行了回购活动。
df9 = df[df['年'] == 2014]
df99 = df9.groupby(by=['月', '客户ID'])['订单ID'].count().reset_index()
for i in range(1, 13):
    v = len(df99[(df99['月'] == i) & (df99['订单ID'] > 1)]) / len(
        df99[df99['月'] == i])
    print(f'{i}月复购率为{v}')
df999 = pd.merge(df9, df99, left_on='客户ID', right_on='客户ID', how='inner')
df999['diff'] = df999['月_y'] - df999['月_x']
df_1 = df999[df999['diff'] == 1].groupby(['月_x', '客户ID']).count().reset_index()
print(f'回购率为{len(df_1["客户ID"]) / len(df9["客户ID"])}')
# 10.  以月为单位，计算每月新用户、活跃用户、不活跃用户和回归用户数量，对结果进行可视化
df = df[df["年"] == 2011]
pivoted_counts = df.pivot_table(index='客户ID',
                                columns='月',
                                values='订单日期',
                                aggfunc='count').fillna(0)
df_s = pivoted_counts.applymap(lambda x: 1 if x > 0 else 0)


def active_status(df):
    status = []
    nlen = len(df)
    data = df.tolist()
    for i in range(nlen):
        if data[i] == 0:
            if len(status) > 0:
                if status[i - 1] == "未注册":
                    status.append("未注册")
                else:
                    status.append("不活跃用户")
            else:
                status.append("未注册")
        else:
            if len(status) == 0:
                status.append("新用户")
            else:
                if status[i - 1] == "不活跃用户":
                    status.append("回归用户")
                elif status[i - 1] == "未注册":
                    status.append("新用户")
                else:
                    status.append("活跃用户")
    return pd.Series(status)


df_o = df_s.apply(active_status, axis=1)
df_o = df_o.replace('未注册', np.NaN).replace('新用户', 'new').replace('活跃用户',
                                                                 'active')
df_o = df_o.replace('不活跃用户', 'unactive').replace('回归用户', 'reback')
df_o = df_o.apply(lambda x: pd.value_counts(x))
df_o.fillna(0).T.plot.area()
plt.show()
