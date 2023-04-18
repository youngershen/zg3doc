# Project: ZG3Doc
# File : test9.py
# Date : 2023/4/18 9:54
# Author: Younger Shen <申延刚>
# Web: https://github.com/youngershen
# Cell: 13811754531
# Wechat: 13811754531
# Email : shenyangang@163.com
"""
1.读取数据集 基因图谱.xlsx,定义训练数据
2.根据机器学习要求，对训练数据进行拆分
3.定义分类算法之决策树模型
4.对定义好的模型进行训练
5.使用模型进行预测
6.使用acc评价指标对模型进行评价
7.如果acc评价得分大于0.9，请预测头长7.0、鼻长2.7，头宽5.1，颌长2.2的个体，属于哪个人种？
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# 1.读取数据集 基因图谱.xlsx,定义训练数据
df=pd.read_excel('基因图谱.xlsx')
# 2.根据机器学习要求，对训练数据进行拆分
le=LabelEncoder()
df['人种']=le.fit_transform(df['人种'])
x=df[df.columns.drop('人种')]
y=df['人种']
x_train,x_test,y_train,y_test=train_test_split(x,y)
# 3.定义分类算法之决策树模型
tree=DecisionTreeClassifier()
# 4.对定义好的模型进行训练
tree.fit(x_train,y_train)
# 5.使用模型进行预测
y_pred=tree.predict(x_test)
print(y_pred)
# 6.使用acc评价指标对模型进行评价
score=accuracy_score(y_test, y_pred)
# 7.如果acc评价得分大于0.9，请预测头长7.0、鼻长2.7，头宽5.1，颌长2.2的个体，属于哪个人种？
if score>0.9:
    print(tree.predict(np.array([7.0,2.7,5.1,2.2]).reshape(1,-1)))
