# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:18
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
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
# model.predict_proba(x_test)
y_pred = model.predict(x_test)
score = accuracy_score(y_pred, y_test)
data['predict'] = model.predict(x)
data.to_json('bank_predict.json')
data.to_html('./bank.html')
