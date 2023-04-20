# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:27
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

"""

2022 年 12 月

"""

import pandas as pd  # as 是给导入的包起一个别名
import numpy as np

# 1.使用列表创建一个numpy数组，内容为
# ['No', 'one', 'can', 'stand', 'it', 'if', 'they', 'are', 'always', 'pressed']
a = ['No', 'one', 'can', 'stand', 'it', 'if', 'they', 'are', 'always',
     'pressed']  # 对于Python是一个列表
# ['No' 'one' 'can' 'stand' 'it' 'if' 'they' 'are' 'always' 'pressed']
arr = np.array(a)  # 创建一维数组
# 2.创建一个一维数组ar1，该数组的元素值全为100，长度为10
### 方法1
# b = [100 for i in range(10)]
# ar1 = np.array(b)  # 创建一维数组
### 方法2
# ar1 = np.ones(10, dtype=int)
# ar1[ar1 % 2 == 1] = 100
### 方法3
ar1 = np.zeros(10, dtype=int)
ar1[ar1 % 2 == 0] = 100
# 3.对ar1进行操作，改变其形状，变成形状为(5,2)的数组
ar3 = ar1.reshape(5, 2)
# 4.生成一个形状为(4,4)、元素值为随机值的二维数组ar2
ar2 = np.random.randint(0, 10, size=(4, 4))
# 5.选取ar2中的元素，打印前位于前两行同时位于前两列的元素的值
ar5 = ar2[0:2, 0:2]  # 类似于python的切片 逗号前的位置是行的索引 逗号后的位置是列的索引
# 6.生成一个形状为（5，5，5）、元素值任意的三维数组
ar6 = np.random.randint(0, 10, size=(5, 5, 5))
# 7.使用数据[["taxi",100,10000,100],["car",1000,1000,1000],["train",5000,5000,5000]]
# 创建一个pandas的dataframe数据集df1
df1 = pd.DataFrame(data=[["taxi", 100, 10000, 100], ["car", 1000, 1000, 1000],
                         ["train", 5000, 5000, 5000]])
# 8.更改数据集df1的列名依次为：交通工具，指标1，指标2，指标3
# df1.columns = ['交通工具', '指标1', '指标2', '指标3']
df1.rename(columns={0: '交通工具', 1: '指标1', 2: '指标2', 3: '指标3'}, inplace=True)
# 9.设置数据集df1的行索引为r1, r2,r3
df1.index = ['r1', 'r2', 'r3']
# df1.rename(index={0: 'r1', 1: 'r2', 2: 'r3'}, inplace=True)
# 10.从df1中删除交通工具为taxi的记录
df1.drop(df1[df1['交通工具'] == 'taxi'].index, inplace=True)
# df2 = df1[~ df1['交通工具'].str.contains('taxi')]  # ~  ->  取反   contains -> 包含的意思
# 11.读取数据文件“汽车销量数据.xlsx”，形成dataframe数据集df2
df = pd.read_excel('./汽车销量数据.xlsx')
# df2 = pd.DataFrame(df)
# 12.对df2的空值字段数据进行合理的填充
df.fillna(value=0, inplace=True)  # inplace默认为false  为true的情况下是就地替换
# print(df)
# 13.对数据集df2进行统计性基本信息描述
df1 = df.describe()
# describe函数  为统计函数  会默认得到max, min, mean, std, 25%, 50% ,75%, count
# 14.按照“市”字段分组统计汽车销量情况
# groupby  分组的函数  第一个参数by单个分组使用字符串或者列表均可,多个分组需要使用列表
# count  次数  max  最大值  min 最小值  mean 平均值 median 中位数  std 方差
# df2 = df.groupby(by=['市'])['制造商'].count()
df2 = df.groupby(by=['市']).agg({'制造商': 'count'})  # 与上面的语法是等价的
# print(df2)
# 15.按照“省”进行分组，分组统计每一年的汽车销量情况
df15 = df.groupby(by=['省', '年'])['制造商'].count()
# 16.从df2中选择“所有权”字段值为“个人”的数据，形成新的数据集df3
df3 = df[df['所有权'] == '个人']  # 筛选  会使用 [[]]  最里面[]放我们的方程式
# 17.对df3数据集进行统计，计算“功率”字段的最大值，最小值，平均值
# print(df3['功率'].max())
# print(df3['功率'].min())
# print(df3['功率'].mean())
# 18.筛选df3数据集中的字段“燃料种类”为“汽油”且“车长”字段大于6000的记录，作为新数据集df4，
# 保存到xlsx文件
df4 = df3[(df3['燃料种类'] == '汽油') & (df3['车长'] > 6000)]
df4.to_excel('df4.xlsx')
# 19.对df4中的数据按照“省”进行分组，计算“车高”字段的最大值，最小值，平均值
df19 = df4.groupby(by=['市']).agg({'车高': ['max', 'min', 'mean']})
# 20.需要添加合理的代码注释
