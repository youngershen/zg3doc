# Project: ZG3Doc
# File : test7.py
# Date : 2023/4/18 9:51
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
对上海房地产数据进行预处理，并使用多元线性回归模型进行训练
使用原数据集的特征，对上海房地产的单价进行预测
将数据按8：2的比率拆分成训练集和测试集
输出预测的准确度
计算并输出模型的斜率
"""

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# 1.1对上海房地产数据进行预处理，并使用多元线性回归模型进行训练
df = pd.read_excel('../data/上海房地产.xlsx')
x = df[['地段指数', '配套指数']]
y = df['单价']
# 1.2使用原数据集的特征，对上海房地产的单价进行预测
line = LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=8)
line.fit(x_train, y_train)
# 1.3计算并输出模型的斜率
print(line.coef_)
# 1.4 计算并输出模型的截距
print(line.intercept_)