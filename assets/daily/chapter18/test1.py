# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/14 10:22
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
1．导入相关python库
2．读取附件中的books.csv，相关字段内容为：
bookId, title, genres
bookId:每本书的id
title:书的标题
genres:书的类别
3．读取附件中的ratings.csv
userId, bookId, rating, timestamp
userId: 每个用户的id
bookId: 每本书的id
rating: 用户评分，是5星制，按半颗星的规模递增(0.5 stars - 5 stars)
timestamp: 自1970年1月1日零点后到用户提交评价的时间的秒数
数据排序的顺序按照userId，bookId排列的
4．合并数据集
5．汇总每本的评分数量，并按降序排列
6．获取每本的评分平均值
7．基于用户的协同过滤算法，假设现在用户id为2的，想看一下之前评分为4的动作片的书，推荐哪一本书？
8．基于内容数据的协同过滤算法，假设现在用户id为5的，想看一下评分为5的Drama的书，推荐哪一本书？
"""

# 1．导入相关python库
import pandas as pd
import numpy as np
# 2．读取附件中的books.csv，相关字段内容为：
df = pd.read_csv('books.csv')
print(df)
# bookId, title, genres
# bookId:每本书的id
# title:书的标题
# genres:书的类别
# 3．读取
# 附件中的ratings.csv
df2 = pd.read_csv('ratings.csv')
print(df2)
# userId, bookId, rating, timestamp
# userId: 每个用户的id
# bookId: 每本书的id
# rating: 用户评分，是5星制，按半颗星的规模递增(0.5 stars - 5 stars)
# timestamp: 自1970年1月1日零点后到用户提交评价的时间的秒数
# 数据排序的顺序按照userId，bookId排列的
# 4．合并数据集
df3 = pd.merge(df,df2,left_on='bookId',right_on='bookId',how='inner')
print(df3)
# 5．汇总每本的评分数量，并按降序排列
df5 = df3.groupby(by='bookId').agg({"rating":"sum"}).reset_index()
df5.sort_values(by='rating',ascending=False,inplace=True)
print(df5)
# 6．获取每本的评分平均值
df6 = df3.groupby(by='bookId').agg({"rating":"mean"})
print(df6)
# 7．基于用户的协同过滤算法，假设现在用户id为2的，想看一下之前评分为4的动作片的书，推荐哪一本书？
df7 = df3[df3['rating'] == 4]
df7_1 = df7[df7['userId'] == 2]
df7_2 = df7_1[df7_1['genres'] == 'Drama']
print(df7_2)
# 8．基于内容数据的协同过滤算法，假设现在用户id为5的，想看一下评分为5的Drama的书，推荐哪一本书？
df8 = df3[df3['userId'] == '5']
df8_1 = df8[df8['rating'] == 5]
df8_2 = df8_1[df8_1['genres'] == 'Drama']
print(df8_2)