# Project: ZG3Doc
# File : test1.py
# Date : 2023/4/14 11:32
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
09-18-3-00001

输入数字n，创建数字从 1 到 n 的 1 维数组arr，将 arr 中的所有奇数替换成 -1
给定数组[1, 2, 3, 4, 5]，获取到平均值，将平均值插入到每个元素直接得到新的数组
创建一个5*5的随机值数组，并找到最大值，并替换为0
使用numpy获取昨天、今天、明天的日期
创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积

对附件中数据集testSet.txt进行聚类
a)  导入必要的库
b)  通过迭代寻找k个类簇的一种划分方案，使得用这k个类簇的均值来代表相应各类样本时所得的总体误差最小
c)  重复下面过程直到收敛
d)  用测试数据及测试kmeans算法，获取分类结果
"""

import numpy as np

# 1）输入数字n，创建数字从 1 到 n 的 1 维数组arr，将 arr 中的所有奇数替换成 -1
num = input('输入数字n:')
arr = np.arange(1, int(num))
out = np.where(arr % 2 == 1, -1, arr)  # 不改变原有数组
# arr[arr % 2 == 1] = -1  # 改变原有的数组

# 2）给定数组[1, 2, 3, 4, 5]，获取到平均值，将平均值插入到每个元素直接得到新的数组
arr = np.array([1, 2, 3, 4, 5])
np.insert(arr, np.arange(1, len(arr)), arr.mean())

# 3）创建一个5*5的随机值数组，并找到最大值，并替换为0
arr = np.random.random(25).reshape(5, 5)
arr[arr == arr.max()] = 0

# 4）使用numpy获取昨天、今天、明天的日期
arr = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
arr1 = np.datetime64('today', 'D')
arr2 = np.datetime64('today', 'D') + np.timedelta64(1, 'D')

# 5）创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积
arr = np.random.random(15).reshape(5, 3)
arr1 = np.random.random(6).reshape(3, 2)
np.dot(arr, arr1)

import pandas as pd
import matplotlib.pyplot as plt
from  sklearn.cluster import KMeans
#读取数据
DFdata=pd.read_csv("testSet.csv")
data=DFdata.values#dataframe数据类型转为列表
# print(data)

k = 3  # 假设聚类为 3 类，默认分为 8 个 簇
# 构建算法模型
km = KMeans(n_clusters=k) # n_clusters参数表示分成几个簇（此处k=3）
km.fit(data)

# 获取聚类后样本所属簇的对应编号（label_pred）
label_pred = km.labels_  # labels_属性表示每个点的分簇号，会得到一个关于簇编号的数组
centroids = km.cluster_centers_  #cluster_center 属性用来获取簇的质心点，得到一个关于质心的二维数组，形如[[x1,y1],[x2,y2],[x3,x3]]

# c：表示颜色和色彩序列，此处与 cmap 颜色映射一起使用（cool是颜色映射值）s表示散点的的大小，marker表示标记样式（散点样式）
plt.scatter(data[:, 0], data[:, 1], c=label_pred, s=50, cmap='cool')
# 绘制质心点
plt.scatter(centroids[:,0],centroids[:,1],c='red',marker='o',s=100)
plt.xlabel('x')
plt.ylabel('y')
plt.title("K-Means算法聚类结果")
plt.savefig("1.K-Means实现聚类.png")
plt.show()
