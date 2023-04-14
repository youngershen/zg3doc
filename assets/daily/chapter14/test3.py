# Project: ZG3Doc
# File : test3.py
# Date : 2023/4/14 10:19
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
# -*- coding: utf-8 -*-

# Copyright (c) 2023. All rights reserved.

"""
@author: wenjie
@file: day.py
@time: 2023/3/8 10:33
@desc:

Supported platforms:

 - Linux
 - Windows

Works with Python versions 3.X.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 读取 煤炭分类.xlsx数据集，命名为coal
# 2.将coal的列划分为自变量与因变量
# 3.定义分类之随机森林算法，对模型进行训练
# 4.使用随机森林模型进行预测
# 5.将随机森林的参数n_estimators调整为200，再次进行预测
# 6.对最终的预测结果准确率进行评价

# 读取附件train.csv作为训练集
train = pd.read_excel("./煤炭分类.xlsx")
print(train)
# 定义训练集与测试集
target = train['TYPE']
train = train.drop('TYPE', axis=1)
t1_x, t2_x, t1_y, t2_y = train_test_split(train, target,
                                          test_size=0.2, random_state=1)
# 合理的构建随机森林
for i in range(0, 64):
    plt.subplot(8, 8, i + 1)
    data = train.iloc[i].values.reshape(2, 2)
    plt.imshow(data, interpolation='none', cmap='bone_r')
    plt.xticks([])
    plt.yticks([])
plt.show()
# 对训练集进行训练
# 对测试集进行预测
# 输出预测的结果
rand = RandomForestClassifier(n_estimators=200, n_jobs=4, min_samples_split=2,
                              oob_score=True)
rand.fit(train, target)
print(rand.oob_score_)
# 代码命名符合规范
# 在适当位置添加合理注释
