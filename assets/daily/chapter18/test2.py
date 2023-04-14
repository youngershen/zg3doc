# Project: ZG3Doc
# File : test2.py
# Date : 2023/4/14 10:22
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
1 读取account.xlsx数据,
其中R、F、M、RFM这几列代表用户特征，
type这一列代表用户画像类型

2 将数据拆分为特征与类型标识两种数据结构

3 创建随机森林算法模型

4 对创建好的模型开始训练

5 使用训练好的模型进行预测

6 使用accuracy_score评分方法对模型进行评价

7 当M调整为6.3，R调整为2.9，
F调整为5.1，RFM调整为2.1时，
请使用随机森林模型预测type结果
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# 读取数据
df = pd.read_excel('account.xlsx')
# 拆分数据
X = df[['R', 'F', 'M', 'RFM']]
y = df['type']
# 训练模型
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
rf_model = RandomForestClassifier().fit(X_train, y_train)
# 评估模型
accuracy = accuracy_score(y_test, rf_model.predict(X_test))
print('Accuracy:', accuracy)
# 预测新数据
new_data = pd.DataFrame({'R': [2.9], 'F': [5.1], 'M': [6.3], 'RFM': [2.1]})
predicted_type = rf_model.predict(new_data)
print('Predicted type:', predicted_type)
