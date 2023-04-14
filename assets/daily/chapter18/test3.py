# Project: ZG3Doc
# File : test3.py
# Date : 2023/4/14 10:22
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
1 读取图像聚类.xlsx数据，并转为Dataframe

2 定义分数空列表与K值的取值范围(2-9)

3 使用循环交叉验证的方式，遍历K，
每次遍历都要求用KMeans算法训练、
预测，并使用calinski_harabasz_score
库对预测结果进行评价，
将评价循环写入到上一题定义的分数空列表中

4 使用matplotlib绘图法的plot方法，
找到最高的分数所对应的K值，并最终确认K值

5 使用上题确定的K值，
对数据集进行最终的聚类训练与预测

6 使用matplotlib绘图法的scatter方法，
对聚类预测结果进行绘图展示，
散点为数据分布（任取两列），颜色为预测聚类结果
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score

# 1 读取图像聚类.xlsx数据，并转为Dataframe

df = pd.read_excel('../data/图像聚类.xlsx')
# 2 定义分数空列表与K值的取值范围(2-9)
score_list = []
k_num = range(2, 10)
# 3 使用循环交叉验证的方式，遍历K，每次遍历都要求用KMeans算法训练、预测，
# 并使用calinski_harabasz_score库对预测结果进行评价，将评价循环写入到上一题定义的分数空列表中
for k in k_num:
    kmeans = KMeans(n_clusters=k)
    predict = kmeans.fit_predict(df)
    s = calinski_harabasz_score(df, predict)
    score_list.append(s)
# 4 使用matplotlib绘图法的plot方法，找到最高的分数所对应的K值，并最终确认K值
plt.xlabel('K')
plt.ylabel('score')
plt.plot(k_num, score_list, 'o-')
# plt.show()
new_k = 5
# 5 使用上题确定的K值，对数据集进行最终的聚类训练与预测
kmeans = KMeans(n_clusters=5)
predict = kmeans.fit_predict(df)
# 6 使用matplotlib绘图法的scatter方法，对聚类预测结果进行绘图展示，
# 散点为数据分布（任取两列），颜色为预测聚类结果
plt.scatter(df['pixel_0_2'].tolist(),
            df['pixel_0_3'].tolist(),
            c=predict, alpha=0.7)
# plt.show()