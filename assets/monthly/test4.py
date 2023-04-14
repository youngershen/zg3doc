# Project: ZG3Doc
# File : test4.py
# Date : 2023/4/14 11:37
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
09-18-3-00004


1 读取uservs.csv文件，生成dataframe数据集df1，对df1数据各字段进行缺失值处理；
2对数据进行清洗，去掉”用户行为“字段不属于（”pv”,”cart”,”fav”,”buy”)四种值的数据
3对总体用户行为转化率进行计算，计算pv->buy、pv->cart_fav、cart_fav->buy的转化率
4 根据用户ID和用户行为字段进行计算，生成用户行为偏好表，计算各个用户的各自的pv->buy、pv->cart_fav、cart_fav->buy的转化率
5  计算用户FRM模型，因为无客户单价数据，因此计算R和F。R使用与2017年12月3日最近购买的一次时间差，F为下单数；计算R和F的均值，R_mean和F_mean。按照R和F的实际值与均值比较，分别计算4种行为的用户数量
6 用户活跃时段分析，选择某一个日期，计算此日期内每1小时用户浏览量、用户加入购物车量、用户购买量，并用折线图进行可视化
7 定义所有用户行为称之为uv， 计算每日uv, pv数据，并任意选取连续10个日期的数据进行可视化
8 用户留存率分析，计算3日留存率，计算方式：n日留存率=n日后还登录的用户数/第一天新增总用户数
9 商品购买频次分析，计算购买1次、2次。。。10次的商品数量分布数据，进行可视化
10 商品类别偏好分析，计算不同类别下商品的总销量以及包含的商品数，按销量排序

"""

# -*- coding: utf-8 -*-

# Copyright (c) 2023. All rights reserved.

"""
@author: wenjie
@file: m4.py
@time: 2023/4/6 10:17
@desc:

Supported platforms:

 - Linux
 - Windows

Works with Python versions 3.X.
"""

import pandas as pd
from datetime import datetime
from pyecharts.charts import Line, Bar

# 1 读取uservs.csv文件，生成dataframe数据集df1，对df1数据各字段进行缺失值处理；
df1 = pd.read_csv("./uservs.csv")
df1.dropna(inplace=True)
# 2对数据进行清洗，去掉”用户行为“字段不属于（”pv”,”cart”,”fav”,”buy”)四种值的数据
df1.drop(df1[~df1['用户行为'].isin(['pv', 'cart', 'fav', 'buy'])].index,
         inplace=True)
# 3对总体用户行为转化率进行计算，计算pv->buy、pv->cart_fav、cart_fav->buy的转化率
df3 = df1.groupby(by='用户行为')['用户id'].count()
pv_buy = df3['buy'] / df3['pv']
pv_cart_fav = (df3['cart'] + df3['fav']) / df3['pv']
cart_fav_buy = df3['buy'] / (df3['cart'] + df3['fav'])
# 4 根据用户ID和用户行为字段进行计算，生成用户行为偏好表，
# 计算各个用户的各自的pv->buy、pv->cart_fav、cart_fav->buy的转化率
uids = df1['用户id'].unique()
# for i in uids:
#     user_df = df1[df1['用户id'] == i]
#     df4 = user_df.groupby(by='用户行为')['用户id'].count()
#     if df4.get('pv', 0):
#         pv_buy = df4.get('buy', 0) / df4.get('pv', 0)
#         pv_cart_fav = (df4.get('cart', 0) + df4.get('fav', 0)) / df4.get('pv',
#                                                                          0)
#     else:
#         pv_buy = 0
#         pv_cart_fav = 0
#     if df4.get('cart', 0) + df4.get('fav', 0):
#         cart_fav_buy = df4.get('buy', 0) / (df4.get('cart', 0) + df4.get('fav', 0))
#     else:
#         cart_fav_buy = 0
# 5  计算用户FRM模型，因为无客户单价数据，因此计算R和F。R使用与2017年12月3日最近购买的一次时间差，
# F为下单数；计算R和F的均值，R_mean和F_mean。按照R和F的实际值与均值比较，分别计算4种行为的用户数量
df5 = df1[df1['用户行为'] == 'buy']
r = df5.groupby('用户id').agg({'时间戳': 'max'}).reset_index()
r['R'] = (pd.to_datetime(datetime(year=2017, month=12, day=3)) -
          pd.to_datetime(r['时间戳'], unit='s')).dt.days
R = r[['用户id', 'R']]
f = df5.groupby('用户id').agg({'商品id': 'count'}).reset_index()
RF = pd.merge(R, f, left_on='用户id', right_on='用户id', how='inner')
RF.rename(columns={'商品id': 'F'}, inplace=True)
R_mean = RF['R'].mean()
F_mean = RF['F'].mean()
# 6 用户活跃时段分析，选择某一个日期，计算此日期内每1小时用户浏览量、用户加入购物车量、用户购买量，
# 并用折线图进行可视化
a = datetime.timestamp(datetime(year=2017, month=11, day=30, hour=0, minute=0, second=0))
b = datetime.timestamp(datetime(year=2017, month=12, day=1, hour=0, minute=0, second=0))
df6 = df1[(df1['时间戳'] < b) & (df1['时间戳'] >= a)]
df6['hour'] = df6.apply(lambda x: datetime.fromtimestamp(x['时间戳']).hour, axis=1)
df6_1 = df6.groupby(['hour', '用户行为'])['用户id'].count()
line = Line()
line.add_xaxis([f'{i[0]}-{i[1]}' for i in df6_1.index.tolist()])
line.add_yaxis('购买量', df6_1.values.tolist()[::4])
line.add_yaxis('浏览量', df6_1.values.tolist()[3::4])
line.add_yaxis('购物车量', df6_1.values.tolist()[1::4])
line.render('./6.html')
# 7 定义所有用户行为称之为uv， 计算每日uv, pv数据，并任意选取连续10个日期的数据进行可视化
c = datetime.timestamp(datetime(year=2017, month=12, day=10, hour=0, minute=0, second=0))
df7 = df1[(df1['时间戳'] < c) & (df1['时间戳'] >= a)]
df7['day'] = df7.apply(lambda x: datetime.fromtimestamp(x['时间戳']).day, axis=1)
uv = df7.groupby(by=['day'])['用户行为'].count()
v = df7.groupby(by=['day', '用户行为'])['用户id'].count()
pv = v.values.tolist()[3::4]
bar = Bar()
bar.add_xaxis(uv.index.tolist())
bar.add_yaxis('uv', uv.values.tolist())
bar.add_yaxis('pv', pv)
bar.render('./7.html')
# 8 用户留存率分析，计算3日留存率，计算方式：n日留存率=n日后还登录的用户数/第一天新增总用户数
df1['day'] = df1.apply(lambda x: datetime.fromtimestamp(x['时间戳']).day, axis=1)
df8 = df1.groupby(by=['用户id']).agg({'day': 'min'})
user_dic = df8.to_dict()['day']
df1['login'] = df1.apply(lambda x: user_dic[x['用户id']], axis=1)
df1['登录差值'] = df1['day'] - df1['login']
user_df = df1.groupby(by='登录差值')['用户id'].count()
user_df_dic = user_df.to_dict()
df1['code'] = df1.apply(lambda x: user_df_dic[x['登录差值']], axis=1)
df1.drop_duplicates(subset=['用户id', 'day'], keep='first', inplace=True)
df8_1 = df1.pivot(index='用户id', columns='登录差值', values='code')
df8_1.fillna(value=0, inplace=True)
print(df8_1.iloc[:, :3])
# 9 商品购买频次分析，计算购买1次、2次。。。10次的商品数量分布数据，进行可视化
df9 = df1[df1['用户行为'] == 'buy']
df9 = df9['商品id'].value_counts().to_frame().reset_index()
df9.rename(columns={'index': '商品id', '商品id': '购买次数'}, inplace=True)
df9_1 = df9.groupby('购买次数')['商品id'].count()
bar1 = Bar()
bar1.add_xaxis(df9_1.index.tolist())
bar1.add_yaxis('', df9_1.values.tolist())
bar1.render('./9.html')
# 10 商品类别偏好分析，计算不同类别下商品的总销量以及包含的商品数，按销量排序
df10 = df1.groupby('类别id').agg({'商品id': 'count'}).sort_values(by='商品id')
print(df10)

