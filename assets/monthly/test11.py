# Project: ZG3Doc
# File : test11.py
# Date : 2023/4/18 9:56
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
1.读取信用卡用户bank.xlsx数据集，命名为bank
2.将bank合理的划分为自变量与因变量
3.定义分类之逻辑回归算法，对模型进行训练
4.使用模型进行预测，
5.对模型准确率进行评价
6.将预测结果作为新列，列名为predict，与bank数据进行合并,合并后的dataframe命名为bank_predict
7.将第6题的bank_predict写入json文件，作为其他系统的API接口文件
"""

import pandas as pd
from sklearn.linear_model._logistic import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 数据加载
data = pd.read_excel('bank.xlsx')

# 自变量
x = data.iloc[:, :-1]

# 因变量
y = data[15].replace(-1, 0)

# 划分测试集
x_train, x_test, y_train, y_test = train_test_split(x, y)

# 训练模型
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
score = accuracy_score(y_test, y_pred)
data['predict'] = model.predict(x)
data.to_json('bank_predict.json')
