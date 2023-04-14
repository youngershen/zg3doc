# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 11:30
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
# -*- coding: utf-8 -*-

# Copyright (c) 2023. All rights reserved.

"""
2022 年 10 月
"""

import pandas as pd
from pyecharts.charts import Line
from sklearn import svm  # svm算法
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  # 线性回归
from sklearn.metrics import mean_squared_error, accuracy_score, recall_score
from sklearn.tree import DecisionTreeClassifier  # 决策树
from sklearn.linear_model import LogisticRegression  # 逻辑回归

# 1.使用pandas库读取数据文件penguins.csv，形成数据对象data
data = pd.read_csv("penguins.csv")
# 2.检查数据对象data中的数据，对空值、以及完全重复的记录进行处理
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)
# 3.对species，island，sex的值进行转换，满足模型建立要求
le = LabelEncoder()
for i in ['species', 'island', 'sex']:
    data[i] = le.fit_transform(data[i])
# 4.以bill_length_mm字段为预测y标签，其他字段为特征字段，按合理比例划分数据集
x_list = data.columns.tolist()
x_list.remove('bill_length_mm')
x = data[x_list]
y = data['bill_length_mm']
x_train, x_test, y_train, y_test = train_test_split(x, y)
# 5.选择合适的回归算法建立模型，能够对bill_length_mm字段值进行预测
line = LinearRegression()
# 6.使用训练好的模型对测试集进行预测，打印预测结果
line.fit(x_train, y_train)
y_pred = line.predict(x_test)
# 7.使用合理的评估指标，例如均方误差对第5题中的模型进行评价
score = mean_squared_error(y_test, y_pred)
print(score)
# 8.对评价结果进行解释，依据要合情合理
# 9.使用折线图描绘第5题中预测结果和实际结果
line1 = Line()
line1.add_xaxis(x_test.index.tolist())
line1.add_yaxis('y_test', y_test)
line1.add_yaxis('y_pred', y_pred)
line1.render('./9.html')
# 10.对第9题中的可视化结果进行解释
# 11.使用pandas 读取geyser.csv文件，kind字段按不同值转换为数字0，1，作为数据预测标签
df = pd.read_csv('geyser.csv')
df['kind'] = le.fit_transform(df['kind'])
# 12.使用sklearn中的决策树算法库对第10题中的数据按恰当比例划分数据集进行建模，要求能对kind进行预测。
x = df.iloc[:, :-1]
y = df.iloc[:, -1:]
dec = DecisionTreeClassifier()
# 13. 调整模型训练的参数，训练5次
score_dic = {}
for i in range(5):
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=i)
    dec.fit(x_train, y_train)
    y_pred = dec.predict(x_test)
    # 14.对训练好的5个模型对测试集进行预测，打印准确率
    ac_score = accuracy_score(y_pred, y_test)
    re_score = recall_score(y_pred, y_test)
    score_dic[i] = (ac_score, re_score)
# 15.比较5个模型的准确率，按从高到低排序
s15 = dict(sorted(score_dic.items(), key=lambda x: x[1][0], reverse=True))
# 16.选择准确率最高的模型，打印模型的评估指标，比如预测准确率、召回率等
print(f'准确率: {list(s15.values())[0]}')
print(f'召回率: {list(s15.values())[1]}')
# 17.使用svm算法对同样的数据集进行训练，打印准确率
clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
ac_score = accuracy_score(y_pred, y_test)
print(ac_score)
# 18.使用逻辑回归算法模对同样的数据集进行训练，打印准确率
log = LogisticRegression()
log.fit(x_train, y_train)
y_pred = log.predict(x_test)
ac_score = accuracy_score(y_pred, y_test)
print(ac_score)
# 19.比较以上三种算法的模型性能，并解释哪种模型更合适
# 决策树更合适
# 20.所有题目需要详细的代码注释

