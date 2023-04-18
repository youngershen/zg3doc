# Project: ZG3Doc
# File : test8.py
# Date : 2023/4/18 9:54
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
引入多元线性回归算法库，和mean_squared_error评价库，并读取50_Startups.xlsx数据
将数据按合理的方式划分为自变量与因变量，为回归模型提供训练数据
定义多元线性回归模型，使用默认参数
对多元线性回归模型进行训练
使用模型进行预测，并输出预测结果
使用mean_squared_error计算模型的均方误差
分别计算模型的斜率、截距，并打印输出
"""

import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# 1.引入多元线性回归算法库，和mean_squared_error评价库，并读取50_Startups.xlsx数据
df = pd.read_excel('../data/50_Startups.xlsx')
# 2.将数据按合理的方式划分为自变量与因变量，为回归模型提供训练数据
x = df[['R&D Spend', 'Administration', 'Marketing Spend']]
y = df['Profit']
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=666)
# 3.定义多元线性回归模型，使用默认参数
line = LinearRegression()
# 4.对多元线性回归模型进行训练
line.fit(x_train, y_train)
# 5.使用模型进行预测，并输出预测结果
y_predict = line.predict(x_test)
print(y_predict)
# 6.使用mean_squared_error计算模型的均方误差
print(mean_squared_error(y_test, y_predict))
# 7.分别计算模型的斜率、截距，并打印输出
print(line.coef_)
print(line.intercept_)