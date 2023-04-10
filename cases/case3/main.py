# Project: ZG3Doc
# File : main.py
# Date : 2023/4/8 9:28
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans


def main():
    # 读取矿产品数据.xlsx文件，进行适当的数据预处理
    df = pd.read_excel('./data/矿产品数据.xlsx')
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
    pass


if __name__ == '__main__':
    main()
