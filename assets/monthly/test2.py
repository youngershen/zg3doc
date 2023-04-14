# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 11:32
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

"""
09-18-3-00002

请生成一个100-200的numpy数字序列一维数组，要求步长为5
请将给定python元组(3,5,8,9,11)转为numpy一维数组
生成一个包含从31-90的整数的二维数组，数组必须为6行，10列
请将上一题中的二维数组，转为pandas的dataframe结构，列名使用自然数索引
生成一个值全部为1的numpy二维数组，数组必须为5行，5列
1. 读取矿产品数据.xlsx文件，进行适当的数据预处理
2. 在k值2-9之间循环KMeans算法，并使用calinski_harabasz_score评分
3. 用绘图法找到最佳k值
4. 使用最佳k值实现位置矿产品聚类，并使用散点图绘制聚类结果
"""

import numpy as np
import pandas as pd

# 1.请生成一个100-200的numpy数字序列一维数组，要求步长为5
arr = np.arange(100, 201, 5)
# 2.请将给定python元组(3,5,8,9,11)转为numpy一维数组
tuple1 = (3, 5, 8, 9, 11)
arr = np.array(tuple1)
# 3.生成一个包含从31-90的整数的二维数组，数组必须为6行，10列
arr = np.arange(31, 91).reshape(6, 10)
# 4.请将上一题中的二维数组，转为pandas的dataframe结构，列名使用自然数索引
df = pd.DataFrame(arr)
# 5.生成一个值全部为1的numpy二维数组，数组必须为5行，5列
arr = np.ones((5, 5))

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans

# 读取矿产品数据.xlsx文件，进行适当的数据预处理
df = pd.read_excel('../data/矿产品数据.xlsx')
#    2.2 在k值2-9之间循环KMeans算法，并使用calinski_harabasz_score评分，用绘图法找到最佳k值
for i in range(2, 10):
    # 构建并训练模型
    kmeans = KMeans(n_clusters=i, random_state=123)
    kmeans.fit(df)
    score = metrics.calinski_harabasz_score(df, kmeans.labels_)
    print(f'数据聚{i}类calinski_harabaz指数为{score}')
#    2.3 使用最佳k值实现位置矿产品聚类，并使用散点图绘制聚类结果
kmeans = KMeans(n_clusters=3, random_state=123)
kmeans.fit(df)
df['cluster'] = kmeans.labels_
centers = kmeans.cluster_centers_
sns.lmplot(x='钙', y='镁', hue='cluster', data=df)
plt.scatter(centers[:, 2], centers[:, 3], marker='*', color='black')
plt.xlabel('钙')
plt.ylabel('镁')
plt.show()