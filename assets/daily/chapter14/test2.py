# Project: ZG3Doc
# File : test2.py
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

# 读取附件train.csv作为训练集
train = pd.read_csv("./训练集.csv")
# 读取附件test.csv作为测试集
test = pd.read_csv("./测试集.csv")
# 定义训练集与测试集
target = train['label']
train = train.drop('label', axis=1)
t1_x, t2_x, t1_y, t2_y = train_test_split(train, target,
                                          test_size=0.2, random_state=1)
# 合理的构建随机森林
# for i in range(0, 64):
#     plt.subplot(8, 8, i + 1)
#     data = train.iloc[i].values.reshape(28, 28)
#     plt.imshow(data, interpolation='none', cmap='bone_r')
#     plt.xticks([])
#     plt.yticks([])
# plt.show()
# 对训练集进行训练
# 对测试集进行预测
# 输出预测的结果
rand = RandomForestClassifier(n_estimators=200, n_jobs=4, min_samples_split=2,
                              oob_score=True)
rand.fit(train, target)
print(rand.oob_score_)
# 代码命名符合规范
# 在适当位置添加合理注释
