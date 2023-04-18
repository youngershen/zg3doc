# Project: ZG3Doc
# File : test6.py
# Date : 2023/4/18 9:50
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
多元线性回归方程和简单线性回归方程类似，不同的是由于因变量个数的增加，求取参数的个数也相应增加，推导和求取过程也不一样。
　　　　y=β0＋β１x1+β2x2+ ... +βpxp+ε
　　对于b0、b1、…、bn的推导和求取过程，引用一个第三方库进行计算。以如下数据为例，对运输里程、运输次数、车型、隐式转换与运输总时间的关系，建立多元线性回归模型：
运输里程  输出次数  运输总时间
100  4  9.3
50  3  4.8
100  4  8.9
100  2  6.5
50  2  4.2
80  2  6.2
75  3  7.4
65  4  6.0
90  3  7.6
100  4  9.3
50  3  4.8
100  4  8.9
100  2  6.5
找到上述数据中的多维关系，使用多元线性回归，请创建线性模型，通过训练，预测运输里程为80，运输次数为3次的运输总时间为多少
"""

import numpy as np
from sklearn import datasets,linear_model

# 定义训练数据
x = np.array([[100,4,9.3],[50,3,4.8],[100,4,8.9],
              [100,2,6.5],[50,2,4.2],[80,2,6.2],
              [75,3,7.4],[65,4,6],[90,3,7.6],[90,2,6.1]])
# print(x)
X = x[:,:-1]  # 取所有数据，抛出最后一列
Y = x[:,-1]   # 取所有数据中的最后一列
# print(X,Y)

# 训练数据
regr = linear_model.LinearRegression()  # 线性回归
regr.fit(X,Y)


# 预测
x_test = np.array([[80,3]])
y_test = regr.predict(x_test)
print(y_test)