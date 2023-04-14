# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/14 9:41
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd

# 1．读取附件中的People.csv文件到df中
df = pd.read_csv('People.csv')
# 2．根据 '性别列' 进行分组, 得到的是一个分组后的对象
df1 = df.groupby(by='性别')
# 3．通过性别, 只对年龄进行分组
df2 = df.groupby(by=['性别', '年龄'])
# 4．遍历分组，获取每个分组的最大年龄，最小年龄，平均年龄分别是多少
# print(df2['年龄'].max())
# print(df2['年龄'].min())
# print(df2['年龄'].mean())
# 5．先按性别分组，再按婚姻状况分组
df3 = df.groupby(by=['性别', '婚姻状况'])
# 6．查看一下分组后每组的数量
# print(df3.size())
# 7．使用agg对分组后的数据进行统计，获取最大年龄，最小年龄，平均年龄
# print(df3.agg({'年龄': ['max', 'min', 'mean']}))
# 8．获取性别为F的年龄的中位数
# print(df[df['性别'] == 'F']['年龄'].median())
# 9．获取两组的薪资总数
# print(df3['薪资'].sum())
# 10．按照婚姻状况进行分组，获取YES组的平均薪资
df['薪资'] = df['薪资'].str.replace('k', '').astype(float)
print(df[df['婚姻状况'] == 'YES']['薪资'].mean())