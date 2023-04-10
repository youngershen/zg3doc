# Project: ZG3Doc
# File : mmain.py
# Date : 2023/4/8 9:19
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 读取数据
DFdata = pd.read_csv("./data/testSet.csv")
data = DFdata.values  # dataframe数据类型转为列表
# print(data)

k = 3  # 假设聚类为 3 类，默认分为 8 个 簇
# 构建算法模型
km = KMeans(n_clusters=k)  # n_clusters参数表示分成几个簇（此处k=3）
km.fit(data)

# 获取聚类后样本所属簇的对应编号（label_pred）
label_pred = km.labels_  # labels_属性表示每个点的分簇号，会得到一个关于簇编号的数组
centroids = km.cluster_centers_  # cluster_center 属性用来获取簇的质心点，得到一个关于质心的二维数组，形如[[x1,y1],[x2,y2],[x3,x3]]

# c：表示颜色和色彩序列，此处与 cmap 颜色映射一起使用（cool是颜色映射值）s表示散点的的大小，marker表示标记样式（散点样式）
plt.scatter(data[:, 0], data[:, 1], c=label_pred, s=50, cmap='cool')
# 绘制质心点
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='o', s=100)
plt.xlabel('x')
plt.ylabel('y')
plt.title("K-Means算法聚类结果")
plt.savefig("1.K-Means实现聚类.png")
plt.show()
