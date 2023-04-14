# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:33
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
2022 年 10 月
"""

# -*- coding: utf-8 -*-

# Copyright (c) 2023. All rights reserved.

"""
@author: wenjie
@file: m10.py
@time: 2023/3/27 14:27
@desc:

Supported platforms:

 - Linux
 - Windows

Works with Python versions 3.X.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1.使用numpy生成一个长度为50的数组，数组元素取值为1-10之间
arr = np.random.randint(1, 10, size=50, dtype=np.int64)
# 2.对第1题中的数组进行操作，变成形状为(2,5,5)的数组
arr = arr.reshape(2, 5, 5)
# 3.使用列表[20,21,22,23,24,25]创建一个numpy数组，转换数组元素数据类型为字符串
arr3 = np.array([20, 21, 22, 23, 24, 25], dtype=np.str_)
# 4.使用numpy创建一个二维数组
arr4 = np.zeros(4).reshape(2, 2)
# 5.使用numpy生成一个3x3x3的随机数组
arr5 = np.random.randint(0, 10, size=3 * 3 * 3).reshape(3, 3, 3)
# 6.读取mall_customers.csv形成pandas dataframe数据集df1
df1 = pd.read_csv('./mall_customers.csv')
# 7.对df1进行缺失值数据处理
df1.fillna(value=0, inplace=True)
# 8.对df1进行操作，创建一个新列gender_value，取值按照gender进行处理，值为Male为1，否则为0
print(df1.columns)
df1['gender_value'] = df1.apply(lambda x: 1 if x.Gender == 'Male' else 0,
                                axis=1)
# 9.对df1进行操作，转变Annual Income列的值为字符串，对每个值加上后缀“千元”，如“70”为“70千元”
df1['Annual Income (千元)'] = df1['Annual Income (k$)'].astype('str') + '千元'
# 10.对df1进行处理，使用列Spending Score 除以列age，结果生成一个新列score_per
# df1['score_per'] = df1.apply(lambda x: x['Spending Score (1-100)'] / x['Age'], axis=1)
df1['score_per'] = df1['Spending Score (1-100)'] / df1['Age']
# 11.对df1进行数据清洗，对字段age字段进行处理，去除age小于25的数据
df1.drop(df1[df1['Age'] < 25].index, inplace=True)
# 12.对数据清洗完成后的df1数据集，保存到excel文件
df1.to_excel('12.xlsx')
# 13.打印df1的行索引，打印df1的列名
# print(df1.index)
# print(df1.columns)
# 14.选择df1中gender值为Male且Annual Income值大于25的的数据为一个新的数据集df2
df2 = df1[(df1['Gender'] == 'Male') & (df1['Annual Income (k$)'] > 25)]
# 15.选择df1中gender值为Femal且Annual Income值小于22的数据为一个新的数据集df3
df3 = df1[(df1['Gender'] == 'Female') & (df1['Annual Income (k$)'] < 22)]


# 16.使用df1对age进行年龄组处理，大于50的值为3，大于等于30且小于50的值为2，小于30的值为1，形成一个新列 age_group
def func(x):
    if x['Age'] > 50:
        return 3
    elif 30 <= x['Age'] < 50:
        return 2
    else:
        return 1


df1['age_group'] = df1.apply(func, axis=1)
# 17.使用pandas自带的函数合并df2和df3数据集形成新的数据集df4，重置索引
df4 = pd.concat([df2, df3], ignore_index=True)
# 18.使用pandas数据透视表功能对df1进行处理，按age_group值计算每个不同年龄组的
# 平均Annual Income，最大Annual Income以及最小Annual Income值
df18 = df1.pivot_table(columns=['age_group'], values=['Annual Income (k$)'],
                       aggfunc=[np.mean, np.max, np.min])
# 19.根据df1数据统计每个age_group下的Spending Score 最大值，用matplotlib柱状图进行可视化
df19 = df1.groupby(by='age_group')['Spending Score (1-100)'].max()
plt.bar(df19.index.tolist(), df19.values.tolist())
plt.show()
# 20.以上每道题均需添加合理的注释
