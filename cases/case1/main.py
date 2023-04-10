# Project: ZG3Doc
# File : main.py
# Date : 2023/4/7 14:05
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com

"""
例题一:
包括三个简单的数据分析小案例, 初学者入门使用
"""
import pandas as pd


def test1():
    # 1.导入线性回归对应模块,并读取Advertising(广告)数据源
    data = pd.read_csv('./data/Advertising.csv')
    # 2.取出所有特征值与目标值

    # 3.拆分训练集和测试集

    # 4.创建线性回归模型并进行训练

    # 5.使用自定义数据对模型进行预测

    # 6.计算模型权重与截距

    # 7.使用R方对模型效果进行评估

    # 8.不调用模型的predict方法,对未知的数据进行预测
    pass


def test2():
    """
    x表示二维矩阵，篮球运动员比赛数据, 第一列表示球员每分钟的助攻数,第二列表示球员每分钟的的分数
    输出完整的kmeans函数，包括很多省略参数
    """
    X = [[0.0888, 0.5885],
         [0.1399, 0.8291],
         [0.0747, 0.4974],
         [0.0983, 0.5772],
         [0.1276, 0.5703],
         [0.1671, 0.5835],
         [0.1906, 0.5276],
         [0.1061, 0.5523],
         [0.2446, 0.4007],
         [0.1670, 0.4770],
         [0.2485, 0.4313],
         [0.1227, 0.4909],
         [0.1240, 0.5668],
         [0.1461, 0.5113],
         [0.2315, 0.3788],
         [0.0494, 0.5590],
         [0.1107, 0.4799],
         [0.2521, 0.5735],
         [0.1007, 0.6318],
         [0.1067, 0.4326],
         [0.1956, 0.4280]]
    print(X)
    # 1. 输出聚类预测结果
    # 2. 将聚类结果绘制成散点图
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans

    clf = KMeans(n_clusters=3)
    y_pred = clf.fit_predict(X)
    print(clf)
    print(y_pred)

    x = [n[0] for n in X]
    print(x)
    y = [n[0] for n in X]

    print(y)
    plt.scatter(x, y, c=y_pred, marker='x')
    plt.title("Kmeans Basketball Dat")
    plt.xlabel("assists per minute")
    plt.ylabel("points per minutes")
    plt.legend("Rank")
    plt.show()


def test3():
    # 输出完整的kmeans函数，包括很多省略参数
    # 10.输出聚类预测结果
    # 11.将聚类结果绘制成散点图
    # 12.导入数据集iris,输出数据集与真实标签
    # 13.分割数据集构造训练集70%训练,%30预测
    # 14.输出测试集与测试样本类别
    # 15.使用决策树DTC包进行训练
    # 16.输出预测结果
    # 17.数据预测结果与真实结果对比
    # 18.输出准确率 召唤率F值
    # 19.获取花卉测试数据集两列数据集
    # 20.进行散点图绘制
    pass


def main():
    test2()
    print("test")
    pass


if __name__ == '__main__':
    main()
