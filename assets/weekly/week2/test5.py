# Project: ZG3Doc
# File : test5.py
# Date : 2023/4/14 10:33
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
2023 年 1 月
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# （一）使用numpy和pandas三方库，实现以下要求，代码放在week_2.py文件中：
# 1.使用numpy 创建一个取值为20-30之间的、长度为10的一维数组
arr = np.arange(20, 30)
# 2.扩展第1题中的数组维度，形成形状为(5, 2)的二维数组
arr = arr.reshape(5, 2)
# 3.使用列表[["1","2","3","4","5","6","7","8"]创建numpy数组，转换数组元素数据类型为整形
arr = np.array(["1", "2", "3", "4", "5", "6", "7", "8"], dtype=int)
# 4.新建一个numpy 数组，形状为（4，4），元素值为0
arr = np.zeros([4, 4], dtype=int)
# 5.对第4题中数组中的第0行和第3行的所有值设置为1
arr[0] = 1
arr[3] = 1
# 6.读取mpg.csv形成pandas dataframe数据集df1
df1 = pd.read_csv('./mpg.csv')
# 7.对df1进行缺失值数据处理
df1.fillna(value=0, inplace=True)
# 8.对df1进行操作，新增一列mode，取值按照字段horsepower进行判断，大于100的，mode值为big，否则为little
df1['mode'] = df1.apply(lambda x: 'big' if x['horsepower'] > 100 else 'little', axis=1)
# 9.对df1进行操作，对字段name进行处理，保留第一个单词，处理后的结果作为数据集的一个新列brand
df1['brand'] = df1.apply(lambda x: x['name'].split(' ')[0], axis=1)
# 10.对生成的df1保存为excel文件
df1.to_excel('./df1.xlsx')
# 11.打印df1的所有列名
print(df1.columns.tolist())
# 12.筛选df1中origin值为usa的数据为一个新的数据集df1_1
df1_1 = df1[df1['origin'] == 'usa']
# 13.筛选df1中origin值为europe的数据为一个新的数据集df1_2
df1_2 = df1[df1['origin'] == 'europe']
# 14.使用pandas自带的函数合并df1_1和df1_2数据集形成新的数据集df1_3，且列的数目保持不变，重置索引
df1_3 = pd.merge(df1_1, df1_2, how='left').reset_index()
# 15.使用pandas数据透视表功能对df1进行处理，
# 按cylinders值计算每个不同cylinders的平均horsepower，最大horsepower以及最小horsepower值
df15 = pd.pivot_table(df1, index='cylinders', columns='horsepower',
                      aggfunc=[np.mean, np.max, np.min])
# 16.根据df1数据统计每个origin下的acceleration平均值，用matplotlib柱状图进行可视化
df16 = df1.groupby(by='origin')['acceleration'].mean()
plt.bar(df16.index.tolist(), df16.values.tolist())
# plt.show()
# 17.统计数据集df1中weight超过2000的数据，打印出name值并去重
df1[df1['weight'] > 2000].drop_duplicates('name')
# 18.对df1中的acceleration字段按照model_year分组统计平均值，
# 用matplotlib中的折线图功能描绘model_year年份中acceleration平均值走势图
df16 = df1.groupby(by='model_year')['acceleration'].mean()
plt.plot(df16.index.tolist(), df16.values.tolist())
# plt.show()
# 19.对第18题中的图形进行保存，输出到网页
plt.savefig('./19.png')
# 20.对df1数据集进行分析，按cylinders字段进行分组，统计displacement的均值、最大值、最小值、标准差
df20 = df1.groupby(by='cylinders').agg({
    'displacement': ['mean', 'max', 'min', 'std']
})
